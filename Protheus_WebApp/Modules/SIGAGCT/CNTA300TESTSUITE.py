import unittest
from CNTA300TESTCASE import CNTA300

suite = unittest.TestSuite()
suite.addTest(CNTA300('test_CNTA300_CT001'))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)