from tir import Webapp
import unittest


class CTBA161(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()

        inst.oHelper.Setup("SIGACTB", "01/01/2019", "T1", "D MG 01", "34")

        inst.oHelper.Program("CTBA161")

#########################################
# Inclusão de Visão - Sintetica -  MODO TRADICIONAL
#########################################
    def test_CTBA161_001(self):
        self.oHelper.WaitShow("Cadastro Visao Gerencial")
        self.oHelper.SetKey("F12")
        self.oHelper.SetValue("Modo de Exibicao ?", "Tradicional")
        self.oHelper.SetButton("OK")

        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("D MG 01 ")
        self.oHelper.SetValue("CTS_CODPLA", "T01")

        # OrdemAut = self.oHelper.GetValue("CTS_ORDEM")
        # EntiGerenAut = self.oHelper.GetValue("CTS_CONTAG")

        # self.oHelper.CheckResult("CTS_ORDEM", OrdemAut)
        # self.oHelper.CheckResult("CTS_CONTAG", EntiGerenAut)

        self.oHelper.SetValue("CTS_CTASUP", "")
        self.oHelper.SetValue("CTS_DESCCG", "ENTIDADE TIR 01 INCLUIR")
        self.oHelper.SetValue("CTS_DETHCG", "TIR")
        self.oHelper.SetValue("CTS_NORMAL", "2 - Credito")
        self.oHelper.SetValue("CTS_COLUNA", "0")
        self.oHelper.SetValue("CTS_CLASSE", "1 - Sintetica")
        self.oHelper.SetValue("CTS_NOME", "TIR INCS")
        self.oHelper.SetValue("CTS_VISENT", "1 - Sim")
        self.oHelper.SetValue("CTS_FATSLD", "1 - Mantem")
        self.oHelper.SetValue("CTS_TOTVIS", "1 - Sim")
        self.oHelper.CheckView("Identificadores")
        self.oHelper.ClickCheckBox("Total Geral")

        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Cancelar")

        chave = "T01"
        # VISUALIZANDO REGISTROS PRREENCHIDOS
        self.oHelper.SearchBrowse(f"D MG 01 {chave}", key=1, index=True)
        self.oHelper.SetButton("Visualizar")
        self.oHelper.CheckResult("CTS_CODPLA", "T01")

        # self.oHelper.CheckResult("CTS_ORDEM", OrdemAut)
        # self.oHelper.CheckResult("CTS_CONTAG", EntiGerenAut)

        self.oHelper.CheckResult("CTS_CTASUP", "")
        self.oHelper.CheckResult("CTS_DESCCG", "ENTIDADE TIR 01 INCLUIR")
        self.oHelper.CheckResult("CTS_DETHCG", "TIR")
        self.oHelper.CheckResult("CTS_NORMAL", "2 - Credito")
        self.oHelper.CheckResult("CTS_COLUNA", "0")
        self.oHelper.CheckResult("CTS_CLASSE", "1 - Sintetica")
        self.oHelper.CheckResult("CTS_NOME", "TIR INCS")
        self.oHelper.CheckResult("CTS_VISENT", "1 - Sim")
        self.oHelper.CheckResult("CTS_FATSLD", "1 - Mantem")
        self.oHelper.CheckResult("CTS_TOTVIS", "1 - Sim")

        self.oHelper.SetButton("Cancelar")
        self.oHelper.AssertTrue()


#####################################################
# Alterar Planilha com Observação - Alterar Cadastro
#####################################################
    def test_CTBA161_002(self):

        chave = "T020000000001001"
        self.oHelper.SearchBrowse(f"D MG 01 {chave}", key=1, index=True)
        self.oHelper.SetButton("Outras Ações", "Alterar Cadastro")
        self.oHelper.SetValue("CVE_DESCRI", "TIR ALT3")
        self.oHelper.SetValue("CVE_OBS", "TIR OBSER")

        self.oHelper.CheckResult("CVE_DESCRI", "TIR ALT3")
        self.oHelper.CheckResult("CVE_OBS", "TIR OBSER")
        self.oHelper.SetButton("Salvar")

        self.oHelper.AssertTrue()
    
#####################################################
# Alterar visão de analitica para sintetica - modo tradicional
#####################################################
    def test_CTBA161_003(self):

        chave = "T050000000001001"
        self.oHelper.SearchBrowse(f"D MG 01 {chave}", key=1, index=True)
        self.oHelper.SetButton("Alterar")

        self.oHelper.SetValue("CTS_DESCCG", "ALTERADO")
        self.oHelper.SetValue("CTS_CLASSE", "1 - Sintetica")
        self.oHelper.SetValue("CTS_VISENT", "1 - Sim")
        self.oHelper.SetValue("CTS_FATSLD", "1 - Mantem")
        self.oHelper.SetValue("CTS_TOTVIS", "1 - Sim")

        self.oHelper.ClickCheckBox("Total Geral")

        self.oHelper.SetButton("Confirmar")

        self.oHelper.SearchBrowse(f"D MG 01 {chave}", key=1, index=True)

        ###
        # visualizando dados
        ###
        self.oHelper.SetButton("Visualizar")
        self.oHelper.CheckResult("CTS_DESCCG", "ALTERADO")
        self.oHelper.CheckResult("CTS_CLASSE", "1 - Sintetica")
        self.oHelper.CheckResult("CTS_VISENT", "1 - Sim")
        self.oHelper.CheckResult("CTS_FATSLD", "1 - Mantem")
        self.oHelper.CheckResult("CTS_TOTVIS", "1 - Sim")

        self.oHelper.SetButton("Confirmar")

        self.oHelper.AssertTrue()

#####################################################
##       Exclusão de visão Gerencial - MODO TRADICIONAL
#####################################################
    def test_CTBA161_004(self):

        chave = "T030000000001001"
        self.oHelper.SearchBrowse(f"D MG 01 {chave}", key=1, index=True)
        self.oHelper.SetButton("Outras Ações", "Excluir")
        self.oHelper.SetButton("Confirmar")

        self.oHelper.SearchBrowse(f"D MG 01 {chave}", key=1, index=True)
        self.oHelper.SetButton("Visualizar")
        self.oHelper.CheckResult("CTS_DESCCG", "TIR EXCLUSAO")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.AssertFalse()

#####################################################
##       Exportar estrutura, visão gerencial
#####################################################
    def test_CTBA161_005(self):

        chave = "T000000000001001"
        self.oHelper.SearchBrowse(f"D MG 01 {chave}", key=1, index=True)

        self.oHelper.SetButton("Outras Ações","Exp. Estrutura")
        self.oHelper.SetValue("Estrutura de visao ?","\\baseline\\visaotir.cve")
        self.oHelper.SetButton("Ok")
        self.oHelper.WaitShow("Exportacao gerada com sucesso")
        self.oHelper.SetButton("Ok")
        self.oHelper.AssertTrue()

#####################################################
##       importar estrutura, visão gerencial
#####################################################
    def test_CTBA161_006(self):

        #self.oHelper.WaitShow("Cadastro Visao Gerencial")
        #self.oHelper.SetKey("F12")
        #self.oHelper.SetValue("Modo de Exibicao ?", "Arvore")
        #self.oHelper.SetButton("OK")
        
        self.oHelper.SetButton("Outras Ações","Imp. Estrutura")
        self.oHelper.SetBranch("D MG 01 ")
        self.oHelper.SetValue("Estrutura de visao ?","\\baseline\\tirImport.cve")
        self.oHelper.SetButton("Ok")

        self.oHelper.SetValue("CVE_CODIGO","T07")
        self.oHelper.SetValue("CVE_DESCRI","TIR IMPORTADO")
        self.oHelper.SetValue("CVE_OBS","TIR")
        self.oHelper.SetButton("Salvar")

        self.oHelper.WaitShow("Importacao finalizada com sucesso")
        self.oHelper.SetButton("Fechar")
        ##aguardar automação - implementação possivelmente futura de clicar com direito em arvores ANALITICAS
        #self.oHelper.SetButton("Visualizar")

        #self.oHelper.ClickTree("TIR IMPORTADO")
        #self.oHelper.ClickTree("00000000000000000005-TIR ARVORE")
        #self.oHelper.ClickLabel("00000000000000000006 - TIR ANALITICO                           TIR")
        #self.oHelper.ClickIcon("Close")

        self.oHelper.AssertTrue()

#########################################
# Inclusão de Visão - Analitica - MODO ARVORE
#########################################
    def test_CTBA161_007(self):
        # Variaveis para verificar codigo gerado automaticamente

        self.oHelper.WaitShow("Cadastro Visao Gerencial")
        self.oHelper.SetKey("F12")
        self.oHelper.SetValue("Modo de Exibicao ?", "Arvore")
        self.oHelper.SetButton("OK")

        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("D MG 01 ")

        self.oHelper.WaitShow("Cadastro Visao Gerencial - INCLUIR")
        self.oHelper.SetValue("CVE_CODIGO","T04")
        self.oHelper.SetFocus("CVE_DESCRI")
        self.oHelper.SetValue("CVE_DESCRI","TIR INC ARVORE")
        self.oHelper.SetFocus("CVE_OBS")
        self.oHelper.SetValue("CVE_OBS","TIR OBS")

        self.oHelper.SetButton("Salvar")
        ##Node da visão Gerencial
        self.oHelper.ClickTree("TIR INC ARVORE",right_click=True)
        self.oHelper.CheckView("Incluir",element_type="str")
        self.oHelper.ClickMenuPopUpItem("Incluir")

        self.oHelper.WaitShow("Conta Gerencial - Inclusao")
        cEntidGerAut=self.oHelper.GetValue("CVF_CONTAG")
        cORDEMAut=self.oHelper.GetValue("CVF_ORDEM")
        self.oHelper.CheckResult("CVF_CONTAG",cEntidGerAut)
        self.oHelper.CheckResult("CVF_ORDEM",cORDEMAut)

        self.oHelper.SetValue("CVF_CLASSE","1 - Sintetica")
        self.oHelper.SetValue("CVF_DESCCG","TIR ARVORE")
        self.oHelper.SetValue("CVF_NORMAL","2 - Credito")
        self.oHelper.SetValue("CVF_COLUNA","0 - Nenhuma")
        self.oHelper.ClickCheckBox("Total Geral")
        self.oHelper.SetValue("CVF_TOTVIS", "1 - Sim")
        self.oHelper.SetValue("CVF_VISENT", "1 - Sim")
        self.oHelper.SetValue("CVF_FATSLD", "1 - Matem")
        #self.oHelper.SetValue("CVF_DETHCG","")
        self.oHelper.SetValue("CVF_TPVALO", "D - Padrao D/C")
        ##self.oHelper.SetValue("CVF_PICTUR", "")

        self.oHelper.SetButton("Confirmar")
        ##Node da entidade gerencial, criando analitica
        self.oHelper.ClickTree(cEntidGerAut+"-TIR ARVORE",right_click=True)
        #self.oHelper.CheckView("Incluir",element_type="str")
        self.oHelper.ClickMenuPopUpItem("Incluir")

        self.oHelper.WaitShow("Conta Gerencial - Inclusao")
        cEntidGerAut2   =  self.oHelper.GetValue("CVF_CONTAG")
        cORDEMAut2  =   self.oHelper.GetValue("CVF_ORDEM")
        self.oHelper.CheckResult("CVF_CONTAG",cEntidGerAut2)
        self.oHelper.CheckResult("CVF_ORDEM",cORDEMAut2)

        self.oHelper.SetValue("CVF_CLASSE","2 - Analitica")
        self.oHelper.CheckResult("CVF_CTASUP",cEntidGerAut)
        self.oHelper.SetValue("CVF_DESCCG","TIR ANALITICO")
        self.oHelper.SetValue("CVF_NORMAL","1 - Debito")
        self.oHelper.SetValue("CVF_TOTVIS", "2 - Nao")
        self.oHelper.SetValue("CVF_VISENT", "1 - Sim")
        self.oHelper.SetValue("CVF_FATSLD", "1 - Matem")
        self.oHelper.SetValue("CVF_DETHCG","TIR")
        self.oHelper.SetValue("CVF_TPVALO", "D - Padrao D/C")

        self.oHelper.SetButton("Confirmar")
            ####ABRIR TASK PARA AUTOMAÇÃO/AGUARDAR RESOLUÇAO
            #self.oHelper.ClickIcon("Alterar")
            #self.oHelper.SetValue("CTS_CT1INI","000000002           ",grid=True,row=1)
            #self.oHelper.SetValue("CTS_CT1FIM","000000002           ",grid=True,row=1)
            #self.oHelper.SetValue("CTS_IDENTI","1 - Soma",grid=True,row=1)
            #self.oHelper.SetButton("Confirmar")
            #self.oHelper.SetButton("X")
            #self.oHelper.SetButton("Cancelar")
        self.oHelper.AssertTrue()

#####################################################
##       Modificações estrutura - MODO Arvore, completa com estrutura
#####################################################
    def test_CTBA161_008(self):

        self.oHelper.WaitShow("Cadastro Visao Gerencial")
        self.oHelper.SetKey("F12")
        self.oHelper.SetValue("Modo de Exibicao ?", "Arvore")
        self.oHelper.SetButton("OK")
        
        chave = "T06"
        self.oHelper.SearchBrowse(f"D MG 01 {chave}", key=1, index=True)
        self.oHelper.SetButton("Alterar")
        
        ##Alterando estrutura sintetica
        #como era
        # self.oHelper.ClickTree("00000000000000000010-TIR ARVORE")
        # self.oHelper.CheckView("")
        # self.oHelper.ClickTree("00000000000000000011-TIR SINT",right_click=True)
        ##
        #alteração sugerida pela task ca-2467
        self.oHelper.ClickTree(" 00000000000000000010-TIR ARVORE> 00000000000000000011-TIR SINT",right_click=True)
        self.oHelper.CheckView("Alterar",element_type="str")
        self.oHelper.ClickMenuPopUpItem("Alterar")
        self.oHelper.WaitShow("Conta Gerencial - Alteracao")
        self.oHelper.SetValue("CVF_DESCCG","TIR SINT ALTERADO")
        self.oHelper.SetButton("Confirmar")
        
        #exclusão de uma entidade sintetica com duas analiticas uma com conta atreladas
        self.oHelper.WaitShow("Conta Gerencial")
        self.oHelper.ClickTree("00000000000000000010-TIR ARVORE")
        self.oHelper.ClickTree("00000000000000000011-TIR SINT ALTERADO",right_click=True)
        self.oHelper.CheckView("Excluir",element_type="str")
        self.oHelper.ClickMenuPopUpItem("Excluir")
        self.oHelper.CheckHelp("Confirma exclusao da conta gerencial","Ok")

        #exclusão estrutura restante sintetica
        self.oHelper.ClickTree("00000000000000000010-TIR ARVORE",right_click=True)
        self.oHelper.CheckView("Excluir",element_type="str")
        self.oHelper.ClickMenuPopUpItem("Excluir")
        self.oHelper.CheckHelp("Confirma exclusao da conta gerencial (serao excluidas todas as contas dependentes).","Ok")
        
        #self.oHelper.TearDown()
        self.oHelper.AssertTrue()


#testes exploratório fechando pelo botão "close", para testes não executar por enquanto
    ##def test_CTBA161_009(self):

       ##self.oHelper.WaitShow("Cadastro Visao Gerencial")
       ##self.oHelper.SetKey("F12")
	   ##self.oHelper.SetValue("Modo de Exibicao ?", "Arvore")
       ##self.oHelper.SetButton("OK")

        #chave = "1660000000001001"

        #chave = "T04"
        #self.oHelper.SearchBrowse(f"D MG 01 {chave}", key=1, index=True)
        #self.oHelper.SetButton("Visualizar")
        #self.oHelper.WaitShow("Visao Gerencial")
        #self.oHelper.SetButton("x")  #Tentativa com Close x,X 
        #self.oHelper.ClickIcon("x")  #Tentativa com x, X, Close
        #self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
