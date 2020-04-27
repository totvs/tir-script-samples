from tir import Webapp
import unittest
from datetime import datetime
import string
import random

class PCOA170(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper =  Webapp()
        inst.oHelper.Setup('SIGAPCO', '08/04/2020', 'T1', 'D MG 02 ')
        inst.oHelper.Program('PCOA170')
    
    def test_PCOA170_CT001(self):
        codigoAKN01 = 'TIR'
        memoAKN01   = 'TESTE TIR - INCLUSAO'
        
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetBranch('D MG 02 ')
        self.oHelper.SetValue('AKN_CODIGO', codigoAKN01)
        self.oHelper.SetValue('AKN_DESCRI', memoAKN01)
        self.oHelper.SetValue('AKN_NMAX', '1'             )
        self.oHelper.SetValue('AKN_CONFIG', '001'    )
        self.oHelper.SetValue('AKN_MEMO', memoAKN01         )
        self.oHelper.SetButton('Salvar')    
        self.oHelper.SetButton('Cancelar')
        self.oHelper.SearchBrowse(f'D MG 02 {codigoAKN01}')
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()    