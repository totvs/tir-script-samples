import unittest
from FINA070TESTCASE import FINA070

suite = unittest.TestSuite()

#testes sem alteração dos parâmetros
suite.addTest(FINA070('test_FINA070_CT093')) # Baixa por lote
suite.addTest(FINA070('test_FINA070_CT152')) # Só tela
suite.addTest(FINA070('test_FINA070_CT150')) # Só tela

# MV_BR10925 = 1
suite.addTest(FINA070('test_FINA070_CT190')) # MV_BR10925
suite.addTest(FINA070('test_FINA070_CT261')) # MV_BR10925
suite.addTest(FINA070('test_FINA070_CT191')) # MV_BR10925
suite.addTest(FINA070('test_FINA070_CT192')) # MV_BR10925

# MV_IMPBAIX = 1
suite.addTest(FINA070('test_FINA070_CT263')) # MV_BR10925 MV_IMPBAIX

# MV_BR10925 = 2 MV_JURTIPO = L
suite.addTest(FINA070('test_FINA070_CT193')) # OK

# #MV_IMPBXCR =2 MV_MULNATR =.T. MV_JURTIPO = M MV_SLDBXCR = C MV_CMC7FIN = S
suite.addTest(FINA070('test_FINA070_CT198')) # OK 
suite.addTest(FINA070('test_FINA070_CT220')) # Cheque MV_SLDBXCR MV_CMC7FIN
suite.addTest(FINA070('test_FINA070_CT260')) # OK
suite.addTest(FINA070('test_FINA070_CT207')) # OK
suite.addTest(FINA070('test_FINA070_CT206')) # OK MV_MOEDBCO
suite.addTest(FINA070('test_FINA070_CT208')) # OK MV_MOEDBCO

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)