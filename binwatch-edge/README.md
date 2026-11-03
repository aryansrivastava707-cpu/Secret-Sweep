# BinWatch Edge

> Estimate a bin fill level from ultrasonic distance readings, filtering isolated sensor spikes.

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

Estimate a bin fill level from ultrasonic distance readings, filtering isolated sensor spikes.

**Stack:** MicroPython, ESP32, ultrasonic sensor, desktop Python simulator

## ✨ Features

- Convert distance readings into a bounded fill percentage.
- Reject timeouts and out-of-range measurements.
- Use a rolling median to reduce the effect of one-off spikes.
- Raise a pickup flag at a configurable fill threshold.

## 🧱 Architecture

`firmware/logic.py` contains portable measurement logic; `firmware/main.py` connects it to the ESP32 sensor. `simulator.py` demonstrates the logic on a desktop, and `test_logic.py` covers boundaries and noisy readings. See [hardware notes](docs/HARDWARE.md).

## 🚀 Quick Start

Python 3.10+ for tests and desktop simulation. MicroPython is needed on an ESP32.

## 🧪 Usage

```bash
python -m unittest -v
python simulator.py

# Copy firmware/logic.py and firmware/main.py to the ESP32 for device use.
```

## ✅ Tests

Run `python -m unittest -v` from this directory. Automated tests use local or synthetic inputs and do not contact external services.

## ⚠️ Limitations

No physical sensor test has been performed. Bin geometry, soft waste, sensor placement, and calibration affect readings. There is no cloud or collection-service connection.

## 📄 License

MIT. See [LICENSE](LICENSE).
