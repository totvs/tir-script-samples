from tir import Webapp
import unittest

class GFEA111(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAGFE", "01/11/2020", "T1", "D MG 01", "78")
        inst.oHelper.Program("GFEA111")

    def test_GFEA111_CT001(self):         
       
        self.oHelper.SetValue('Filial de ?','')
        self.oHelper.SetValue('Filial ate ?','ZZZZZZZZ')
        self.oHelper.SetValue('Nr. Pre-Fatura de ?','0')
        self.oHelper.SetValue('Nr. Pre-Fatura ate ?','99999999')
        self.oHelper.SetValue('Data de Criacao de ?','01/11/2020')
        self.oHelper.SetValue('Data de Criacao ate ?','31/12/2020')
        self.oHelper.SetValue('Transportador de ?','')
        self.oHelper.SetValue('Transportador ate ?','ZZZZZZZZZZZZZZ')
        self.oHelper.SetValue('Destino ?','spool')
                        
        self.oHelper.SetButton('OK')

        self.oHelper.SetButton('Fechar')        

        self.oHelper.AssertTrue()
        
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == "__main__":
    unittest.main()