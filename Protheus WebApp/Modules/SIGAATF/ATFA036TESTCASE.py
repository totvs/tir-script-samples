from tir import Webapp
import unittest

class ATFA036(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAATF', '01052016', 'T1', 'D MG 01 ')
        inst.oHelper.Program('ATFA036')
    
    def test_ATFA036_CT001(self):

        self.oHelper.SearchBrowse('D MG 01 100000000200401')
        #N3_FILIAL+N3_CBASE+N3_ITEM+N3_TIPO+N3_BAIXA+N3_SEQ 

        self.oHelper.SetButton("Visualizar")
        
        self.oHelper.CheckResult('N1_CBASE', '1000000002')
        self.oHelper.CheckResult('N1_ITEM', '005 ')
        self.oHelper.CheckResult('N1_AQUISIC', '01/12/2015')
        
        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()
    
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()  

if __name__ == '__main__':
    unittest.main()


    

