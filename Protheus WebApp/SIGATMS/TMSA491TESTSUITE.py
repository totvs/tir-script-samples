import unittest
from TMSA491TESTCASE import TMSA491

suite = unittest.TestSuite()
suite.addTest(TMSA491('test_TMSA491_CT001')) # Geração de Fatura Automática Simples
suite.addTest(TMSA491('test_TMSA491_CT002')) # Geração de Fatura Automática com Multi-thread
suite.addTest(TMSA491('test_TMSA491_CT004')) # Gerar Fatura com varios documentos e ajustes
suite.addTest(TMSA491('test_TMSA491_CT003')) # Gerar Fatura com varios documentos
suite.addTest(TMSA491('test_TMSA491_CT005')) # Cancelamento total com vários documentos
suite.addTest(TMSA491('test_TMSA491_CT006')) # Cancelamento total com vários documentos com Multi-thread

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)