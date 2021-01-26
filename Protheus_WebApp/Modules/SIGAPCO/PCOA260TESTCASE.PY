from tir import Webapp
import unittest

class PCOA260(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()

        inst.oHelper.Setup("SIGAPCO", "10/05/2016", "T1", "D MG 01 ", "57")

        inst.oHelper.Program("PCOA260")

    ######################################################################
    # Caso de teste 001                                                  #
    # Liberação de contingencia                                          #
    ######################################################################

    def test_PCOA260_001(self):
        self.oHelper.SetButton("Visualizar")

        Codigo = self.oHelper.GetValue("ALD_CODIGO")
        self.oHelper.CheckResult("ALD_CODIGO",Codigo)
       
        TpUnidade = self.oHelper.GetValue("ALD_TPUNID")
        self.oHelper.CheckResult("ALD_TPUNID",TpUnidade)

        UnidadeSuperior = self.oHelper.GetValue("ALD_GESSUP")
        self.oHelper.CheckResult("ALD_GESSUP",UnidadeSuperior)

        self.oHelper.SetButton("Fechar")
        
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()