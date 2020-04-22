import unittest
from FINC010TESTCASE import FINC010

suite = unittest.TestSuite()
suite.addTest(FINC010('test_FINC010_CT012'))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)