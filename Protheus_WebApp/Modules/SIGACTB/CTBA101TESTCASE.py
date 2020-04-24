from tir import Webapp
import unittest


class CTBA101(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGACTB", "01/01/2019", "T1", "D MG 01", "34")
        inst.oHelper.Program("CTBA101")

    def test_CTBA101_001(self):
        COD = "000000004           01/06/2015"
        self.oHelper.SearchBrowse(f"D MG 01 {COD}", "Filial+cta Debito + Data Lcto")
        self.oHelper.SetButton("Outras Ações", "Estornar")
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Sim")

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
