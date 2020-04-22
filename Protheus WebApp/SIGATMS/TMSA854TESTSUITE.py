import unittest
from TMSA854TESTCASE import TMSA854

suite = unittest.TestSuite()
suite.addTest(TMSA854('test_TMSA854_CT001')) # Geração de Fatura Automática Simples
suite.addTest(TMSA854('test_TMSA854_CT002')) # Geração de Fatura com Multithreads
suite.addTest(TMSA854('test_TMSA854_CT003')) # Geração de fatura com 1 Doc eletrônico não-autorizado
suite.addTest(TMSA854('test_TMSA854_CT004')) # Geração de Fatura de documento de Coleta
suite.addTest(TMSA854('test_TMSA854_CT005')) # Geração de fatura de Doc. já faturado
suite.addTest(TMSA854('test_TMSA854_CT007')) # Exclusão de linha inserida
suite.addTest(TMSA854('test_TMSA854_CT008')) # Visualização de faturas geradas

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)