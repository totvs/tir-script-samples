from tir import Webapp
import unittest

class CTBA080(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGACTB', '11/03/2019', 'T1', 'D MG 01 ')
        inst.oHelper.Program('CTBA080')
    
    @classmethod
    def test_CTBA080_CT001(self):

        self.oHelper.SearchBrowse('D MG 01 317001')

        self.oHelper.SetButton("Visualizar")
        
        self.oHelper.CheckResult('CT5_LANPAD', '317')
        self.oHelper.CheckResult('CT5_SEQUEN', '001')
        self.oHelper.CheckResult('CT5_STATUS', '1 - Ativo')
        
        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()