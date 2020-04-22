from tir import Webapp
import unittest

class ATFA240(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAATF', '10/04/2016', 'T1', 'M PR 01 ')
        inst.oHelper.Program('ATFA240')
    
    @classmethod
    def test_ATFA240_CT001(self):

        self.oHelper.SearchBrowse('M PR 01 NFE00000250001')

        self.oHelper.SetButton("Classificar")
        self.oHelper.SetBranch("M PR 01 ")

        self.oHelper.SetValue("Grupo","0001")
        self.oHelper.SetButton("Sim")
        
        self.oHelper.SetValue("Num.Plaqueta","NFE0000025")
        
        self.oHelper.SetButton("Confirmar")

        self.oHelper.WaitShow("Registro alterado com sucesso.")

        self.oHelper.SetButton("Fechar")

        self.oHelper.SearchBrowse('M PR 01 NFE00000250001')

        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult('N1_CBASE'   , 'NFE0000025')
        self.oHelper.CheckResult('N1_ITEM'    , '0001')
        self.oHelper.CheckResult('N1_AQUISIC' , '10/03/2016')

        self.oHelper.CheckResult('N3_TIPO'    , '01')
        self.oHelper.CheckResult('N3_CCONTAB' , '101010105')
        self.oHelper.CheckResult('N3_CDEPREC' , '101010105')
        self.oHelper.CheckResult('N3_TXDEPR1' , '10,0000')
        
        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()
    
    @classmethod   
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()