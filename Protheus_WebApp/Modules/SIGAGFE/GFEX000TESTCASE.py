from tir import Webapp
import unittest

class GFEX000(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAGFE", "26/06/2020", "T1", "D MG 01", "78")
        inst.oHelper.Program("GFEX000")

    def test_GFEX000_CT001(self):   
                
        self.oHelper.SetButton('Outras Ações','Filial x Emitente')

        self.oHelper.SetButton('Cancelar')

        self.oHelper.SetButton('Fechar')

        self.oHelper.AssertTrue()      
        
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == "__main__":
    unittest.main()
