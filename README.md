# Gear Generator public docs

The source for the public documentation site, published with GitHub Pages. The guide itself lives in the plugin at
`Plugins/GearGenerator/Docs` and ships with it; this folder only adds the site around it. Nothing here ships to Fab.

## Setting up the site

The site is published at https://docs.technomyth.com/gear-generator/, from the `TechnoMyth/gear-generator` repository. Its issue tracker is the
plugin's support contact.

1. **Organization site, once:** create a public repository `TechnoMyth/technomyth.github.io` with a short `index.html`
   or `index.md` listing the plugins. In its **Settings > Pages**, publish from its `main` branch and set the custom
   domain to `docs.technomyth.com`. At the DNS provider, add a `CNAME` record from `docs` to `technomyth.github.io`.
   In the organization's **Settings > Pages**, verify `technomyth.com`, so no other account can claim its subdomains.
   Tick **Enforce HTTPS** once the certificate is issued.
2. **This site:** create a public repository `TechnoMyth/gear-generator`, run `python sync_docs.py` to copy the guide
   in, and push the contents of this folder to its `main` branch.
3. Every push to `main` runs `.github/workflows/publish.yml`, which builds the site with MkDocs Material and pushes it
   to the `gh-pages` branch.
4. In the repository's **Settings > Pages**, set the source to **Deploy from a branch**, branch `gh-pages`. Project
   sites take the organization site's domain, so it appears at `docs.technomyth.com/gear-generator/` with no `CNAME`
   file of its own.

## Updating

Edit the guide in the plugin, run `python sync_docs.py`, and push. To preview locally:
`pip install mkdocs-material`, then `mkdocs serve`.
