#!/usr/bin/env bash
# Rebuild assets/Delon-Pyle-Resume.pdf from resume.html with headless Edge/Chrome.
# Run from Git Bash: ./scripts/build-resume-pdf.sh
set -euo pipefail
cd "$(dirname "$0")/.."

for b in "/c/Program Files (x86)/Microsoft/Edge/Application/msedge.exe" \
         "/c/Program Files/Google/Chrome/Application/chrome.exe"; do
  [ -x "$b" ] && browser="$b" && break
done
: "${browser:?no Edge or Chrome found}"

out="$(cygpath -w "$PWD/assets/Delon-Pyle-Resume.pdf")"
src="file:///$(cygpath -m "$PWD/resume.html")"
# virtual-time-budget gives the Google Fonts a moment to load before printing
"$browser" --headless --disable-gpu --no-pdf-header-footer \
  --virtual-time-budget=12000 --print-to-pdf="$out" "$src"
echo "wrote assets/Delon-Pyle-Resume.pdf"
