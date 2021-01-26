from tir import Webapp
import unittest
from datetime import datetime
import time
DateSystem = datetime.today().strftime("%d/%m/%Y")

class PMSA220(unittest.TestCase):

    @classmethod
    def setUpClass(self): 
        self.oHelper = Webapp()
        self.oHelper.Setup("SIGAPMS", DateSystem, "T1", "D MG 01 ", "44")
        self.oHelper.Program("PMSA220") 

    def test_PMSA220_CT021(self):
        """
        Test Case CT021- GTSER-T32626 - Gera Empenho do projeto para 1 armazém - MV_REQEPMS = .F.
        """
        
        projeto = "PMSU000021"
        prod1 = "PMSR00000000000000000000000001"
        prod2 = "PMSR00000000000000000000000002"
     
        self.oHelper.SearchBrowse(f"D MG 01 {projeto}", "Filial+projeto")
        self.oHelper.SetButton("Planejamentos")
        self.oHelper.SetBranch("D MG 01")
        self.oHelper.SetButton("Gerar")
        self.oHelper.SetValue("Descricao", projeto)
        self.oHelper.SetValue("Planej. De", "29/06/2020")
        self.oHelper.SetValue("Planej. Ate", "03/07/2020")
        self.oHelper.SetButton("Salvar")

        # Verifica Empenho Gerado
        self.oHelper.SetButton("Visualizar")
        self.oHelper.SetButton("Outras Ações")
        self.oHelper.ClickMenuPopUpItem("Detalhes")
        self.oHelper.ClickMenuPopUpItem("Empenhos")

        self.oHelper.CheckResult("Produto", prod1, grid=True, line=1)
        self.oHelper.CheckResult("Armazem", "01", grid=True, line=1)
        self.oHelper.CheckResult("Qtd.Empenhada", "2,00", grid=True, line=1)

        self.oHelper.CheckResult("Produto", prod1, grid=True, line=2)
        self.oHelper.CheckResult("Armazem", "01", grid=True, line=2)
        self.oHelper.CheckResult("Qtd.Empenhada", "4,00", grid=True, line=2)

        self.oHelper.CheckResult("Produto", prod2, grid=True, line=3)
        self.oHelper.CheckResult("Armazem", "01", grid=True, line=3)
        self.oHelper.CheckResult("Qtd.Empenhada", "3,00", grid=True, line=3)
        
        self.oHelper.CheckResult("Produto", prod2, grid=True, line=4)
        self.oHelper.CheckResult("Armazem", "01", grid=True, line=4)
        self.oHelper.CheckResult("Qtd.Empenhada", "5,00", grid=True, line=4)
         
        self.oHelper.LoadGrid()
       
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton("Sair")

        self.oHelper.AssertTrue()
    
    def test_PMSA220_CT022(self):
        """
        Test Case CT022- GTSER-T52378 - Gera Empenho do projeto para múltiplos armazéns - MV_REQEPMS = .T. - Variacao 1
        """

        self.oHelper.AddParameter("MV_REQEPMS","D MG 01",".T.",".T.",".T.")
        self.oHelper.SetParameters()

        projeto = "PMSU000022"
        prod1 = "PMSR00000000000000000000000003"
        prod2 = "PMSR00000000000000000000000004"

        self.oHelper.SearchBrowse(f"D MG 01 {projeto}", "Filial+projeto")
        self.oHelper.SetButton("Planejamentos")
        self.oHelper.SetBranch("D MG 01")
        self.oHelper.SetButton("Gerar")
        self.oHelper.SetValue("Descricao", projeto)
        self.oHelper.SetValue("Planej. De", "29/06/2020")
        self.oHelper.SetValue("Planej. Ate", "03/07/2020")
        self.oHelper.SetValue("Cons.Armaz.", "01,02")
        self.oHelper.SetButton("Salvar")
      
        # Verifica Empenho Gerado
        self.oHelper.SetButton("Visualizar")
        self.oHelper.SetButton("Outras Ações")
        self.oHelper.ClickMenuPopUpItem("Detalhes")
        self.oHelper.ClickMenuPopUpItem("Empenhos")

        self.oHelper.CheckResult("Produto", prod1, grid=True, line=1)
        self.oHelper.CheckResult("Armazem", "01", grid=True, line=1)
        self.oHelper.CheckResult("Qtd.Empenhada", "100,00", grid=True, line=1)

        self.oHelper.CheckResult("Produto", prod1, grid=True, line=2)
        self.oHelper.CheckResult("Armazem", "01", grid=True, line=2)
        self.oHelper.CheckResult("Qtd.Empenhada", "1,00", grid=True, line=2)

        self.oHelper.CheckResult("Produto", prod1, grid=True, line=3)
        self.oHelper.CheckResult("Armazem", "02", grid=True, line=3)
        self.oHelper.CheckResult("Qtd.Empenhada", "89,00", grid=True, line=3)

        self.oHelper.CheckResult("Produto", prod2, grid=True, line=4)
        self.oHelper.CheckResult("Armazem", "01", grid=True, line=4)
        self.oHelper.CheckResult("Qtd.Empenhada", "20,00", grid=True, line=4)
        
        self.oHelper.CheckResult("Produto", prod2, grid=True, line=5)
        self.oHelper.CheckResult("Armazem", "02", grid=True, line=5)
        self.oHelper.CheckResult("Qtd.Empenhada", "5,00", grid=True, line=5)

        self.oHelper.CheckResult("Produto", prod2, grid=True, line=6)
        self.oHelper.CheckResult("Armazem", "02", grid=True, line=6)
        self.oHelper.CheckResult("Qtd.Empenhada", "10,00", grid=True, line=6)

        self.oHelper.LoadGrid()
       
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton("Sair")

        self.oHelper.RestoreParameters()
        self.oHelper.AssertTrue()

    def test_PMSA220_CT023(self):
        """
        Test Case CT023- GTSER-T52420 - Gera Empenho do projeto para múltiplos armazéns - MV_REQEPMS = .T. - Variacao 2
        """

        self.oHelper.AddParameter("MV_REQEPMS","D MG 01",".T.",".T.",".T.")
        self.oHelper.SetParameters()

        projeto = "PMSU000023"
        prod1 = "PMSR00000000000000000000000005"
        prod2 = "PMSR00000000000000000000000006"

        self.oHelper.SearchBrowse(f"D MG 01 {projeto}", "Filial+projeto")
        self.oHelper.SetButton("Planejamentos")
        self.oHelper.SetBranch("D MG 01")
        self.oHelper.SetButton("Gerar")
        self.oHelper.SetValue("Descricao", projeto)
        self.oHelper.SetValue("Planej. De", "29/06/2020")
        self.oHelper.SetValue("Planej. Ate", "03/07/2020")
        self.oHelper.SetValue("Cons.Armaz.", "01,02")
        self.oHelper.SetButton("Salvar")
      
        # Verifica Empenho Gerado
        self.oHelper.SetButton("Visualizar")
        self.oHelper.SetButton("Outras Ações")
        self.oHelper.ClickMenuPopUpItem("Detalhes")
        self.oHelper.ClickMenuPopUpItem("Empenhos")

        self.oHelper.CheckResult("Produto", prod1, grid=True, line=1)
        self.oHelper.CheckResult("Armazem", "01", grid=True, line=1)
        self.oHelper.CheckResult("Qtd.Empenhada", "10,00", grid=True, line=1)

        self.oHelper.CheckResult("Produto", prod1, grid=True, line=2)
        self.oHelper.CheckResult("Armazem", "02", grid=True, line=2)
        self.oHelper.CheckResult("Qtd.Empenhada", "5,00", grid=True, line=2)

        self.oHelper.CheckResult("Produto", prod1, grid=True, line=3)
        self.oHelper.CheckResult("Armazem", "02", grid=True, line=3)
        self.oHelper.CheckResult("Qtd.Empenhada", "25,00", grid=True, line=3)

        self.oHelper.CheckResult("Produto", prod2, grid=True, line=4)
        self.oHelper.CheckResult("Armazem", "01", grid=True, line=4)
        self.oHelper.CheckResult("Qtd.Empenhada", "10,00", grid=True, line=4)
        
        self.oHelper.CheckResult("Produto", prod2, grid=True, line=5)
        self.oHelper.CheckResult("Armazem", "02", grid=True, line=5)
        self.oHelper.CheckResult("Qtd.Empenhada", "20,00", grid=True, line=5)

        self.oHelper.LoadGrid()
       
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton("Sair")

        self.oHelper.RestoreParameters()
        self.oHelper.AssertTrue()
       
    @classmethod
    def tearDownClass(self):
        """
        Method that finishes the test case. 
        """
        self.oHelper.TearDown() 

if __name__ == "__main__":
    unittest.main()