"""Copies the user guide from the plugin into this site's docs folder, so the site and the shipped guide match.

  python sync_docs.py [path to the GearGenerator plugin]
"""

import os
import shutil
import sys

here = os.path.dirname(os.path.abspath(__file__))
plugin = sys.argv[1] if len(sys.argv) > 1 else os.path.join(here, "..", "PluginDev", "Plugins", "GearGenerator")
source = os.path.join(plugin, "Docs")
target = os.path.join(here, "docs")
if not os.path.isfile(os.path.join(source, "index.md")):
    sys.exit(f"No guide found at {source}")
if os.path.isdir(target):
    shutil.rmtree(target)
shutil.copytree(source, target)
print(f"Copied {source} to {target}")
