from tir import Webapp
import unittest

class GFEA100(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAGFE','04/12/2020','T1','D MG 01 ','78')
		inst.oHelper.Program('GFEA100')

	def test_GFEA100_CT001(self):

		self.oHelper.SetButton('Incluir')

		self.oHelper.SetButton('OK')
		
		self.oHelper.SetValue('Dt Vencto', '04/12/2020')

		self.oHelper.SetValue('Proprietario', '161')

		self.oHelper.SetButton('Confirmar')

		self.oHelper.SetButton('Fechar')

		self.oHelper.SetButton('Visualizar')

		self.oHelper.SetButton('Fechar')

		self.oHelper.SetButton('Alterar')

		self.oHelper.SetValue('Dt Vencto', '05/12/2020')

		self.oHelper.SetButton('Confirmar')

		self.oHelper.SetButton('Fechar')

		self.oHelper.SetButton('Outras Ações','Excluir')

		self.oHelper.SetButton('Confirmar')

		self.oHelper.SetButton('Fechar')
		
		self.oHelper.AssertTrue()

	def test_GFEA100_CT002(self):

		self.oHelper.SearchBrowse('D MG 01 00000001')

		self.oHelper.SetButton('Outras Ações','Selecionar Cálculos')

		self.oHelper.SetValue('De Data Criacao ?', '07/12/2020')

		self.oHelper.SetValue('Ate Data Criacao ?', '07/12/2020')

		self.oHelper.SetButton('OK')

		self.oHelper.SetButton('Cancelar')

		self.oHelper.SearchBrowse('D MG 01 00000001')

		self.oHelper.SetButton('Outras Ações','Impostos')

		self.oHelper.SetButton('Confirmar')

		self.oHelper.SearchBrowse('D MG 01 00000001')

		self.oHelper.SetButton('Outras Ações','Cancelar')

		self.oHelper.SetButton('Sim')
		
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()
if __name__ == '__main__':
	unittest.main()