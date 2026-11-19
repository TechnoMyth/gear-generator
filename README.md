# Gear Generator docs

The public documentation for Gear Generator, published at https://docs.technomyth.com/gear-generator/. Bug reports
and questions for every engine go in this repository's [issues](https://github.com/TechnoMyth/gear-generator/issues),
labelled by engine.

The site is organised by engine, under one landing page (`docs/index.md`):

| Engine | Pages | Guide written in |
|---|---|---|
| Unreal Engine | `docs/unreal/`, at `/gear-generator/unreal/` | The plugin, at `Plugins/GearGenerator/Docs` in the PluginDev repository |
| Unity | `docs/unity/`, at `/gear-generator/unity/` | The package, at `Packages/com.technomyth.geargenerator/Documentation~` in the Unity GearGenerator repository |

Each guide ships with its product; this repository adds the site around copies of them. The shipped products link to
their engine's page, so those paths must not change. Another engine gets its own folder and a line in `sync_docs.py`.

## Updating

1. Edit the guide in its product repository.
2. Run `python sync_docs.py` to copy the guides in. It expects the product repositories beside this clone
   (`../PluginDev` and `../../Unity/GearGenerator`), skips any it can't find, and takes `--unreal` and `--unity`
   paths otherwise. Add the Unity guide to the `nav` in `mkdocs.yml` when it is first published.
3. Commit and push to `main`. `.github/workflows/publish.yml` builds the site with MkDocs Material and pushes it to
   the `gh-pages` branch, which Pages serves.

To preview locally: `pip install mkdocs-material`, then `mkdocs serve`.

## How it is hosted

- **This repository:** Settings > Pages deploys from the `gh-pages` branch. It has no custom domain of its own: as a
  project site it takes the organization site's domain, so it appears under `/gear-generator/`, with each engine
  below that.
- **Organization site:** `TechnoMyth/technomyth.github.io` holds the index page listing the plugins, and has the custom
  domain `docs.technomyth.com` set in its Settings > Pages. Another plugin's docs repository appears beside this one
  under its own path.
- **DNS:** `docs` is a `CNAME` to `technomyth.github.io`, proxied by Cloudflare. Cloudflare provides the HTTPS
  certificate and redirects HTTP to HTTPS (SSL/TLS mode **Full**, **Always Use HTTPS** on), so GitHub's **Enforce
  HTTPS** isn't available or needed. Don't combine Cloudflare's **Flexible** mode with GitHub's Enforce HTTPS, or the
  two redirect each other in a loop.
- **Access:** the TechnoMyth organization only allows approved apps. Pushing over HTTPS uses Git Credential Manager,
  which needs organization access granted for TechnoMyth.
