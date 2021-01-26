from tir import Webapp
import unittest

class ATFA050(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()
        
        inst.oHelper.Setup("SIGAATF", "01/04/2016", "T1", "D MG 01 ", "01")
        inst.oHelper.Program("ATFA050")

        #inst.oHelper.AddParameter("MV_TIPDEPR","", "1")
        #inst.oHelper.AddParameter("MV_ULTDEPR","D MG 01",  "20160226")
        #inst.oHelper.AddParameter("MV_CALCDEP", "", "0" )

        #inst.oHelper.SetParameters()      

    def test_ATFA050_001(self):
        
        self.oHelper.SetButton("Informações") 
        self.oHelper.SetButton("Perguntas") 
        self.oHelper.SetButton("Log de Processos") 

        self.oHelper.SetButton("Perguntas") 


        
        self.oHelper.SetButton("Log de Processos") 

        self.oHelper.SetButton("Informações") 
        self.oHelper.SetButton("Cancelar") 


        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
