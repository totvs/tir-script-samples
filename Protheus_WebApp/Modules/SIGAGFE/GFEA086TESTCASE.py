from tir import Webapp
import unittest

class GFEA086(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAGFE", "29/12/2020", "T1", "D MG 01", "78")
        inst.oHelper.Program("GFEA086")
           
    def test_GFEA086_CT001(self):
               
        self.oHelper.SetValue('Filial de ?','D MG 01')
        self.oHelper.SetValue('Filial até ?','D MG 01')
        self.oHelper.SetValue('Data Criação de ?','01/01/2018')
        self.oHelper.SetValue('Data Criação até ?','31/12/2020')
        self.oHelper.SetValue('Data Liberação de ?','01/01/2018')
        self.oHelper.SetValue('Data Liberação até ?','31/12/2020')
        self.oHelper.SetButton('OK')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('x')
                      
        self.oHelper.AssertTrue()
    
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == "__main__":
    unittest.main()