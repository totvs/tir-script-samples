import unittest
from FINA910TESTCASE import FINA910

suite = unittest.TestSuite()
suite.addTest(FINA910('test_FINA910_CT028'))
suite.addTest(FINA910('test_FINA910_CT029'))
suite.addTest(FINA910('test_FINA910_CT030'))
suite.addTest(FINA910('test_FINA910_CT031'))
suite.addTest(FINA910('test_FINA910_CT032'))
suite.addTest(FINA910('test_FINA910_CT033'))
suite.addTest(FINA910('test_FINA910_CT034'))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)