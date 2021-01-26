from tir import Webapp
import unittest
import datetime
import time

class GFEA116(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()

        dataAtual = str(datetime.datetime.now().strftime("%d/%m/%Y")) 

        inst.oHelper.Setup("SIGAGFE", dataAtual, "T1", "D MG 01", "78")
        inst.oHelper.Program("GFEA116")

    def test_GFEA116_CT001(self):

        time.sleep(10)         
        
        self.oHelper.SetButton('Importar')
        self.oHelper.SetButton('OK')
                        
        self.oHelper.SetValue('Transportador de ?','')
        self.oHelper.SetValue('Transportador ate ?','ZZZZZZZZ')
        self.oHelper.SetValue('Filial das Faturas ?','D MG 01')
        self.oHelper.SetValue('Diretorio Importacao ?','\EDI_DOCCOB')
        self.oHelper.SetValue('Diretorio Backup OK?','\EDI_DOCCOB\OK')
        self.oHelper.SetValue('Diretorio Backup NOK ?','\EDI_DOCCOB\ERRO')
        self.oHelper.SetValue('Manter zeros esquerda Nr Fat ?','Sim')
        self.oHelper.SetValue('Acao ?','Imp e Processar')

        self.oHelper.SetButton('OK')

        self.oHelper.SetButton('Fechar')

        self.oHelper.AssertTrue()
            
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == "__main__":
    unittest.main()
