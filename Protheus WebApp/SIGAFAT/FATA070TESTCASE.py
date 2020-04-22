from tir import Webapp 
import unittest
from datetime import datetime
import time  
DateSystem = datetime.today().strftime("%d/%m/%Y")

class FATA070(unittest.TestCase):

    @classmethod
    def setUpClass(self): 
        self.oHelper = Webapp()
        self.oHelper.Setup("SIGAFAT", DateSystem, "T1", "M PR 01 ", "05")
        self.oHelper.Program("FATA070") 

    def test_FATA070_CT001(self):  
        """
        Test Case CT001 - Inclui e exclui todas as estruturas de negócio
        """
       
        self.oHelper.ClickTree("Estrutura de Negócio", right_click=True)
        self.oHelper.ClickMenuPopUpItem("Anexa  Unid. de Negócio")  
       	time.sleep(3)
        self.oHelper.SearchBrowse(f"MPR01", "Codigo") 
        self.oHelper.SetButton("OK") 
        time.sleep(3)
        self.oHelper.SetButton("Sim")
        self.oHelper.ClickTree("Estrutura de Negócio > MPR01 -Unidade Filial M Pr 01  - Faturamento", right_click=True)
        self.oHelper.ClickMenuPopUpItem("Anexa Equipe") 
        time.sleep(3) 
        self.oHelper.SearchBrowse(f"EQMPR1", "Grupo") 
        self.oHelper.SetButton("OK")
        time.sleep(3) 
        self.oHelper.SetButton("Sim")
        self.oHelper.ClickTree("EQMPR1-Equipe Filial Mpr01 - Fat", right_click=True)
        self.oHelper.ClickMenuPopUpItem("Pesquisa")   
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Ok")
        self.oHelper.ClickTree("EQMPR1-Equipe Filial Mpr01 - Fat", right_click=True) 
        self.oHelper.ClickMenuPopUpItem("Anexa Vendedor")  
        time.sleep(3)
        self.oHelper.SearchBrowse(f"FAT001", "Código")
        self.oHelper.SetButton("OK")
        self.oHelper.SetButton("Sim")
        self.oHelper.ClickTree("EQMPR1-Equipe Filial Mpr01 - Fat > FAT001-Vendedor Fat001 - 100% Emissao - FAta070", right_click=True)
        self.oHelper.ClickMenuPopUpItem("Exclui vendedor")  
        self.oHelper.SetButton("Sim")
        self.oHelper.ClickTree("EQMPR1-Equipe Filial Mpr01 - Fat", right_click=True)
        self.oHelper.ClickMenuPopUpItem("Exclui Equipe")  
        time.sleep(3)  
        self.oHelper.SetButton("Sim")
        self.oHelper.ClickTree("MPR01 -Unidade Filial M Pr 01  - Faturamento", right_click=True)
        self.oHelper.ClickMenuPopUpItem("Exclui Unid. de Negócio")  
        time.sleep(3)
        self.oHelper.SetButton("Sim") 
        self.oHelper.ClickTree("Estrutura de Negócio", right_click=True) 
        self.oHelper.ClickMenuPopUpItem("Anexa  Unid. de Negócio")  
       	time.sleep(3)
        self.oHelper.SearchBrowse(f"MPR01", "Codigo")
        self.oHelper.SetButton("OK") 
        time.sleep(3)
        self.oHelper.SetButton("Sim")
        self.oHelper.ClickTree("Estrutura de Negócio > MPR01 -Unidade Filial M Pr 01  - Faturamento", right_click=True)
        self.oHelper.ClickMenuPopUpItem("Anexa Equipe")  
        time.sleep(3) 
        self.oHelper.SearchBrowse(f"EQMPR1", "Grupo") 
        self.oHelper.SetButton("OK")
        time.sleep(3) 
        self.oHelper.SetButton("Sim")
        self.oHelper.ClickTree("EQMPR1-Equipe Filial Mpr01 - Fat", right_click=True)
        self.oHelper.ClickMenuPopUpItem("Anexa Vendedor")  
        time.sleep(3)
        self.oHelper.SearchBrowse(f"FAT001", "Código")
        self.oHelper.SetButton("OK")
        self.oHelper.SetButton("Sim")

        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Fechar")
        
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(self):
        """
        Method that finishes the test case. 
        """
        self.oHelper.TearDown()  


if __name__ == "__main__":
    unittest.main()