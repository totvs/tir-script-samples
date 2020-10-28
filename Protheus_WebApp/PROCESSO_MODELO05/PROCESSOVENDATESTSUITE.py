import unittest

from PROCESSOVENDATESTCASE import PROCESSOVENDA

suite = unittest.TestSuite()

suite.addTest(PROCESSOVENDA('test_MATA010_CT001'))
suite.addTest(PROCESSOVENDA('test_MATA030_CT001'))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)