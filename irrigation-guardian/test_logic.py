import unittest
from firmware.logic import decide_pump,adc_to_percent
class IrrigationTests(unittest.TestCase):
 def test_hysteresis_keeps_state_between_thresholds(self):
  self.assertTrue(decide_pump(25,False)['pump_on']);self.assertTrue(decide_pump(38,True)['pump_on']);self.assertFalse(decide_pump(46,True)['pump_on'])
 def test_sensor_failure_fails_safe_off(self):self.assertFalse(decide_pump(20,True,sensor_ok=False)['pump_on'])
 def test_adc_calibration(self):self.assertEqual(adc_to_percent(3200),0);self.assertEqual(adc_to_percent(1400),100)
 def test_invalid_thresholds_rejected(self):
  with self.assertRaises(ValueError):decide_pump(20,False,dry_threshold=50,wet_threshold=40)
if __name__=='__main__':unittest.main()
