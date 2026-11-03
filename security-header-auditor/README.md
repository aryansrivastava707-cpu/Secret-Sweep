# Security Header Auditor

> Review HTTP response headers against a focused set of browser security recommendations.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
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

Review HTTP response headers against a focused set of browser security recommendations.

**Stack:** Python 3.10+, Python standard library

## ✨ Features

- Fetch response headers from a supplied HTTP or HTTPS URL.
- Check a focused set of browser security headers.
- Explain missing or weak settings and calculate a simple score.
- Test header evaluation with local synthetic responses.

## 🧱 Architecture

`auditor.py` contains URL fetching and pure header evaluation. `audit.py` is the CLI, and `test_auditor.py` checks scoring and URL validation without making network requests.

## 🚀 Quick Start

Python 3.10 or newer. No third-party packages are required. Internet access is needed only to audit a live URL.

```bash
python -m unittest -v
```

## 🧪 Usage

Audit a site you own or have permission to assess:

```bash
python audit.py https://your-authorized-site.example
```

To save JSON output, add `--json report.json`.

## ✅ Tests

Run `python -m unittest -v` from this directory. Automated tests use local or synthetic inputs and do not contact external services.

## ⚠️ Limitations

This reviews response headers only. It is not a penetration test, TLS audit, or security certification. Only assess systems you own or have permission to test. Live URL fetching is not part of the automated tests.

## 📄 License

MIT. See [LICENSE](LICENSE).
