import unittest

from PROCESSOVENDATESTCASE import PROCESSOVENDA

suite = unittest.TestSuite()

suite.addTest(PROCESSOVENDA('test_MATA030_001'))
suite.addTest(PROCESSOVENDA('test_MATA010_001'))
suite.addTest(PROCESSOVENDA('test_MATA410_001'))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)