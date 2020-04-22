from FINA460TESTCASE import FINA460
import unittest

suite = unittest.TestSuite()
suite.addTest(FINA460("test_FINA460_001"))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)