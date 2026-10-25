# delonpyle.com

Static portfolio site, no build step. See README.md for layout and deployment.

## When Delon shares a new document (certificate, diploma, transcript, job letter…)

The resume must stay in sync with the site. Every new document means updating **all** of:

1. **Image** — render it into `assets/` (PDFs: pypdfium2, scale 3, longest side 1600px, JPEG q85).
   Name it `cert-<slug>.jpg`, or `diploma-<slug>.jpg` for academic awards.
2. **`index.html`**
   - Add a `.cert-card` to the `.cert-wall`, ordered newest first, with real `width`/`height`.
   - Bump the "Certifications" stat (`data-target`) for certifications — not for diplomas/degrees.
   - Academic awards also belong in the Education `.xp` list, with a `.view-cert` button
     whose `data-cert` matches the image `src`.
   - New roles go in Experience; update the "Roles held" stat.
3. **`resume.html`** — add it to the matching section (Certifications & Courses, Education,
   Employment History or Internships). Keep the cert list in the same order as the cert wall.
4. **PDF** — run `./scripts/build-resume-pdf.sh`, then read the PDF back and check the layout
   (two Letter pages, navy sidebar on every page, nothing orphaned).
5. Update `<lastmod>` in `sitemap.xml`.

Take dates, titles and issuers from the document itself. Where the document disagrees with what
the site or resume already says (grade, dates, course title), use the document and tell Delon.
If a document has no date, say what year you assumed.

## Personal details kept off the public resume

The site is public, so `resume.html` and the PDF deliberately leave out: street address, place of
birth, gender, and referees' names, phone numbers and emails. Don't add them back unless Delon
asks for that specific detail to be published.

## Git

The remote is `https://Delon17@github.com/Delon17/delonportfolio.git` — the username in the URL
makes Git Credential Manager use the Delon17 account rather than another saved GitHub login.
Pushing to `main` redeploys the site.
