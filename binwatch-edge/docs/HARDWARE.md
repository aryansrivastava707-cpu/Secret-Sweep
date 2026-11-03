# Hardware notes

- ESP32 with MicroPython, HC-SR04-compatible ultrasonic module, and a level shifter if the echo output is 5V.
- Trigger: GPIO5. Echo: GPIO18 through the level shifter.
- The sample assumes empty distance 80 cm and full distance 12 cm. Calibrate for the bin.
- Keep the sensor face clear and mount it away from lids or obstructions.
