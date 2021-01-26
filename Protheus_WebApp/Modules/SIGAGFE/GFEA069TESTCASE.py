from tir import Webapp
import unittest

class GFEA069(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAGFE", "29/12/2020", "T1", "D MG 01", "78")
        inst.oHelper.Program("GFEA069")

    def test_GFEA069_CT001(self):         
       
        self.oHelper.SetButton('Importar Tarifas')

        self.oHelper.SetButton('Cancelar')

        self.oHelper.SetButton('Outras Ações','Modelo importação')

        self.oHelper.SetButton('OK')

        self.oHelper.SetButton('Cancelar')

        self.oHelper.SetButton('Outras Ações','Imprimir Browse')

        self.oHelper.SetButton('Imprimir')

        self.oHelper.SetButton('Sair')

        self.oHelper.AssertTrue()      
            
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == "__main__":
    unittest.main()