from tir import Webapp 
import unittest
from datetime import datetime
import time  
DateSystem = datetime.today().strftime("%d/%m/%Y")

class PMSC050(unittest.TestCase):

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
        self.oHelper.Program("PMSC050") 

    def test_PMSC050_CT001(self):
        '''
        Test Case CT001 - GTSER-T45098 (1.0) - Consultar um projeto
        '''

        budget = 'FATSERV001'

        self.oHelper.SearchBrowse(f"D MG 01 {budget}", "Filial+orcamento + Descricao")
        self.oHelper.SetButton("Outras Ações","Consultar")
        self.oHelper.WaitShow('Planilha de Consulta do Orcamento - CONSULTAR')        
        self.oHelper.SetButton("Outras Ações","Informacoes do Orcamento")
        time.sleep(10)        
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.AssertTrue()

    def test_PMSC050_CT002(self):
        '''
        Test Case CT002 - GTSER-T45099 (1.0)- Acessar a opcao 'nova'
        '''

        budget = 'FATSERV001'
        cpath = 'baseline\pmsc050_ct002.pln'

        self.oHelper.SearchBrowse(f"D MG 01 {budget}", "Filial+orcamento + Descricao")
        self.oHelper.SetButton("Nova")
        self.oHelper.SetValue("Descricao ? *","pmsc050_ct002")
        self.oHelper.SetValue("Arquivo ? *",f"\{cpath}")
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Add.Todos >>")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.WaitShow('Planilha de Consulta do Orcamento - NOVA')
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton("Outras Ações","Configurar")
        self.oHelper.SetButton("<< Rem.Todos")
        self.oHelper.SetButton("Formula >>")
        self.oHelper.SetValue("Titulo ?","pmsc050ct002")
        self.oHelper.SetValue("Formula ?","pmsc050ct002")
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