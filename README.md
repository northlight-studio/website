# Northlight Studio website

The Northlight Studio website: the studio home page and a page for each project, starting with Barricade.

| Page | File |
|---|---|
| Studio home, `/` | `site/index.html` |
| Barricade, `/barricade` | `site/barricade/index.html` |
| Barricade download, `/barricade/download` | `site/barricade/download/index.html` (holding page until the signed installer exists) |

The look is direction A, Horizon, from the website mocks: the same calm style as Barricade's app and
block page.

## Develop

Plain HTML and CSS, no build step. To preview:

```bash
python3 -m http.server 8000 --directory site
```

Vercel serves `site/` as configured in `vercel.json`, with clean URLs (`/barricade` serves
`site/barricade/index.html`) and security headers.

`./ci.sh` runs every check, exactly as CI does on the Mac mini for each pull request and push to
`main`.

Started with `new-project` from [northlight-studio/dev-tools](https://github.com/northlight-studio/dev-tools).
