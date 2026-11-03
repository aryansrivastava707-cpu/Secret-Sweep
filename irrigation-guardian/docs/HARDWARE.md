# Hardware and wiring

- ESP32 ADC input: GPIO34 to a 3.3V-compatible capacitive soil probe output.
- Pump relay control: GPIO5 to a low-voltage relay module input.
- Share ground between ESP32, probe, and relay logic.
- Power the pump from a correctly rated, isolated supply; do not connect mains to a breadboard.

The sample calibration maps ADC 3200 to dry and 1400 to wet. Measure your own dry/wet range and update `dry_raw`/`wet_raw`. The relay is configured fail-off at boot.
