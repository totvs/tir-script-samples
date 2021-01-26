from tir import Webapp
import unittest

class GFEC011(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAGFE", "26/06/2020", "T1", "D MG 01", "78")
        inst.oHelper.Program("GFEC011")

    def test_GFEC011_CT001(self):        

        self.oHelper.ClickGridHeader(column = 1 )

        self.oHelper.SetButton('Movimentação')

        self.oHelper.SetValue('Tipo período ?','Anual')
        self.oHelper.SetValue('Data final ?','31/12/2018')
        self.oHelper.SetValue('Qtd períodos ?','2')
        self.oHelper.SetValue('Transp de ?','')
        self.oHelper.SetValue('Transp até ?','ZZZZZZZZZZZZZZ')
        self.oHelper.SetValue('Grupo transp ?','')
        
        self.oHelper.SetButton('Ok')

        self.oHelper.SetButton('X')

        self.oHelper.SetButton('Ocorrências')

        self.oHelper.SetValue('Tipo período ?','Anual')
        self.oHelper.SetValue('Data final ?','31/12/2018')
        self.oHelper.SetValue('Qtd períodos ?','2')
        self.oHelper.SetValue('Transp de ?','')
        self.oHelper.SetValue('Transp até ?','ZZZZZZZZZZZZZZ')
        self.oHelper.SetValue('Grupo transp ?','')

        self.oHelper.SetButton('Ok')
        
        self.oHelper.SetButton('X')    

        self.oHelper.AssertTrue()      
        
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == "__main__":
    unittest.main()
