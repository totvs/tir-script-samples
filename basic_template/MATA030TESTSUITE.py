import unittest

from MATA030TESTCASE import MATA030

suite = unittest.TestSuite()

suite.addTest(MATA030('test_MATA030_CT133'))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)