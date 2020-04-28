from tir import Webapp 
import unittest
from datetime import datetime
 
DateSystem = datetime.today().strftime("%d/%m/%Y")

class CRMA240(unittest.TestCase):

    @classmethod
    def setUpClass(self): 
        self.oHelper = Webapp()
        self.oHelper.Setup("SIGACRM", DateSystem, "T1", "D RJ 01 ", "73")
        self.oHelper.Program("CRMA240")  

    def test_CRMA240_CT001(self):  
        self.oHelper.SetButton("Hierárquico") 
        self.oHelper.WaitShow("Estrutura de Negócio")
        self.oHelper.ClickTree("Estrutura de Negócio",right_click=True)
        self.oHelper.ClickMenuPopUpItem("Pesquisar")
        self.oHelper.SetButton("Ok")
        self.oHelper.ClickTree("000001         - CRM D RJ 01 MATRIZ > CRM005         - EQUIPE VENDEDORES D RJ 01 > 000165         - VENDFAT06",right_click=True)
        self.oHelper.ClickMenuPopUpItem("Excluir Usuário")
        self.oHelper.SetButton("Sim")
        self.oHelper.ClickTree("000163         - VENDFAT04", right_click=True)
        self.oHelper.ClickMenuPopUpItem("Recortar")
        self.oHelper.ClickTree("000001         - CRM D RJ 01 MATRIZ",right_click=True)
        self.oHelper.ClickMenuPopUpItem("Colar")
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Completa")
        self.oHelper.WaitHide("Estrutura de Negócio")
        self.oHelper.AssertTrue()
       
    @classmethod
    def tearDownClass(self):
        self.oHelper.TearDown()  

if __name__ == "__main__":
    unittest.main()