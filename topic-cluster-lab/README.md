# Topic Cluster Lab

> Group a folder of text documents with a compact TF-IDF and k-means implementation.

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

Group a folder of text documents with a compact TF-IDF and k-means implementation.

**Stack:** Python 3.10+, plain-text documents, Python standard library

## ✨ Features

- Tokenize text and calculate normalized TF-IDF vectors.
- Cluster documents with seeded k-means for repeatable runs.
- Print cluster membership and representative terms as JSON.
- Include four small sample articles across two broad topics.

## 🧱 Architecture

`cluster.py` contains tokenization, vectorization, clustering, and the CLI. `data/articles/` contains sample `.txt` files; `test_cluster.py` covers tokenization, empty input, invalid cluster counts, and repeatability.

## 🚀 Quick Start

Python 3.10 or newer. No third-party packages are required.

## 🧪 Usage

```bash
python -m unittest -v
python cluster.py data/articles --k 2 --out clusters.json
```

## ✅ Tests

Run `python -m unittest -v` from this directory. Automated tests use local or synthetic inputs and do not contact external services.

## ⚠️ Limitations

The sample corpus is tiny, and the implementation uses simple tokenization and bag-of-words TF-IDF. Results depend on the selected cluster count and are exploratory, not verified topic labels.

## 📄 License

MIT. See [LICENSE](LICENSE).
