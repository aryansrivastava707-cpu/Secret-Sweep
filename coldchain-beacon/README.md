# Coldchain Beacon

> Monitor temperature and humidity against configurable limits and raise an alarm when readings are unsafe.

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

Monitor temperature and humidity against configurable limits and raise an alarm when readings are unsafe.

**Stack:** MicroPython, ESP32, DHT22-compatible sensor, desktop Python simulator

## ✨ Features

- Check temperature and humidity against configured safe bands.
- Use clear thresholds to reduce rapid alarm toggling.
- Enter an alarm state when a sensor read fails.
- Print timestamped readings to serial output.

## 🧱 Architecture

`firmware/logic.py` evaluates readings and alarm state; `firmware/main.py` reads the sensor and emits records on ESP32. `simulator.py` and `test_logic.py` exercise normal, alert, recovery, and sensor-error cases on a desktop. See [hardware notes](docs/HARDWARE.md).

## 🚀 Quick Start

Python 3.10+ for desktop tests and simulation. MicroPython on an ESP32 for device firmware.

## 🧪 Usage

```bash
python -m unittest -v
python simulator.py

# For device setup, see docs/HARDWARE.md.
```

## ✅ Tests

Run `python -m unittest -v` from this directory. Automated tests use local or synthetic inputs and do not contact external services.

## ⚠️ Limitations

The firmware has not been calibrated or tested in a real shipment. This prototype is not a regulated cold-chain logger and does not provide durable remote storage.

## 📄 License

MIT. See [LICENSE](LICENSE).
