# Hardware notes

- ESP32 board with MicroPython firmware.
- DHT22 data line to GPIO4; follow the sensor module's pull-up and power requirements.
- Status LED uses GPIO2 on boards that expose the built-in LED.
- Sample band is 2–8 °C; adjust for the product and sensor calibration.

CSV-like serial records are not tamper-proof storage. Add a validated RTC, persistent logging, and calibrated sensor if you extend this demo.
