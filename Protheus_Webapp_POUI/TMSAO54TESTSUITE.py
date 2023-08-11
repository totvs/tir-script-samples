import unittest
from TMSAO54TESTCASE import TMSAO54

suite = unittest.TestSuite()

suite.addTest(TMSAO54('test_TMSAO54_001'))
 
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
