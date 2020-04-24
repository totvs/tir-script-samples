from tir import Webapp
import unittest

class MATA552(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAEST", "12/12/2019", "T1", "D MG 01 ", "04")
        inst.oHelper.Program("MATA552")

    def test_MATA552_001(self):
        self.oHelper.AddParameter("MV_GRADE", "", "T", "T", "T")
        self.oHelper.SetParameters()
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetButton("OK")
        self.oHelper.SetValue("Prod. Refer.", "ESTSE00000000000000000003")
        self.oHelper.SetValue("Cod. Curva", "0001")
        self.oHelper.SetValue("Cod. Curva", "0001")
        self.oHelper.SetValue("Quantidade", "1,00", grid=True, grid_number=0)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.AssertTrue()
    
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
