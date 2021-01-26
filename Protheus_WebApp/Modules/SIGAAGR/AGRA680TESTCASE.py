from tir import Webapp
import unittest

class AGRA680(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAAGR','21/11/2019','T1','D MG 01 ','67')		
        inst.oHelper.Program('AGRA680')

    def test_AGRA680_CT001(self): #TESTECASE IMPORTACAO HVI        
                                   
        self.oHelper.SetValue("_cGetSafra", "1920", name_attr=True)
        self.oHelper.SetValue("_cGetLayout", "008", name_attr=True)        
        self.oHelper.SetButton("Path")        
        self.oHelper.SetFilePath("\\sigaagr\\hvi\\")
        self.oHelper.SetButton("Buscar")                
        self.oHelper.ClickGridCell("Arquivo", row=1, grid_number=2)
        self.oHelper.ClickBox("Arquivo", select_all=True , grid_number=2)       
        self.oHelper.SetButton("Importar")                        
        self.oHelper.SetButton("Ok")                
        fardo1    = self.oHelper.GetValue("Cod. Fardo", grid=True, line=1, grid_number=1)
        micFardo1 = self.oHelper.GetValue("Mic", grid=True, line=1, grid_number=1)
        fardo2    = self.oHelper.GetValue("Cod. Fardo", grid=True, line=2, grid_number=1)        
        micFardo2 = self.oHelper.GetValue("Mic", grid=True, line=2, grid_number=1)

        if micFardo1 == '0,02' and micFardo2 == '0,03' and fardo1 == '012226' and fardo2 == '012227':
           self.oHelper.AssertTrue()
        else:
           self.oHelper.AssertFalse()
                      
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()