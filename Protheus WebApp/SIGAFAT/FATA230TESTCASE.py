from tir import Webapp 
import unittest
from datetime import datetime
import time  
DateSystem = datetime.today().strftime("%d/%m/%Y")

class FATA230(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        '''
        SETUP
        Test Case Initial Setup
        '''
        #Endereco do webapp e o nome do Browser 
        self.oHelper = Webapp()

        #Parametros de inicializacao
        self.oHelper.Setup("SIGAFAT", DateSystem, "T1", "D RJ 01 ", "05")

        #Nome da rotina do Caso de Teste
        self.oHelper.Program("FATA230") 

    def test_FATA230_CT001(self):
        '''
        Test Case CT001 - Incluir Web Service
        '''

        cWs = "FTC001"
        cDesc = "CT001 - INCLUSAO"
        
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("D RJ 01 ")
        self.oHelper.WaitShow("Web Services - INCLUIR")
        self.oHelper.SetValue("AI7_WEBSRV", cWs)
        self.oHelper.SetValue("AI7_DESCRI", cDesc)     
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        #Valida resultado
        self.oHelper.SearchBrowse(f"D RJ    {cWs}", "Filial+codigo WS")        
        self.oHelper.SetButton("Visualizar")
        self.oHelper.CheckResult("AI7_WEBSRV", cWs)
        self.oHelper.CheckResult("AI7_DESCRI", cDesc)
        self.oHelper.SetButton("Fechar")
        self.oHelper.AssertTrue()

    def test_FATA230_CT002(self):
        '''
        Test Case CT002 - Alterar Web service
        '''

        cWs = "FTU002"
        cDesc = "CT002 - ALTERADO"

        self.oHelper.SearchBrowse(f"D RJ    {cWs}", "Filial+codigo WS")
        self.oHelper.SetButton("Alterar")        
        self.oHelper.WaitShow("Web Services - ALTERAR")
        self.oHelper.SetValue("AI7_DESCRI", cDesc)
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        #Valida resultado
        self.oHelper.SearchBrowse(f"D RJ    {cWs}", "Filial+codigo WS")        
        self.oHelper.SetButton("Visualizar")
        self.oHelper.CheckResult("AI7_WEBSRV", cWs)
        self.oHelper.CheckResult("AI7_DESCRI", cDesc)
        self.oHelper.SetButton("Fechar")
        self.oHelper.AssertTrue()

    def test_FATA230_CT003(self):
        '''
        Test Case CT003 - Excluir Web service
        '''
        cWs = "FTEXC"
        cDesc = "CT003 - EXCLUIR"
        
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("D RJ 01 ")
        self.oHelper.WaitShow("Web Services - INCLUIR")
        self.oHelper.SetValue("AI7_WEBSRV", cWs)
        self.oHelper.SetValue("AI7_DESCRI", cDesc)     
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")

        self.oHelper.SearchBrowse(f"D RJ    {cWs}", "Filial+codigo WS")
        self.oHelper.SetButton("Outras Ações","Excluir")        
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.AssertTrue()

    def test_FATA230_CT004(self):
        '''
        Test Case CT004 - Acessar a opcao Automatico
        '''

        cWs = "FTU002"

        self.oHelper.SearchBrowse(f"D MG    {cWs}", "Filial+codigo WS")
        self.oHelper.SetButton("Outras Ações","Automatico")
        self.oHelper.SetBranch("D RJ 01 ")
        time.sleep(10)
        self.oHelper.SetButton("X")
        self.oHelper.Program("FATA240")

        self.oHelper.AssertTrue()
    @classmethod
    def tearDownClass(self):
        '''
        Method that finishes the test case. 
        '''
        self.oHelper.TearDown()  

if __name__ == "__main__":
    unittest.main()