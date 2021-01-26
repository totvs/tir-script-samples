from tir import Webapp
import unittest

class OGC040(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        
        from datetime import datetime
        DateSystem = datetime.today().strftime('%d/%m/%Y')
    
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAADV',DateSystem,'T1','D MG 01 ','67')
        inst.oHelper.Program('OGA290')
        inst.oHelper.AddParameter("MV_AGRA001","",".T.",".T.",".T.")#Novo UBA
        inst.oHelper.AddParameter("MV_AGRO002","",".T.",".T.",".T.")#Nova comercialização
        inst.oHelper.SetParameters()
        
    def test_OGC040_CT001(self):         
       
        self.oHelper.SearchBrowse("D MG 01 "+"000043")
        self.oHelper.SetButton("Outras Ações","Blocos e Fardos Vinculados")
        self.oHelper.SetButton("Fechar")
       
        self.oHelper.SearchBrowse("D MG 01 "+"000043")
        self.oHelper.SetButton("Visualizar")
        self.oHelper.CheckResult("NJR_CODCTR", user_value = "000043")
        self.oHelper.SetButton("Fechar")
        self.oHelper.AssertTrue()
        
    @classmethod
    def tearDownClass(inst):
            inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()




