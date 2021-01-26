from CNTA121TESTCASE import CNTA121
import unittest

suite = unittest.TestSuite()
suite.addTest(CNTA121("test_CNTA121_001"))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)