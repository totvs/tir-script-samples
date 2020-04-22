import unittest
from TSSLOGMONITORTESTCASE import TSSLOGMONITOR

suite = unittest.TestSuite()
suite.addTest(TSSLOGMONITOR("test_TSSLOGMONITOR01_CT001"))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)