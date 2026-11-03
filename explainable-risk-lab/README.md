# Explainable Risk Lab

> Fit a small logistic-regression classifier and inspect how each feature contributes to its output.

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

Fit a small logistic-regression classifier and inspect how each feature contributes to its output.

**Stack:** Python 3.10+, CSV, Python standard library

## ✨ Features

- Standardize numeric input features.
- Train binary logistic regression without a machine-learning framework.
- Report accuracy, precision, recall, and a confusion matrix.
- Show signed feature contributions for an example prediction.

## 🧱 Architecture

`model.py` implements scaling, training, prediction, and per-feature contributions. `metrics.py` calculates classification metrics, while `cli.py` loads a CSV and prints a JSON report. `data/synthetic.csv` contains example data.

## 🚀 Quick Start

Python 3.10 or newer. No third-party packages are required.

## 🧪 Usage

```bash
python -m unittest -v
python cli.py data/synthetic.csv --epochs 5000
```

## ✅ Tests

Run `python -m unittest -v` from this directory. Automated tests use local or synthetic inputs and do not contact external services.

## ⚠️ Limitations

The included dataset is synthetic and very small. Its metrics do not indicate real-world performance. Do not use this educational example to make lending, hiring, eligibility, or other consequential decisions.

## 📄 License

MIT. See [LICENSE](LICENSE).
