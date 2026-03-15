#!/usr/bin/env python3
"""Generate an index.html listing all tools in the repo."""
import re
from pathlib import Path
from datetime import datetime, timezone

EXCLUDE = {"index.html", "colophon.html", "404.html"}


def get_title(filepath):
    """Extract <title> from an HTML file."""
    try:
        content = filepath.read_text(encoding="utf-8")
        match = re.search(r"<title>(.*?)</title>", content, re.IGNORECASE)
        return match.group(1) if match else filepath.stem.replace("-", " ").title()
    except Exception:
        return filepath.stem.replace("-", " ").title()


def get_description(filepath):
    """Extract meta description from an HTML file."""
    try:
        content = filepath.read_text(encoding="utf-8")
        match = re.search(
            r'<meta\s+name="description"\s+content="(.*?)"',
            content,
            re.IGNORECASE,
        )
        return match.group(1) if match else ""
    except Exception:
        return ""


def main():
    tools = []

    # Scan root directory
    for path in sorted(Path(".").glob("*.html")):
        if path.name in EXCLUDE or path.name.startswith("."):
            continue
        name = path.stem
        title = get_title(path)
        description = get_description(path)
        tools.append((name, title, description))

    # Scan subdirectories
    for path in sorted(Path(".").rglob("*.html")):
        if path.name in EXCLUDE or path.name.startswith("."):
            continue
        if path.parts[0].startswith(".") or path.parts[0] == "_site":
            continue
        if len(path.parts) > 1:
            name = str(path.with_suffix(""))
            title = get_title(path)
            description = get_description(path)
            tools.append((name, title, description))

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    print(f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Tools</title>
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: system-ui, -apple-system, sans-serif;
            max-width: 700px;
            margin: 2rem auto;
            padding: 0 1rem;
            line-height: 1.6;
            color: #1a1a1a;
        }}
        h1 {{ margin-bottom: 0.5rem; }}
        .subtitle {{
            color: #666;
            margin-bottom: 2rem;
        }}
        .tools-list {{
            list-style: none;
            padding: 0;
        }}
        .tools-list li {{
            margin: 0.75rem 0;
            padding: 0.75rem 1rem;
            background: #f8f9fa;
            border-radius: 8px;
            border: 1px solid #e9ecef;
        }}
        .tools-list li:hover {{
            background: #e9ecef;
        }}
        .tools-list a {{
            color: #2563eb;
            text-decoration: none;
            font-weight: 500;
            font-size: 1.05rem;
        }}
        .tools-list a:hover {{
            text-decoration: underline;
        }}
        .tool-desc {{
            color: #666;
            font-size: 0.9rem;
            margin-top: 0.25rem;
        }}
        footer {{
            margin-top: 3rem;
            padding-top: 1rem;
            border-top: 1px solid #e9ecef;
            color: #999;
            font-size: 0.85rem;
        }}
    </style>
</head>
<body>
    <h1>My Tools</h1>
    <p class="subtitle">A collection of browser-based tools. Each runs entirely in your browser.</p>
    <ul class="tools-list">""")

    for name, title, description in tools:
        desc_html = (
            f'\n            <div class="tool-desc">{description}</div>'
            if description
            else ""
        )
        print(
            f"""        <li>
            <a href="/{name}">{title}</a>{desc_html}
        </li>"""
        )

    print(f"""    </ul>
    <footer>
        Last updated {now}. {len(tools)} tools available.
    </footer>
</body>
</html>""")


if __name__ == "__main__":
    main()
