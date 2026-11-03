# Secret Sweep

> Scan a local project for common credential patterns and report locations with secret values redacted.

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

Scan a local project for common credential patterns and report locations with secret values redacted.

**Stack:** Python 3.10+, Python standard library

## ✨ Features

- Scan text files recursively while skipping common generated folders.
- Detect selected cloud-token, private-key, and generic secret patterns.
- Redact matched values in reports and identify findings by fingerprints.
- Support inline ignores and an optional fingerprint allowlist.

## 🧱 Architecture

`scanner.py` contains pattern matching, redaction, and directory traversal. `scan.py` provides the CLI; `test_scanner.py` checks detection, redaction, and exclusions. `.secret-sweep-allow.example.json` is an example allowlist.

## 🚀 Quick Start

Python 3.10 or newer. No third-party packages are required.

## 🧪 Usage

```bash
python -m unittest -v
python scan.py path/to/project --out secret-findings.json

# Optional: copy .secret-sweep-allow.example.json to
# .secret-sweep-allow.json and add approved fingerprints.
```

## ✅ Tests

Run `python -m unittest -v` from this directory. Automated tests use local or synthetic inputs and do not contact external services.

## ⚠️ Limitations

Pattern matching can miss credentials or flag harmless text. Redaction reduces accidental exposure but does not make findings risk-free. Review results and rotate credentials that may have been exposed.

## 📄 License

MIT. See [LICENSE](LICENSE).
