#!/usr/bin/env python3
"""Writes the site's pages into site/.

Every page shares the same header (the studio's name and the tabs), icons and footer. There's no
build step on Vercel: the generated HTML is committed, and `./ci.sh` fails if it's out of date.
Edit the pages here, then run:  python3 tools/build_pages.py
"""
import sys
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent / "site"

TABS = [("Home", "/"), ("Barricade", "/barricade"), ("Pulse", "/pulse"), ("About", "/about")]

ICONS = """<svg class="defs" aria-hidden="true"><defs>
<symbol id="barricade" viewBox="0 0 20 16"><rect x="4" y="3" width="2" height="12" rx="1" fill="#fff"/><rect x="14" y="3" width="2" height="12" rx="1" fill="#fff"/><rect x=".5" y="5.5" width="19" height="5" rx="1.2" fill="#FF6A13"/><path d="M3.7 6.5 2 9.5h2.3L6 6.5zm5 0L7 9.5h2.3L11 6.5zm5 0L12 9.5h2.3L16 6.5z" fill="#1D1D1F"/></symbol>
<symbol id="pulse" viewBox="0 0 28 20"><path d="M1 11h6l3-8 5 15 4-10 2 3h6" fill="none" stroke="#1F9D55" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></symbol>
<symbol id="down" viewBox="0 0 14 16"><path d="M7 1v9m0 0L3 6m4 4 4-4M1 14h12" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></symbol>
</defs></svg>"""

DOWNLOAD = '<a class="button" href="/barricade/download"><svg width="14" height="16" aria-hidden="true"><use href="#down"/></svg>Download for Mac</a>'


def dots():
    held = {13, 22, 26, 28}
    return "".join(f'<i class="{"held" if i in held else "on"}"></i>' if i >= 7 else "<i></i>" for i in range(30))


APP = f"""<figure class="stage">
      <div class="app" role="img" aria-label="The Barricade app: 23 days protected, the last 30 days as dots, and the list of blocked sites">
        <div class="app-stripe"></div>
        <div class="app-bar"><div class="lights"><i></i><i></i><i></i></div><b>Barricade</b></div>
        <div class="app-body" aria-hidden="true">
          <div class="app-left"><div class="app-number">23</div><strong>days protected</strong><small>since October 18</small><div class="dots">{dots()}</div></div>
          <div class="app-right"><strong>Blocked</strong><div class="app-add">+ Add a site</div>
            <div class="app-row"><b>Adult content</b><span>Automatic</span></div>
            <div class="app-row">reddit.com<span>3 this month</span></div>
            <div class="app-row">twitch.tv</div>
            <div class="app-row">nfl.com</div>
          </div>
        </div>
      </div>
      <figcaption>The Barricade app, with sample data</figcaption>
    </figure>"""


def page(path, title, description, tab, body, download=False, index=True):
    current = ' aria-current="page"'
    tabs = "".join(f'<a href="{href}"{current if name == tab else ""}>{name}</a>' for name, href in TABS)
    get = '<a class="get" href="/barricade/download">Download</a>' if download else "<span></span>"
    robots = "" if index else '\n<meta name="robots" content="noindex">'
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{description}">{robots}
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/styles.css">
</head>
<body>
{ICONS}
<header class="top"><div class="wrap nav">
  <a class="word" href="/"><i></i>Northlight Studio</a>
  <nav class="tabs" aria-label="Main">{tabs}</nav>
  {get}
</div></header>

<main>
{body}
</main>

<footer class="foot"><div class="wrap"><span>© 2026 Northlight Studio</span><a href="/about">About</a></div></footer>
</body>
</html>
"""
    return SITE / path, html


PAGES = [
    page("index.html", "Northlight Studio", "Small, careful apps that help you keep the habits you chose.", "Home", """  <section class="wrap hero">
    <h1>Apps for the person you're trying to be.</h1>
    <p class="lede">Small, careful apps that help you keep the habits you chose.</p>
  </section>

  <section class="wrap apps" aria-label="Our apps">
    <a class="product" href="/barricade">
      <div class="pic" style="background:#1D1D1F"><svg width="110" height="88" aria-hidden="true"><use href="#barricade"/></svg></div>
      <div class="text"><h2>Barricade</h2><p>Block the sites that pull you back. For Mac.</p><span class="more">Learn more →</span></div>
    </a>
    <a class="product" href="/pulse">
      <div class="pic" style="background:#DDF5E6"><svg width="120" height="86" aria-hidden="true"><use href="#pulse"/></svg></div>
      <div class="text"><h2>Pulse</h2><p>Your health and fitness in one place, with an AI coach. For iPhone.</p><span class="later">Coming soon</span></div>
    </a>
  </section>"""),

    page("barricade/index.html", "Barricade · block the sites that pull you back",
         "Barricade blocks the sites you choose in every browser on your Mac, and stays on through the nights you wish it wouldn't.",
         "Barricade", f"""  <section class="wrap hero">
    <span class="icon barricade"><svg width="38" height="30" aria-hidden="true"><use href="#barricade"/></svg></span>
    <h1>Block the sites that pull you back.</h1>
    <p class="lede">Barricade blocks them in every browser on your Mac, and stays on through the nights you wish it wouldn't.</p>
    {DOWNLOAD}
    <span class="fine">macOS 15 or later</span>
  </section>

  <div class="wrap">
    {APP}
  </div>

  <section class="wrap three" aria-label="Why Barricade">
    <div class="card"><svg width="30" height="30" viewBox="0 0 30 30" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><rect x="3" y="6" width="24" height="17" rx="3"/><path d="M3 11h24"/></svg><h2>Works everywhere</h2><p>Every browser, private windows included. There's no other door.</p></div>
    <div class="card"><svg width="30" height="30" viewBox="0 0 30 30" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="6" y="13" width="18" height="12" rx="3"/><path d="M10 13V9a5 5 0 0 1 10 0v4"/></svg><h2>Stays on</h2><p>You can't switch it off on a whim. Changing your mind takes seven days.</p></div>
    <div class="card"><svg width="30" height="30" viewBox="0 0 30 30" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 4 5 8v7c0 6 4.500 9.500 10 11 5.500-1.500 10-5 10-11V8z"/><path d="m11 15 3 3 5-6"/></svg><h2>Private</h2><p>No account, nothing sent anywhere. Everything stays on your Mac.</p></div>
  </section>

  <section class="wrap how" aria-labelledby="how">
    <h2 id="how">How it works</h2>
    <ol class="steps">
      <li><i>1</i><b>Add a site</b><span>Type it in from the menu bar. It takes a second.</span></li>
      <li><i>2</i><b>It's blocked</b><span>Right away, everywhere on your Mac. Adult sites are blocked automatically.</span></li>
      <li><i>3</i><b>Watch the days add up</b><span>Every protected day fills a dot.</span></li>
    </ol>
  </section>""", download=True),

    page("barricade/download/index.html", "Download Barricade", "Barricade's installer for Mac is almost ready.", "Barricade",
         """  <!-- Holding page until the signed, notarized installer exists. Then vercel.json redirects
       /barricade/download straight to the file and this page goes. -->
  <section class="wrap hero alone">
    <span class="icon barricade"><svg width="38" height="30" aria-hidden="true"><use href="#barricade"/></svg></span>
    <h1>The download is almost ready.</h1>
    <p class="lede">Apple is checking Barricade's installer, so your Mac knows it's safe to open. This page becomes the download as soon as that's done.</p>
    <a class="button quiet" href="/barricade">Back to Barricade</a>
  </section>""", index=False),

    page("pulse/index.html", "Pulse · health and fitness with an AI coach",
         "Pulse keeps your workouts, meals, sleep and habits in one place, with an AI coach that knows all of it. Coming soon for iPhone.",
         "Pulse", """  <section class="wrap hero alone">
    <span class="icon pulse"><svg width="40" height="29" aria-hidden="true"><use href="#pulse"/></svg></span>
    <h1>Your health, in one place.</h1>
    <p class="lede">Pulse keeps your workouts, meals, sleep and habits together, with an AI coach that knows all of it. For iPhone.</p>
    <span class="soon">Coming soon</span>
  </section>"""),

    page("about/index.html", "About · Northlight Studio", "Northlight Studio is a small studio making apps that help you keep the habits you chose.",
         "About", """  <section class="wrap hero">
    <h1>A small studio for good habits.</h1>
  </section>
  <section class="wrap">
    <div class="about">
      <p>Northlight Studio makes apps that help you keep the habits you chose: what you block, how you train, what you eat.</p>
      <p>We build things we use ourselves, and we'd rather make a few apps well than many quickly.</p>
    </div>
  </section>"""),
]


def main():
    check = "--check" in sys.argv
    stale = []
    for path, html in PAGES:
        if check:
            if not path.is_file() or path.read_text(encoding="utf-8") != html:
                stale.append(str(path.relative_to(SITE.parent)))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(html, encoding="utf-8")
    if stale:
        print("Out of date (run python3 tools/build_pages.py): " + ", ".join(stale))
        sys.exit(1)
    print(f"{len(PAGES)} pages {'up to date' if check else 'written'}.")


if __name__ == "__main__":
    main()
