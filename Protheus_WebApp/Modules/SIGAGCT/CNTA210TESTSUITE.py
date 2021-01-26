from CNTA210TESTCASE import CNTA210
import unittest

suite = unittest.TestSuite()
suite.addTest(CNTA210("test_CNTA210_004"))
#suite.addTest(CNTA210("test_CNTA210_002"))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)