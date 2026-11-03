import unittest
from firmware.logic import evaluate
class ColdChainTests(unittest.TestCase):
 def test_normal_temperature(self):self.assertEqual(evaluate(5,50)['status'],'normal')
 def test_alarm_and_hysteresis_recovery(self):
  self.assertTrue(evaluate(9,50)['alarm']);self.assertTrue(evaluate(7.5,50,True)['alarm']);self.assertFalse(evaluate(6.5,50,True)['alarm'])
 def test_humidity_outside_band_alarms(self):self.assertEqual(evaluate(5,95)['reason'],'humidity outside band')
 def test_sensor_failure_alarms(self):self.assertEqual(evaluate(None,None,sensor_ok=False)['status'],'sensor_error')
 def test_out_of_range_sensor_value_alarms(self):self.assertEqual(evaluate(200,50)['status'],'invalid_reading')
if __name__=='__main__':unittest.main()
