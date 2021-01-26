from tir import Webapp
import unittest
import time

class TJurPesquisa(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAJURI','','T1','D MG 01 ','05')
		inst.oHelper.Program('JURA162')

	def test_TJurPesquisa_CT001(self):
		print('CT001 - Visualizar tela de escolha de assunto jurídico')

		# Abre a tela de pesquisas e valida se o novo assunto esta disponivel na Inclusão de um processo
		self.oHelper.SetValue("cValor","Criminal",name_attr=True)
		self.oHelper.WaitFieldValue("NSZ_LCLIEN","")

		# Inclui um processo com o novo assunto juridico
		self.oHelper.ClickLabel('Incluir')
		self.oHelper.ClickGridCell("Descrição",row=2)
		self.oHelper.SetButton('Cancelar')
		self.oHelper.ClickLabel('Sair')
		self.oHelper.AssertTrue()


	def test_TJurPesquisa_CT002(self):
		print('CT002 - Visualizar as opções de legenda de processos')
		self.oHelper.Program('JURA162')

		self.oHelper.SetValue("cValor","Contencioso",name_attr=True)
		self.oHelper.WaitFieldValue("NSZ_COD","")
		self.oHelper.SetValue("NSZ_COD","0000000154")
		self.oHelper.ClickLabel('Pesquisar')
		self.oHelper.ClickGridCell("",row=1)
		time.sleep(3)
		self.oHelper.SetKey("Enter",grid=True)
		time.sleep(2)
		self.oHelper.SetButton('Ok')
		self.oHelper.ClickLabel('Sair')
		self.oHelper.AssertTrue()


	def test_TJurPesquisa_CT003(self):
		print('CT003 - Aplicar correção monetária em um processo')
		self.oHelper.Program('JURA162')

		# Pesquisa o assunto juridico
		self.oHelper.SetValue("cValor","Contencioso",name_attr=True)
		self.oHelper.WaitFieldValue("NSZ_COD","")
		self.oHelper.SetValue("NSZ_COD","0000000154")
		self.oHelper.ClickLabel('Pesquisar')
		self.oHelper.SetValue("NSZ_COD","0000000154")
		self.oHelper.ClickGridCell("Código Assunto Jurídico",row=1)

		# Clica no botão de correção monetaria
		self.oHelper.ClickLabel('Correção Monetária')
		self.oHelper.SetButton("Fechar")
		self.oHelper.ClickLabel('Sair')
		self.oHelper.AssertTrue()


	def test_TJurPesquisa_CT004(self):

		print('CT004 - Alterar layout de pesquisa')
		self.oHelper.Program('JURA162')
		self.oHelper.ClickLabel('Configurar')
		self.oHelper.SetButton('Avançar >>')
		self.oHelper.SetValue("Indique a quantidade de seções","1")
		self.oHelper.SetButton('Avançar >>')
		self.oHelper.SetValue("Self:cCmbOpc1","Campos",name_attr=True)
		self.oHelper.SetValue("Self:cCmbOpc2","Grid",name_attr=True)
		self.oHelper.SetButton('Avançar >>')
		self.oHelper.SetButton('Finalizar')
		self.oHelper.SetButton('Fechar')
		self.oHelper.ClickLabel('Sair')

		self.oHelper.Program('JURA162')
		self.oHelper.ClickLabel('Configurar')
		self.oHelper.SetButton('Avançar >>')
		self.oHelper.SetValue("Indique a quantidade de seções","2")
		self.oHelper.SetButton('Avançar >>')
		self.oHelper.SetValue("Self:cCmbPerc","35",name_attr=True)
		self.oHelper.SetValue("Self:cCmbOpc1","Campos",name_attr=True)
		self.oHelper.SetValue("Self:cCmbOpc2","",name_attr=True)
		self.oHelper.SetButton('Avançar >>')
		self.oHelper.SetValue("Self:cCmbPerc","65",name_attr=True,position=2)
		self.oHelper.SetValue("Self:cCmbOpc1","Grid",name_attr=True,position=2)
		self.oHelper.SetButton('Avançar >>')
		self.oHelper.SetButton('Finalizar')
		self.oHelper.SetButton('Fechar')
		self.oHelper.ClickLabel('Sair')

		self.oHelper.Program('JURA162')
		self.oHelper.ClickLabel('Configurar')
		self.oHelper.SetButton('Avançar >>')
		self.oHelper.SetButton('Restaurar Padrão')
		self.oHelper.SetButton('Fechar')
		self.oHelper.SetButton('Finalizar')
		self.oHelper.ClickLabel('Sair')

		self.oHelper.Program('JURA162')
		self.oHelper.ClickLabel('Sair')
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()
