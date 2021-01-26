from tir import Webapp
import unittest

class OGA450(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        
        from datetime import datetime
        DateSystem = datetime.today().strftime('%d/%m/%Y')
    
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAADV',DateSystem,'T1','D MG 01 ','67')
        inst.oHelper.Program('OGA450')        
    
    #Cenário 001: Ajustar pendência de fixação, gerando complemento de preço - modelo clássico
    def test_OGA450_CT001(self):       
       
        self.oHelper.SetValue("Entidade", "000003")
        self.oHelper.SetValue("cLojEnt", "01",name_attr=True)
        self.oHelper.SetButton("Atualizar")        
        self.oHelper.SearchBrowse("D MG 01 2011920           AGR-SOJA GRANEL")
        self.oHelper.ClickGridCell('Contrato',2,grid_number = 2)        
        self.oHelper.SetButton("Outras Ações","Financeiro",position=2, check_error=True)        
        self.oHelper.SetButton("Pendências")
        self.oHelper.ClickBox("Romaneio","0000000079",grid_number = 2)
        self.oHelper.SetButton("Ajustar Pendencia")
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("x")        
        self.oHelper.ClickGridCell('Romaneio',1,grid_number = 2)
        self.oHelper.CheckResult("Vr.Complem.", user_value = "0,00", grid=True,line=2 ,grid_number = 2, name_attr=False)        
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("x")        
        self.oHelper.AssertTrue()

    def test_OGA450_CT002(self):
        ##Cenário 002: Automatizar o processo de alterar/incluir  fixacao        
        self.oHelper.SetValue("Entidade", "000003")
        self.oHelper.SetValue("cLojEnt", "01",name_attr=True)
        self.oHelper.SetButton("Atualizar")
        self.oHelper.SearchBrowse("D MG 01 2011920           AGR-SOJA GRANEL")
        self.oHelper.ScrollGrid(column="Contrato", match_value="000125", grid_number=2)        
        self.oHelper.SetButton("Outras Ações","Financeiro",position=2, check_error=True)
        self.oHelper.ClickGridCell("Filial", row=2, grid_number=1)
        self.oHelper.SetButton("Alterar")        
        self.oHelper.SetValue("Dt.Ini.Ent.", "01/08/2020" )
        self.oHelper.SetValue("Dt.Fin.Ent.", "31/08/2020" ) 
        self.oHelper.SetButton("Confirmar")    
        self.oHelper.SetValue("Descrição/Observação", "Teste Automatizado - TIR")
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Fechar")                   
        
        self.oHelper.SetButton("Visualizar")
        self.oHelper.CheckResult("NN8_VALTOT", user_value = "100.000,00")
        self.oHelper.SetButton("Fechar")        
        self.oHelper.AssertTrue()     

    def test_OGA450_CT003(self):
        #Cenário 003: Ajustar pendência de fixação, gerando complemento de preço - modelo novo
        self.oHelper.AddParameter("MV_SIGAAGR","",".T.",".T.",".T.")
        self.oHelper.AddParameter("MV_AGRA001","",".T.",".T.",".T.")#Novo UBA
        self.oHelper.AddParameter("MV_AGRO002","",".T.",".T.",".T.")#Nova comercialização
        self.oHelper.SetParameters()
        self.oHelper.SetValue("Entidade", "000001")
        self.oHelper.SetValue("cLojEnt", "01",name_attr=True)
        self.oHelper.SetButton("Atualizar")
        self.oHelper.SearchBrowse("D MG 01 2011920           AGR-SOJA GRANEL")
        self.oHelper.ScrollGrid(column="Contrato", match_value="000128", grid_number=2)        
        self.oHelper.SetButton("Outras Ações","Pendências",position=2, check_error=True)
        self.oHelper.ClickBox("Filial", "D MG 01", grid_number=1)
        self.oHelper.SetButton("Solucionar Pendências")        
        self.oHelper.SetButton("OK")                
        self.oHelper.SetButton("Gerar Complemento")                
        self.oHelper.WaitProcessing("Gerando Nf de Complemento.")
        self.oHelper.CheckResult("Valor", user_value = "49.713,72", grid_number=2, grid=True)
        self.oHelper.LoadGrid()
        self.oHelper.AssertTrue()        

    def test_OGA450_CT004(self):
        #Cenário 004: Transferência simples de saldo entre contratos
        self.oHelper.AddParameter("MV_SIGAAGR","",".T.",".T.",".T.")
        self.oHelper.AddParameter("MV_AGRA001","",".F.",".F.",".F.")#Novo UBA
        self.oHelper.AddParameter("MV_AGRO002","",".F.",".F.",".F.")#Nova comercialização
        self.oHelper.SetParameters()
        self.oHelper.SetValue("Entidade", "000003")
        self.oHelper.SetValue("cLojEnt", "01",name_attr=True)
        self.oHelper.SetButton("Atualizar")
        self.oHelper.SearchBrowse("D MG 01 1011920           AGR-SOJA GRANEL")
        self.oHelper.ScrollGrid(column="Contrato", match_value="000015", grid_number=2)        
        self.oHelper.SetButton("Outras Ações","Transferência",position=2, check_error=True)
        self.oHelper.SetValue("cTesDev", "501", name_attr=True)
        self.oHelper.SetValue("cLocalO", "01", name_attr=True)
        self.oHelper.SetValue("cDCodEnt", "000002", name_attr=True)
        self.oHelper.SetValue("cDLojEnt", "01", name_attr=True)
        self.oHelper.SetValue("cTipoDest", "Compra", name_attr=True)
        self.oHelper.SetValue("cTESDest", "001",name_attr=True)
        self.oHelper.SetValue("nQtd","200",name_attr=True, check_value=False)
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Sim")
        self.oHelper.ScrollGrid(column="Contrato", match_value="000050", grid_number=1)        
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")

        self.oHelper.SetButton("Romaneios")        
        self.oHelper.CheckResult("Qtd. Fiscal", user_value = "200,00", grid_number=2, grid=True, line=2)
        self.oHelper.LoadGrid()
        self.oHelper.AssertTrue()        
    
    def test_OGA450_CT005(self):
        #Cenário 004: Transferência múltipla de saldo entre contratos
        self.oHelper.AddParameter("MV_SIGAAGR","",".T.",".T.",".T.")
        self.oHelper.AddParameter("MV_AGRA001","",".F.",".F.",".F.")#Novo UBA
        self.oHelper.AddParameter("MV_AGRO002","",".F.",".F.",".F.")#Nova comercialização
        self.oHelper.SetParameters()
        self.oHelper.SetValue("Entidade", "000001")
        self.oHelper.SetValue("cLojEnt", "01",name_attr=True)
        self.oHelper.SetButton("Atualizar")        
        self.oHelper.SetButton("Trf. Mul. Origens")
        self.oHelper.SetButton("Outras Ações", "Filtro")
        self.oHelper.SetValue("MV_PAR01", "000001", name_attr=True)
        self.oHelper.SetValue("MV_PAR02", "01", name_attr=True)
        self.oHelper.SetValue("MV_PAR03", "000002", name_attr=True)
        self.oHelper.SetValue("MV_PAR04", "01", name_attr=True)
        self.oHelper.SetValue("MV_PAR05", "000024", name_attr=True, check_value=False)
        self.oHelper.SetValue("MV_PAR06", "000029", name_attr=True, check_value=False)
        self.oHelper.SetButton("OK")
        self.oHelper.ClickBox("Contrato", "000024", grid_number=1)        
        self.oHelper.ClickBox("Contrato", "000029", grid_number=1)        
        self.oHelper.SetButton("Transferir")
        self.oHelper.SetValue("cTipoDest", "Compra", name_attr=True)
        self.oHelper.SetValue("cTESDest", "004",name_attr=True)
        self.oHelper.SetValue("nQtd","20200",name_attr=True, check_value=False)
        self.oHelper.SetValue("cLocalD", "01", name_attr=True)
        self.oHelper.SetValue("cNFPSer","01",name_attr=True)
        self.oHelper.SetValue("cNFPNum","151520",name_attr=True)
        self.oHelper.SetValue("TES","504",grid=True, row=1)
        self.oHelper.SetValue("Local","01",grid=True, row=1)
        self.oHelper.SetValue("Qt.Transf","200",grid=True, row=1, check_value=False)
        self.oHelper.SetValue("TES","504",grid=True, row=2)
        self.oHelper.SetValue("Local","01",grid=True, row=2)
        self.oHelper.SetValue("Qt.Transf","20000",grid=True, row=2, check_value=False)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Sim")
        self.oHelper.ScrollGrid(column="Contrato", match_value="000074")        
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("x")
        self.oHelper.SearchBrowse("D MG 01 1011920           AGR-SOJA GRANEL")
        self.oHelper.ScrollGrid(column="Contrato", match_value="000074", grid_number=2)                

        self.oHelper.SetButton("Romaneios")        
        self.oHelper.CheckResult("Qtd. Fiscal", user_value = "20.200,00", grid_number=2, grid=True, line=1)
        self.oHelper.LoadGrid()
        self.oHelper.AssertTrue()    

    @classmethod
    def tearDownClass(inst):
            inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()

