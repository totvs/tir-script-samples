from tir import Webapp 
import unittest
from datetime import datetime
import time  
DateSystem = datetime.today().strftime("%d/%m/%Y")

class FATA240(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        '''
        SETUP
        Test Case Initial Setup
        '''
        #Endereco do webapp e o nome do Browser 
        self.oHelper = Webapp()

        #Parametros de inicializacao
        self.oHelper.Setup("SIGAFAT", DateSystem, "T1", "D MG 01 ", "05")

        #Nome da rotina do Caso de Teste
        self.oHelper.Program("FATA240") 

    def test_FATA240_CT001(self):
        '''
        Test Case CT001 - Incluir Portal
        '''

        cPortal = "FTC001"
        cDesc = "CT001 - INCLUSAO"
        
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("D MG 01 ")
        self.oHelper.WaitShow("Menu dos Portais - INCLUIR")
        self.oHelper.SetValue("AI9_PORTAL", cPortal)
        self.oHelper.SetValue("AI9_DESCRI", cDesc)
        self.oHelper.SetValue("AI9_DESC_S", cDesc)
        self.oHelper.SetValue("AI9_DESC_E", cDesc)        
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SearchBrowse(f"D MG    {cPortal}", "Filial+portal")
        #Valida resultado
        self.oHelper.SetButton("Visualizar")
        self.oHelper.CheckResult("AI9_PORTAL", cPortal)
        self.oHelper.CheckResult("AI9_DESCRI", cDesc)
        self.oHelper.CheckResult("AI9_DESC_S", cDesc)
        self.oHelper.CheckResult("AI9_DESC_E", cDesc)
        self.oHelper.SetButton("Fechar")
        self.oHelper.AssertTrue()

    def test_FATA240_CT002(self):
        '''
        Test Case CT002 - Alterar Portal
        '''

        cPortal = "FTU002"
        cDesc = "CT002 / CT004 - ALTERADO"

        self.oHelper.SearchBrowse(f"D MG    {cPortal}", "Filial+portal")
        self.oHelper.SetButton("Alterar")        
        self.oHelper.WaitShow("Menu dos Portais - ALTERAR")
        self.oHelper.SetValue("AI9_PORTAL", cPortal)
        self.oHelper.SetValue("AI9_DESCRI", cDesc)
        self.oHelper.SetValue("AI9_DESC_S", cDesc)
        self.oHelper.SetValue("AI9_DESC_E", cDesc)
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SearchBrowse(f"D MG    {cPortal}", "Filial+portal")
        #Valida resultado
        self.oHelper.SetButton("Visualizar")
        self.oHelper.CheckResult("AI9_PORTAL", cPortal)
        self.oHelper.CheckResult("AI9_DESCRI", cDesc)
        self.oHelper.CheckResult("AI9_DESC_S", cDesc)
        self.oHelper.CheckResult("AI9_DESC_E", cDesc)
        self.oHelper.SetButton("Fechar")
        self.oHelper.AssertTrue()

    def test_FATA240_CT003(self):
        '''
        Test Case CT004 - Excluir Portal
        '''

        cPortal = "FTD003"

        self.oHelper.SearchBrowse(f"D MG    {cPortal}", "Filial+portal")
        self.oHelper.SetButton("Outras Ações","Excluir")        
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.AssertTrue()

    def test_FATA240_CT004(self):
        '''
        Test Case CT004 - Inclui menu no portal
        '''

        cPortal = "FTU002"
        cText = 'CT004 - INCLUI MENU'    

        self.oHelper.SearchBrowse(f"D MG    {cPortal}", "Filial+portal")
        self.oHelper.SetButton("Outras Ações","Menu") 
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetValue("AI8_TEXTO", cText)
        self.oHelper.SetValue("AI8_TEXTOE", cText)
        self.oHelper.SetValue("AI8_TEXTOS", cText)
        self.oHelper.SetValue("AI8_ORDEM", '1')
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Ok")
        self.oHelper.AssertTrue()

    def test_FATA240_CT005(self):
        '''
        Test Case CT005 - Altera menu do portal
        '''

        cPortal = "FTU005"
        cText = 'CT005 - ALTERADO'    

        self.oHelper.SearchBrowse(f"D MG    {cPortal}", "Filial+portal")
        self.oHelper.SetButton("Outras Ações","Menu")
        self.oHelper.ClickTree("CT005 / CT006 - MENU > CT005 - ALTERACAO")
        self.oHelper.SetButton("Editar")
        self.oHelper.SetValue("AI8_TEXTO", cText)
        self.oHelper.SetValue("AI8_TEXTOE", cText)
        self.oHelper.SetValue("AI8_TEXTOS", cText)
        self.oHelper.SetValue("AI8_ORDEM", '1')
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Ok")
        self.oHelper.AssertTrue()

    def test_FATA240_CT006(self):
        '''
        Test Case CT006 - Exclui menu do portal
        '''

        cPortal = "FTU005"

        self.oHelper.SearchBrowse(f"D MG    {cPortal}", "Filial+portal")
        self.oHelper.SetButton("Outras Ações","Menu")
        self.oHelper.ClickTree("CT005 / CT006 - MENU > CT006 - EXCLUSAO")
        self.oHelper.SetButton("Excluir")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Ok")
        self.oHelper.AssertTrue()

    def test_FATA240_CT007(self):
        '''
        Test Case CT007 - Mover item para baixo/cima
        '''

        cPortal = "FTR007"

        self.oHelper.SearchBrowse(f"D MG    {cPortal}", "Filial+portal")
        self.oHelper.SetButton("Outras Ações","Menu")
        self.oHelper.ClickTree("CT007 - MOVER > NIVEL001")
        self.oHelper.SetButton("Mover para baixo")
        self.oHelper.SetButton("Mover para cima")
        self.oHelper.SetButton("Ok")        
        self.oHelper.AssertTrue()
    @classmethod
    def tearDownClass(self):
        """
        Method that finishes the test case. 
        """
        self.oHelper.TearDown()  

if __name__ == "__main__":
    unittest.main()