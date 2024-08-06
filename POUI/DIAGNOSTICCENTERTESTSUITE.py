import unittest
from DIAGNOSTICCENTERTESTCASE import POUI

suite = unittest.TestSuite()

suite.addTest(POUI('test_POUI_001'))
 
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
