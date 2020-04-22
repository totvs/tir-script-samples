import unittest
from TMSA200TESTCASE import TMSA200

suite = unittest.TestSuite()
suite.addTest(TMSA200('test_TMSA200_CT007')) # Cálculo de Lote com configurações para gerar "Bloqueio de crédito"


runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)