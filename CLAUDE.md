# Northlight Studio website

The Northlight Studio website: the studio home page and a page for each project, starting with Barricade. See README.md for what exists. Same owner and conventions as Pulse, Let's Go and Lyceum.

## Stack
- Plain HTML and CSS in `site/`, no build step. Vercel serves `site/` as-is (`vercel.json`: clean URLs, so `/barricade` is `site/barricade/index.html`).
- One stylesheet, `site/styles.css`, in the Horizon look shared with Barricade's app and block page: thin display type, one band of the barricade's stripe, the 30 dots. Light and dark follow the system.
- No inline scripts: the Content-Security-Policy in `vercel.json` blocks them. Internal links are root paths (`/barricade`).
- Each project gets a folder: `site/<project>/index.html`. Barricade's download link is `/barricade/download`; it's a holding page until the signed, notarized installer exists, then a redirect in `vercel.json` to the file.
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
`./ci.sh` is the project's whole check. `.github/workflows/ci.yml` runs exactly that on the Mac mini (the organization's self-hosted runners, labels `self-hosted, macOS, ARM64`) for every pull request and every push to `main`. Run it before pushing when you can, and say plainly when something wasn't built or tested.

## Pull requests
- **Merge it yourself.** When your PR is ready, merge it, squashed like the rest of `main`: `gh pr merge <n> --squash`. Don't hand it back to be merged. Ready means its checks finished green, it merges cleanly with `main`, and your own pass over the diff found nothing.
- **Wait for the checks in the same turn, then merge** (`gh pr checks <n> --watch --fail-fast`). A PR that starts no checks merges as soon as it's open.
- **Never merge while a check is running or red.** Red: fix it on the branch, push, wait again. A conflict with `main`: bring `main` in, push, wait again. If it won't go green, leave it open and say why.
- **One PR per task.** Follow-ups to the same ask go on the open PR's branch. Check it hasn't merged before pushing more.
- Merge as the owner, not with a workflow's `GITHUB_TOKEN`: a merge made that way starts no workflows.
- Don't merge when told to hold it or that someone wants to look first.
- Don't schedule self check-ins on a PR. Wait for its checks in the turn, merge, report the link.
