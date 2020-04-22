from tir import Webapp 
import unittest
from datetime import datetime
import time  
DateSystem = datetime.today().strftime("%d/%m/%Y")

class CRMA240(unittest.TestCase):

    @classmethod
    def setUpClass(self): 
        self.oHelper = Webapp()
        self.oHelper.Setup("SIGACRM", DateSystem, "T1", "D RJ 01 ", "73")
        self.oHelper.Program("CRMA240")  

    def test_CRMA240_CT001(self):  
        """
        Test Case CT001 - Manipular a estrutura de negócio, utilizando as funcionalidades Excluir, 
        Recortar e Colar com processamento completo.
        """
        
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
       
    def test_CRMA240_CT002(self):  
        """
        Test Case CT002 - Manipular a estrutura de negócio, utilizando as funcionalidade Excluir com processamento parcial
        """
        self.oHelper.Program("CRMA240") 
        self.oHelper.SetButton("Hierárquico")  
        self.oHelper.WaitShow("Estrutura de Negócio") 
        self.oHelper.ClickTree("Estrutura de Negócio") 
        self.oHelper.ClickTree("000001         - CRM D RJ 01 MATRIZ > CRM005         - EQUIPE VENDEDORES D RJ 01 > 000164         - VENDFAT05",right_click=True)
        self.oHelper.ClickMenuPopUpItem("Excluir Usuário") 
        self.oHelper.SetButton("Sim")
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Parcial")
        self.oHelper.WaitHide("Estrutura de Negócio")
        self.oHelper.AssertTrue()
    
    def test_CRMA240_CT003(self):  
        """
        Test Case CT003 - Abrir Estrutura de Negócio (Formato Tabela)
        """

        self.oHelper.Program("CRMA240")  
        self.oHelper.SetButton("Tabela") 
        self.oHelper.WaitShow("Estrutura de Negócios x Entidades") 
        self.oHelper.SetButton("Visualizar")
        self.oHelper.WaitShow("Estrutura de Negócios x Entidades - VISUALIZAR")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("X")
        self.oHelper.AssertTrue()
  
    @classmethod
    def tearDownClass(self):
        """
        Method that finishes the test case. 
        """
        self.oHelper.TearDown()  


if __name__ == "__main__":
    unittest.main()