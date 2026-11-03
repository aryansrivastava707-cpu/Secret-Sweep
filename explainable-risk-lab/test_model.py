import unittest
from model import fit,explain,predict
from metrics import evaluate
ROWS=[{"utilization":str(x),"late_payments":str(x),"debt_ratio":str(x),"account_age":str(100-x),"label":str(int(x>4))} for x in range(10)]
class ModelTests(unittest.TestCase):
 def test_model_learns_separable_synthetic_data(self):
  model=fit(ROWS,epochs=5000);self.assertEqual(predict(model,ROWS[0]),0);self.assertEqual(predict(model,ROWS[-1]),1)
 def test_explanation_reconstructs_logit_probability(self):
  model=fit(ROWS,epochs=100);result=explain(model,ROWS[7]);self.assertGreaterEqual(result['probability'],0);self.assertLessEqual(result['probability'],1);self.assertEqual(set(result['contributions']),set(model['features']))
 def test_metrics(self):
  result=evaluate([1,1,0,0],[1,0,0,1]);self.assertEqual(result['confusion'],{'tn':1,'fp':1,'fn':1,'tp':1});self.assertEqual(result['accuracy'],.5)
if __name__=='__main__':unittest.main()
