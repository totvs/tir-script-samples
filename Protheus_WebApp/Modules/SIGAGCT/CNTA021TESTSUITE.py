import unittest
from CNTA021TESTCASE import CNTA021

suite = unittest.TestSuite()
suite.addTest(CNTA021("test_CNTA021_001"))
#suite.addTest(CNTA021("test_CNTA021_002"))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)