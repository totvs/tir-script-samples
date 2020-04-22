from FINA340TESTCASE import FINA340
import unittest

suite = unittest.TestSuite()

suite.addTest(FINA340("test_FINA340_CT043"))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)