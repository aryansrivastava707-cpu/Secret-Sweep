# Markdown Studio

> Build a small static site from Markdown notes, with escaped HTML and a simple local search index.

[![Node.js](https://img.shields.io/badge/Node.js-20%2B-339933.svg?logo=nodedotjs&logoColor=white)](https://nodejs.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📖 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Architecture](#-architecture)
- [Quick Start](#-quick-start)
- [Usage](#-usage)
- [Tests](#-tests)
- [Limitations](#-limitations)
- [License](#-license)

## 🎯 Overview

Build a small static site from Markdown notes, with escaped HTML and a simple local search index.

**Stack:** Node.js 20+, JavaScript, HTML, CSS; no third-party runtime packages

## ✨ Features

- Render a deliberately small subset of Markdown.
- Escape raw HTML in note content.
- Generate one HTML page per Markdown file plus an index page.
- Write a JSON search index and browser-side title search script.

## 🧱 Architecture

`src/render.mjs` contains Markdown and page rendering helpers. `src/cli.mjs` reads Markdown files and writes the static output. `content/` is sample input; `test/` contains the Node test suite.

## 🚀 Quick Start

Node.js 20 or newer. No package installation is required.

```bash
npm test
```

## 🧪 Usage

Build the example Markdown content into a static site:

```bash
npm run build -- --input content --output site
```

Open `site/index.html` in a browser.

## ✅ Tests

Run `npm test` from this directory. The tests use Node's built-in test runner and need no network access.

## ⚠️ Limitations

The renderer supports only a small Markdown subset and is not a complete CommonMark implementation. Search is a basic local title filter, not full-text ranking.

## 📄 License

MIT. See [LICENSE](LICENSE).
