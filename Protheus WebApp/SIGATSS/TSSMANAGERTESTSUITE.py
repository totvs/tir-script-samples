import unittest
from TSSMANAGERTESTCASE import TSSMANAGER

suite = unittest.TestSuite()
suite.addTest(TSSMANAGER("test_TSSMANAGER01_CT001"))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite) 