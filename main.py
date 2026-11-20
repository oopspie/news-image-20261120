"""Entry program for make.fun news-image-20261120.

Writes the front-page image held in this repository to the output
directory. Standard library only, no network access, and the output
is byte-identical on every run.
"""

import os
import shutil
from pathlib import Path

ENTRY = Path(__file__).resolve().parent / "entry.png"


def main():
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    if not ENTRY.is_file():
        raise SystemExit(f"missing entry image: {ENTRY}")
    target = out / "entry.png"
    shutil.copyfile(ENTRY, target)
    if target.stat().st_size != ENTRY.stat().st_size:
        raise SystemExit("output size does not match entry image")


if __name__ == "__main__":
    main()
