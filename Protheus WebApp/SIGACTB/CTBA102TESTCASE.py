from tir import Webapp
import unittest


class CTBA102(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        # Endereço do webapp e o nome do Browser
        inst.oHelper = Webapp()

        # Parametros de inicializaçao
        inst.oHelper.Setup("SIGACTB", "15/04/2015", "T1", "M SP 01 ", "34")

        # Nome da rotina do Caso de Teste
        inst.oHelper.Program("CTBA102")
        
        inst.oHelper.AddParameter("MV_CTBAPLA","","4")
        inst.oHelper.AddParameter("MV_ATUSAL" ,"","N")
        inst.oHelper.AddParameter("MV_CONTBAT","","S")
        inst.oHelper.AddParameter("MV_CONTSB" ,"","N")
        inst.oHelper.AddParameter("MV_CTBLIMC","","0.20;0.20;0.20;0.20;0.20")
        inst.oHelper.AddParameter("MV_CTBCENC","","10101010003")
        inst.oHelper.SetParameters()

    @classmethod
    def test_CTBA102_001(self):

        self.oHelper.SetButton("Incluir")

        self.oHelper.SetBranch("M SP 01 ")
        
        self.oHelper.SetValue("Lote", "000001")
        self.oHelper.SetButton("Ok")

        self.oHelper.SetValue("Tipo Lcto" ,"3 - Partida Dobrada",grid=True)
        self.oHelper.SetValue("CT2_DEBITO","101030105" ,grid=True)
        self.oHelper.SetValue("CT2_CREDIT","2130205"   ,grid=True)
        self.oHelper.SetValue("CT2_VALOR" ,"1000,00"   ,grid=True)
        self.oHelper.SetValue("Hist Lanc" ,"TESTE INC.",grid=True) 
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Salvar")

        self.oHelper.SetButton("Cancelar")

        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("CT2_VALOR", "1.000,00", grid=True, line=1)

        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Cancelar")

        self.oHelper.AssertTrue()

    def test_CTBA102_002(self):
        # INCLUSAO COLOCANDO O LOTE PROPRIO

        self.oHelper.SetButton("Incluir")

        self.oHelper.SetBranch("M SP 01 ")

        self.oHelper.SetValue("Lote", "998877")
        self.oHelper.SetButton("Ok")

        self.oHelper.SetValue("Tipo Lcto", "3 - Partida Dobrada", grid=True)
        self.oHelper.SetValue("CT2_DEBITO", "101030105", grid=True)
        self.oHelper.SetValue("CT2_CREDIT", "2130205", grid=True)
        self.oHelper.SetValue("CT2_VALOR", "5000000000,00", grid=True)
        self.oHelper.SetValue("CT2_HP", "456", grid=True)
        self.oHelper.SetValue("CT2_CCD", "124", grid=True)
        self.oHelper.SetValue("CT2_CCC", "223", grid=True)

        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Salvar")

        self.oHelper.SetButton("Cancelar")

        self.oHelper.SetButton("Visualizar")

        self.oHelper.ClickGridCell("CT2_VALOR")        
        self.oHelper.SetKey("F4", grid=True)
        self.oHelper.SetButton("x")       
        
        self.oHelper.ClickGridCell("CT2_VALOR")        
        self.oHelper.SetKey("F5", grid=True)
        self.oHelper.SetButton("Fechar")

        #self.oHelper.ClickGridCell("CT2_VALOR")        
        #self.oHelper.SetKey("F6", grid=True)
        #self.oHelper.SetButton("Fechar")          

        self.oHelper.ClickGridCell("CT2_VALOR")        
        self.oHelper.SetKey("F7", grid=True)
        self.oHelper.SetButton("x")       

        self.oHelper.CheckResult("CT2_VALOR", "5.000.000.000,00", grid=True, line=1)

        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Cancelar")

        self.oHelper.AssertTrue()

    def test_CTBA102_003(self):
        # Copiar para filial atual.
        codigo = "101010100           13/07/2015"

        self.oHelper.SearchBrowse(f"M SP 01 {codigo}", "Filial+cta Debito + Data Lcto")

        self.oHelper.SetButton("Outras Ações", "Copiar")

        self.oHelper.SetBranch("M SP 01 ")

        self.oHelper.SetButton("Ok")

        self.oHelper.SetButton("Salvar")

        self.oHelper.SetButton("Cancelar")

        self.oHelper.AssertTrue()

    def test_CTBA102_004(self):
        
        codigo = "15/04/2015998877"

        self.oHelper.SearchBrowse(f"M SP 01 {codigo}",key=1,index=True)

        # Excluir em lote        
        self.oHelper.SetButton("Outras Ações", "Excluir")
        self.oHelper.SetButton("Sim")
        
        # PARAMETROS
        self.oHelper.SetValue("mv_par01", "15042015")  # Da data ?
        self.oHelper.SetValue("mv_par02", "15042015")  # Ate a Data ?
        self.oHelper.SetValue("mv_par03", "998877")  # Do Lote?
        self.oHelper.SetValue("mv_par04", "998877")  # Ate o Lote?
        self.oHelper.SetValue("mv_par05", "000")  # Do SubLote ?
        self.oHelper.SetValue("mv_par06", "999")  # Ate o SubLote?
        self.oHelper.SetValue("mv_par07", "000000")  # Do Documento ?
        self.oHelper.SetValue("mv_par08", "999999")  # Ate o Documento ?
        self.oHelper.SetValue("mv_par08", "999999")  # Ate o Documento ?
        self.oHelper.SetValue("Gerar na data lanc.orig. ?", "Não")  # Ate o Documento ?        
        self.oHelper.SetValue("Imp.relat. inconsist. ?", "Não")  # Ate o Documento ?

        self.oHelper.SetButton("Ok")

        self.oHelper.SetButton("Ok")

        self.oHelper.SearchBrowse(f"M SP 01 {codigo}")

        self.oHelper.SetButton('Visualizar')        

        self.oHelper.CheckResult("CT2_DEBITO", "101030105", grid=True, line=1)
        self.oHelper.CheckResult("CT2_CREDIT", "2130205", grid=True, line=1)
        self.oHelper.CheckResult("CT2_VALOR", "5.000.000.000,00", grid=True, line=1)        
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Cancelar")

        self.oHelper.AssertFalse()

    def test_CTBA102_005(self):

        codigo = "101010100           13/07/2015"
        
        self.oHelper.SearchBrowse(f"M SP 01 {codigo}", "Filial+cta Debito + Data Lcto")

        self.oHelper.SetButton("Outras Ações", "Excluir")
        self.oHelper.SetButton("Não")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Sim")

        self.oHelper.SearchBrowse(f"M SP 01 {codigo}", "Filial+cta Debito + Data Lcto")

        self.oHelper.AssertTrue()

    def test_CTBA102_006(self):
        # Alteração  moeda e historico
        
        codigo = "101030105           15/04/2015"        

        self.oHelper.SearchBrowse(f"M SP 01 {codigo}", "Filial+cta Debito + Data Lcto")

        self.oHelper.SetButton("Alterar")
        self.oHelper.SetButton("Ok")

        self.oHelper.SetValue("CT2_HIST", "TESTANDOO",grid=True)
        self.oHelper.SetValue("CT2_VALOR", "5.000,00",grid=True)
        self.oHelper.LoadGrid()

        self.oHelper.CheckResult("CT2_HIST", "TESTANDOO", grid=True)
        self.oHelper.CheckResult("CT2_VALOR", "5.000,00", grid=True)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Salvar")

        self.oHelper.AssertTrue()

    def test_CTBA102_007(self):
        # Copiar para filial destino com inserção automatica - Data somente preenchda na capa do lote
        
        codigo = "101010100           13/07/2015"

        self.oHelper.SearchBrowse(f"M SP 01 {codigo}", "Filial+cta Debito + Data Lcto")

        self.oHelper.SetButton("Outras Ações", "Cópia Filial")

        self.oHelper.SetValue("MV_PAR01", "D MG 01",name_attr=True)

        self.oHelper.SetButton("Ok")

        self.oHelper.SetValue("Data", "18042018")

        self.oHelper.SetButton("Ok")

        self.oHelper.SetButton("Salvar")

        self.oHelper.SearchBrowse(f"D MG 01 {codigo}", "Filial+cta Debito + Data Lcto")

        self.oHelper.AssertTrue()

    def test_CTBA102_008(self):
        #Inclui lançamento com LP pelo CTBA102

        self.oHelper.SetButton("Incluir")

        self.oHelper.SetBranch("M SP 01 ")

        self.oHelper.SetValue("Lote","TIR008")
        self.oHelper.SetValue("Lçto.Padrão","TIR")
        self.oHelper.SetButton("Ok")

        self.oHelper.SetButton("Salvar")

        self.oHelper.SetButton("Cancelar")

        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("CT2_VALOR", "1.000,00", grid=True)

        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Cancelar")

        self.oHelper.AssertTrue()
    
    def test_CTBA102_009(self):
        #Inclui lançamento com Rateio online

        self.oHelper.SetButton("Incluir")

        self.oHelper.SetBranch("M SP 01 ")

        self.oHelper.SetValue("Lote","TIR009")
        self.oHelper.SetValue("Lçto.Padrão","TIR")
        self.oHelper.SetButton("Ok")

        self.oHelper.ClickGridCell("CT2_DEBITO")        
        self.oHelper.SetKey("F3", grid=True)  
        self.oHelper.SearchBrowse("012340000")
        self.oHelper.SetButton("Ok")

        self.oHelper.SetValue("nValRat","1.000,00",name_attr=True)                
        
        self.oHelper.SetButton("Ok")        

        self.oHelper.SetButton("Salvar")
        
        self.oHelper.SetButton("Cancelar")

        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("CT2_VALOR", "500,00",grid=True,line=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Cancelar")

        self.oHelper.AssertTrue()        
        
    def test_CTBA102_010(self):
        #Inclui lançamento com Rateio online

        self.oHelper.SetButton("Incluir")

        self.oHelper.SetBranch("M SP 01 ")

        self.oHelper.SetValue("Lote","TIR010")
        self.oHelper.SetValue("Lçto.Padrão","TIR")
        self.oHelper.SetButton("Ok")
    
        self.oHelper.ClickGridCell("CT2_HP")
        
        self.oHelper.SetKey("F3", grid=True)    

        self.oHelper.SearchBrowse("TIR")
        
        self.oHelper.SetButton("Ok")

        self.oHelper.SetButton("Ok")

        self.oHelper.SetButton("Salvar")

        self.oHelper.SetButton("Cancelar")

        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("CT2_VALOR", "1.000,00",grid=True,line=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Cancelar")

        self.oHelper.AssertTrue()
        
    def test_CTBA102_011(self):

        codigo = "11/10/2015008810001000001"        
        
        self.oHelper.SearchBrowse(f"M SP 01 {codigo}",key=1,index=True)

        self.oHelper.SetButton("Outras Ações", "Excluir")
        self.oHelper.SetButton("Não")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Sim")

        self.oHelper.WaitProcessing("Aguarde")

        self.oHelper.SearchBrowse(f"M SP 01 {codigo}",key=1,index=True)

        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("CT2_DEBITO", "012340002", grid=True, line=1)        
        self.oHelper.CheckResult("CT2_VALOR", "10.000,00", grid=True, line=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Cancelar")

        self.oHelper.AssertFalse()   
        
    def test_CTBA102_012(self):
        
        codigo = "11/10/2015008850001000001"        
        
        self.oHelper.SearchBrowse(f"M SP 01 {codigo}",key=1,index=True)

        self.oHelper.SetButton("Outras Ações", "Excluir")
        self.oHelper.SetButton("Não")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Sim")

        self.oHelper.WaitProcessing("Aguarde")

        self.oHelper.SearchBrowse(f"M SP 01 {codigo}",key=1,index=True)

        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("CT2_DEBITO", "012340003", grid=True, line=1)        
        self.oHelper.CheckResult("CT2_VALOR", "10.000,00", grid=True, line=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Cancelar")

        self.oHelper.AssertFalse()
        
    def test_CTBA102_013(self):
        
        codigo = "11/10/2015008850001000002"        
        
        self.oHelper.SearchBrowse(f"M SP 01 {codigo}",key=1,index=True)

        self.oHelper.SetButton("Outras Ações", "Excluir")
        self.oHelper.SetButton("Não")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Sim")

        self.oHelper.WaitProcessing("Aguarde")

        self.oHelper.SearchBrowse(f"M SP 01 {codigo}",key=1,index=True)

        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("CT2_DEBITO", "012340002", grid=True, line=1)        
        self.oHelper.CheckResult("CT2_VALOR", "1.000,00", grid=True, line=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Cancelar")

        self.oHelper.AssertFalse()   
     
     
    def test_CTBA102_014(self):

        self.oHelper.SetButton("Incluir")

        self.oHelper.SetBranch("M SP 01 ")
        
        self.oHelper.SetValue("Lote", "CTB666")
        self.oHelper.SetButton("Ok")

        self.oHelper.SetValue("Tipo Lcto" ,"1 - Debito" ,grid=True)
        self.oHelper.SetValue("CT2_DEBITO","10101010001",grid=True)
        self.oHelper.SetValue("CT2_CREDIT",""           ,grid=True)
        self.oHelper.SetValue("Hist Lanc" ,"TESTE"      ,grid=True) 
        self.oHelper.SetValue("CT2_VALR02","100,00"     ,grid=True)        
        self.oHelper.LoadGrid()

        self.oHelper.SetKey("DOWN",grid=True)       

        self.oHelper.SetValue("Tipo Lcto" ,"2 - Credito",grid=True)
        self.oHelper.SetValue("CT2_DEBITO",""           ,grid=True)
        self.oHelper.SetValue("CT2_CREDIT","10101010002",grid=True)
        self.oHelper.SetValue("Hist Lanc" ,"TESTE"      ,grid=True) 
        self.oHelper.SetValue("CT2_VALR02","100,15"     ,grid=True)        
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Salvar")

        self.oHelper.SetButton("Cancelar")

        self.oHelper.SetButton("Visualizar")
        
        self.oHelper.CheckResult("CT2_DEBITO", "10101010003", grid=True, line=3)
        self.oHelper.CheckResult("CT2_VALR02", "0,15"       , grid=True, line=3)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Cancelar")

        self.oHelper.AssertTrue()

    ################################################################################
    # Inclusão de lançamento com rateio online
    # https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T50023
    ################################################################################

    def test_CTBA102_015(self):

        codLote = 'RTON01'

        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("D RJ 02 ")
        self.oHelper.SetValue("Data", "14/04/2015")
        self.oHelper.SetValue("Lote", codLote)
        self.oHelper.SetButton("Ok")

        self.oHelper.SetValue("Tipo Lcto" ,"5 - Rateio",grid=True, row=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetValue("Valor a Ratear", "100,00")
        self.oHelper.SetValue("Histórico", "CT015 CTBA102 RATEIO ONLINE")
        self.oHelper.SetButton("Ok")

        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Cancelar")

        self.oHelper.SearchBrowse(f"D RJ 02 14/04/2015RTON01001000001001")
        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("Tipo Lcto", "3 - Partida Dobrada", grid=True, line=1)        
        self.oHelper.CheckResult("CT2_DEBITO", "RTONCTBA102D", grid=True, line=1)        
        self.oHelper.CheckResult("CT2_CREDIT", "RTONCTBA102C", grid=True, line=1)        
        self.oHelper.CheckResult("CT2_VALOR", "50,00", grid=True, line=1)
        self.oHelper.CheckResult("CT2_HIST", "CT015 CTBA102 RATEIO ONLINE", grid=True, line=1)

        self.oHelper.CheckResult("Tipo Lcto", "3 - Partida Dobrada", grid=True, line=2)        
        self.oHelper.CheckResult("CT2_DEBITO", "RTONCTBA102D", grid=True, line=2)        
        self.oHelper.CheckResult("CT2_CREDIT", "RTONCTBA102C", grid=True, line=2)        
        self.oHelper.CheckResult("CT2_VALOR", "50,00", grid=True, line=2)
        self.oHelper.CheckResult("CT2_HIST", "CT015 CTBA102 RATEIO ONLINE", grid=True, line=2)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Confirmar")


    ################################################################################
    # Alteração de histórico de lançamento utilizando a funcionalidade de replica
    # https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T50025
    ################################################################################    
    def test_CTBA102_016(self):

        codLote = 'TIR016'

        self.oHelper.SearchBrowse(f"M SP 01 14/04/2015{codLote}001000001001")
        self.oHelper.SetButton("Alterar")
        self.oHelper.SetButton("Ok")

        self.oHelper.SetFocus("Hist Lanc", grid_cell=True, row_number=2)
        self.oHelper.SetKey("ESC")
        self.oHelper.SetButton("Outras Ações", "Replicar")

        self.oHelper.ClickCheckBox("Replicar conteúdo do campo em todas as linhas anteriores")
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Sim")
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Salvar")

        self.oHelper.SearchBrowse(f"M SP 01 14/04/2015{codLote}001000001001")
        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("CT2_DEBITO", "RPLCTBA102TR16", grid=True, line=1)        
        self.oHelper.CheckResult("CT2_CREDIT", "RPLCTBA102TR16C", grid=True, line=1)
        self.oHelper.CheckResult("CT2_VALOR", "6.000,00", grid=True, line=1)      
        self.oHelper.CheckResult("CT2_HIST", "REPLICA DE HISTORICO", grid=True, line=1)
        
        self.oHelper.CheckResult("CT2_DEBITO", "RPLCTBA102TR16", grid=True, line=2)        
        self.oHelper.CheckResult("CT2_CREDIT", "RPLCTBA102TR16C", grid=True, line=2)
        self.oHelper.CheckResult("CT2_VALOR", "5.000,00", grid=True, line=2)      
        self.oHelper.CheckResult("CT2_HIST", "REPLICA DE HISTORICO", grid=True, line=2)
        
        self.oHelper.CheckResult("CT2_DEBITO", "RPLCTBA102TR16", grid=True, line=3)        
        self.oHelper.CheckResult("CT2_CREDIT", "RPLCTBA102TR16C", grid=True, line=3)
        self.oHelper.CheckResult("CT2_VALOR", "4.000,00", grid=True, line=3)      
        self.oHelper.CheckResult("CT2_HIST", "REPLICA DE HISTORICO", grid=True, line=3)
        
        self.oHelper.CheckResult("Tipo Lcto", "Cont.Hist", grid=True, line=4)        
        self.oHelper.CheckResult("CT2_VALOR", "0,00", grid=True, line=4)      
        self.oHelper.CheckResult("CT2_HIST", "CONTINUACAO DE HISTORICO REPLICA", grid=True, line=4)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Confirmar")

        self.oHelper.AssertTrue()


    @classmethod
    def tearDownClass(inst):        

        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
