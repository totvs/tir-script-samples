from tir import Webapp
import unittest

class ATFA040(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()

        inst.oHelper.Setup("SIGAATF", "17/12/2019", "T1", "D MG 01 ", "01")
        inst.oHelper.Program("ATFA040")
        inst.oHelper.AddParameter("MV_ULTDEPR", "D MG 01", "20191211")
        inst.oHelper.SetParameters()

    def test_ATFA040_001(self):
        ##cancelamento de baixa
        self.oHelper.WaitShow("Baixa de Adiantamentos de Ativos Imobilizados")
        self.oHelper.SetKey("F12")
        # self.oHelper.SetButton("Param")
        # --
        self.oHelper.SetValue("Mostra Lanc.Contab ?","Nao")  
        self.oHelper.SetValue("Aglut Lancamentos ?","Nao")  
        self.oHelper.SetValue("Contabiliza Online ?","Não")  
        self.oHelper.SetButton("OK")
                

        self.oHelper.SearchBrowse("D MG 01 000100")
              
        self.oHelper.SetButton("Canc. Baixa")
        self.oHelper.SetButton("Salvar")
        self.oHelper.AssertTrue()

        self.oHelper.SearchBrowse("D MG 01 000100")
        self.oHelper.SetButton("Visualizar")
        self.oHelper.ClickFolder("Valores")
        self.oHelper.CheckResult("N3_VORIG1","100,22")
        self.oHelper.SetButton("Fechar")

        self.oHelper.SearchBrowse("D MG 01 000030")
        self.oHelper.SetButton("Visualizar")
        
        self.oHelper.CheckResult("N1_CBASE","000030")
        self.oHelper.AssertFalse()
                
    
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
