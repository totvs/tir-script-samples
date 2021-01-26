from tir import Webapp
import unittest

class PCOA285(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()

        inst.oHelper.Setup("SIGAPCO", "10/05/2016", "T1", "D MG 01 ", "57")

        inst.oHelper.Program("PCOA285")

    ######################################################################
    # Caso de teste 001                                                  #
    # Liberação de contingencia                                          #
    ######################################################################

    def test_PCOA285_001(self):
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("D MG 01 ")

        self.oHelper.SetValue("AMN_CODIGO","AUTIN3")
        self.oHelper.SetValue("AMN_DESCRI","AUTINC DESCRICAO")


        self.oHelper.SetKey("F3")
        self.oHelper.ClickGridCell("Codigo",row=2)
        self.oHelper.SetButton("Confirmar")
        
        Descricao = self.oHelper.GetValue("AMN_DESCRI")
        self.oHelper.CheckResult("AMN_DESCRI",Descricao)
        
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        ##Confirmando
        self.oHelper.SearchBrowse("D MG 01 AUTIN3")
        self.oHelper.SetButton("Visualizar")

        Codigo = self.oHelper.GetValue("AMN_CODIGO")
        ##Verificando codigo apos pegar do modelo
        self.oHelper.CheckResult("AMN_CODIGO",Codigo)
        self.oHelper.SetButton("Fechar")
        
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()