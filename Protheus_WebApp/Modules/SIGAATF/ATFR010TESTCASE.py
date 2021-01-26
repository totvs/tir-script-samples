from tir import Webapp
import unittest

class ATFR010(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAATF', '01052016', 'T1', 'M SP 02')
        inst.oHelper.Program('ATFR010')
    
    @classmethod
    def test_ATFR010_001(self):

        self.oHelper.SetButton("Outras Ações", "Parâmetros")
        self.oHelper.SetValue('DE :','01/01/2018')
        self.oHelper.SetValue('ATE :','31/01/2018')
        self.oHelper.SetButton('Ok')
        self.oHelper.SetButton("Imprimir")
    
        self.oHelper.SetButton("Sair")

        self.oHelper.AssertTrue()   

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()  

if __name__ == '__main__':
    unittest.main()


    

