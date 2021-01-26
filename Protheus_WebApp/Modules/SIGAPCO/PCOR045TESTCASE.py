from tir import Webapp
import unittest

class PCOR045(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAPCO', '05/09/2019', 'T1', 'M SP 01')
        inst.oHelper.Program('PCOR045')
    
    @classmethod
    def test_PCOR045_001(self):

        self.oHelper.SetValue("Planilha ?",'TIRPCO1003')
        self.oHelper.SetValue("Versao ?",'0001')

        self.oHelper.SetValue("Periodo de ?",'01/01/2019')
        self.oHelper.SetValue("Periodo ate ?",'31/12/2019')
        self.oHelper.SetValue("C.O. de ?",'')
        self.oHelper.SetValue("C.O. ate ?",'ZZZZZZZZZZZZZZZ')
        self.oHelper.SetValue("Classe de ?",'')
        self.oHelper.SetValue("Classe ate ?",'ZZZZZZ')
        self.oHelper.SetValue("Operacao de ?",'')
        self.oHelper.SetValue("Operacao ate ?",'ZZZZZZZZZZ')
        self.oHelper.SetValue("Imprime Sinteticas ?",'Sim')
        self.oHelper.SetValue("Totaliza Sinteticas ?",'Por Planilha')

        self.oHelper.SetButton("OK")
        
        self.oHelper.SetButton("Imprimir")
        self.oHelper.WaitShow('Numero de copias')

        self.oHelper.AssertTrue()   

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()  

if __name__ == '__main__':
    unittest.main()