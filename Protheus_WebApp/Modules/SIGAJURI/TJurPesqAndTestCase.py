from tir import Webapp
import unittest
import time


class TJurPesqAnd(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAJURI', '16/10/2020', 'T1', 'D MG 01 ', '76')
        inst.oHelper.Program('JURA100')
        inst.oHelper.AddParameter("MV_JHBPESA", "", "1", "", "")
        inst.oHelper.AddParameter("MV_JINTVAL", "", "2", "", "")
        inst.oHelper.SetParameters()

    def test_TJurPesqAnd_CT001(self):

        print('INICIO - CT001 - Inclusão de andamento')
        self.oHelper.SetValue(
            "cValor",
            "TIR-TJURPESQAND",
            name_attr=True)
        self.oHelper.SetValue("NT4_CAJURI", "0000000164")
        self.oHelper.ClickLabel("Incluir")

        self.oHelper.SetValue("NT4_DESC", "TIR-TJURPESAND-CT001-INCLUSÃO")
        self.oHelper.SetValue("NT4_CAJURI", "0000000164")
        self.oHelper.SetValue("NT4_DTANDA", "23/11/2020")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.CheckHelp(
            text="Registro inserido com sucesso.",
            button="Fechar")

        self.oHelper.SetValue("NT4_DTANDA", "23/11/2020")
        self.oHelper.ClickLabel("Pesquisar")
        self.oHelper.WaitHide("Pesquisando...")
        self.oHelper.SetValue("NT4_DTANDA", "23/11/2020")
        self.oHelper.ClickLabel("Visualizar")
        self.oHelper.CheckResult(
            "NT4_DESC",
            "TIR-TJURPESAND-CT001-INCLUSÃO")
        self.oHelper.SetButton("Fechar")
        self.oHelper.ClickLabel("Sair")

        self.oHelper.AssertTrue()
        print('FIM - CT001')

    def test_TJurPesqAnd_CT002(self):

        print('INICIO - CT002 - Alteração de andamento')
        self.oHelper.Program('JURA100')
        self.oHelper.SetValue(
            "cValor",
            "TIR-TJURPESQAND",
            name_attr=True)
        self.oHelper.SetValue("NT4_CAJURI", "0000000164")
        self.oHelper.SetValue("NT4_DTANDA", "09/11/2020")
        self.oHelper.ClickLabel("Pesquisar")
        self.oHelper.WaitHide("Pesquisando...")
        self.oHelper.SetValue("NT4_CAJURI", "0000000164")
        self.oHelper.ClickLabel("Alterar")
        self.oHelper.SetValue("NT4_CFASE", "001")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.CheckHelp(
            text="Registro alterado com sucesso.",
            button="Fechar")
        self.oHelper.SetValue("NT4_CFASE", "001")
        self.oHelper.ClickLabel("Pesquisar")
        self.oHelper.WaitHide("Pesquisando...")
        self.oHelper.SetValue("NT4_CFASE", "001")
        self.oHelper.ClickLabel("Visualizar")
        self.oHelper.CheckResult(
            "NT4_CFASE",
            "001")
        self.oHelper.SetButton("Fechar")
        self.oHelper.ClickLabel("Sair")

        self.oHelper.AssertTrue()

        print('FIM - CT002')

    def test_TJurPesqAnd_CT003(self):

        print('INICIO - CT003 - Alteração em lote')
        self.oHelper.Program('JURA100')
        self.oHelper.SetValue(
            "cValor",
            "TIR-TJURPESQAND",
            name_attr=True)
        self.oHelper.SetValue("NT4_CAJURI", "0000000164")
        self.oHelper.SetValue("NT4_DTANDA", "10/11/2020")
        self.oHelper.SetValue("NT4_CFASE", "001")
        self.oHelper.ClickLabel("Pesquisar")
        self.oHelper.WaitHide("Pesquisando...")
        self.oHelper.SetValue("NT4_CAJURI", "0000000164")
        self.oHelper.ClickLabel("Alteração em Lote")
        self.oHelper.SetValue("NT4_CFASE", "002")

        self.oHelper.SetButton("Ok")
        self.oHelper.WaitHide("Processando...")

        self.oHelper.CheckHelp(
            text="2 Registros alterados",
            button="Fechar")
        self.oHelper.CheckHelp(
            text="Nenhum registro encontrado.",
            button="Fechar")
        self.oHelper.SetValue("NT4_CFASE", "002")
        self.oHelper.ClickLabel("Pesquisar")
        self.oHelper.WaitHide("Pesquisando...")
        self.oHelper.SetValue("NT4_CFASE", "002")
        self.oHelper.ClickLabel("Visualizar")
        self.oHelper.CheckResult(
            "NT4_CFASE",
            "002")
        self.oHelper.SetButton("Fechar")
        self.oHelper.ClickLabel("Sair")

        self.oHelper.AssertTrue()

        print('FIM - CT003')

    def test_TJurPesqAnd_CT004(self):

        print('INICIO - CT004 - Exclusão de andamento')
        self.oHelper.Program('JURA100')
        self.oHelper.SetValue(
            "cValor",
            "TIR-TJURPESQAND",
            name_attr=True)
        self.oHelper.SetValue("NT4_CAJURI", "0000000164")
        self.oHelper.SetValue("NT4_DTANDA", "11/11/2020")
        self.oHelper.ClickLabel("Pesquisar")
        self.oHelper.WaitHide("Pesquisando...")
        self.oHelper.SetValue("NT4_CAJURI", "0000000164")
        self.oHelper.ClickLabel("Excluir")
        self.oHelper.WaitHide("Carregando...")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.CheckHelp(
            text="Registro excluído com sucesso.",
            button="Fechar")
        self.oHelper.SetValue("NT4_DTANDA", "11/11/2020")
        self.oHelper.ClickLabel("Pesquisar")
        self.oHelper.WaitHide("Pesquisando...")
        self.oHelper.CheckHelp(
            text="Nenhum registro encontrado.",
            button="Fechar")
        self.oHelper.ClickLabel("Sair")

        self.oHelper.AssertTrue()

        print('FIM - CT004')

    def test_TJurPesqAnd_CT005(self):

        print('INICIO - CT005 - Geração de relatório')
        self.oHelper.Program('JURA100')
        self.oHelper.SetValue(
            "cValor",
            "TIR-TJURPESQAND",
            name_attr=True)
        self.oHelper.SetValue("NT4_CAJURI", "0000000164")
        self.oHelper.SetValue("NT4_DTANDA", "10/11/2020")
        self.oHelper.ClickLabel("Pesquisar")
        self.oHelper.WaitHide("Pesquisando...")
        self.oHelper.SetValue("NT4_CAJURI", "0000000164")
        self.oHelper.ClickLabel("Andamentos")
        self.oHelper.ClickLabel("Sair")

        self.oHelper.AssertTrue()

        print('FIM - CT005')

    def test_TJurPesqAnd_CT006(self):

        print('INICIO - CT006 - Exportar resultados')
        self.oHelper.Program('JURA100')
        self.oHelper.SetValue(
            "cValor",
            "TIR-TJURPESQAND",
            name_attr=True)
        self.oHelper.SetValue("NT4_CAJURI", "0000000164")
        self.oHelper.SetValue("NT4_DTANDA", "10/11/2020")
        self.oHelper.ClickLabel("Pesquisar")
        self.oHelper.WaitHide("Pesquisando...")
        self.oHelper.SetValue("NT4_CAJURI", "0000000164")
        self.oHelper.ClickLabel("Exportar Resultados")
        time.sleep(3)
        self.oHelper.SetValue(
            "cFile",
            "TIR-TJURPESQAND-CT006",
            name_attr=True)
        self.oHelper.SetButton("Imprimir")

        self.oHelper.SetButton("Sair")
        self.oHelper.ClickLabel("Sair")

        self.oHelper.AssertTrue()

        print('FIM - CT006')
        print('FIM - Restaurando parametros')
        self.oHelper.RestoreParameters()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
