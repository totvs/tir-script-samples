from tir import Webapp
import unittest

class ATFA006(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAATF', '01042019', 'T1', 'D MG 01 ')
        inst.oHelper.Program('ATFA006')
    
    @classmethod
    def test_ATFA006_CT001(self):
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetValue('FNT_CODIND', '06')
        self.oHelper.SetValue('FNT_DATA', '01/04/2019')
        self.oHelper.SetValue('FNT_TAXA', "5,00000000")       
        self.oHelper.CheckResult('FNT_CODIND', '06')
        self.oHelper.CheckResult('FNT_DATA', '01/04/2019')
        self.oHelper.CheckResult('FNT_TAXA', "5,00000000") 
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.AssertTrue()
       
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()