from tir import Webapp
import unittest
import time


class TJurPesqGar(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAJURI', '15/10/2018', 'T1', 'D MG 01 ', '05')
        inst.oHelper.Program('JURA098')
        inst.oHelper.AddParameter("MV_JHBPESG", "", "1", "", "")
        inst.oHelper.AddParameter("MV_JINTVAL", "", "2", "", "")
        inst.oHelper.SetParameters()

    def test_TJurPesqGar_CT001(self):

        print('INICIO - CT001 - Alteração em lote')
        self.oHelper.SetValue("cValor", "Contencioso - Garantia", name_attr=True)
        self.oHelper.SetValue("NT2_CAJURI", "0000000146")
        self.oHelper.SetValue("NT2_CTPGAR", "004")
        self.oHelper.SetValue("NT2_CCOMON", "04")
        self.oHelper.ClickLabel("Pesquisar")
        self.oHelper.WaitHide("Pesquisando...")
        self.oHelper.SetValue("NT2_CAJURI", "0000000146")
        self.oHelper.ClickLabel("Alteração em Lote")
        self.oHelper.SetValue("NT2_CTPGAR", "007")
        self.oHelper.SetValue("NT2_CCOMON", "05")
        self.oHelper.SetButton("Ok")
        self.oHelper.WaitHide("Processando...")
        self.oHelper.SetButton("Não")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetValue("NT2_CAJURI", "0000000146")
        self.oHelper.SetValue("NT2_CTPGAR", "007")
        self.oHelper.SetValue("NT2_CCOMON", "05")
        self.oHelper.ClickLabel("Pesquisar")
        self.oHelper.ClickLabel("Visualizar")
        self.oHelper.CheckResult("NT2_CTPGAR", "007")
        self.oHelper.CheckResult("NT2_CCOMON", "05")
        self.oHelper.SetButton("Fechar")
        self.oHelper.ClickLabel("Sair")
        self.oHelper.AssertTrue()
        print('FIM - CT001')

    def test_TJurPesqGar_CT002(self):

        print('INICIO - CT002 - Inclusão de garantia')
        self.oHelper.SetLateralMenu("Atualizações > Assuntos Jurídicos > Garantias e Alvarás")
        self.oHelper.SetValue("cValor", "Contencioso - Garantia", name_attr=True)
        self.oHelper.ClickLabel("Incluir")
        self.oHelper.SetValue("NT2_CAJURI", "0000000146")
        self.oHelper.SetValue("NT2_CTPGAR", "007")
        self.oHelper.SetValue("NT2_DATA", "21/10/2020")
        self.oHelper.SetValue("NT2_CMOEDA", "01")
        self.oHelper.SetValue("NT2_VALOR", "2.000,00")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Não")
        self.oHelper.SetButton("Fechar")
        self.oHelper.ClickLabel("Sair")
        self.oHelper.AssertTrue()
        print('FIM - CT002')

    def test_TJurPesqGar_CT003(self):

        print('INICIO - CT003 - Pesquisa de garantia')
        self.oHelper.SetLateralMenu("Garantias e Alvarás")
        self.oHelper.SetValue("cValor", "Contencioso - Garantia", name_attr=True)
        self.oHelper.SetValue("NT2_CAJURI", "0000000146")
        self.oHelper.SetValue("NT2_CTPGAR", "008")
        self.oHelper.SetValue("NT2_CCOMON", "")
        self.oHelper.ClickLabel("Pesquisar")
        self.oHelper.WaitHide("Pesquisando...")
        self.oHelper.ClickLabel("Visualizar")

        self.oHelper.CheckResult("NT2_CAJURI", "0000000146")
        self.oHelper.CheckResult("NT2_CTPGAR", "008")
        self.oHelper.SetButton("Fechar")
        self.oHelper.ClickLabel("Sair")
        self.oHelper.AssertTrue()
        print('FIM - CT003')

    def test_TJurPesqGar_CT004(self):

        print('INICIO - CT004 - Alteração de garantia')
        self.oHelper.SetLateralMenu("Garantias e Alvarás")
        self.oHelper.SetValue("cValor", "Contencioso - Garantia", name_attr=True)
        self.oHelper.SetValue("NT2_CAJURI", "0000000146")
        self.oHelper.SetValue("NT2_COD", "0000000136")

        self.oHelper.ClickLabel("Pesquisar")
        self.oHelper.WaitHide("Pesquisando...")
        self.oHelper.ClickLabel("Alterar")
        self.oHelper.WaitHide("Carregando...")
        self.oHelper.SetValue("NT2_CCOMON", "04")
        self.oHelper.SetValue("NT2_VALOR", "1.200,30")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Não")
        self.oHelper.SetButton("Fechar")

        self.oHelper.SetValue("NT2_CAJURI", "0000000146")
        self.oHelper.SetValue("NT2_COD", "0000000136")
        self.oHelper.SetValue("NT2_CCOMON", "04")
        self.oHelper.ClickLabel("Pesquisar")
        self.oHelper.WaitHide("Pesquisando...")
        self.oHelper.ClickLabel("Visualizar")

        self.oHelper.CheckResult("NT2_CAJURI", "0000000146")
        self.oHelper.CheckResult("NT2_COD", "0000000136")
        self.oHelper.CheckResult("NT2_CCOMON", "04")
        self.oHelper.SetButton("Fechar")
        self.oHelper.ClickLabel("Sair")
        self.oHelper.AssertTrue()
        print('FIM - CT004')

    def test_TJurPesqGar_CT005(self):

        print('INICIO - CT005 - Exclusão de garantia')
        self.oHelper.Program('JURA098')
        self.oHelper.SetValue("cValor", "Contencioso - Garantia", name_attr=True)
        self.oHelper.SetValue("NT2_CAJURI", "0000000146")
        self.oHelper.SetValue("NT2_CCOMON", "JU")

        self.oHelper.ClickLabel("Pesquisar")
        self.oHelper.WaitHide("Pesquisando...")
        self.oHelper.ClickLabel("Excluir")
        self.oHelper.WaitHide("Carregando...")
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Não')
        self.oHelper.SetButton('Fechar')
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
 