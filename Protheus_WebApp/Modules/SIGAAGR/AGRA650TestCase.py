from tir import Webapp
import unittest

class AGRA650(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        
        from datetime import datetime
        DateSystem = datetime.today().strftime('%d/%m/%Y')
    
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAADV',DateSystem,'T1','D MG 01 ','67')
        inst.oHelper.Program('AGRA650')
        
    def test_AGRA650_CT001(self):
        
        self.oHelper.SearchBrowse("D MG 01 "+"1920           "+"000013")
        self.oHelper.SetButton("Outras Ações","Incluir Fardos",position=1, check_error=True)
        self.oHelper.SetValue("MV_PAR02", "999999",name_attr=True)
        self.oHelper.SetValue("MV_PAR03", "1",name_attr=True)
        self.oHelper.SetButton("OK") 
        self.oHelper.ClickLabel("Etiqueta")
        self.oHelper.ClickBox("Etiqueta","00000000000010000243",grid_number = 1)
        self.oHelper.SetButton("Salvar")   
        self.oHelper.SearchBrowse("D MG 01 "+"1920           "+"000013")
        self.oHelper.SetButton("Visualizar")
        self.oHelper.CheckResult("DXD_CODIGO", user_value = "000013")
        self.oHelper.SetButton("Fechar")
        self.oHelper.AssertTrue()       
    
    @classmethod
    def tearDownClass(inst):
            inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
