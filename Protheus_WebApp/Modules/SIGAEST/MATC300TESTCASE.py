from tir import Webapp
import unittest

class MATC300(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAEST","01/04/2018","T1","D MG 01 ","04")
        inst.oHelper.Program("MATC300")

    def test_MATC300_001(self):
        self.oHelper.SetValue("MV_PAR01", "Mar")
        self.oHelper.SetValue("MV_PAR02","2018")
        self.oHelper.SetButton("Processar")
        self.oHelper.ClickLabel("Sair")
        self.oHelper.SetButton("Sim")
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()