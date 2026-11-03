import unittest
from firmware.logic import assess,fill_percent,median
class BinWatchTests(unittest.TestCase):
 def test_calibration_clamps_fill(self):self.assertEqual(fill_percent(80),0);self.assertEqual(fill_percent(12),100);self.assertEqual(fill_percent(0),100)
 def test_median_resists_one_outlier(self):self.assertEqual(median([70,71,72,4,70]),70)
 def test_pickup_threshold(self):self.assertTrue(assess([20,19,21])['pickup']);self.assertFalse(assess([60,58,62])['pickup'])
 def test_missing_measurements_report_error(self):self.assertEqual(assess([None])['status'],'sensor_error')
if __name__=='__main__':unittest.main()
