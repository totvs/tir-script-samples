from tir import Webapp
import unittest

class OGA290(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAAGR','20/09/2019','T1','D MG 01 ','67')		
        inst.oHelper.Program('OGA290')
        inst.oHelper.AddParameter("MV_INTGFE","",".T.",".T.",".T.")
        inst.oHelper.AddParameter("MV_AGRA001","",".T.",".T.",".T.")#Novo UBA
        inst.oHelper.AddParameter("MV_AGRO002","",".T.",".T.",".T.")#Nova comercialização
        inst.oHelper.SetParameters()

    def test_OGA290_CT001(self): 
        
        self.oHelper.SearchBrowse("D MG 01 000069", key="Filial+contrato")
        self.oHelper.SetButton('Outras Ações', 'Gerar Previsão Financeira')									
        self.oHelper.WaitProcessing("Processando...")
        self.oHelper.SetButton('Visualizar')							
        self.oHelper.WaitShow("Contratos - VISUALIZAR")						
        self.oHelper.ClickFolder("Financeiro")		
        self.oHelper.CheckResult("NN7_VALOR", "139.624,70", grid=True, line=1)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton('Outras Ações', 'Demonstrativo de Preços')							
        self.oHelper.SetButton('Close')					
        self.oHelper.SetButton('Fechar')						
        self.oHelper.AssertTrue()
    
    def test_OGA290_CT002(self): 
        
        if self.oHelper.GetRelease() > '12.1.027':
            self.oHelper.SearchBrowse("D MG 01 000329", key="Filial+contrato")
            self.oHelper.SetButton("Alterar")
            self.oHelper.ClickFolder("Previsão de Entrega")                                
            self.oHelper.SetValue("TES Rem", "517", grid=True, grid_number=2, row=1)
            self.oHelper.SetValue("Op.Futura", "1", grid=True, grid_number=2, row=1)
            self.oHelper.LoadGrid()        
            self.oHelper.SetButton('Confirmar')                
            self.oHelper.SetButton('Fechar')		                
            self.oHelper.SetButton('Outras Ações', 'Confirmar')
            self.oHelper.SetValue("Descrição/Observação","Ok")
            self.oHelper.SetButton('Salvar')	
            self.oHelper.SetButton('Fechar')		        
            self.oHelper.SetButton('Outras Ações','Mais ações...,Emitir NF Operação Futura')									                    
            self.oHelper.ClickBox("Id Regra", "001", grid_number = 1)
            self.oHelper.SetButton("Salvar")
            self.oHelper.WaitShow("Romaneio(s) gerado(s) com sucesso.")        
            self.oHelper.SetButton("Fechar")
            
            self.oHelper.SetButton('Outras Ações', 'Mais Ações...,Romaneios')
            self.oHelper.CheckResult("TOTAIS", "(S) VENDA ENTREGA FUTURA", grid=True, grid_number=2, line=1)
            self.oHelper.CheckResult("Qtd. Fisica", "100.000,00", grid=True, grid_number=2, line=1)
            self.oHelper.CheckResult("Qtd. Fiscal", "100.000,00", grid=True, grid_number=2, line=1)
            self.oHelper.CheckResult("Valor Total", "177.580,50", grid=True, grid_number=2, line=1)
            self.oHelper.LoadGrid()        
            self.oHelper.SetButton('Close')					        
            self.oHelper.AssertTrue()
    
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()