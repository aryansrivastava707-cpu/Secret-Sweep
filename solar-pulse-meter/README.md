# Solar Pulse Meter

> Estimate power and cumulative energy from pulses emitted by an isolated low-voltage energy sensor.

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

Estimate power and cumulative energy from pulses emitted by an isolated low-voltage energy sensor.

**Stack:** MicroPython, ESP32 GPIO, pulse-output energy sensor, desktop Python simulator

## ✨ Features

- Debounce pulses and ignore rapid duplicate edges.
- Calculate power from recent pulse timing.
- Accumulate energy using a configurable pulses-per-kWh constant.
- Separate measurement logic from GPIO handling for desktop tests.

## 🧱 Architecture

`firmware/logic.py` contains pulse filtering and energy calculations. `firmware/main.py` connects the logic to ESP32 GPIO; `simulator.py` and `test_logic.py` exercise pulse sequences on a desktop. See [hardware notes](docs/HARDWARE.md).

## 🚀 Quick Start

Python 3.10+ for desktop tests and simulation. MicroPython is needed on an ESP32.

```bash
python -m unittest -v
```

## 🧪 Usage

Run the desktop simulator:

```bash
python simulator.py
```

For device setup, see [hardware notes](docs/HARDWARE.md).

## ✅ Tests

Run `python -m unittest -v` from this directory. Automated tests use local or synthetic inputs and do not contact external services.

## ⚠️ Limitations

No physical meter has been tested. Calibrate the pulse constant against sensor documentation and a known reference. Use only an isolated low-voltage pulse output; never connect an ESP32 directly to mains.

## 📄 License

MIT. See [LICENSE](LICENSE).
