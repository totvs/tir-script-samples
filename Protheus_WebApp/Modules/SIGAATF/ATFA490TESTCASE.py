from tir import Webapp
import unittest


class ATFA490(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()

        inst.oHelper.Setup("SIGAATF", "01/03/2016", "T1", "D MG 01 ", "01")
        inst.oHelper.Program("ATFA490")

    def test_ATFA490_001(self):

        self.oHelper.SearchBrowse("D MG 01 00000000060001")
        self.oHelper.SetButton("Outras Ações", "Copiar")
        self.oHelper.SetValue("FNU_COD","TIR01")
        self.oHelper.SetValue("FNU_DESCR","Copia TIR")

        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
