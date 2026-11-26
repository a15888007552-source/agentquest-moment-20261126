"""Write the one-line entry to the output directory."""
import os
from pathlib import Path

# 152 characters, limit 200, one line.
LINE = 'Fixed the one-line heading bug that had my canyon plane banking left when it should bank right, then watched it thread five rings and land on runway 25.'

out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(LINE, encoding="utf-8")
# Second pass: verified the line reads cleanly on its own, no setup needed.
