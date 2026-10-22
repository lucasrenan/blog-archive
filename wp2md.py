#!/usr/bin/env python3
"""
Convert a WordPress export (WXR .xml) into Markdown files, text only.

- Keeps published posts and pages (drafts, attachments, menus etc. are skipped)
- Removes images, galleries, captions and other shortcodes
- Ignores comments
- Writes one file per post with YAML front matter (title, date, categories, tags)

Usage:
    pip install markdownify
    python3 wp2md.py export.xml output_dir
"""
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

from markdownify import markdownify

NS = {
    "content": "http://purl.org/rss/1.0/modules/content/",
    "wp": "http://wordpress.org/export/1.2/",
}


def detect_wp_ns(root):
    # WXR version varies (1.0, 1.1, 1.2) depending on the WordPress release
    for el in root.iter():
        if el.tag.startswith("{http://wordpress.org/export/"):
            NS["wp"] = el.tag[1:].split("}")[0]
            return


def autop(text):
    """Minimal version of WordPress' wpautop: blank lines become paragraphs,
    single newlines become <br>. Older WordPress stores posts without <p> tags."""
    blocks = re.split(r"\n\s*\n", text.replace("\r\n", "\n").strip())
    out = []
    block_tags = re.compile(r"^\s*<(p|div|h[1-6]|ul|ol|li|blockquote|pre|table|hr)\b", re.I)
    for b in blocks:
        if block_tags.match(b):
            out.append(b)
        else:
            out.append("<p>" + b.replace("\n", "<br>\n") + "</p>")
    return "\n".join(out)


def clean_html(html):
    # Captions wrap images: drop them entirely, caption text included
    html = re.sub(r"\[caption[^\]]*\].*?\[/caption\]", "", html, flags=re.S | re.I)
    # Any other shortcode ([gallery], [embed]...[/embed], [youtube ...], etc.)
    html = re.sub(r"\[(\w+)[^\]]*\].*?\[/\1\]", "", html, flags=re.S)
    html = re.sub(r"\[/?\w+[^\]]*\]", "", html)
    # Links that only wrap an image, then any remaining images
    html = re.sub(r"<a[^>]*>\s*<img[^>]*>\s*</a>", "", html, flags=re.S | re.I)
    html = re.sub(r"<img[^>]*>", "", html, flags=re.I)
    # Embedded media and scripts
    html = re.sub(r"<(iframe|object|embed|script|style|figure)[^>]*>.*?</\1>", "", html, flags=re.S | re.I)
    # WordPress "read more" marker
    html = html.replace("<!--more-->", "")
    return html


def to_markdown(html):
    md = markdownify(autop(clean_html(html)), heading_style="ATX", bullets="-")
    md = re.sub(r"\n{3,}", "\n\n", md)  # collapse leftover blank lines
    return md.strip() + "\n"


def yaml_str(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def slugify(s):
    s = re.sub(r"[^\w\s-]", "", s.lower(), flags=re.U)
    return re.sub(r"[\s_-]+", "-", s).strip("-") or "untitled"


def main(xml_path, out_dir):
    root = ET.parse(xml_path).getroot()
    detect_wp_ns(root)
    out = Path(out_dir)
    counts = {"post": 0, "page": 0}

    for item in root.iter("item"):
        ptype = item.findtext("wp:post_type", namespaces=NS)
        status = item.findtext("wp:status", namespaces=NS)
        if ptype not in counts or status != "publish":
            continue

        title = (item.findtext("title") or "").strip() or "Untitled"
        date = item.findtext("wp:post_date", namespaces=NS) or ""
        slug = item.findtext("wp:post_name", namespaces=NS) or slugify(title)
        html = item.findtext("content:encoded", namespaces=NS) or ""
        cats = [c.text for c in item.findall("category") if c.get("domain") == "category" and c.text]
        tags = [c.text for c in item.findall("category") if c.get("domain") == "post_tag" and c.text]

        front = ["---", f"title: {yaml_str(title)}"]
        if date:
            front.append(f"date: {date}")
        if cats:
            front.append("categories: [" + ", ".join(yaml_str(c) for c in cats) + "]")
        if tags:
            front.append("tags: [" + ", ".join(yaml_str(t) for t in tags) + "]")
        front.append("---\n")

        folder = out / ("posts" if ptype == "post" else "pages")
        folder.mkdir(parents=True, exist_ok=True)
        name = f"{date[:10]}-{slug}.md" if ptype == "post" and date else f"{slug}.md"
        (folder / name).write_text("\n".join(front) + "\n" + to_markdown(html), encoding="utf-8")
        counts[ptype] += 1

    print(f"Wrote {counts['post']} posts and {counts['page']} pages to {out}/")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
