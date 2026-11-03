# Irrigation Guardian

> Control a small irrigation pump with soil-moisture hysteresis and a safe response to sensor failures.

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

Control a small irrigation pump with soil-moisture hysteresis and a safe response to sensor failures.

**Stack:** MicroPython, ESP32 ADC/GPIO, soil-moisture probe, desktop Python simulator

## ✨ Features

- Use separate dry/start and wet/stop thresholds to reduce relay chatter.
- Turn the pump output off when sensor readings are invalid.
- Keep decision logic portable and testable on a desktop.
- Simulate moisture readings before hardware setup.

## 🧱 Architecture

`firmware/logic.py` contains moisture conversion and pump-state decisions. `firmware/main.py` connects them to ESP32 ADC/GPIO. `simulator.py` and `test_logic.py` provide desktop examples and tests. See [hardware notes](docs/HARDWARE.md).

## 🚀 Quick Start

Python 3.10+ for desktop tests and simulation. MicroPython on an ESP32 for device firmware.

## 🧪 Usage

```bash
python -m unittest -v
python simulator.py
```

## ✅ Tests

Run `python -m unittest -v` from this directory. Automated tests use local or synthetic inputs and do not contact external services.

## ⚠️ Limitations

The firmware has not been tested with a physical probe, pump, or ESP32. Calibrate ADC values and use a correctly rated, isolated switching circuit. Do not use exposed mains wiring.

## 📄 License

MIT. See [LICENSE](LICENSE).
