from FINA645TESTCASE import FINA645
import unittest

suite = unittest.TestSuite()
suite.addTest(FINA645("test_FINA645_CT001"))
suite.addTest(FINA645("test_FINA645_CT002"))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)