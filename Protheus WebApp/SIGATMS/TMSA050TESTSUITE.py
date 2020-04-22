import unittest
from TMSA050TESTCASE import TMSA050

suite = unittest.TestSuite()
suite.addTest(TMSA050('test_TMSA050_CT017')) # Cópia de Documento de Entrada Simples
# suite.addTest(TMSA050('test_TMSA050_CT018')) # Fechamento do Lote do Documento de Entrada
suite.addTest(TMSA050('test_TMSA050_CT019')) # Alterar nota fiscal e informar o valor do frete informado.
suite.addTest(TMSA050('test_TMSA050_CT020')) # Exclusão do Documento de Entrada

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)