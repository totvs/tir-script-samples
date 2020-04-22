from tir import Webapp 
import unittest
from datetime import datetime
import time  
DateSystem = datetime.today().strftime("%d/%m/%Y")

class PMSC200(unittest.TestCase):

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
        self.oHelper.Program("PMSC200") 

    def test_PMSC200_CT001(self):
        '''
        Test Case CT001 - CT001 - GTSER-T45082 (1.0) - Consultar um projeto
        '''

        projects = 'PMS0000200'

        self.oHelper.SearchBrowse(f"D MG 01 {projects}", "Filial+projeto")
        self.oHelper.SetButton("Outras Ações","Consultar")
        self.oHelper.WaitShow('Planilha de Consulta do Projeto - CONSULTAR')
        #Passo 1 - Legenda/Informações do projeto
        self.oHelper.SetButton("Outras Ações","Informacoes do Projeto")
        time.sleep(10)        
        self.oHelper.SetButton("Fechar")
        #Passo 2 - Pesquisar (Localizar Tarefa 02) - Teste Negativo        
        self.oHelper.SetButton("Outras Ações","Pesquisar")
        self.oHelper.WaitShow("Pesquisar")
        self.oHelper.SetValue("Pesquisar por?","03")
        self.oHelper.ClickCheckBox("Utilizar Pesquisa Exata")
        self.oHelper.ClickCheckBox("Pesquisar Proxima Ocorrencia")
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Fechar")
        #Passo 3 - Pesquisar
        self.oHelper.SetButton("Outras Ações","Pesquisar")
        self.oHelper.WaitShow("Pesquisar")
        self.oHelper.SetValue("Pesquisar por?","PMS0000200")
        self.oHelper.SetButton("Ok")
        #Passo 4 - Legenda do Browse
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Outras Ações","Legenda")
        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()

    def test_PMSC200_CT002(self):
        '''
        Test Case CT002 - GTSER-T45083 (1.0)- Acessar a opcao 'nova'
        '''

        projects = 'PMS0000200'
        cpath = 'baseline\pmsc200_ct002.pln'

        self.oHelper.SearchBrowse(f"D MG 01 {projects}", "Filial+projeto")
        self.oHelper.SetButton("Nova")
        self.oHelper.SetValue("Descricao ? *","pmsc200_ct002")
        self.oHelper.SetValue("Arquivo ? *",f"\{cpath}")
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Add.Todos >>")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.WaitShow('Planilha de Consulta do Projeto - NOVA')
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Outras Ações","Configurar")
        self.oHelper.SetButton("<< Rem.Todos")
        self.oHelper.SetButton("Formula >>")
        self.oHelper.SetValue("Titulo ?","pmsc200ct002")
        self.oHelper.SetValue("Formula ?","pmsc200ct002")
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Restaurar")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.AssertTrue()
    @classmethod
    def tearDownClass(self):
        """
        Method that finishes the test case. 
        """
        self.oHelper.TearDown()  

if __name__ == "__main__":
    unittest.main()