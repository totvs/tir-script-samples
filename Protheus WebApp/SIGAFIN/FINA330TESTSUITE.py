import unittest
from FINA330TESTCASE import FINA330

suite = unittest.TestSuite()
suite.addTest(FINA330('test_FINA330_CT001'))
suite.addTest(FINA330('test_FINA330_CT002'))
suite.addTest(FINA330('test_FINA330_CT003'))
suite.addTest(FINA330('test_FINA330_CT200'))

# MV_BR10925 = 1
suite.addTest(FINA330('test_FINA330_CT046'))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)