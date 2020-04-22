import unittest
from TMSA040TESTCASE import TMSA040

suite = unittest.TestSuite()

suite.addTest(TMSA040('test_TMSA040_CT009')) # Inclusão de cotação com tipo de veiculo frete informado
suite.addTest(TMSA040('test_TMSA040_CT019')) # Inclusão de cotação com valor fechado percentual de desconto 25%
suite.addTest(TMSA040('test_TMSA040_CT041')) # Cópia de cotação
suite.addTest(TMSA040('test_TMSA040_CT051')) # Visualização de cotação
suite.addTest(TMSA040('test_TMSA040_CT037')) # Cancelamento de cotação
suite.addTest(TMSA040('test_TMSA040_CT026')) # Inclusão de cotação com regras de restrições com produtos diferentes 
suite.addTest(TMSA040('test_TMSA040_CT040')) # Retomar Cotação

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)