# CLAUDE.md

## Project Overview

This is a collection of standalone browser-based HTML/JS tools, deployed to GitHub Pages via GitHub Actions. Inspired by [tools.simonwillison.net](https://tools.simonwillison.net/).

## Architecture

- Each tool is a **single self-contained `.html` file** — all HTML, CSS, and JS inline
- **No frameworks, no build step for tools** — just push HTML and it's live
- `generate_index.py` auto-generates the index page during CI
- GitHub Pages strips `.html` extensions (e.g., `word-counter.html` → `/word-counter`)

## Key Files

- `.github/workflows/pages.yml` — GitHub Actions deployment workflow
- `generate_index.py` — Builds `index.html` from all tool files (reads `<title>` and `<meta name="description">`)
- `.nojekyll` — Prevents Jekyll processing on GitHub Pages

## Creating a New Tool

1. Create a new `.html` file in the repo root (or a subdirectory)
2. Use this structure:
   - `<title>` — used as the tool name in the index
   - `<meta name="description" content="...">` — shown as description in the index
   - All CSS in a `<style>` block, all JS in a `<script>` block
3. No external dependencies unless explicitly needed (e.g., Pyodide, Marked)
4. Make it responsive/mobile-friendly
5. Push to `main` — deployment is automatic

## Conventions

- File names use kebab-case: `my-new-tool.html`
- Tools should be client-side only — no server, no API keys baked in
- Use `system-ui, -apple-system, sans-serif` as the default font stack
- Use `max-width: 600px–900px` with `margin: 2rem auto` for layout
- Common accent color: `#2563eb`
- External libraries can be loaded from CDNs when needed (no npm/node)

## Deployment

- Pushes to `main` trigger the GitHub Actions workflow
- The workflow copies all `.html` files to `_site/`, runs `generate_index.py`, and deploys via `actions/deploy-pages`
- The `index.html` in `_site/` is auto-generated — do not edit it manually

## Testing

- Open any `.html` file directly in a browser to test locally
- Run `python3 generate_index.py` to verify index generation
