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
        
    def test_OGAA580_CT002(self):         
        
        self.oHelper.SetButton("Outras Ações","Alterar em Lote",position=1, check_error=True)
        self.oHelper.SetValue("mv_par01", "INDICE000123214",name_attr=True)
        self.oHelper.SetValue("mv_par02", "1920",name_attr=True)
        self.oHelper.SetValue("mv_par04", "ZAUTOCONTIDA",name_attr=True)
        self.oHelper.SetValue("mv_par05", "111",name_attr=True)
        self.oHelper.SetValue("mv_par06", "999",name_attr=True)
        self.oHelper.SetValue("mv_par08", "31/10/2019",name_attr=True)
        self.oHelper.SetValue("MV_PAR10", "30/11/2019",name_attr=True)
        self.oHelper.SetValue("MV_PAR12", "AC",name_attr=True)
        self.oHelper.SetValue("MV_PAR14", "AL",name_attr=True)
        self.oHelper.SetValue("MV_PAR16", "ZZZZZZZZZZZZZZZ",name_attr=True)
        self.oHelper.SetButton("OK") 
        self.oHelper.SetValue("TMP_OBSERV", "TESTE",name_attr=True)
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
   
        self.oHelper.SearchBrowse("INDICE000123214"+"AGR-SOJA GRANEL")
        self.oHelper.SetButton("Visualizar")
        self.oHelper.CheckResult("N9H_INDICE", user_value = "INDICE000123214")
        self.oHelper.SetButton("Fechar")
   
        self.oHelper.AssertTrue()
        
    
    
    def test_OGAA580_CT003(self):         
        
        self.oHelper.SetButton("Outras Ações","Copiar em Lote",position=1, check_error=True)
        self.oHelper.SetValue("mv_par01", "INDICE000123214",name_attr=True)
        self.oHelper.SetValue("mv_par02", "1920",name_attr=True)
        self.oHelper.SetValue("mv_par04", "ZAUTOCONTIDA",name_attr=True)
        self.oHelper.SetValue("mv_par05", "111",name_attr=True)
        self.oHelper.SetValue("mv_par06", "999",name_attr=True)
        self.oHelper.SetValue("mv_par08", "31/10/2019",name_attr=True)
        self.oHelper.SetValue("MV_PAR10", "30/11/2019",name_attr=True)
        self.oHelper.SetValue("MV_PAR12", "AC",name_attr=True)
        self.oHelper.SetValue("MV_PAR14", "AL",name_attr=True)
        self.oHelper.SetValue("MV_PAR16", "ZZZZZZZZZZZZZZZ",name_attr=True)
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Sim")
        self.oHelper.SetValue("TMP_INDICE", "INDICE000123213",name_attr=True)
        self.oHelper.SetValue("TMP_CODSAF", "1920",name_attr=True)
        self.oHelper.SetValue("TMP_DTINVG", "31/10/2019",name_attr=True)
        self.oHelper.SetValue("TMP_DTFNVG", "31/10/2021",name_attr=True)
        self.oHelper.ClickCheckBox("Substituir?",1)
        self.oHelper.SetButton("Sim")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetValue("TMP_INDICE", "INDICE000123213",name_attr=True)
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Sim")
        self.oHelper.SetButton("Fechar")
        
   
        self.oHelper.SearchBrowse("INDICE000123213"+"AGR-SOJA GRANEL")
        self.oHelper.SetButton("Visualizar")
        self.oHelper.CheckResult("N9H_INDICE", user_value = "INDICE000123213")
        self.oHelper.SetButton("Fechar")
   
        self.oHelper.AssertTrue()
		
    
        
    @classmethod
    def tearDownClass(inst):
            inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
