import unittest
from TSSMANAGERMONITORTESTCASE import TSSMANAGERMONITOR

suite = unittest.TestSuite()
suite.addTest(TSSMANAGERMONITOR("test_TSSMANAGERMONITOR01_CT001"))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)