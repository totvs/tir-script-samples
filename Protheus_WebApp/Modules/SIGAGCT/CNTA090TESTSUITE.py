from CNTA090TESTCASE import CNTA090
import unittest

suite = unittest.TestSuite()
suite.addTest(CNTA090("test_CNTA090_001"))
suite.addTest(CNTA090("test_CNTA090_002"))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)