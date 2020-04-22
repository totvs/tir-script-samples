from tir import Webapp 
import unittest
from datetime import datetime
import time  
DateSystem = datetime.today().strftime("%d/%m/%Y")

class FATA150(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        '''
        SETUP
        Test Case Initial Setup
        '''
        #Endereço do webapp e o nome do Browser
        self.oHelper = Webapp()

        #Parametros de inicializaçao
        self.oHelper.Setup("SIGAFAT", DateSystem, "T1", "D MG 01 ", "05")

        #Nome da rotina do Caso de Teste
        self.oHelper.Program("FATA150")

    def test_FATA150_CT001(self):
        '''
        Test Case CT001 - Inclusão de Categoria x Produto - Interface Por categoria
        '''

        cCategory = 'FATC01'
        cProduct01 = 'FATC00000000000000000000000001'
        cProduct02 = 'FATC00000000000000000000000002'

        self.oHelper.WaitShow("Parametros")
        self.oHelper.SetValue("Tipo de Interface","Por Categoria")
        self.oHelper.SetButton("OK")
        self.oHelper.WaitShow("Amarração Categoria x Grupo ou Produto")
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("D MG 01 ")
        self.oHelper.WaitShow("Amarração Categoria x Grupo ou Produto - INCLUIR")
        self.oHelper.SetValue("Categoria", cCategory)        
        self.oHelper.SetValue("Produto", cProduct01, grid=True, row=1)        
        self.oHelper.SetKey("DOWN", grid=True, grid_number=1)
        self.oHelper.SetValue("Produto", cProduct02, grid=True, row=2)        
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SearchBrowse(f"D MG    {cCategory}", "Filial+categoria + Grupo + Produto")
        self.oHelper.SetButton("Visualizar")
        self.oHelper.WaitShow("Amarração Categoria x Grupo ou Produto - VISUALIZAR")
        self.oHelper.CheckResult("Categoria", cCategory)
        self.oHelper.CheckResult("Produto", cProduct01, grid=True, line=1)
        self.oHelper.CheckResult("Produto", cProduct02, grid=True, line=2)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Cancelar")
        self.oHelper.AssertTrue()

    def test_FATA150_CT002(self):
        '''
        Test Case CT002 - Alteração de Categoria x Produto - Interface Por categoria
        '''

        cCategory = 'FATU01'
        cProduct = 'FATU00000000000000000000000003'

        self.oHelper.SearchBrowse(f"D MG    {cCategory}", "Filial+categoria + Grupo + Produto")
        self.oHelper.SetButton("Alterar")
        self.oHelper.WaitShow("Amarração Categoria x Grupo ou Produto - ALTERAR")
        self.oHelper.SetValue("Produto", cProduct, grid=True, row=2)
        self.oHelper.ClickGridCell("Produto", row=1, grid_number=1)
        self.oHelper.SetKey("DELETE", grid=True, grid_number=1)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Salvar")
        self.oHelper.SearchBrowse(f"D MG    {cCategory}", "Filial+categoria + Grupo + Produto")
        self.oHelper.SetButton("Visualizar")
        self.oHelper.WaitShow("Amarração Categoria x Grupo ou Produto - VISUALIZAR")
        self.oHelper.CheckResult("Produto", cProduct, grid=True, line=1)        
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Cancelar")
        self.oHelper.AssertTrue()

    def test_FATA150_CT003(self):
        '''
        Test Case CT003 - Cópia de Categoria x Produto - Interface Por categoria
        '''

        cCategory = 'FATC02'
        cProduct = 'FATC00000000000000000000000005'

        self.oHelper.SearchBrowse(f"D MG    FATR01", "Filial+categoria + Grupo + Produto")
        self.oHelper.SetButton("Outras Ações", "Copiar")
        self.oHelper.WaitShow("Amarração Categoria x Grupo ou Produto - COPIAR")
        self.oHelper.SetValue("Categoria", cCategory)
        self.oHelper.SetValue("Produto", cProduct, grid=True, row=1)
        self.oHelper.ClickGridCell("Produto",row=2,grid_number=1)
        self.oHelper.SetKey("DELETE",grid=True)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Salvar")
        self.oHelper.SearchBrowse(f"D MG    {cCategory}", "Filial+categoria + Grupo + Produto")
        self.oHelper.SetButton("Visualizar")
        self.oHelper.WaitShow("Amarração Categoria x Grupo ou Produto - VISUALIZAR")
        self.oHelper.CheckResult("Categoria", cCategory)
        self.oHelper.CheckResult("Produto", cProduct, grid=True, line=1)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Cancelar")
        self.oHelper.AssertTrue()

    def test_FATA150_CT004(self):
        '''
        Test Case CT004 - Visualização de Categoria x Produto - Interface Por categoria
        '''

        cCategory = 'FATR01'
        cProduct01 = 'FATC00000000000000000000000003'
        cProduct02 = 'FATC00000000000000000000000004'

        self.oHelper.SearchBrowse(f"D MG    {cCategory}", "Filial+categoria + Grupo + Produto")
        self.oHelper.SetButton("Visualizar")
        self.oHelper.WaitShow("Amarração Categoria x Grupo ou Produto - VISUALIZAR")
        self.oHelper.CheckResult("Categoria", cCategory)
        self.oHelper.CheckResult("Produto", cProduct01, grid=True, line=1)
        self.oHelper.CheckResult("Produto", cProduct02, grid=True, line=2)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Confirmar")
        self.oHelper.AssertTrue()

    def test_FATA150_CT005(self):
        '''
        Test Case CT005 - Legenda de Categoria x Produto - Interface Por categoria
        '''

        self.oHelper.SetButton("Outras Ações","Legenda")
        self.oHelper.WaitShow("Amarração Categoria x Grupo ou Produto - LEGENDA")
        self.oHelper.SetButton("Fechar")
        self.oHelper.AssertTrue()

    def test_FATA150_CT006(self):
        '''
        Test Case CT006 - Exclusão de Categoria x Produto - Interface Por categoria
        '''

        cCategory = 'FATD01'

        self.oHelper.SearchBrowse(f"D MG    {cCategory}", "Filial+categoria + Grupo + Produto")
        self.oHelper.SetButton("Outras Ações", "Excluir")
        self.oHelper.WaitShow("Amarração Categoria x Grupo ou Produto - EXCLUIR")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("X")
        self.oHelper.AssertTrue()
        '''
        self.oHelper.SearchBrowse(f"D MG    {cCategory}", "Filial+categoria + Grupo + Produto")
        self.oHelper.SetButton("Visualizar")
        self.oHelper.WaitShow("Amarração Categoria x Grupo ou Produto - VISUALIZAR")
        self.oHelper.CheckResult("Categoria", cCategory)        
        self.oHelper.SetButton("Confirmar")
        self.oHelper.AssertFalse()
        '''

    def test_FATA150_CT007(self):
        '''
        Test Case CT007 - Categoria x Produto - Interfaces Por Produto / Por Grupo / Por Grade - Teste Negativo
        '''
        self.oHelper.Program("FATA150")
        self.oHelper.WaitShow("Parametros")
        self.oHelper.SetValue("Tipo de Interface","Por Produto")
        self.oHelper.CheckHelp(text_help="FT150E02", button="Fechar")
        self.oHelper.SetValue("Tipo de Interface","Por Grupo")
        self.oHelper.CheckHelp(text_help="FT150E02", button="Fechar")
        self.oHelper.SetValue("Tipo de Interface","Por Grade")
        self.oHelper.CheckHelp(text_help="FT150E02", button="Fechar")
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(self):
        """
        Method that finishes the test case.
        """
        self.oHelper.TearDown()

if __name__ == "__main__":
    unittest.main()