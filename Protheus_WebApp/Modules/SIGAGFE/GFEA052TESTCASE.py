from tir import Webapp
import unittest

class GFEA052(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAGFE", "29/12/2020", "T1", "D MG 01", "78")
        inst.oHelper.Program("GFEA052")
           
    def test_GFEA052_CT001(self):
               
        self.oHelper.SetValue('Filial ?','D MG 01')
        self.oHelper.SetValue('Romaneio de ?','00000041')
        self.oHelper.SetValue('Romaneio até ?','00000041')
        self.oHelper.SetValue('Tipo Impressão ?','Previa/Reimpres')
        self.oHelper.SetValue('Modelo Impressão ?','Romaneio')
        self.oHelper.SetButton('OK')
        self.oHelper.SetButton('OK')
        self.oHelper.SetButton('OK')
        self.oHelper.SetButton('Sair')
               
        self.oHelper.AssertTrue()
    
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == "__main__":
    unittest.main()