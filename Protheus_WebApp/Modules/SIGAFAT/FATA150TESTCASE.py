from tir import Webapp 
import unittest
from datetime import datetime
DateSystem = datetime.today().strftime("%d/%m/%Y")

class FATA150(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.oHelper = Webapp()
        self.oHelper.Setup("SIGAFAT", DateSystem, "T1", "D MG 01 ", "05")
        self.oHelper.Program("FATA150")

    def test_FATA150_CT001(self):
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

    @classmethod
    def tearDownClass(self):
        self.oHelper.TearDown()

if __name__ == "__main__":
    unittest.main()