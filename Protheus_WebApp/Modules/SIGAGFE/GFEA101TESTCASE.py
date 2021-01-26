from tir import Webapp
import unittest

class GFEA101(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAGFE", "30/12/2020", "T1", "D MG 01", "78")
        inst.oHelper.Program("GFEA101")
           
    def test_GFEA101_CT001(self):
               
        self.oHelper.SetValue('Proprietario De ?','161')
        self.oHelper.SetValue('Proprietario Ate ?','161')
        self.oHelper.SetValue('Data de Criacao De ?','01/01/2011')
        self.oHelper.SetValue('Data de Criacao Ate ?','31/12/2020')
        self.oHelper.SetValue('Data de Vencimento ?','31/12/2020')
        self.oHelper.SetValue('Considerar Calculos Entrada ?','Nao')
        
        self.oHelper.SetButton('OK')

        self.oHelper.SetButton('OK')        
       
        self.oHelper.AssertTrue()
    
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == "__main__":
    unittest.main()