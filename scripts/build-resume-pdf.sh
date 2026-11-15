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
# virtual-time-budget gives the Google Fonts a moment to load before printing. If they
# arrive late, the wider fallback fonts push the resume onto a third page, so retry.
for attempt in 1 2 3 4 5; do
  "$browser" --headless --disable-gpu --no-pdf-header-footer \
    --virtual-time-budget=12000 --print-to-pdf="$out" "$src" 2>/dev/null
  pages=$(python -I -c "import pypdfium2,sys; print(len(pypdfium2.PdfDocument(sys.argv[1])))" "$out" 2>/dev/null || echo 0)
  [ "$pages" = 2 ] && break
  echo "attempt $attempt: $pages pages, retrying"
done
echo "wrote assets/Delon-Pyle-Resume.pdf ($pages pages)"
