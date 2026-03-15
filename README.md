# My LLM Tools

A collection of standalone browser-based HTML/JS tools, hosted on GitHub Pages.

Each tool is a single `.html` file — no frameworks, no server, no build step. The index page is auto-generated during deployment.

Inspired by [tools.simonwillison.net](https://tools.simonwillison.net/).

## How it works

- Each tool is a self-contained HTML file with inline CSS and JS
- GitHub Actions deploys to GitHub Pages on every push to `main`
- `generate_index.py` auto-generates an index page listing all tools
- GitHub Pages strips `.html` extensions for clean URLs

## Adding a new tool

1. Create a new `.html` file in the repo root (or a subdirectory)
2. Push to `main`
3. It's live at `yoursite.github.io/tools/tool-name`

## Local development

Just open any `.html` file in your browser. No build step needed.
