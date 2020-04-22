import unittest
from FINA040TESTCASE import FINA040

suite = unittest.TestSuite()

suite.addTest(FINA040('test_FINA040_CT001'))
suite.addTest(FINA040('test_FINA040_CT002'))
suite.addTest(FINA040('test_FINA040_CT003'))
suite.addTest(FINA040('test_FINA040_CT074'))
suite.addTest(FINA040('test_FINA040_CT103'))
suite.addTest(FINA040('test_FINA040_CT110'))
suite.addTest(FINA040('test_FINA040_CT154'))
suite.addTest(FINA040('test_FINA040_CT161'))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)