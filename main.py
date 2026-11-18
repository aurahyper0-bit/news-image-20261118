"""Entry point: copy the bundled front-page image to the output path."""
import os
import shutil

SOURCE = "entry.png"
DEST = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")


def main():
    os.makedirs(os.path.dirname(DEST), exist_ok=True)
    shutil.copyfile(SOURCE, DEST)
    assert os.path.getsize(DEST) > 0, "empty output image"


if __name__ == "__main__":
    main()
