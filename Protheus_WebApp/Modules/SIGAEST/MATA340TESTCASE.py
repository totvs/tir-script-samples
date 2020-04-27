from tir import Webapp
import unittest

class MATA340(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAEST","15/01/2020","T1","D MG 01 ","04")
        inst.oHelper.Program("MATA340")

    def test_MATA340_001(self):
        self.oHelper.SetButton("Visualizar")
        self.oHelper.SetButton("Detalhes")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Sair")
        self.oHelper.SetButton("Parâmetros")
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Ok")
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()