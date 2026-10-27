# delonpyle.com

Static portfolio site, no build step. See README.md for layout and deployment.

## When Delon shares a new document (certificate, diploma, transcript, job letter…)

The resume must stay in sync with the site. Every new document means updating **all** of:

1. **Image** — render it into `assets/` (PDFs: pypdfium2, scale 3, longest side 1600px), saved as
   WebP quality 80 via Pillow. Name it `cert-<slug>.webp`, or `diploma-<slug>.webp` for academic
   awards — the Certifications stat counts `cert-` images, so the prefix matters.
   Certificates are published without a watermark (Delon's choice).
   Transcripts are `transcript-<slug>.webp` and get a card on the wall plus a "View transcript"
   button next to the matching Education entry's "View diploma".
2. **`index.html`**
   - Add a `.cert-card` to the `.cert-wall`, ordered newest first, with real `width`/`height`.
   - The stats band counts roles, `cert-` images and skill tags itself (`data-count`); just keep
     `data-target` roughly right as the no-JavaScript fallback.
   - Academic awards also belong in the Education `.xp` list, with a `.view-cert` button
     whose `data-cert` matches the image `src`.
   - New roles go in Experience.
   - Milestones (a finished degree, a new role, a Master's) also go in the Journey `<ol>`: flip the
     matching `future` item to `done`, and move `data-state="current"` (and its "You are here"
     badge) to the newest role. The 3D path and the progress count are drawn from that list.
3. **`resume.html`** — add it to the matching section (Certifications & Courses, Education,
   Employment History or Internships). Keep the cert list in the same order as the cert wall.
4. **PDF** — run `./scripts/build-resume-pdf.sh`, then read the PDF back and check the layout
   (two Letter pages, navy sidebar on every page, nothing orphaned).
5. Update `<lastmod>` in `sitemap.xml`.

Take dates, titles and issuers from the document itself. Where the document disagrees with what
the site or resume already says (grade, dates, course title), use the document and tell Delon.
Documents that show a date of birth, candidate/ID numbers or similar (e.g. CSEC result slips) are
never published as images — list the qualification and grades as text instead.
If a document has no date, say what year you assumed.

The resume photo is `assets/delon-pyle-resume.jpg` (320px JPEG), not the WebP portrait: Chrome
embeds WebP uncompressed when printing, which bloated the PDF to 2 MB.

## Skills

Skills live in three places that must match: the `#skills` tags in `index.html`, the Skills list in
`resume.html` (then rebuild the PDF), and the `SKILLS` / `RELATED` arrays in the hero's skills-network
script (each skill's "used" line is its tooltip; only claim uses the site already states).

## Personal details kept off the public resume

The site is public, so `resume.html` and the PDF deliberately leave out: street address, place of
birth, gender, and referees' names, phone numbers and emails. Don't add them back unless Delon
asks for that specific detail to be published.

## Git

The remote is `https://Delon17@github.com/Delon17/delonportfolio.git` — the username in the URL
makes Git Credential Manager use the Delon17 account rather than another saved GitHub login.
Pushing to `main` redeploys the site.
