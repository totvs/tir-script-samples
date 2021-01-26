from tir import Webapp
import unittest

class OGA360(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        
        from datetime import datetime
        DateSystem = datetime.today().strftime('%d/%m/%Y')
    
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAADV',DateSystem,'T1','D MG 01 ','67')
        inst.oHelper.Program('OGA450')        
   
   #incluir pagamento financeiro
    def test_OGA360_CT001(self):                
        from datetime import datetime
        DataVcto = datetime.today().strftime('%d/%m/%Y')

        self.oHelper.SetValue("Entidade", "000002")
        self.oHelper.SetValue("cLojEnt", "01",name_attr=True)
        self.oHelper.SetButton("Atualizar")
        self.oHelper.SearchBrowse("D MG 01 "+"1"+"01"+"1920           "+"AGR-SOJA GRANEL")
        self.oHelper.ScrollGrid(column="Contrato", match_value="000050", grid_number=2)        
        self.oHelper.SetButton("Outras Ações","Financeiro",position=2, check_error=True) 
        
        self.oHelper.WaitShow("Fixações do Contrato : 000050")
        self.oHelper.SearchBrowse("D MG 01 "+"000050"+"001")
        
        self.oHelper.SetButton("Incluir",position=2) 
        
        self.oHelper.WaitShow("Ordem de Pagamento - INCLUIR")

        self.oHelper.SetKey("F11", grid=False)
        
        self.oHelper.SetValue("mv_par01", "000",      name_attr=True)
        self.oHelper.SetValue("mv_par02", "AGR00001D",name_attr=True)
        self.oHelper.SetButton("OK") 

        self.oHelper.SetValue("Dt.Vencto.", DataVcto, grid=False)
        self.oHelper.SetValue("Qtidade/KG", "10000", grid=False,  check_value=False)
        self.oHelper.SetValue("Valor",  "10000", grid=True, check_value=False )
        self.oHelper.SetValue("Banco",  "237", grid=True, check_value=False )
        self.oHelper.SetValue("Agencia",  "152", grid=True, check_value=False )
        self.oHelper.SetValue("DV Agencia",  "1", grid=True, check_value=False )
        self.oHelper.SetValue("Conta",  "15256", grid=True, check_value=False )
        self.oHelper.SetValue("DV Conta",  "2", grid=True, check_value=False )
        self.oHelper.LoadGrid()        
        self.oHelper.SetButton("Confirmar")                
        self.oHelper.SetValue("Cta Credito",  "1110202", grid=True, check_value=False, row=1 )
        self.oHelper.SetValue("Cta Credito",  "1110202", grid=True, check_value=False, row=4 )
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Salvar")                
        self.oHelper.SetButton("Fechar")                
        self.oHelper.SetButton("Visualizar", position=2)                        
        self.oHelper.CheckResult("NN5_VLRTOT", user_value = "10.000,00")
        self.oHelper.AssertTrue() 
        
    ##Excluir ordem de pagamento de compra OGA360
    def test_OGA360_CT002(self):        
        if self.oHelper.GetRelease() > "12.1.027":
            self.oHelper.SetValue("Entidade", "000002")
            self.oHelper.SetValue("cLojEnt", "01",name_attr=True)
            self.oHelper.SetButton("Atualizar")
            self.oHelper.SearchBrowse("D MG 01 "+"1"+"01"+"1920           "+"AGR-SOJA GRANEL")
            self.oHelper.ScrollGrid(column="Contrato", match_value="000126", grid_number=2)        
            self.oHelper.SetButton("Outras Ações","Financeiro",position=2, check_error=True) 
            
            self.oHelper.WaitShow("Fixações do Contrato : 000126")
            self.oHelper.SearchBrowse("D MG 01 "+"000126"+"001")
            
            self.oHelper.ClickGridHeader(column = 1 , grid_number =  3)
            self.oHelper.SetButton("Outras Ações","Excluir",position=3, check_error=True ) 
            self.oHelper.CheckResult("NN5_CODOPG", user_value = "000003")
            self.oHelper.CheckResult("NN5_CODCTR", user_value = "000126")
            self.oHelper.CheckResult("NN5_CODFIX", user_value = "001")
            self.oHelper.AssertTrue() 
            self.oHelper.SetButton("Confirmar")
            self.oHelper.WaitShow("Registro excluído com sucesso.")   
            self.oHelper.SetButton("Fechar") 
            self.oHelper.AssertTrue()           
        
    @classmethod
    def tearDownClass(inst):
            inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()

