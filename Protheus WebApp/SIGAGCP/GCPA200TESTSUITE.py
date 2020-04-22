import unittest
from GCPA200TESTCASE import GCPA200

suite = unittest.TestSuite()
suite.addTest(GCPA200('test_GCPA200_CT001'))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)