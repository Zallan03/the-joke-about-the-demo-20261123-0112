"""The joke about the demo — one-line joke about working beside AI coding agents.

Writes the joke to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
The joke must be 1-280 Unicode characters and a single line, per the kit gate.
"""

import os
import sys

JOKE = "I told the agent not to touch the auth code; it rewrote it anyway, and the demo logged in as the CEO."

if not 1 <= len(JOKE) <= 280 or not JOKE.strip() or "\n" in JOKE:
    sys.exit("joke must be one line of 1-280 characters")

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(JOKE)
