from tir import Webapp
import unittest

class OGA450(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        
        from datetime import datetime
        DateSystem = datetime.today().strftime('%d/%m/%Y')
    
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAADV',DateSystem,'T1','D MG 01 ','67')
        inst.oHelper.Program('OGA450')
        
    def test_OGA450_CT001(self):
        self.oHelper.SetValue("Entidade", "000003")
        self.oHelper.SetValue("cLojEnt", "01",name_attr=True)
        self.oHelper.SetButton("Atualizar")        
        self.oHelper.SearchBrowse("D MG 01 2011920           AGR-SOJA GRANEL")
        self.oHelper.ClickGridCell('Contrato',2,grid_number = 2)        
        self.oHelper.SetButton("Outras Ações","Financeiro",position=2, check_error=True)        
        self.oHelper.SetButton("Pendências")
        self.oHelper.ClickBox("Romaneio","0000000079",grid_number = 2)
        self.oHelper.SetButton("Ajustar Pendencia")
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Close")        
        self.oHelper.ClickGridCell('Romaneio',1,grid_number = 2)
        self.oHelper.CheckResult("Vr.Complem.", user_value = "0,00", grid=True,line=2 ,grid_number = 2, name_attr=False)        
        self.oHelper.LoadGrid()
        self.oHelper.AssertTrue()
                
    @classmethod
    def tearDownClass(inst):
            inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()

