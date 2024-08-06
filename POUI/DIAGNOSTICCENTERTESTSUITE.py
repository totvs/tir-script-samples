import unittest
from DIAGNOSTICCENTERTESTCASE import DIAGNOSTICCENTER

suite = unittest.TestSuite()

suite.addTest(DIAGNOSTICCENTER('test_POUI_001'))
 
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
