from TMSA440TESTCASE import TMSA440
import unittest

suite = unittest.TestSuite()
suite.addTest(TMSA440("test_TMSA440_001"))
suite.addTest(TMSA440("test_TMSA440_002"))
suite.addTest(TMSA440("test_TMSA440_003"))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite) 