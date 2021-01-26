from tir import Webapp
import unittest
import time

class CNTA021(unittest.TestCase):
    
    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAGCT','25/04/2019','T1','D MG 01 ','69')
        inst.oHelper.Program("CNTA021")



    def test_CNTA021_001(self):
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetBranch("D MG 01 ")

        #self.oHelper.SetValue("aCab","CN1_DESCRI", "COMPRA")
        self.oHelper.SetValue("Descricao", 'COMPRA')
        self.oHelper.SetValue("Med Eventual", '1')
        self.oHelper.SetValue("Esp. Contrat", '1')
        self.oHelper.SetValue("Multa/Bonif.", '2')
        self.oHelper.SetValue("Mult. manual", '1')



        #self.oHelper.SetValue("aCab","CN1_MULMAN", "1")
        #self.oHelper.SetValue("aCab","CN1_ESPCTR", "1")


        self.oHelper.SetButton("Confirmar")

        self.oHelper.SetButton('Fechar')
        
        self.oHelper.SetButton('Visualizar')

        self.oHelper.CheckResult("CN1_DESCRI", "COMPRA")
        self.oHelper.CheckResult("CN1_MEDEVE", "1")  
        self.oHelper.CheckResult("CN1_TPMULT", "2")
        self.oHelper.CheckResult("CN1_MULMAN", "1")
        self.oHelper.CheckResult("CN1_ESPCTR", "1")
       
        self.oHelper.CheckResult("CN1_MEDAUT", "2")
        self.oHelper.CheckResult("CN1_CROFIS", "2")
        self.oHelper.CheckResult("CN1_TPLMT" , "1")
        self.oHelper.CheckResult("CN1_CROCTB", "2")
        self.oHelper.CheckResult("CN1_CTRFIX", "1")
        self.oHelper.CheckResult("CN1_VLRPRV", "1")

        self.oHelper.SetButton('Fechar')

        self.oHelper.AssertTrue()
    
    @classmethod
    def tearDownClass(inst):
        
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()

       # @classmethod
    #def tearDownClass(inst):

       # inst.oHelper.TearDown()
        
#if __name__ == '__main__':
	#unittest.main()