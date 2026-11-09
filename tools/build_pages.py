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
<symbol id="eye" viewBox="0 0 100 100"><circle cx="50" cy="50" r="6.5" fill="currentColor"/><path d="M50.0 23.0Q52.4 16.0 50.0 2.0Q47.6 16.0 50.0 23.0zM58.3 24.3Q62.8 18.4 64.8 4.3Q58.2 16.9 58.3 24.3zM65.9 28.2Q71.9 23.9 78.2 11.2Q68.0 21.1 65.9 28.2zM71.8 34.1Q78.9 32.0 88.8 21.8Q76.1 28.1 71.8 34.1zM75.7 41.7Q83.1 41.8 95.7 35.2Q81.6 37.2 75.7 41.7zM77.0 50.0Q84.0 52.4 98.0 50.0Q84.0 47.6 77.0 50.0zM75.7 58.3Q81.6 62.8 95.7 64.8Q83.1 58.2 75.7 58.3zM71.8 65.9Q76.1 71.9 88.8 78.2Q78.9 68.0 71.8 65.9zM65.9 71.8Q68.0 78.9 78.2 88.8Q71.9 76.1 65.9 71.8zM58.3 75.7Q58.2 83.1 64.8 95.7Q62.8 81.6 58.3 75.7zM52.8 76.9Q51.2 84.1 55.0 97.7Q55.9 83.6 52.8 76.9zM47.2 76.9Q44.1 83.6 45.0 97.7Q48.8 84.1 47.2 76.9zM39.0 74.7Q34.0 80.1 30.5 93.9Q38.4 82.0 39.0 74.7zM31.9 70.1Q25.5 73.7 17.9 85.7Q29.0 76.9 31.9 70.1zM26.6 63.5Q19.4 64.9 8.4 74.0Q21.8 69.1 26.6 63.5zM23.6 55.6Q16.2 54.7 3.0 60.0Q17.2 59.4 23.6 55.6zM23.1 47.2Q16.4 44.1 2.3 45.0Q15.9 48.8 23.1 47.2zM25.3 39.0Q19.9 34.0 6.1 30.5Q18.0 38.4 25.3 39.0zM29.9 31.9Q26.3 25.5 14.3 17.9Q23.1 29.0 29.9 31.9zM36.5 26.6Q35.1 19.4 26.0 8.4Q30.9 21.8 36.5 26.6z" fill="currentColor"/></symbol>
<symbol id="down" viewBox="0 0 14 16"><path d="M7 1v9m0 0L3 6m4 4 4-4M1 14h12" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></symbol>
</defs></svg>"""

THEME = """<button class="theme" type="button" aria-label="Switch between light and dark"><svg class="moon" width="18" height="18" viewBox="0 0 18 18" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 10.500A6.500 6.500 0 0 1 7.500 3 6.500 6.500 0 1 0 15 10.500z"/></svg><svg class="sun" width="18" height="18" viewBox="0 0 18 18" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" aria-hidden="true"><circle cx="9" cy="9" r="3.200"/><path d="M9 1.500v1.800M9 14.700v1.800M1.500 9h1.800M14.700 9h1.800M3.700 3.700l1.300 1.300M13 13l1.300 1.300M3.700 14.300 5 13M13 5l1.300-1.300"/></svg></button>"""

DOWNLOAD = '<a class="button" href="/barricade/download"><svg width="14" height="16" aria-hidden="true"><use href="#down"/></svg>Download for Mac</a>'


def dots():
    held = {13, 22, 26, 28}
    return "".join(f'<i class="{"held" if i in held else "on"}"></i>' if i >= 7 else "<i></i>" for i in range(30))


APP = f"""<figure class="stage" data-reveal>
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
    get = '<a class="get" href="/barricade/download">Download</a>' if download else ""
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
<link rel="icon" href="/eye.svg" type="image/svg+xml">
<link rel="icon" href="/eye-64.png" type="image/png" sizes="64x64">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="stylesheet" href="/styles.css">
<script src="/theme.js"></script>
<script src="/reveal.js" defer></script>
</head>
<body>
{ICONS}
<header class="top"><div class="wrap nav">
  <a class="word" href="/"><svg class="mark" width="26" height="26" aria-hidden="true"><use href="#eye"/></svg>Northlight</a>
  <nav class="tabs" aria-label="Main">{tabs}</nav>
  <div class="right">{THEME}{get}</div>
</div></header>

<main>
{body}
</main>

<footer class="foot"><div class="wrap"><span>© 2026 Northlight</span><a href="/about">About</a></div></footer>
</body>
</html>
"""
    return SITE / path, html


PAGES = [
    page("index.html", "Northlight", "Northlight makes calm apps that help you keep the habits you chose.", "Home", """  <section class="wrap hero home">
    <h1>Apps for the person you're trying to be.</h1>
    <p class="lede">Northlight makes calm apps that help you keep the habits you chose.</p>
  </section>

  <section class="wrap apps" aria-label="Apps">
    <a class="product" href="/barricade" data-reveal>
      <div class="pic barricade"><svg width="120" height="96" aria-hidden="true"><use href="#barricade"/></svg></div>
      <div class="text"><span class="for">For Mac</span><h2>Barricade</h2><p>Block the sites that pull you back, in every browser. It stays on through the nights you wish it wouldn't.</p><span class="more">See Barricade →</span></div>
    </a>
    <a class="product" href="/pulse" data-reveal>
      <div class="pic" style="background:#0A120E"><img src="/pulse/icon.png" alt="" width="230" height="230"></div>
      <div class="text"><span class="for">For iPhone · coming soon</span><h2>Pulse</h2><p>Your workouts, meals, sleep and habits in one place, with an AI coach that knows all of it.</p><span class="more">See Pulse →</span></div>
    </a>
  </section>

  <section class="wrap closing" data-reveal>
    <p>A few apps, each made with care.</p>
    <a href="/about">About Northlight →</a>
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
    <div class="card" data-reveal><svg width="30" height="30" viewBox="0 0 30 30" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><rect x="3" y="6" width="24" height="17" rx="3"/><path d="M3 11h24"/></svg><h2>Works everywhere</h2><p>Every browser, private windows included. There's no other door.</p></div>
    <div class="card" data-reveal><svg width="30" height="30" viewBox="0 0 30 30" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="6" y="13" width="18" height="12" rx="3"/><path d="M10 13V9a5 5 0 0 1 10 0v4"/></svg><h2>Stays on</h2><p>You can't switch it off on a whim. Changing your mind takes seven days.</p></div>
    <div class="card" data-reveal><svg width="30" height="30" viewBox="0 0 30 30" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 4 5 8v7c0 6 4.500 9.500 10 11 5.500-1.500 10-5 10-11V8z"/><path d="m11 15 3 3 5-6"/></svg><h2>Private</h2><p>No account, nothing sent anywhere. Everything stays on your Mac.</p></div>
  </section>

  <section class="wrap how" aria-labelledby="how">
    <h2 id="how" data-reveal>How it works</h2>
    <ol class="steps">
      <li data-reveal><i>1</i><b>Add a site</b><span>Type it in from the menu bar. It takes a second.</span></li>
      <li data-reveal><i>2</i><b>It's blocked</b><span>Right away, everywhere on your Mac. Adult sites are blocked automatically.</span></li>
      <li data-reveal><i>3</i><b>Watch the days add up</b><span>Every protected day fills a dot.</span></li>
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
    <img class="icon" src="/pulse/icon.png" alt="Pulse app icon" width="68" height="68">
    <h1>Your health, in one place.</h1>
    <p class="lede">Pulse keeps your workouts, meals, sleep and habits together, with an AI coach that knows all of it. For iPhone.</p>
    <span class="soon">Coming soon</span>
  </section>"""),

    page("about/index.html", "About · Northlight", "Northlight makes calm apps that help you keep the habits you chose.",
         "About", """  <section class="wrap hero">
    <h1>Calm tools for the habits you chose.</h1>
    <p class="lede">Northlight makes apps for the everyday things that are hard to stick to: what you block, how you train, what you eat.</p>
  </section>

  <section class="wrap name" data-reveal>
    <div>
      <h2>The name</h2>
      <p>North light is the steady, even light from a north-facing window. Painters like to work by it because it stays the same all day.</p>
      <p>That's how a Northlight app is meant to feel: calm, clear, and the same on a good day as on a hard one.</p>
    </div>
  </section>

  <section class="wrap ways" aria-labelledby="ways">
    <h2 id="ways" data-reveal>How the apps are made</h2>
    <div class="three plain">
      <div data-reveal><h3>Small on purpose</h3><p>Each app does one job and does it properly.</p></div>
      <div data-reveal><h3>Calm to use</h3><p>No noise, no clutter. Open it, do the thing, get on with your day.</p></div>
      <div data-reveal><h3>Used every day</h3><p>Each app is used daily by the person who makes it. Anything annoying gets fixed.</p></div>
    </div>
  </section>

  <section class="wrap list" aria-labelledby="apps">
    <h2 id="apps" data-reveal>The apps</h2>
    <a class="line" href="/barricade" data-reveal><span class="icon barricade small"><svg width="26" height="21" aria-hidden="true"><use href="#barricade"/></svg></span><span><b>Barricade</b><span>Block the sites that pull you back. For Mac.</span></span><span class="go">→</span></a>
    <a class="line" href="/pulse" data-reveal><img class="icon small" src="/pulse/icon.png" alt="" width="48" height="48"><span><b>Pulse</b><span>Your health in one place, with an AI coach. For iPhone, coming soon.</span></span><span class="go">→</span></a>
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
