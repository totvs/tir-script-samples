from tir import Webapp
import unittest

class OGA840(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        
        from datetime import datetime
        DateSystem = datetime.today().strftime('%d/%m/%Y')
    
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAAGR',DateSystem,'T1','D MG 01 ','67')
        inst.oHelper.Program('OGA840')
        
    def test_OGA840_CT001(self):
         
        if self.oHelper.GetRelease() > "12.1.027":
            self.oHelper.SetButton("Outras Ações","Gestão de Volumes/Preço")                
            self.oHelper.WaitShow("Itens do Plano de Vendas")
            self.oHelper.ClickGridCell("Mês/Ano", row=1, grid_number=1)                       
        
            self.oHelper.SetValue("Tipo Mercado", "1",grid_number=1, grid=True)        
            self.oHelper.SetValue("Mês/Ano", "122020",grid_number=1, grid=True)                
            self.oHelper.SetValue('Perc Venda',"100,000000",grid_number=1, grid=True)                
            self.oHelper.SetValue('Moeda',"2",grid_number=1, grid=True)                
            self.oHelper.LoadGrid()
            self.oHelper.SetValue('Período',"122020",grid_number=2, grid=True, row=1)                
            self.oHelper.SetValue('%',"100,000000",grid_number = 2, grid=True, row=1)                        
            self.oHelper.LoadGrid()    

            self.oHelper.SetButton("Confirmar")
            self.oHelper.SetButton("Fechar") 

            self.oHelper.ClickFolder("Gestão de Preço")
            self.oHelper.SetValue('Componente',"000002",grid_number = 2, grid=True)
            self.oHelper.LoadGrid()           

            self.oHelper.SetButton("Confirmar")
            self.oHelper.SetButton("Fechar")
            self.oHelper.SetButton("x")

            self.oHelper.SetButton("Outras Ações","Gestão de Volumes/Preço",position=2)        
        
            self.oHelper.ClickFolder("Gestão de Preço")
            self.oHelper.SetButton("Atualizar Preço")
            self.oHelper.SetValue("Basis(Dolar/BU)","1",grid_number = 2, grid=True)
            self.oHelper.LoadGrid()
            self.oHelper.SetButton("Salvar")        
            self.oHelper.SetButton("Confirmar")
            self.oHelper.SetButton("Close")

            self.oHelper.CheckResult("%Prev Venda", user_value = "100,000000", grid=True,line=4 ,grid_number = 1)
            self.oHelper.AssertTrue()
        
        
    @classmethod
    def tearDownClass(inst):
            inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()

