import unittest
from TMSA500TESTCASE import TMSA500

suite = unittest.TestSuite()
suite.addTest(TMSA500('test_TMSA500_CT018')) # Cenario 018: Visualizar documento com a aba Impostos
suite.addTest(TMSA500('test_TMSA500_CT019')) # Cenario 019: Visualizar documento sem a aba Impostos

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)