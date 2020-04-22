from TMSA150TESTCASE import TMSA150
import unittest 

suite = unittest.TestSuite()
suite.addTest(TMSA150("test_TMSA150_CT001"))#Incluir
suite.addTest(TMSA150("test_TMSA150_CT002"))#Excluir

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)