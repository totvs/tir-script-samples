from tir import Webapp
import unittest
import time


class TJurPesqDes(unittest.TestCase):

	@classmethod
	def setUpClass(inst):

		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAJURI', '15/10/2018', 'T1', 'D MG 01 ', '05')
		inst.oHelper.Program('JURA099')
		inst.oHelper.AddParameter("MV_JHBPESD", "", "1", "", "")
		inst.oHelper.AddParameter("MV_JINTVAL", "", "2", "", "")
		inst.oHelper.SetParameters()

	def test_TJurPesqDes_CT001(self):
		print('INICIO - CT001 - Pesquisa de despesas')
		self.oHelper.SetValue("cValor", "Contencioso - Desp", name_attr=True)
		self.oHelper.SetValue("NT3_CAJURI", "0000000140")
		self.oHelper.SetValue("NT3_CTPDES", "001")
		self.oHelper.ClickLabel("Pesquisar")
		self.oHelper.SetValue("NT3_CAJURI", "0000000140")
		self.oHelper.ClickGridCell("Código do cliente",row=1)

		self.oHelper.ClickLabel("Visualizar")
		self.oHelper.CheckResult("NT3_CAJURI", "0000000140")
		self.oHelper.CheckResult("NT3_CTPDES", "001")
		self.oHelper.SetButton("Fechar")
		self.oHelper.ClickLabel("Sair")
		self.oHelper.AssertTrue()
		print('FIM - CT001')

	def test_TJurPesqDes_CT002(self):
		print('INICIO - CT002 - Inclusão de despesa')
		self.oHelper.Program('JURA099')
		self.oHelper.SetValue("cValor", "Contencioso - Desp", name_attr=True)
		self.oHelper.ClickLabel("Incluir")
		self.oHelper.SetValue("NT3_CAJURI", "0000000140")
		self.oHelper.SetValue("NT3_CTPDES", "005")
		self.oHelper.SetValue("NT3_DATA", "21/10/2020")
		self.oHelper.SetValue("NT3_CMOEDA", "01")
		self.oHelper.SetValue("NT3_VALOR", "140,02")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")

		print('Pesquisa despesa incluída')
		self.oHelper.SetValue("NT3_DATA", "21/10/2020")
		self.oHelper.SetValue("NT3_CTPDES", "005")
		self.oHelper.SetValue("NT3_CAJURI", "0000000140")
		self.oHelper.SetValue("NT3_VALOR", "140,02")
		self.oHelper.SetValue("NT3_VALOR", "140,02", position=2)
		self.oHelper.ClickLabel("Pesquisar")
		self.oHelper.WaitHide("Pesquisando...")

		print('Valida despesa incluída')
		self.oHelper.ClickLabel("Visualizar")
		self.oHelper.CheckResult("NT3_CAJURI", "0000000140")
		self.oHelper.CheckResult("NT3_DATA", "21/10/2020")
		self.oHelper.CheckResult("NT3_CTPDES", "005")
		self.oHelper.CheckResult("NT3_CAJURI", "0000000140")
		self.oHelper.CheckResult("NT3_VALOR", "140,02")
		self.oHelper.SetButton("Fechar")
		self.oHelper.ClickLabel("Sair")
		self.oHelper.AssertTrue()
		print('FIM - CT002')


	def test_TJurPesqDes_CT003(self):
		print('INICIO - CT003 - Alteração de despesa')
		self.oHelper.Program('JURA099')
		self.oHelper.SetValue("cValor", "Contencioso - Desp", name_attr=True)
		self.oHelper.SetValue("NT3_CAJURI", "0000000140")
		self.oHelper.SetValue("NT3_CTPDES", "001")
		self.oHelper.ClickLabel("Pesquisar")
		self.oHelper.WaitHide("Pesquisando...")

		self.oHelper.ClickLabel("Alterar")
		self.oHelper.WaitHide("Carregando...")
		self.oHelper.SetValue("NT3_DATA", "21/10/2020")
		self.oHelper.SetValue("NT3_CTPDES", "005")
		self.oHelper.SetValue("NT3_CAJURI", "0000000140")
		self.oHelper.SetValue("NT3_VALOR", "140,03")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")

		print('Pesquisa despesa alterada')
		self.oHelper.SetValue("NT3_DATA", "21/10/2020")
		self.oHelper.SetValue("NT3_CTPDES", "005")
		self.oHelper.SetValue("NT3_CAJURI", "0000000140")
		self.oHelper.SetValue("NT3_VALOR", "140,03")
		self.oHelper.SetValue("NT3_VALOR", "140,03", position=2)
		self.oHelper.ClickLabel("Pesquisar")
		self.oHelper.WaitHide("Pesquisando...")

		print('Valida despesa alterada')
		self.oHelper.ClickLabel("Visualizar")
		self.oHelper.CheckResult("NT3_CAJURI", "0000000140")
		self.oHelper.CheckResult("NT3_DATA", "21/10/2020")
		self.oHelper.CheckResult("NT3_CTPDES", "005")
		self.oHelper.CheckResult("NT3_VALOR", "140,03")
		self.oHelper.SetButton("Fechar")
		self.oHelper.ClickLabel("Sair")
		self.oHelper.AssertTrue()
		print('FIM - CT003')

	
	def test_TJurPesqDes_CT004(self):
		print('INICIO - CT004 - Alteração em lote')
		self.oHelper.Program('JURA099')
		self.oHelper.SetValue("cValor", "Contencioso - Desp", name_attr=True)
		self.oHelper.SetValue("NT3_CTPDES", "005")
		self.oHelper.SetValue("NT3_CAJURI", "0000000140")
		self.oHelper.SetValue("NT3_VALOR", "140,02")
		self.oHelper.ClickLabel("Pesquisar")
		self.oHelper.WaitHide("Pesquisando...")

		self.oHelper.ClickLabel("Alteração em Lote")
		self.oHelper.SetValue("NT3_CTPDES", "001")
		self.oHelper.SetButton("Ok")
		self.oHelper.WaitHide("Processando...")
		self.oHelper.SetButton("Fechar")

		print('Valida - Alteração em lote')
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetValue("NT3_CAJURI", "0000000140")
		self.oHelper.SetValue("NT3_CTPDES", "001")
		self.oHelper.SetValue("NT3_VALOR", "140,02")
		self.oHelper.SetValue("NT3_VALOR", "140,04", position=2)
		self.oHelper.ClickLabel("Pesquisar")
		self.oHelper.ClickLabel("Visualizar")
		self.oHelper.CheckResult("NT3_CAJURI", "0000000140")
		self.oHelper.CheckResult("NT3_CTPDES", "001")

		self.oHelper.SetButton("Fechar")
		self.oHelper.ClickLabel("Sair")
		self.oHelper.AssertTrue()
		print('FIM - CT004')

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()


if __name__ == '__main__':
	unittest.main()
 