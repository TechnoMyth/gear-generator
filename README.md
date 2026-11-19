# Gear Generator docs

The public user guide for the Gear Generator Unreal Engine plugin, published at
https://docs.technomyth.com/gear-generator/. Bug reports and questions go in this repository's
[issues](https://github.com/TechnoMyth/gear-generator/issues).

The guide itself is written in the plugin, at `Plugins/GearGenerator/Docs`, and ships with it. This repository adds the
site around a copy of it.

## Updating

1. Edit the guide in the plugin.
2. Run `python sync_docs.py` to copy it into `docs`. It looks for the plugin at
   `../PluginDev/Plugins/GearGenerator`; pass another path as the first argument if it is elsewhere.
3. Commit and push to `main`. `.github/workflows/publish.yml` builds the site with MkDocs Material and pushes it to
   the `gh-pages` branch, which Pages serves.

To preview locally: `pip install mkdocs-material`, then `mkdocs serve`.

## How it is hosted

- **This repository:** Settings > Pages deploys from the `gh-pages` branch. It has no custom domain of its own: as a
  project site it takes the organization site's domain, so it appears under `/gear-generator/`.
- **Organization site:** `TechnoMyth/technomyth.github.io` holds the index page listing the plugins, and has the custom
  domain `docs.technomyth.com` set in its Settings > Pages. Another plugin's docs repository appears beside this one
  under its own path.
- **DNS:** `docs` is a `CNAME` to `technomyth.github.io`, proxied by Cloudflare. Cloudflare provides the HTTPS
  certificate and redirects HTTP to HTTPS (SSL/TLS mode **Full**, **Always Use HTTPS** on), so GitHub's **Enforce
  HTTPS** isn't available or needed. Don't combine Cloudflare's **Flexible** mode with GitHub's Enforce HTTPS, or the
  two redirect each other in a loop.
- **Access:** the TechnoMyth organization only allows approved apps. Pushing over HTTPS uses Git Credential Manager,
  which needs organization access granted for TechnoMyth.
