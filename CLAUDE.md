# Northlight Studio website

The Northlight Studio website: the studio home page and a page for each project, starting with Barricade. See README.md for what exists. Same owner and conventions as Pulse, Let's Go and Lyceum.

## Stack
- Plain HTML and CSS in `site/`, no build step on Vercel. Vercel serves `site/` as-is (`vercel.json`: clean URLs, so `/barricade` is `site/barricade/index.html`).
- **The pages are generated.** Every page shares the header (the studio's name and the tabs: Home, Barricade, Pulse, About), icons and footer, so they're written by `tools/build_pages.py` and committed. Edit pages there, run `python3 tools/build_pages.py`, and commit the result; `ci.sh` fails when `site/` is out of date. Never hand-edit the HTML in `site/`.
- One stylesheet, `site/styles.css`, in the Calm look (round 2 of the website mocks): centered, lots of white, pill tabs, one orange button, a picture of the app. Light and dark follow the system. Copy is plain and non-technical: say what an app does for the person, never how it works underneath.
- No inline scripts: the Content-Security-Policy in `vercel.json` blocks them. Internal links are root paths (`/barricade`).
- Each project gets a folder and a tab. Barricade's download link is `/barricade/download`; it's a holding page until the signed, notarized installer exists, then a redirect in `vercel.json` to the file.
- `tests/check_site.py` (run by `ci.sh`) checks every page's structure and metadata and that every internal link resolves.

## Rules
- **Recommend what's best, never what's easiest.** When laying out options and picking one, pick the one that's best for the product and the person using it. Effort and diff size are not reasons, and not tiebreakers either. If the best option is a big job, recommend it and say how big.
- **Weeks start Monday** if anything ever needs a calendar week.
- **MVVM-ish**: views stay dumb. Logic that can be tested lives in plain types.
- **Sample means sample.** Anything shown as a real person, place, count or listing that isn't one is marked Sample.
- Saves and network calls log on failure and surface to the user. Never fail silently.
- Small focused files.
- Never commit secrets: the App Store Connect key (`*.p8`, `asc_api_key.json`), `.env`, API keys.

## CI
`./ci.sh` is the project's whole check. This repo is **public** (Vercel's free plan only deploys an organization's repos when they're public), so `.github/workflows/ci.yml` runs it on GitHub's own `ubuntu-latest` runners, free for public repos, never on the Mac mini: anyone can open a pull request on a public repo, and a self-hosted runner would run their code on that machine. Keep it that way. Nothing secret goes in this repo.

## Deploys
Vercel project `northlight-studio` (account yasser100ali) is linked to this repo: every push to `main` deploys production at https://northlight-studio-seven.vercel.app, and pull requests get preview deployments.

## Pull requests
- **Merge it yourself.** When your PR is ready, merge it, squashed like the rest of `main`: `gh pr merge <n> --squash`. Don't hand it back to be merged. Ready means its checks finished green, it merges cleanly with `main`, and your own pass over the diff found nothing.
- **Wait for the checks in the same turn, then merge** (`gh pr checks <n> --watch --fail-fast`). A PR that starts no checks merges as soon as it's open.
- **Never merge while a check is running or red.** Red: fix it on the branch, push, wait again. A conflict with `main`: bring `main` in, push, wait again. If it won't go green, leave it open and say why.
- **One PR per task.** Follow-ups to the same ask go on the open PR's branch. Check it hasn't merged before pushing more.
- Merge as the owner, not with a workflow's `GITHUB_TOKEN`: a merge made that way starts no workflows.
- Don't merge when told to hold it or that someone wants to look first.
- Don't schedule self check-ins on a PR. Wait for its checks in the turn, merge, report the link.
