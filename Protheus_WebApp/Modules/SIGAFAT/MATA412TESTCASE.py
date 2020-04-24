from tir import Webapp
import unittest

class MATA412(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAFAT','02/09/2019','T1','D MG 01 ','05')
		inst.oHelper.Program('MATA412')

	def test_MATA412_CT002(self):
		self.oHelper.SearchBrowse("D MG 01 000000005")
		self.oHelper.SetButton('Outras Ações', 'Gerar Pedido de Venda')
		self.oHelper.WaitProcessing('Aguarde, gerando o Pedido de Venda.')
		self.oHelper.SearchBrowse("D MG 01 000000005")
		self.oHelper.SetButton('Outras Ações', 'Visualizar')
		self.oHelper.SetButton('Fechar')
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()