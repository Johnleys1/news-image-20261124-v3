import os
import shutil
from pathlib import Path


def main():
    here = Path(__file__).resolve().parent
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))
    out.mkdir(parents=True, exist_ok=True)
    dest = out / "entry.png"
    shutil.copyfile(here / "entry.png", dest)
    # confirm the copy is byte-identical to the source image
    if (here / "entry.png").read_bytes() != dest.read_bytes():
        raise SystemExit("entry.png copy mismatch")


if __name__ == "__main__":
    main()
