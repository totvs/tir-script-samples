from tir import Webapp
import unittest


class PCOC360(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()

        inst.oHelper.Setup("SIGAPCO", "01/01/2019", "T1", "M SP 01", "57")

        inst.oHelper.Program("PCOC360")

    def test_PCOC360_001(self):
        # Caso de teste PCOC360 com movimento do periodo e PROCNIV falso
        self.oHelper.AddParameter("MV_PCOCNIV", "", "F")
        self.oHelper.SetParameters()

        COD = "VS"
        self.oHelper.SearchBrowse(
            f"M SP 01 {COD}", "Filial+codigo")

        self.oHelper.SetButton("Consultar")
        self.oHelper.SetValue("MV_PAR01", "01012019")  # Periodo de ?
        self.oHelper.SetValue("MV_PAR02", "31122019")  # Periodo Ate ?
        # Tipo Periodo ? Semanal/Quinzenal/Mensal/Bimestral/Semestral/Anual/Diario
        self.oHelper.SetValue("MV_PAR03", "3 - Mensal")
        # Moeda ? Moeda 1/Moeda 2/Moeda 3//Moeda 4//Moeda 5/
        self.oHelper.SetValue("MV_PAR04", "1 - Moeda 1")
        # Tipo do Grafico ? /Linha/Area/Pontos/Barra/Piramide/Cilindro/Barra Horizontal/Piramide Horizontal/Cilindro Horizontal/Pizza/Forma/Linha Rapida/Flechas/Gantt/Bolha
        self.oHelper.SetValue("MV_PAR05", "4 - Barra")
        self.oHelper.SetValue("MV_PAR06", "1")  # Qtd. Series ?
        # Detalhar cubos ? Sim/Nao
        self.oHelper.SetValue("MV_PAR07", "2 - Nao")
        # Mostrar valores ? Unidade/Milhar/Milhão
        self.oHelper.ClickLabel("Unidade")
        self.oHelper.SetValue("MV_PAR09", "@E 999,999,999,999.99")  # Picture ?
        self.oHelper.SetButton("Ok")

        self.oHelper.SetValue("MV_PAR01", "OR")  # Config.Cubo Serie 1 ?
        self.oHelper.ClickLabel("Sim")  # Exibe Configurações ?  Sim/Nao
        self.oHelper.SetValue("MV_PAR03", "ORCADO")  # Descrição Série ?
        # Considerar  ? Saldo final do periodo/Movimento do periodo
        self.oHelper.ClickLabel("Movimento do periodo")
        self.oHelper.SetButton("Ok")

        self.oHelper.SetValue("MV_PAR01", "")  # CO de ?
        self.oHelper.SetValue("MV_PAR02", "zzzzzzzzz")  # CO ate ?
        self.oHelper.SetValue("MV_PAR04", "")  # Centro de Custo de ?
        self.oHelper.SetValue("MV_PAR05", "zzzzzzzzz")  # Centro de Custo de ?
        self.oHelper.SetValue("MV_PAR07", "")  # TP.SALDO de ?
        self.oHelper.SetValue("MV_PAR08", "zz")  # TP.SALDO ate ?
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Confirmar")

        self.oHelper.RestoreParameters()
        self.oHelper.AssertTrue()

    def test_PCOC360_002(self):
        # Caso de teste PCOC360 com movimentos por saldo final no periodo e  PROCNIV falso
        self.oHelper.AddParameter("MV_PCOCNIV", "", "F")
        self.oHelper.SetParameters()

        COD = "VS"
        self.oHelper.SearchBrowse(
            f"M SP 01 {COD}", "Filial+codigo")

        self.oHelper.SetButton("Consultar")
        self.oHelper.SetValue("MV_PAR01", "01012019")  # Periodo de ?
        self.oHelper.SetValue("MV_PAR02", "31122019")  # Periodo Ate ?
        # Tipo Periodo ? Semanal/Quinzenal/Mensal/Bimestral/Semestral/Anual/Diario
        self.oHelper.SetValue("MV_PAR03", "3 - Mensal")
        # Moeda ? Moeda 1/Moeda 2/Moeda 3//Moeda 4//Moeda 5/
        self.oHelper.SetValue("MV_PAR04", "1 - Moeda 1")
        # Tipo do Grafico ? /Linha/Area/Pontos/Barra/Piramide/Cilindro/Barra Horizontal/Piramide Horizontal/Cilindro Horizontal/Pizza/Forma/Linha Rapida/Flechas/Gantt/Bolha
        self.oHelper.SetValue("MV_PAR05", "4 - Barra")
        self.oHelper.SetValue("MV_PAR06", "1")  # Qtd. Series ?
        # Detalhar cubos ? Sim/Nao
        self.oHelper.SetValue("MV_PAR07", "2 - Nao")
        # Mostrar valores ? Unidade/Milhar/Milhão
        self.oHelper.ClickLabel("Unidade")
        self.oHelper.SetValue("MV_PAR09", "@E 999,999,999,999.99")  # Picture ?
        self.oHelper.SetButton("Ok")

        self.oHelper.SetValue("MV_PAR01", "OR")  # Config.Cubo Serie 1 ?
        self.oHelper.ClickLabel("Sim")  # Exibe Configurações ?  Sim/Nao
        self.oHelper.SetValue("MV_PAR03", "ORCADO")  # Descrição Série ?
        # Considerar  ? Saldo final do periodo/Movimento do periodo
        self.oHelper.ClickLabel("Saldo final do periodo")
        self.oHelper.SetButton("Ok")

        self.oHelper.SetValue("MV_PAR01", "")  # CO de ?
        self.oHelper.SetValue("MV_PAR02", "zzzzzzzzz")  # CO ate ?
        self.oHelper.SetValue("MV_PAR04", "")  # Centro de Custo de ?
        self.oHelper.SetValue("MV_PAR05", "zzzzzzzzz")  # Centro de Custo de ?
        self.oHelper.SetValue("MV_PAR07", "")  # TP.SALDO de ?
        self.oHelper.SetValue("MV_PAR08", "zz")  # TP.SALDO ate ?
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Confirmar")

        self.oHelper.RestoreParameters()
        self.oHelper.AssertTrue()

    # PCOC361
    def test_PCOC360_003(self):
        # Caso de teste PCOC361 com movimento do periodo e PROCNIV TRUE
        self.oHelper.AddParameter("MV_PCOCNIV", "", "T")
        self.oHelper.SetParameters()

        COD = "VS"
        self.oHelper.SearchBrowse(
            f"M SP 01 {COD}", "Filial+codigo")

        self.oHelper.SetButton("Consultar")
        self.oHelper.SetValue("MV_PAR01", "01012019")  # Periodo de ?
        self.oHelper.SetValue("MV_PAR02", "31122019")  # Periodo Ate ?
        # Tipo Periodo ? Semanal/Quinzenal/Mensal/Bimestral/Semestral/Anual/Diario
        self.oHelper.SetValue("MV_PAR03", "3 - Mensal")
        # Moeda ? Moeda 1/Moeda 2/Moeda 3//Moeda 4//Moeda 5/
        self.oHelper.SetValue("MV_PAR04", "1 - Moeda 1")
        # Tipo do Grafico ? /Linha/Area/Pontos/Barra/Piramide/Cilindro/Barra Horizontal/Piramide Horizontal/Cilindro Horizontal/Pizza/Forma/Linha Rapida/Flechas/Gantt/Bolha
        self.oHelper.SetValue("MV_PAR05", "4 - Barra")
        self.oHelper.SetValue("MV_PAR06", "1")  # Qtd. Series ?
        # Detalhar cubos ? Sim/Nao
        self.oHelper.SetValue("MV_PAR07", "2 - Nao")
        # Mostrar valores ? Unidade/Milhar/Milhão
        self.oHelper.ClickLabel("Unidade")
        self.oHelper.SetValue("MV_PAR09", "@E 999,999,999,999.99")  # Picture ?
        self.oHelper.SetButton("Ok")

        self.oHelper.SetValue("MV_PAR01", "OR")  # Config.Cubo Serie 1 ?
        self.oHelper.ClickLabel("Sim")  # Exibe Configurações ?  Sim/Nao
        self.oHelper.SetValue("MV_PAR03", "ORCADO")  # Descrição Série ?
        # Considerar  ? Saldo final do periodo/Movimento do periodo
        self.oHelper.ClickLabel("Movimento do periodo")
        self.oHelper.SetButton("Ok")

        self.oHelper.SetValue("MV_PAR01", "")  # CO de ?
        self.oHelper.SetValue("MV_PAR02", "zzzzzzzzz")  # CO ate ?
        self.oHelper.SetValue("MV_PAR04", "")  # Centro de Custo de ?
        self.oHelper.SetValue("MV_PAR05", "zzzzzzzzz")  # Centro de Custo de ?
        self.oHelper.SetValue("MV_PAR07", "")  # TP.SALDO de ?
        self.oHelper.SetValue("MV_PAR08", "zz")  # TP.SALDO ate ?
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Confirmar")

        self.oHelper.RestoreParameters()
        self.oHelper.AssertTrue()

    def test_PCOC360_004(self):
        # Caso de teste PCOC361 com movimentos por saldo final no periodo e  PROCNIV TRUE
        self.oHelper.AddParameter("MV_PCOCNIV", "", "T")
        self.oHelper.SetParameters()

        COD = "VS"
        self.oHelper.SearchBrowse(
            f"M SP 01 {COD}", "Filial+codigo")

        self.oHelper.SetButton("Consultar")
        self.oHelper.SetValue("MV_PAR01", "01012019")  # Periodo de ?
        self.oHelper.SetValue("MV_PAR02", "31122019")  # Periodo Ate ?
        # Tipo Periodo ? Semanal/Quinzenal/Mensal/Bimestral/Semestral/Anual/Diario
        self.oHelper.SetValue("MV_PAR03", "3 - Mensal")
        # Moeda ? Moeda 1/Moeda 2/Moeda 3//Moeda 4//Moeda 5/
        self.oHelper.SetValue("MV_PAR04", "1 - Moeda 1")
        # Tipo do Grafico ? /Linha/Area/Pontos/Barra/Piramide/Cilindro/Barra Horizontal/Piramide Horizontal/Cilindro Horizontal/Pizza/Forma/Linha Rapida/Flechas/Gantt/Bolha
        self.oHelper.SetValue("MV_PAR05", "4 - Barra")
        self.oHelper.SetValue("MV_PAR06", "1")  # Qtd. Series ?
        # Detalhar cubos ? Sim/Nao
        self.oHelper.SetValue("MV_PAR07", "2 - Nao")
        # Mostrar valores ? Unidade/Milhar/Milhão
        self.oHelper.ClickLabel("Unidade")
        self.oHelper.SetValue("MV_PAR09", "@E 999,999,999,999.99")  # Picture ?
        self.oHelper.SetButton("Ok")

        self.oHelper.SetValue("MV_PAR01", "OR")  # Config.Cubo Serie 1 ?
        self.oHelper.ClickLabel("Sim")  # Exibe Configurações ?  Sim/Nao
        self.oHelper.SetValue("MV_PAR03", "ORCADO")  # Descrição Série ?
        # Considerar  ? Saldo final do periodo/Movimento do periodo
        self.oHelper.ClickLabel("Saldo final do periodo")
        self.oHelper.SetButton("Ok")

        self.oHelper.SetValue("MV_PAR01", "")  # CO de ?
        self.oHelper.SetValue("MV_PAR02", "zzzzzzzzz")  # CO ate ?
        self.oHelper.SetValue("MV_PAR04", "")  # Centro de Custo de ?
        self.oHelper.SetValue("MV_PAR05", "zzzzzzzzz")  # Centro de Custo de ?
        self.oHelper.SetValue("MV_PAR07", "")  # TP.SALDO de ?
        self.oHelper.SetValue("MV_PAR08", "zz")  # TP.SALDO ate ?
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Confirmar")

        self.oHelper.RestoreParameters()
        self.oHelper.AssertTrue()

    def test_PCOC360_005(self):
        # Caso de teste PCOC361 com movimentos por saldo final no periodo e  PROCNIV FALSE
        #self.oHelper.AddParameter("MV_PCOCNIV", "", "F")
        # self.oHelper.SetParameters()
        COD = "VS"

        self.oHelper.SearchBrowse(f"M SP 01 {COD}", "Filial+codigo")

        self.oHelper.SetButton("Consultar")
        self.oHelper.SetValue("MV_PAR01", "01012019")  # Periodo de ?
        self.oHelper.SetValue("MV_PAR02", "31122019")  # Periodo Ate ?
        # Tipo Periodo ? Semanal/Quinzenal/Mensal/Bimestral/Semestral/Anual/Diario
        self.oHelper.SetValue("MV_PAR03", "3 - Mensal")
        # Moeda ? Moeda 1/Moeda 2/Moeda 3//Moeda 4//Moeda 5/
        #self.oHelper.SetValue("MV_PAR04", "1 - Moeda 1")
        # Tipo do Grafico ? /Linha/Area/Pontos/Barra/Piramide/Cilindro/Barra Horizontal/Piramide Horizontal/Cilindro Horizontal/Pizza/Forma/Linha Rapida/Flechas/Gantt/Bolha
        self.oHelper.SetValue("MV_PAR05", "4 - Barra")
        self.oHelper.SetValue("MV_PAR06", "1")  # Qtd. Series ?
        # Detalhar cubos ? Sim/Nao
        self.oHelper.SetValue("MV_PAR07", "1 - Sim")
        # Mostrar valores ? Unidade/Milhar/Milhão
        self.oHelper.ClickLabel("Unidade")
        self.oHelper.SetValue("MV_PAR09", "@E 999,999,999,999.99")  # Picture ?
        self.oHelper.SetButton("Ok")
        self.oHelper.SetValue("MV_PAR01", "OR")  # Config.Cubo Serie 1 ?
        self.oHelper.ClickLabel("Sim")  # Exibe Configurações ?  Sim/Nao
        self.oHelper.SetValue("MV_PAR03", "ORCADO")  # Descrição Série ?
        # Considerar  ? Saldo final do periodo/Movimento do periodo
        self.oHelper.ClickLabel("Saldo final do periodo")
        self.oHelper.SetButton("Ok")

        self.oHelper.SetValue("MV_PAR01", "")  # CO de ?
        self.oHelper.SetValue("MV_PAR02", "zzzzzzzzz")  # CO ate ?
        self.oHelper.SetValue("MV_PAR04", "")  # Centro de Custo de ?
        self.oHelper.SetValue("MV_PAR05", "zzzzzzzzz")  # Centro de Custo de ?
        self.oHelper.SetValue("MV_PAR07", "")  # TP.SALDO de ?
        self.oHelper.SetValue("MV_PAR08", "zz")  # TP.SALDO ate ?
        self.oHelper.SetButton("Ok")

        #self.oHelper.WaitShow("Aguarde Processando...")
        #self.oHelper.ClickGridCell("01/01/2019 - 31/01/2019[ORCADO]", row=2)

        #self.oHelper.SetKey("Down", grid=True)
        self.oHelper.ClickGridCell("Descricao", row=2)
        self.oHelper.SetButton("Outras Ações", "Drilldown")

        # self.oHelper.ClickGridCell("Descricao")
        ##self.oHelper.SetButton("Outras Ações", "Drilldown", position = 2)

        # self.oHelper.ClickGridCell("Descricao")
        ##self.oHelper.SetButton("Outras Ações", "Drilldown", position = 2)

        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Confirmar")
        # self.oHelper.SetButton("Confirmar")
        # self.oHelper.SetButton("Confirmar")
        # self.oHelper.SetButton("Confirmar")

        self.oHelper.SetButton("Sim")
        # self.oHelper.RestoreParameters()
        self.oHelper.AssertTrue()

    def test_PCOC360_006(self):
        # Caso de teste PCOC361 com movimentos por saldo final no periodo e  PROCNIV TRUE
        self.oHelper.AddParameter("MV_PCOCNIV", "", "T","T","T")
        self.oHelper.SetParameters()
        COD = "VS"

        self.oHelper.SearchBrowse(f"M SP 01 {COD}", "Filial+codigo")

        self.oHelper.SetButton("Consultar")
        self.oHelper.SetValue("MV_PAR01", "01012019")  # Periodo de ?
        self.oHelper.SetValue("MV_PAR02", "31122019")  # Periodo Ate ?
        # Tipo Periodo ? Semanal/Quinzenal/Mensal/Bimestral/Semestral/Anual/Diario
        self.oHelper.SetValue("MV_PAR03", "3 - Mensal")
        # Moeda ? Moeda 1/Moeda 2/Moeda 3//Moeda 4//Moeda 5/
        #self.oHelper.SetValue("MV_PAR04", "1 - Moeda 1")
        # Tipo do Grafico ? /Linha/Area/Pontos/Barra/Piramide/Cilindro/Barra Horizontal/Piramide Horizontal/Cilindro Horizontal/Pizza/Forma/Linha Rapida/Flechas/Gantt/Bolha
        self.oHelper.SetValue("MV_PAR05", "4 - Barra")
        self.oHelper.SetValue("MV_PAR06", "1")  # Qtd. Series ?
        # Detalhar cubos ? Sim/Nao
        self.oHelper.SetValue("MV_PAR07", "1 - Sim")
        # Mostrar valores ? Unidade/Milhar/Milhão
        self.oHelper.ClickLabel("Unidade")
        self.oHelper.SetValue("MV_PAR09", "@E 999,999,999,999.99")  # Picture ?
        self.oHelper.SetButton("Ok")
        self.oHelper.SetValue("MV_PAR01", "OR")  # Config.Cubo Serie 1 ?
        self.oHelper.ClickLabel("Sim")  # Exibe Configurações ?  Sim/Nao
        self.oHelper.SetValue("MV_PAR03", "ORCADO")  # Descrição Série ?
        # Considerar  ? Saldo final do periodo/Movimento do periodo
        self.oHelper.ClickLabel("Saldo final do periodo")
        self.oHelper.SetButton("Ok")

        self.oHelper.SetValue("MV_PAR01", "")  # CO de ?
        self.oHelper.SetValue("MV_PAR02", "zzzzzzzzz")  # CO ate ?
        self.oHelper.SetValue("MV_PAR04", "")  # Centro de Custo de ?
        self.oHelper.SetValue("MV_PAR05", "zzzzzzzzz")  # Centro de Custo de ?
        self.oHelper.SetValue("MV_PAR07", "")  # TP.SALDO de ?
        self.oHelper.SetValue("MV_PAR08", "zz")  # TP.SALDO ate ?
        self.oHelper.SetButton("Ok")

        #self.oHelper.WaitShow("Aguarde Processando...")
        #self.oHelper.ClickGridCell("01/01/2019 - 31/01/2019[ORCADO]", row=2)

        #self.oHelper.SetKey("Down", grid=True)
        self.oHelper.ClickGridCell("Descricao", row=2)
        self.oHelper.SetButton("Outras Ações", "Drilldown")

        # self.oHelper.ClickGridCell("Descricao")
        ##self.oHelper.SetButton("Outras Ações", "Drilldown", position = 2)

        # self.oHelper.ClickGridCell("Descricao")
        ##self.oHelper.SetButton("Outras Ações", "Drilldown", position = 2)

        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Confirmar")
        # self.oHelper.SetButton("Confirmar")
        # self.oHelper.SetButton("Confirmar")
        # self.oHelper.SetButton("Confirmar")

        self.oHelper.SetButton("Sim")
        self.oHelper.RestoreParameters()
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
