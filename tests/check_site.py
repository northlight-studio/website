#!/usr/bin/env python3
"""Checks every page in site/ the way Vercel will serve it.

- Every page is well-formed: balanced tags, a doctype, lang, charset, viewport, title, description.
- Every internal link and asset resolves to a file, using Vercel's clean URLs (/barricade serves
  site/barricade/index.html, /about serves site/about.html).
- No inline scripts: vercel.json's Content-Security-Policy would block them.
- vercel.json is valid and points at site/.
"""
import json
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr",
        "path", "rect", "circle", "stop"}
failures = []


def fail(page, message):
    failures.append(f"{page.relative_to(ROOT)}: {message}")


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.links, self.meta = [], [], {}
        self.doctype = self.lang = self.title = self.inline_script = False
        self.errors = []
        self._in_title = False

    def handle_decl(self, decl):
        self.doctype = self.doctype or decl.lower() == "doctype html"

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html" and a.get("lang"):
            self.lang = True
        if tag == "meta":
            if "charset" in a:
                self.meta["charset"] = a["charset"]
            if a.get("name"):
                self.meta[a["name"]] = a.get("content", "")
        if tag == "title":
            self._in_title = True
        if tag == "script" and "src" not in a:
            self.inline_script = True
        for key in ("href", "src"):
            if a.get(key):
                self.links.append(a[key])
        if tag not in VOID:
            self.stack.append((tag, self.getpos()[0]))

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID:
            self.stack.pop()

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        if tag in VOID:
            return
        if not self.stack or self.stack[-1][0] != tag:
            self.errors.append(f"line {self.getpos()[0]}: </{tag}> doesn't close "
                               f"{'<' + self.stack[-1][0] + '>' if self.stack else 'anything'}")
            return
        self.stack.pop()

    def handle_data(self, data):
        if self._in_title and data.strip():
            self.title = True


def served(path):
    """The file Vercel serves for an internal URL path, or None."""
    path = path.split("#", 1)[0].split("?", 1)[0]
    if not path.startswith("/"):
        return None
    rel = path.strip("/")
    candidates = [SITE / rel] if rel else []
    candidates += [SITE / rel / "index.html", SITE / f"{rel}.html"] if rel else [SITE / "index.html"]
    return next((c for c in candidates if c.is_file()), None)


pages = sorted(SITE.rglob("*.html"))
if not pages:
    print("no pages in site/")
    sys.exit(1)

for page in pages:
    parser = Page()
    parser.feed(page.read_text(encoding="utf-8"))
    parser.close()
    for error in parser.errors:
        fail(page, error)
    for tag, line in parser.stack:
        fail(page, f"<{tag}> opened on line {line} is never closed")
    if not parser.doctype:
        fail(page, "missing <!doctype html>")
    if not parser.lang:
        fail(page, "missing <html lang>")
    if parser.meta.get("charset", "").lower() != "utf-8":
        fail(page, "missing <meta charset=\"utf-8\">")
    if "viewport-fit=cover" not in parser.meta.get("viewport", ""):
        fail(page, "missing the viewport meta")
    if not parser.title:
        fail(page, "missing a <title>")
    if not parser.meta.get("description"):
        fail(page, "missing a meta description")
    if parser.inline_script:
        fail(page, "has an inline <script>, which the Content-Security-Policy blocks")
    for link in parser.links:
        if link.startswith(("http://", "https://", "mailto:", "#")):
            continue
        if not link.startswith("/"):
            fail(page, f"relative link {link!r}: use a path from the site root")
        elif served(link) is None:
            fail(page, f"link {link!r} doesn't resolve to a file")

try:
    config = json.loads((ROOT / "vercel.json").read_text())
    if config.get("outputDirectory") != "site":
        failures.append("vercel.json: outputDirectory should be \"site\"")
    if not config.get("cleanUrls"):
        failures.append("vercel.json: cleanUrls should be on (links are written without .html)")
except (OSError, ValueError) as error:
    failures.append(f"vercel.json: {error}")

if failures:
    print("\n".join(failures))
    sys.exit(1)
print(f"{len(pages)} pages checked: well-formed, every internal link resolves, no inline scripts.")
