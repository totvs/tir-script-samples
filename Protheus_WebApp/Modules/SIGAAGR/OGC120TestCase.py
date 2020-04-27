from tir import Webapp
import unittest

class OGC120(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        from datetime import datetime
        DateSystem = datetime.today().strftime('%d/%m/%Y')
    
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAAGR',DateSystem,'T1','D MG 01 ','67')        
        inst.oHelper.Program('OGC120')
        inst.oHelper.AddParameter("MV_AGRO002","",".T.",".T.",".T.")#Nova comercialização
        inst.oHelper.AddParameter("MV_AGRO207","",".T.",".T.",".T.")#Baixa automática
        inst.oHelper.AddParameter("MV_SIGAAGR","",".T.",".T.",".T.")#Módulo AGRO
        inst.oHelper.SetParameters()
           
    def test_OGC120_CT003(self):    
        self.oHelper.SearchBrowse("D MG 01 "+"000043")
        self.oHelper.SetButton('Outras Ações','Contato')
        self.oHelper.SetValue("Sts. Contato", "1 - Confirmado")
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')        
        self.oHelper.AssertTrue()
          
    @classmethod
    def tearDownClass(inst):
            inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()




