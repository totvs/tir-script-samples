from tir import Webapp
import unittest
import time


class TJurPesqAsj(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAJURI', '15/10/2018', 'T1', 'D MG 01 ', '05')
        inst.oHelper.AddParameter("MV_JFTJURI", "", "2", "", "")
        inst.oHelper.AddParameter("MV_JFLXCOR", "", "2", "", "")
        inst.oHelper.Program('JURA162')
        inst.oHelper.SetParameters()

    def test_TJurPesqAsj_CT001(self):

        print('INICIO - CT001 - Alteração em lote')
        self.oHelper.SetValue("cValor", "Contratos", name_attr=True)
        self.oHelper.SetValue("NSZ_CAREAJ", "JUR01")
        self.oHelper.ClickLabel("Pesquisar")
        self.oHelper.WaitHide("Pesquisando...")
        self.oHelper.SetValue("NSZ_LCLIEN", "01")
        self.oHelper.ClickLabel("Alteração em Lote")
        self.oHelper.SetValue("NSZ_CAREAJ", "JUR02")
        self.oHelper.SetButton("Ok")
        self.oHelper.WaitHide("Processando...")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetValue("NSZ_CAREAJ", "JUR02")
        self.oHelper.SetValue("NSZ_COD", "0000000092")
        self.oHelper.ClickLabel("Pesquisar")
        self.oHelper.SetValue("NSZ_LCLIEN", "01")
        self.oHelper.ClickLabel("Visualizar")
        self.oHelper.CheckResult("NSZ_CAREAJ", "JUR02")
        self.oHelper.SetButton("Fechar")
        self.oHelper.ClickLabel("Sair")
        self.oHelper.AssertTrue()

        print('FIM - CT001')

    def test_TJurPesqAsj_CT002(self):

        print('INICIO - CT002 - EXCLUSÃO DE MODELO')

        self.oHelper.Program('JURA162')
        self.oHelper.SetValue("cValor", "Contencioso", name_attr=True)
        self.oHelper.ClickLabel("Excluir Modelo")
        self.oHelper.SearchBrowse('TIR-PESQASJ-CT002', key=3, index=True)
        self.oHelper.ClickGridCell('Código', row=1)
        self.oHelper.SetButton('Ok')
        self.oHelper.CheckHelp(
            text="Modelo excluido com sucesso!",
            button="Fechar")
        self.oHelper.ClickLabel("Sair")
        self.oHelper.AssertTrue()

        print('FIM - CT002')

    def test_TJurPesqAsj_CT003(self):

        print('INICIO - CT003 - INCLUSÃO DE PROCESSO USANDO MODELO')
        self.oHelper.Program('JURA162')
        self.oHelper.SetValue("cValor", "Contencioso", name_attr=True)
        self.oHelper.ClickLabel("Incluir com Modelo")
        self.oHelper.SearchBrowse('TIR-PESQASJ-CT003', key=3, index=True)
        self.oHelper.ClickGridCell('Código', row=1)
        self.oHelper.SetButton('Ok')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton("Fechar")
        self.oHelper.ClickLabel("Sair")
        self.oHelper.AssertTrue()

        print('FIM - CT003')

    def test_TJurPesqAsj_CT004(self):

        print('INICIO - CT004 - ALTERAÇÃO DE PROCESSO ENCERRADO EM LOTE')
        self.oHelper.Program('JURA162')
        self.oHelper.SetValue("cValor", "Contencioso", name_attr=True)
        self.oHelper.SetValue("NSZ_SIGLA1", "JAFL")
        self.oHelper.SetValue("NSZ_SITUAC", "2")
        self.oHelper.ClickLabel("Pesquisar")
        self.oHelper.WaitHide("Pesquisando...")
        time.sleep(3)
        self.oHelper.ClickLabel("Alteração em Lote")
        self.oHelper.SetValue("NSZ_SIGLA1", "DFR")

        self.oHelper.SetValue("NUV_CMOTIV", "0002")
        self.oHelper.SetValue(
            "NUV_JUSTIF",
            "TIR PESQASJ CT004 - ALTERAÇÃO DE PROCESSO ENCERRADO EM LOTE")
        self.oHelper.SetButton("Ok")
        self.oHelper.WaitHide("Processando...")
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetValue("NSZ_SIGLA1", "DFR")
        self.oHelper.ClickLabel("Pesquisar")
        self.oHelper.WaitHide("Pesquisando...")
        self.oHelper.SetValue("NSZ_SIGLA1", "DFR")
        self.oHelper.ClickLabel("Visualizar")
        self.oHelper.CheckResult("NSZ_SIGLA1", "DFR")
        self.oHelper.SetButton("Fechar")
        self.oHelper.ClickLabel("Sair")
        self.oHelper.AssertTrue()

        print('FIM - CT004')

    def test_TJurPesqAsj_CT005(self):

        print('INICIO - CT005 - Alteração em lote de escritórios' +
              ' credenciados de processos ativos')
        self.oHelper.Program('JURA162')
        self.oHelper.SetValue("cValor", "Contencioso", name_attr=True)
        self.oHelper.SetValue("NSZ_SIGLA1", "JAFL")
        self.oHelper.SetValue("NSZ_SIGLA2", "DFR")
        self.oHelper.SetValue("NUQ_CCORRE", "TIRASJ")
        self.oHelper.SetValue("NUQ_LCORRE", "01")
        self.oHelper.ClickLabel("Pesquisar")
        self.oHelper.WaitHide("Pesquisando...")

        time.sleep(3)
        self.oHelper.ClickLabel("Alteração em Lote")
        self.oHelper.SetValue("NUQ_CCORRE", "FUP001")
        self.oHelper.SetButton("Ok")
        self.oHelper.WaitHide("Processando...")
        self.oHelper.SetValue(
            "NTC_MOTIVO",
            "TIR PESQASJ CT005 - ALTERAÇÃO DE CORRESPONDENTE EM LOTE")
        self.oHelper.SetButton("Ok")
        self.oHelper.WaitHide("Processando...")
        time.sleep(3)
        self.oHelper.CheckHelp(
            text="2 Registro(s) alterado(s).",
            button="Fechar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetValue("NUQ_CCORRE", "FUP001")
        self.oHelper.ClickLabel("Pesquisar")
        self.oHelper.WaitHide("Pesquisando...")
        self.oHelper.SetValue("NUQ_CCORRE", "FUP001")
        self.oHelper.ClickLabel("Visualizar")
        self.oHelper.CheckResult(
            "NSZ_DETALH",
            "TIR PESQASJ CT005")
        self.oHelper.SetButton("Fechar")
        self.oHelper.ClickLabel("Sair")
        self.oHelper.AssertTrue()

        print('FIM - CT005')
        print('FIM - Restaurando parametros')
        self.oHelper.RestoreParameters()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
