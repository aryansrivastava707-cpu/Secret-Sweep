# Hardware notes

- ESP32 GPIO27 input with internal pull-up.
- Connect only an opto-isolated, low-voltage pulse output from an energy sensor.
- Sample configuration: 1000 pulses per kWh; replace with the meter's documented pulse constant.
- Confirm pulse polarity and isolation before connecting. Do not connect mains voltage directly to the board.
