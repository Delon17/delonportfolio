# delonpyle.com

Personal portfolio for Delon Pyle — a single static page, no build step.

```
index.html      the whole site (markup, CSS and JS inline)
assets/         portrait + certificate images
_headers        Cloudflare Pages response headers
robots.txt
sitemap.xml
```

## Editing

Open `index.html` in a browser to preview — everything is inline, so there is
nothing to compile or install. Sections are marked with `<!-- ===== NAME ===== -->`
comments, and the spots most likely to change carry an `<!-- EDIT: ... -->` note.

To add a certificate, drop the image in `assets/` and copy an existing
`.cert-card` block. Set `width` and `height` on the `<img>` to the image's real
pixel size so the page doesn't shift while it loads.

## Deploying to Cloudflare Pages

One-time setup:

1. Cloudflare dashboard → **Workers & Pages** → **Create** → **Pages** →
   **Connect to Git**, and pick `Delon17/Portfolio`.
2. Build settings — this is a plain static site, so leave them empty:
   - Framework preset: **None**
   - Build command: *(blank)*
   - Build output directory: `/`
3. **Save and Deploy**. You get a `*.pages.dev` URL.

Custom domain:

4. In the Pages project → **Custom domains** → **Set up a custom domain** →
   `delonpyle.com`. Repeat for `www.delonpyle.com` if you want both.
5. If `delonpyle.com` already uses Cloudflare for DNS, the records are created
   for you. If it doesn't, move the domain's nameservers to Cloudflare first.

After that, every push to `main` redeploys automatically.

## Notes

- Fonts come from Google Fonts over the network; the page falls back to system
  fonts if they don't load.
- Images were originally base64-inlined in the HTML (870 KB). They now live in
  `assets/`, which cuts the HTML to ~40 KB and lets the browser cache and
  lazy-load them.
- Absolute URLs in the `og:`/`twitter:` meta tags, the canonical link and
  `sitemap.xml` all point at `https://delonpyle.com/`. Update them together if
  the domain ever changes.
