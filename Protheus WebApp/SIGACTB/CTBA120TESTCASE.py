from tir import Webapp
import unittest

class CTBA120(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGACTB", "04/11/2019", "T1", "D MG 01 ", "34")
        inst.oHelper.Program("CTBA120")

    #Importar arquivo csv
    def test_CTBA120_001(self):

        self.oHelper.SetButton("Outras Ações","Importar")
        

        self.oHelper.SetBranch("D MG 01 ")

        self.oHelper.SetValue("Arquivo para Importação ?","\\baseline\\rateio_externo2.csv")
        self.oHelper.SetValue("Sobrescreve regra existente", "Não")
       
        self.oHelper.SetButton("OK")

        self.oHelper.SetButton("Sair")
        
        

        self.oHelper.SearchBrowse("D MG 01 100   001")
        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("CTJ_RATEIO", "100")
       

        self.oHelper.AssertTrue()
    
    
    

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
