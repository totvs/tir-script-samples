from tir import Webapp
import unittest
import datetime

class OMSA320(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
         # set the date
        dataAtual = str(datetime.datetime.now().strftime("%d/%m/%Y")) 
        inst.oHelper.Setup('SIGAOMS',dataAtual,'T1','D MG 01 ','39')
        inst.oHelper.Program("OMSA320")

    #Efetuar Retorno
    def test_OMSA320_CT001(self): 

        self.oHelper.SearchBrowse("D MG 01 000020")

        self.oHelper.SetButton("Efetua Retorno")

        self.oHelper.SetButton("Outras Ações", "Apont.")
        self.oHelper.SetButton("Salvar")

        self.oHelper.SetButton("Salvar")
        
        self.oHelper.AssertTrue()  

    #Estornar Retorno
    def test_OMSA320_CT002(self): 

        self.oHelper.SearchBrowse("D MG 01 000020")

        self.oHelper.SetButton("Visualiza")
        self.oHelper.SetButton("Cancelar")

        self.oHelper.SetButton("Outras Ações", "Estorna Retorno")
        self.oHelper.SetButton("Sim")
        
        self.oHelper.AssertTrue()  

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == "__main__":
    unittest.main()