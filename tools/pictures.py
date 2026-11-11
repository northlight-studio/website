"""The pictures of each app that the pages show: Barricade's window, and a phone for each iPhone app.

Every picture is drawn in HTML and CSS (site/styles.css: .app for the Mac window, .phone for a
phone), in the app's own colours, and every one is sample data and says so in its caption.
"""


def dots():
    held = {13, 22, 26, 28}
    return "".join(f'<i class="{"held" if i in held else "on"}"></i>' if i >= 7 else "<i></i>" for i in range(30))


BARRICADE = f"""<figure class="stage" data-reveal>
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


def phone(app, label, colours, screen):
    """A phone showing one screen of an app. `colours` sets the screen's own palette."""
    return f"""<figure class="stage" data-reveal>
      <div class="phone" role="img" aria-label="{label}" style="{colours}">
        <div class="scr" aria-hidden="true">
{screen}
        </div>
      </div>
      <figcaption>{app}, with sample data</figcaption>
    </figure>"""


# Pulse and Runway share the Midnight Bronze look: near-black, peach for what's yours, green for good news.
PULSE = phone("Pulse", "Pulse's Today screen: sleep, steps and protein, today's workout, and a note from the coach",
              "--scr:#040405;--ink:#FFFFFF;--dim:#9A9AA0;--card:#17171A;--hue:#FAC79E", """          <span class="p-eye">Tuesday</span>
          <div class="p-big">Today</div>
          <div class="p-tiles">
            <div class="p-card"><span class="p-eye">Sleep</span><b>7h 42m</b></div>
            <div class="p-card"><span class="p-eye">Steps</span><b>8,214</b></div>
            <div class="p-card"><span class="p-eye">Protein</span><b>96 g</b></div>
          </div>
          <div class="p-card"><span class="p-eye">Workout</span><b>Push day</b><span class="p-dim">Bench, incline press, dips and two more</span></div>
          <div class="p-card"><span class="p-eye p-hue">Coach</span><span>You slept 40 minutes less than usual. Keep today's lifts and skip the extra set.</span></div>
          <div class="p-card"><div class="p-row"><span>Dinner</span><span class="p-dim">Chicken, rice, greens</span></div></div>""")

RUNWAY = phone("Runway", "Runway's Home screen: net worth and its line over the year, what moved it this month, and a suggested move",
               "--scr:#040405;--ink:#FFFFFF;--dim:#9A9AA0;--card:#17171A;--hue:#B7C9E0", """          <span class="p-eye">Net worth</span>
          <div class="p-big">$48,210</div>
          <span style="color:#4FD182">Up $1,340 this month</span>
          <svg class="p-art" viewBox="0 0 264 84" aria-hidden="true"><path d="M2 70C30 66 44 60 66 58s34 4 54-6 30-6 48-16 34-8 50-18 26-6 44-10" fill="none" stroke="#B7C9E0" stroke-width="2.4" stroke-linecap="round"/><circle cx="262" cy="8" r="4" fill="#B7C9E0"/></svg>
          <div class="p-tiles">
            <div class="p-card"><span class="p-eye">Earned</span><b>$5,200</b></div>
            <div class="p-card"><span class="p-eye">Spent</span><b>$3,610</b></div>
            <div class="p-card"><span class="p-eye">Kept</span><b>31%</b></div>
          </div>
          <div class="p-card"><span class="p-eye" style="color:#FAC79E">A move worth making</span><span>$4,100 is sitting in checking. In savings it would earn about $14 a month.</span></div>
          <div class="p-card"><div class="p-row"><span>This week</span><span class="p-dim">$212 of $350</span></div></div>""")

COSMOPOLIS = phone("Cosmopolis", "Cosmopolis's Atrium: the quote of the day, and the subjects as arched doors",
               "--scr:#0B0F0E;--ink:#EEEAE2;--dim:#B8B2A5;--card:#121816;--hue:#CDAA63", """          <span class="p-eye">Good evening</span>
          <div class="p-serif">I love the sticky little leaves as they open in spring.</div>
          <span class="p-dim">Dostoevsky, The Brothers Karamazov</span>
          <div class="p-tiles doors">
            <div><svg viewBox="0 0 60 84" aria-hidden="true"><path d="M5 82V32a25 25 0 0 1 50 0v50z" fill="#121816" stroke="#CDAA63" stroke-width="1.6"/><path d="M30 12v70" stroke="#6F5523" stroke-width="1.2"/></svg><span>Letters</span></div>
            <div><svg viewBox="0 0 60 84" aria-hidden="true"><path d="M5 82V32a25 25 0 0 1 50 0v50z" fill="#121816" stroke="#8FA8E6" stroke-width="1.6"/><path d="M30 12v70" stroke="#3E4A66" stroke-width="1.2"/></svg><span>Mathematics</span></div>
            <div><svg viewBox="0 0 60 84" aria-hidden="true"><path d="M5 82V32a25 25 0 0 1 50 0v50z" fill="#121816" stroke="#D98E70" stroke-width="1.6"/><path d="M30 12v70" stroke="#6A4435" stroke-width="1.2"/></svg><span>History</span></div>
          </div>
          <div class="p-card"><span class="p-eye p-hue">Up next</span><b>The Russians, lesson 3</b><span class="p-dim">About ten minutes</span></div>""")

LETS_GO = phone("Let's Go", "Let's Go's map at night: glowing pins for what's on nearby, a ring showing a ten-minute walk, and one suggestion",
                "--scr:#0D0C12;--ink:#F6F2EA;--dim:#A8A3B3;--card:#24212C;--hue:#FF5B3A", """          <span class="p-eye">Tonight, near you</span>
          <svg class="p-art map" viewBox="0 0 264 250" aria-hidden="true"><path d="M-10 60h290M-10 130h290M-10 200h290M50-10v270M132-10v270M214-10v270" stroke="#24212C" stroke-width="9"/><path d="M-10 250 280 20" stroke="#24212C" stroke-width="6"/><circle cx="132" cy="130" r="92" fill="none" stroke="#7FB2FF" stroke-width="1.4" stroke-dasharray="3 6"/><circle cx="132" cy="130" r="7" fill="#0A84FF" stroke="#F6F2EA" stroke-width="2"/><circle cx="186" cy="84" r="20" fill="#FF5B3A" opacity=".22"/><circle cx="186" cy="84" r="8" fill="#FF5B3A"/><circle cx="70" cy="176" r="16" fill="#FFB547" opacity=".22"/><circle cx="70" cy="176" r="7" fill="#FFB547"/><circle cx="212" cy="196" r="14" fill="#4FD08E" opacity=".22"/><circle cx="212" cy="196" r="6" fill="#4FD08E"/><circle cx="60" cy="52" r="12" fill="#FF9A80" opacity=".22"/><circle cx="60" cy="52" r="5" fill="#FF9A80"/></svg>
          <div class="p-card"><span class="p-eye p-hue">Wren</span><span>Pickup soccer at the park. Four of six are in, and it's a six-minute walk. Leave by 6:40.</span><span class="p-btn">I'm in</span></div>""")

PARCEL = phone("Parcel", "Parcel showing a house: its floor plan, an early price, and what has been checked",
               "--scr:#0E1214;--ink:#ECE7DC;--dim:#9AA19F;--card:#151B1E;--hue:#F5B65A", """          <span class="p-eye">The hillside house</span>
          <svg class="p-art" viewBox="0 0 264 150" aria-hidden="true"><rect x="6" y="6" width="252" height="138" fill="#151B1E" stroke="#ECE7DC" stroke-width="2.4"/><path d="M110 6v84M6 90h160M166 90v54M190 6v48M190 54h68" stroke="#ECE7DC" stroke-width="1.6" fill="none"/><path d="M110 40v22M70 90h22" stroke="#151B1E" stroke-width="3"/><text x="58" y="52" fill="#9AA19F" font-size="10" text-anchor="middle">Kitchen</text><text x="150" y="52" fill="#9AA19F" font-size="10" text-anchor="middle">Living</text><text x="224" y="34" fill="#9AA19F" font-size="10" text-anchor="middle">Bath</text><text x="86" y="122" fill="#9AA19F" font-size="10" text-anchor="middle">Bedroom</text><text x="212" y="104" fill="#9AA19F" font-size="10" text-anchor="middle">Studio</text></svg>
          <span class="p-eye">Early estimate</span>
          <div class="p-big">$612,000</div>
          <div class="p-card">
            <div class="p-row"><span>Structure</span><span style="color:#4CC38A">Checked</span></div>
            <div class="p-row"><span>Energy rules</span><span style="color:#4CC38A">Checked</span></div>
            <div class="p-row"><span>The slope</span><span class="p-hue">Needs a soils report</span></div>
          </div>""")
