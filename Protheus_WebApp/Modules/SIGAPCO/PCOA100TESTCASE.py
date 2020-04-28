from tir import Webapp
import unittest
from datetime import datetime
import string
import random

class PCOA100(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper =  Webapp()
        inst.oHelper.Setup('SIGAPCO', '26/02/2019', 'T1', 'D MG 01 ')
        inst.oHelper.Program('PCOA100')
  
    def test_PCOA100_CT001(self):
        codigoCT001 = 'PLANILHA0000001'
        memoCT001   = 'PLANILHA SEMANAL'
        
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetBranch('D MG 01 ')
        self.oHelper.SetValue('AK1_CODIGO', codigoCT001)
        self.oHelper.SetValue('AK1_DESCRI', codigoCT001)
        self.oHelper.SetValue('AK1_TPPERI', '1'             )
        self.oHelper.SetValue('AK1_INIPER', '01/01/2019'    )
        self.oHelper.SetValue('AK1_FIMPER', '31/12/2019'    )
        self.oHelper.SetValue('AK1_MEMO', memoCT001         )
        self.oHelper.SetValue('AK1_CTRUSR', '1'             )
        self.oHelper.SetButton('Salvar')    
        self.oHelper.SetButton('Cancelar')
        self.oHelper.SearchBrowse(f'D MG 01 {codigoCT001}0001')
        self.oHelper.AssertTrue()
    
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()    