from tir import Webapp
import unittest

class PCOA040(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()

        inst.oHelper.Setup("SIGAPCO", "10/03/2017", "T1", "D MG 01 ", "57")

        inst.oHelper.Program("PCOA040")

    def test_PCOA040_001(self):
        #Altera
        codigo = 'D MG 01 00000101'
        self.oHelper.SearchBrowse(f"{codigo}", "Filial+processo + item")
        
        self.oHelper.SetButton("Lançamentos")
        self.oHelper.SetValue("C.O.","AK2->AK2_CO", grid=True) #AKC_CO
        self.oHelper.LoadGrid()   
        self.oHelper.SetButton("Confirmar")
        
        #Visualiza
        self.oHelper.SearchBrowse(f"{codigo}", "Filial+processo + item")
        
        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("C.O.","AK2->AK2_CO",grid=True, line=1)
        self.oHelper.LoadGrid()   
        self.oHelper.SetButton("Confirmar")

        self.oHelper.AssertTrue()


    def test_PCOA040_002(self):
        #Altera
        codigo = 'D MG 01 00000101'
        self.oHelper.SearchBrowse(f"{codigo}", "Filial+processo + item")
        self.oHelper.SetButton("Lançamentos")
        
        
        self.oHelper.SetValue("Chave Ident.","AK2->AK2_CO", grid=True,check_value=False) #AKC_CO
        self.oHelper.LoadGrid()   
        self.oHelper.SetButton("Ok")

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
