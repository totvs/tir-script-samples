from tir import Webapp
import unittest


class PCOA201(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()

        inst.oHelper.Setup("SIGAPCO", "01/01/2019", "T1", "M SP 01", "57")

        inst.oHelper.Program("PCOA201")

    def test_PCOA201_001(self):
        # Inclusão
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("M SP 01")
        self.oHelper.SetValue("AKR_ORCAME", "PCO0000010002")
        self.oHelper.SetValue("AKR_VERBAS", "0001")
        self.oHelper.SetValue("AKR_REVISA", "0002")
        self.oHelper.SetValue("AKR_DESCRI", "SIMULACAO INCLUSAO CONTROL")
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.AssertTrue()

    def test_PCOA201_002(self):
            # Simulação
        COD = "PCO0000010002  0005"
        self.oHelper.SearchBrowse(
            f"M SP 01 {COD}", "Filial+planilha Orc + Versao Sim")

        self.oHelper.SetButton("Outras Ações", "Simular")
        self.oHelper.ClickLabel("PCO000001000-SQUAD CONTROL PCOA201")
        self.oHelper.ClickLabel("057-SQUAD CONTROL SINT C.O")
        self.oHelper.ClickLabel("057000000002-SQUAD CONTROL C.O ANALITICA")

        self.oHelper.SetButton("Gerar Gráfico")

        # self.oHelper.SetButton("Nao")
        self.oHelper.SetButton("Salvar", position=2)

        self.oHelper.AssertTrue()

    def test_PCOA201_003(self):
            # Simular com 2 graficos
        COD = "PCO0000010002  0005"
        self.oHelper.SearchBrowse(
            f"M SP 01 {COD}", "Filial+planilha Orc + Versao Sim")

        self.oHelper.SetButton("Outras Ações", "Simular")
        self.oHelper.ClickTree("PCO000001000-SQUAD CONTROL PCOA201")
        self.oHelper.ClickTree("057-SQUAD CONTROL SINT C.O")
        self.oHelper.ClickLabel("057000000002-SQUAD CONTROL C.O ANALITICA")

        self.oHelper.SetButton("Gerar Gráfico")

        self.oHelper.SetButton("Outras Ações", "Pl.Compar.")

        self.oHelper.SetValue("MV_PAR01", "PCO000001")
        self.oHelper.SetValue("MV_PAR02", "0001")
        self.oHelper.SetButton("Ok")

        # aqui ele ao abrir a outra planilha e clicar para gerar os dois graficos COMPARATIVOS com valor comparando com um sem nada
        self.oHelper.ClickTree("057000000002-SQUAD CONTROL C.O ANALITICA")
        self.oHelper.ClickTree("057-SQUAD CONTROL SINT C.O")
        self.oHelper.ClickLabel("057-SQUAD CONTROL SINT C.O")
        self.oHelper.ClickTree("057-SQUAD CONTROL SINT C.O")
        
        self.oHelper.ClickTree("057000000002-SQUAD CONTROL C.O ANALITICA")
        self.oHelper.ClickLabel("057000000002-SQUAD CONTROL C.O ANALITICA")

        self.oHelper.SetButton("Gerar Gráfico")
        # self.oHelper.SetButton("Nao")
        self.oHelper.SetButton("Salvar", position=2)

        self.oHelper.AssertTrue()

    def test_PCOA201_004(self):
        # Efetivar
        COD = "PCO0000010002  0004"
        self.oHelper.SearchBrowse(
            f"M SP 01 {COD}", "Filial+planilha Orc + Versao Sim")

        self.oHelper.SetButton("Outras Ações", "Efetivar")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Ok")
        self.oHelper.AssertTrue()

    def test_PCOA201_005(self):
        # EXCLUSAO

        COD = "PCO0000010002  0004"

        self.oHelper.SearchBrowse(
            f"M SP 01 {COD}", "Filial+planilha Orc + Versao Sim")

        self.oHelper.SetButton("Outras Ações", "Excluir")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.AssertTrue()

    def test_PCOA201_006(self):
        # Testes botoes diversos
        COD = "PCO0000010002  0005"
        self.oHelper.SearchBrowse(
            f"M SP 01 {COD}", "Filial+planilha Orc + Versao Sim")

        self.oHelper.SetButton("Outras Ações", "Simular")

        self.oHelper.ClickLabel("PCO000001000-SQUAD CONTROL PCOA201")
        self.oHelper.ClickLabel("057-SQUAD CONTROL SINT C.O")
        self.oHelper.ClickLabel("057000000002-SQUAD CONTROL C.O ANALITICA")

        self.oHelper.SetButton("Outras Ações", "Legenda")
        self.oHelper.SetButton("Fechar")

        self.oHelper.SetValue("Data Inicial", "311218")
        self.oHelper.SetButton("Ok")
        self.oHelper.SetValue("Data Inicial", "010115")

        # self.oHelper.SetButton("Aplic.Form")
        # self.oHelper.SetButton("Fechar")
        # self.oHelper.SetButton("Executar")
        # self.oHelper.SetButton("Salvar")

        self.oHelper.SetButton("Salvar", position=2)
        self.oHelper.AssertTrue()

    def test_PCOA201_007(self):
        # Testes botoes diversos
        COD = "SIM000000000   "
        self.oHelper.WaitShow("Nova Simulação")
        self.oHelper.SearchBrowse(
            f"M SP 01 {COD}", "Filial+planilha Orc + Versao Sim")

        self.oHelper.SetButton("Outras Ações", "Simular")

        self.oHelper.ClickTree("SIM000000000-Planilha para simulacao")
        self.oHelper.ClickTree("CA0000000012-CONTA ANALITICA SIMULACAO")
        self.oHelper.ClickLabel("CA0000000012-CONTA ANALITICA SIMULACAO")

        self.oHelper.SetButton("Aplic.Form")
        self.oHelper.SetValue("cInterv", "O1:O2", name_attr=True)
        #self.oHelper.SetValue("Expressão - Fórmula","=PLAN1!O2+999")
        self.oHelper.SetButton("Executar")
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Fechar")

        ###AGUARDO DA AUTOMAÇÃO SOBRE PROBLEMA COM LOADGRID APÓS SETVALUE COM TRIGGER DE HELP ANTES DA CONFIRMAÇÃO
        # Colocando na grid para verificação, TENTAR GRID CELL COM SETKEY ENTER 
        #self.oHelper.SetValue("O", grid=True, row=2)
        #self.oHelper.SetValue("O", "=125>af", grid=True, row=2)
        # self.oHelper.SetButton("Fechar") #TENTAR FECHAR SOMENTE O BOTÃO

        #self.oHelper.LoadGrid()  # COM LOADGRID ELE CLICA NO CAMPO COM METODO ACIMA
        # Não checa após loadgrid  preso ?
        #self.oHelper.CheckHelp("A fórmula digitada contém erro(s)", "Fechar")
        ##self.oHelper.CheckView("A fórmula digitada contém erro(s)")
        #self.oHelper.LoadGrid()
        ##self.oHelper.SetButton("Fechar", position=2)
        #self.oHelper.SetValue("O", "", grid=True, row=2)


        self.oHelper.SetValue("O", "200000", grid=True, row=2)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Outras Ações", "Pl.Compar.")
        self.oHelper.SetValue("Orçamento ?", "SIM000000000")
        self.oHelper.SetValue("Versão ?", "0001")
        self.oHelper.SetButton("Ok")

        self.oHelper.SetButton("Salvar", position=2)

        self.oHelper.SetButton("Sim")

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
