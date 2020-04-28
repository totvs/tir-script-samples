from tir import Webapp
import unittest

class OGAA580(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        
        from datetime import datetime
        DateSystem = datetime.today().strftime('%d/%m/%Y')
    
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAADV',DateSystem,'T1','D MG 01 ','67')
        
    def test_OGAA580_CT001(self):
        self.oHelper.SetLateralMenu("Atualizações > Comercialização > Cadastros Básicos > Tabela de Índice")
        self.oHelper.SetButton("Incluir") 
        self.oHelper.SetValue("N9H_INDICE", "INDICE000123212",name_attr=True)
        self.oHelper.SetValue("N9H_PROD", "AGR-SOJA GRANEL",name_attr=True)
        self.oHelper.SetValue("N9H_CODSAF", "1920",name_attr=True)
        self.oHelper.SetValue("N9H_UFORIG", "AC",name_attr=True)
        self.oHelper.SetValue("N9H_UFDEST", "AL",name_attr=True)
        self.oHelper.SetValue("N9H_DTINVG", "31/10/2019",name_attr=True)
        self.oHelper.SetValue("N9H_DTFNVG", "31/10/2021",name_attr=True)
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Sim")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SearchBrowse("INDICE000123212"+"AGR-SOJA GRANEL")
        self.oHelper.SetButton("Visualizar")
        self.oHelper.CheckResult("N9H_INDICE", user_value = "INDICE000123212")
        self.oHelper.SetButton("Fechar")
        self.oHelper.AssertTrue()
        
    @classmethod
    def tearDownClass(inst):
            inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
