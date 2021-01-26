from tir import Webapp
import unittest
import time

class GFEA117(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAGFE", "01/12/2020", "T1", "D MG 01", "78")
        inst.oHelper.Program("GFEA117")

    def test_GFEA117_CT001(self):      

        time.sleep(10)   
        
        self.oHelper.SetButton('Importar')
        self.oHelper.SetButton('OK')

        self.oHelper.SetValue('Transportador de ?','')
        self.oHelper.SetValue('Transportador ate ?','ZZZZZZZZ')
        self.oHelper.SetValue('Filial Ocorrencias ?','D MG 01')
        self.oHelper.SetValue('Diretorio Importacao ?','\EDI_OCORREN')
        self.oHelper.SetValue('Diretorio Backup ?','\EDI_OCORREN\OK')
        self.oHelper.SetValue('Diretorio Backup NOK ?','\EDI_OCORREN\ERRO')
                        
        self.oHelper.SetButton('OK')
        self.oHelper.SetButton('OK')

        self.oHelper.SetButton('Processar')
        self.oHelper.SetButton('Fechar')

        self.oHelper.AssertTrue()
            
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == "__main__":
    unittest.main()
