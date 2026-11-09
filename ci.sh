#!/bin/bash
# Northlight Studio website's checks. CI runs exactly this on the Mac mini; run it locally too.
set -euo pipefail
cd "$(dirname "$0")"

# The site is plain HTML and CSS in site/, served as-is by Vercel (vercel.json). Check every page
# and link the way Vercel will serve them.
python3 tests/check_site.py
