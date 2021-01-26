from tir import Webapp
import unittest

class OGA280(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAAGR','04/11/2019','T1','D MG 01 ','67')		
        inst.oHelper.Program('OGA280')		

    def test_OGA280_CT001(self): 
        #Cenário 001: Vínculo contrato de compra x contrato de venda
        self.oHelper.AddParameter("MV_AGRA001","",".F.",".F.",".F.")#Novo UBA
        self.oHelper.AddParameter("MV_AGRO002","",".F.",".F.",".F.")#Nova comercialização
        self.oHelper.SetParameters()
        self.oHelper.SearchBrowse("D MG 01 000071", key="Filial+contrato")		
        self.oHelper.SetButton('Outras Ações',"Mais Ações..., Vínculo Contratos")									
        self.oHelper.SetButton('Alocar')							
        self.oHelper.SetButton('OK')							
        self.oHelper.SetValue("Alocar", "40.000,00", grid=True, grid_number=1, name_attr=True, row=3)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton('Salvar')

        self.oHelper.SetButton('Alocar')							
        self.oHelper.SetButton('OK')							
        self.oHelper.SetValue("Alocar", "60.000,00", grid=True, grid_number=1, name_attr=True, row=3)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton('Salvar')	

        self.oHelper.CheckResult("Qtd. Vinculada", "100.000,00", grid=True, line=1, grid_number=1)
        self.oHelper.LoadGrid()
        self.oHelper.CheckResult("Qtd. Vinculada", "100.000,00", grid=True, line=1, grid_number=2)
        self.oHelper.LoadGrid()
        
        #teste delete do vínculo 
        self.oHelper.ClickGridCell("Contrato", row=1, grid_number=2)
        self.oHelper.ClickBox("Contrato", select_all=True, grid_number=2)
        self.oHelper.SetButton('Deletar Vínculo')
        self.oHelper.CheckResult("Qtd. Vinculada", "0,00", grid=True, line=1, grid_number=1)
        self.oHelper.LoadGrid()
        self.oHelper.AssertTrue()
        self.oHelper.SetButton('Sair')
        self.oHelper.RestoreParameters()        
    
    def test_OGA280_CT002(self): 
        #Cenário 002: Nota fiscal global futura
        self.oHelper.AddParameter("MV_AGRA001","",".T.",".T.",".T.")#Novo UBA
        self.oHelper.AddParameter("MV_AGRO002","",".T.",".T.",".T.")#Nova comercialização
        self.oHelper.SetParameters()
        self.oHelper.SearchBrowse("D MG 01 000129", key="Filial+contrato")		
        self.oHelper.SetButton('Alterar')    
        self.oHelper.ClickFolder("Cadência")
        self.oHelper.SetValue("TES",      "010", grid=True, grid_number=2)
        self.oHelper.SetValue("TES Rem",  "009", grid=True, grid_number=2)
        self.oHelper.SetValue("Op.Futura",  "1", grid=True, grid_number=2)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton('Confirmar')                
        self.oHelper.SetButton('Fechar')		                
        self.oHelper.SetButton('Outras Ações', 'Confirmar')
        self.oHelper.SetValue("Descrição/Observação","Ok")
        self.oHelper.SetButton('Salvar')	
        self.oHelper.SetButton('Fechar')		        
        self.oHelper.SetButton('Outras Ações','Mais ações...,Emitir NF Operação Futura')									                    
        self.oHelper.SetButton('Não')		        
        self.oHelper.ClickBox("Id Regra", "001", grid_number = 1)
        self.oHelper.SetValue("Numero NF",  "1010", grid=True, grid_number=1)
        self.oHelper.SetValue("Serie NF",  "01", grid=True, grid_number=1)
        self.oHelper.SetValue("Emissao NF",  "20/08/2020", grid=True, grid_number=1)
        self.oHelper.SetValue("Especie NF",  "NF", grid=True, grid_number=1)
        self.oHelper.LoadGrid()        
        self.oHelper.SetButton("Salvar")
        self.oHelper.WaitShow("Romaneio(s) gerado(s) com sucesso.")        
        self.oHelper.SetButton("Fechar")

        self.oHelper.SetButton('Outras Ações', 'Mais Ações...,Romaneios')
        self.oHelper.CheckResult("TOTAIS", "(E) VENDA ENTREGA FUTURA", grid=True, grid_number=2, line=1)
        self.oHelper.CheckResult("Qtd. Fisica", "100.000,00", grid=True, grid_number=2, line=1)
        self.oHelper.CheckResult("Qtd. Fiscal", "100.000,00", grid=True, grid_number=2, line=1)
        self.oHelper.CheckResult("Valor Total", "180.556,70", grid=True, grid_number=2, line=1)
        self.oHelper.LoadGrid()        
        self.oHelper.AssertTrue()        
        self.oHelper.SetButton('Close')					                
        self.oHelper.RestoreParameters()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()