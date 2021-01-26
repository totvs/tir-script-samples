from tir import Webapp
import unittest

class GFEA115(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAGFE", "01/12/2020", "T1", "D MG 01", "78")
        inst.oHelper.Program("GFEA115")

    def test_GFEA115_CT001(self):         
        
        self.oHelper.SetButton('Importar')
        self.oHelper.SetButton('OK')

        self.oHelper.SetValue('Transportador de ?','')
        self.oHelper.SetValue('Transportador ate ?','ZZZZZZZZ')
        self.oHelper.SetValue('Diretorio Importacao ?','\EDI_CONEMB')
        self.oHelper.SetValue('Diretorio Backup OK?','\EDI_CONEMB\OK')
        self.oHelper.SetValue('Diretorio Backup NOK ?','\EDI_CONEMB\ERRO')
        self.oHelper.SetValue('Acao ?','Imp e Processar')
                        
        self.oHelper.SetButton('OK')
        
        self.oHelper.SetButton('Fechar')

        self.oHelper.AssertTrue()
            
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == "__main__":
    unittest.main()
