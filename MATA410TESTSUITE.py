from MATA410TESTCASE import MATA410
import unittest

suite = unittest.TestSuite()
suite.addTest(MATA410("test_MATA410_001"))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)