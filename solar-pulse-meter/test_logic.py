import unittest
from firmware.logic import PulseMeter
class PulseMeterTests(unittest.TestCase):
 def test_counts_only_debounced_pulses(self):
  m=PulseMeter(1000,30);self.assertTrue(m.pulse(0));self.assertFalse(m.pulse(10));self.assertTrue(m.pulse(50));self.assertEqual(m.count,2)
 def test_energy_conversion(self):
  m=PulseMeter(1000);[m.pulse(t) for t in (0,50,100)];self.assertAlmostEqual(m.energy_kwh(),.003)
 def test_power_from_pulse_rate(self):
  m=PulseMeter(1000);[m.pulse(t) for t in (0,1000,2000)];self.assertAlmostEqual(m.power_w(2000),3600)
 def test_invalid_constant(self):
  with self.assertRaises(ValueError):PulseMeter(0)
if __name__=='__main__':unittest.main()
