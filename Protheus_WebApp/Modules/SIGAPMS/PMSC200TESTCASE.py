from tir import Webapp 
import unittest
from datetime import datetime 
DateSystem = datetime.today().strftime("%d/%m/%Y")

class PMSC200(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.oHelper = Webapp()
        self.oHelper.Setup("SIGAPMS", DateSystem, "T1", "D MG 01 ", "44")
        self.oHelper.Program("PMSC200") 

    def test_PMSC200_CT001(self):
        projects = 'PMS0000200'

        self.oHelper.SearchBrowse(f"D MG 01 {projects}", "Filial+projeto")
        self.oHelper.SetButton("Outras Ações","Consultar")
        self.oHelper.WaitShow('Planilha de Consulta do Projeto - CONSULTAR')
        self.oHelper.SetButton("Outras Ações","Informacoes do Projeto")     
        self.oHelper.SetButton("Fechar")       
        self.oHelper.SetButton("Outras Ações","Pesquisar")
        self.oHelper.WaitShow("Pesquisar")
        self.oHelper.SetValue("Pesquisar por?","03")
        self.oHelper.ClickCheckBox("Utilizar Pesquisa Exata")
        self.oHelper.ClickCheckBox("Pesquisar Proxima Ocorrencia")
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Outras Ações","Pesquisar")
        self.oHelper.WaitShow("Pesquisar")
        self.oHelper.SetValue("Pesquisar por?","PMS0000200")
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Outras Ações","Legenda")
        self.oHelper.SetButton("Fechar")
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(self):
        self.oHelper.TearDown()  

if __name__ == "__main__":
    unittest.main()