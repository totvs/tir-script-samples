from tir import Webapp 
import unittest
from datetime import datetime
DateSystem = datetime.today().strftime("%d/%m/%Y")

class PMSC140(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.oHelper = Webapp()
        self.oHelper.Setup("SIGAPMS", DateSystem, "T1", "D MG 01 ", "44")
        self.oHelper.Program("PMSC140") 

    def test_PMSC140_CT001(self):
        project = 'PMS0000200'

        self.oHelper.SearchBrowse(f"D MG 01 {project}", "Filial+projeto")
        self.oHelper.SetButton("Consulta")
        self.oHelper.WaitShow('Consulta de EDT/Tarefa Filhas')        
        self.oHelper.SetButton("Outras Ações","Informacoes do Projeto")       
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Outras Ações","Pesquisar")
        self.oHelper.SetValue("Pesquisar por ? ","PMS0000200")
        self.oHelper.ClickCheckBox("Pesquisar Proxima Ocorrencia")
        self.oHelper.SetButton("Ok")  
        self.oHelper.SetButton("Outras Ações","Consultas")
        self.oHelper.SetButton("X")
        self.oHelper.SetButton("Fechar")
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(self):
        self.oHelper.TearDown()  

if __name__ == "__main__":
    unittest.main()