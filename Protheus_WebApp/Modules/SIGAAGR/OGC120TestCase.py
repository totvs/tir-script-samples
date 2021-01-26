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
        
    def test_OGC120_CT001(self):         
        
        self.oHelper.SearchBrowse("D MG 01 "+"000001")
        self.oHelper.SetButton("Outras Ações","Desvincular Adiantamentos")
        self.oHelper.ClickBox("Contrato","000001",grid_number = 2)
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Sim")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Close")        
    
        self.oHelper.SearchBrowse("D MG 01 "+"000001")
        self.oHelper.SetButton("Consulta de Previsões")
        self.oHelper.CheckResult("Valor Total à Pagar", user_value = "322.530,00")
        self.oHelper.CheckResult("Valor Total à Faturar", user_value ="322.530,00")
        self.oHelper.CheckResult("Valor Total Pago", user_value ="0,00" )
        self.oHelper.SetButton("Close")                
        self.oHelper.AssertTrue()
        
  
    def test_OGC120_CT002(self):        
        
        self.oHelper.SearchBrowse("D MG 01 "+"000043")
        self.oHelper.SetButton("Vincular Adiantamentos")
        self.oHelper.ClickBox("Contrato","000043",grid_number=2)
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Sim")        
        self.oHelper.SetButton("Close")
        
        self.oHelper.SearchBrowse("D MG 01 "+"000043")
        self.oHelper.SetButton("Consulta de Previsões")
        self.oHelper.CheckResult("Valor Total à Pagar", user_value = "18.182.955,71")
        self.oHelper.CheckResult("Valor Total à Faturar", user_value ="18.182.970,71")
        self.oHelper.CheckResult("Valor Total Pago", user_value ="15,00" )
        self.oHelper.SetButton("Close")         
        self.oHelper.AssertTrue()
    
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




