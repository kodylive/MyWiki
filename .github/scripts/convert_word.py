"""Turn Word documents in word/ into wiki pages in pages/.

Usage: python convert_word.py word/Some File.docx [more.docx ...]
Each document becomes pages/<slug>.md; its pictures go to images/<slug>/.
"""
import re
import shutil
import subprocess
import sys
from pathlib import Path
from urllib.parse import quote


def slugify(name):
    slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return slug or "document"


def convert(docx):
    docx = Path(docx)
    title = docx.stem
    slug = slugify(title)
    media_dir = Path("images") / slug
    shutil.rmtree(media_dir, ignore_errors=True)

    body = subprocess.run(
        ["pandoc", str(docx), "-t", "gfm", "--wrap=none",
         f"--extract-media={media_dir}"],
        check=True, capture_output=True, text=True,
    ).stdout

    # Pages live in pages/, so pictures are one folder up.
    body = body.replace(f"]({media_dir.as_posix()}/", f"](../{media_dir.as_posix()}/")
    body = body.replace(f'src="{media_dir.as_posix()}/', f'src="../{media_dir.as_posix()}/')

    safe_title = title.replace("\\", "\\\\").replace('"', '\\"')
    download = "../word/" + quote(docx.name)
    page = (
        "---\n"
        f'title: "{safe_title}"\n'
        "---\n\n"
        f"# {title}\n\n"
        f"[Download the original Word document]({download})\n"
        "{: .fs-2 }\n\n"
        "{% raw %}\n"
        f"{body.strip()}\n"
        "{% endraw %}\n"
    )
    out = Path("pages") / f"{slug}.md"
    out.write_text(page, encoding="utf-8")
    print(f"{docx} -> {out}")


if __name__ == "__main__":
    for path in sys.argv[1:]:
        if path.lower().endswith(".docx") and Path(path).exists():
            convert(path)
