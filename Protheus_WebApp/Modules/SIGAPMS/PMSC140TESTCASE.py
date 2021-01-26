from tir import Webapp 
import unittest
from datetime import datetime
import time  
DateSystem = datetime.today().strftime("%d/%m/%Y")

class PMSC140(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        '''
        SETUP
        Test Case Initial Setup
        '''
        #Endereco do webapp e o nome do Browser 
        self.oHelper = Webapp()

        #Parametros de inicializacao
        self.oHelper.Setup("SIGAPMS", DateSystem, "T1", "D MG 01 ", "44")

        #Nome da rotina do Caso de Teste
        self.oHelper.Program("PMSC140") 

    def test_PMSC140_CT001(self):
        '''
        Test Case CT001 - GTSER-T45103 (1.0) - Consultar uma EDT/Tarefa
        '''

        project = 'PMS0000200'

        self.oHelper.SearchBrowse(f"D MG 01 {project}", "Filial+projeto")
        #Passo 1
        self.oHelper.SetButton("Consulta")
        self.oHelper.WaitShow('Consulta de EDT/Tarefa Filhas')        
        self.oHelper.SetButton("Outras Ações","Informacoes do Projeto")
        time.sleep(10)        
        self.oHelper.SetButton("Fechar")
        #Passo 2 - Pesquisar
        self.oHelper.SetButton("Outras Ações","Pesquisar")
        self.oHelper.SetValue("Pesquisar por ? ","PMS0000200")
        self.oHelper.ClickCheckBox("Pesquisar Proxima Ocorrencia")
        self.oHelper.SetButton("Ok")
        #Passo 3 - Consultas    
        self.oHelper.SetButton("Outras Ações","Consultas")
        self.oHelper.SetButton("X")
        self.oHelper.SetButton("Fechar")
        self.oHelper.AssertTrue()

    def test_PMSC140_CT002(self):
        '''
        Test Case CT002 - GTSER-T45104 (1.0) - Outras Ações - Legenda
        '''

        project = 'PMS0000200'

        self.oHelper.SearchBrowse(f"D MG 01 {project}", "Filial+projeto")
        #Passo 1 - Pesquisar
        self.oHelper.SetButton("Consulta")
        self.oHelper.WaitShow('Consulta de EDT/Tarefa Filhas')
        self.oHelper.SetButton("Outras Ações","Pesquisar")
        self.oHelper.SetValue("Pesquisar por ? ","PMS0000200")
        self.oHelper.ClickCheckBox("Utilizar Pesquisa Exata")
        self.oHelper.ClickCheckBox("Pesquisar Proxima Ocorrencia")
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Fechar")
        #Passo 3 - Legenda 
        self.oHelper.SetButton("Outras Ações","Legenda")
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