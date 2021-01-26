from tir import Webapp
import unittest

class PCOA280(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()

        inst.oHelper.Setup("SIGAPCO", "10/05/2016", "T1", "D MG 01 ", "57")

        inst.oHelper.Program("PCOA280")

    ######################################################################
    # Caso de teste 001                                                  #
    # Liberação de contingencia                                          #
    ######################################################################

    def test_PCOA280_001(self):
        self.oHelper.SetButton("Visualizar")

        Codigo = self.oHelper.GetValue("AL0_CODIGO")
        self.oHelper.CheckResult("AL0_CODIGO",Codigo)
       
        Descricao = self.oHelper.GetValue("AL0_DESCRI")
        self.oHelper.CheckResult("AL0_DESCRI",Descricao)

        Tipo = self.oHelper.GetValue("AL0_TIPO")
        self.oHelper.CheckResult("AL0_TIPO",Tipo)

        self.oHelper.SetButton("Fechar")
        
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()