from FINA171TESTCASE import FINA171
import unittest

suite = unittest.TestSuite()
suite.addTest(FINA171('test_FINA171_CT006'))
suite.addTest(FINA171("test_FINA171_CT007"))
suite.addTest(FINA171("test_FINA171_CT008"))
suite.addTest(FINA171("test_FINA171_CT009"))
suite.addTest(FINA171("test_FINA171_CT010"))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)