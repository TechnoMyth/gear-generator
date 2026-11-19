"""Copies the user guide from the plugin into this site's docs folder, so the site and the shipped guide match.

  python sync_docs.py [path to the GearGenerator plugin]
"""

import os
import shutil
import sys

here = os.path.dirname(os.path.abspath(__file__))
plugin = sys.argv[1] if len(sys.argv) > 1 else os.path.join(here, "..", "..", "Plugins", "GearGenerator")
source = os.path.join(plugin, "Docs")
target = os.path.join(here, "docs")
# The custom domain file belongs to the site, not the guide
cname_path = os.path.join(target, "CNAME")
cname = open(cname_path, encoding="utf-8").read() if os.path.isfile(cname_path) else None
if os.path.isdir(target):
    shutil.rmtree(target)
shutil.copytree(source, target)
if cname is not None:
    with open(cname_path, "w", encoding="utf-8") as file:
        file.write(cname)
print(f"Copied {source} to {target}")
