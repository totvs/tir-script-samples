import unittest
from tir import Webapp


class BIXLOG(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGACFG','11/12/2018','T1','D MG 01 ')
		inst.oHelper.SetLateralMenu('Ambiente > Extrator Bi > Log de Extração')

	def test_BIXLOG_CT001(self):

		self.oHelper.SetButton("Outras Ações", sub_item="Log de Extração")
		self.oHelper.SetButton('Fechar')
		self.oHelper.SetButton("Outras Ações", sub_item="Análise de Performance")
		self.oHelper.SetButton('Fechar')
		self.oHelper.SetButton("Outras Ações", sub_item="Configuração")
		self.oHelper.ClickLabel("Habilitar modo de debug ?")
		self.oHelper.ClickLabel("Alertar sobre ocorrência de erro na extração de fatos e dimensões ?")
		self.oHelper.ClickLabel("Alertar no momento em que uma extração for finalizada ?")
		self.oHelper.ClickLabel("Alertar no momento em que uma extração for cancelada ?")		
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton("Outras Ações", sub_item="Gerar Relatório")
		self.oHelper.ClickLabel("Enviar arquivo HTML gerado por e-mail ? ")
		self.oHelper.SetValue("Quem deve receber e-mail com o relatório gerado anexo ?", "teste@teste.com.br")
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')
		self.oHelper.SetButton("Outras Ações", sub_item="Gerar Relatório")
		self.oHelper.ClickLabel("Abrir arquivo HTML gerado no browser após confirmação? ")
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')
		self.oHelper.SetButton("Outras Ações", sub_item="Configurar")
		self.oHelper.SetButton('OK')
		self.oHelper.SetButton('Fechar')

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()
