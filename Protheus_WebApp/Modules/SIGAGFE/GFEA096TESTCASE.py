from tir import Webapp
import unittest

class GFEA096(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAGFE','30/12/2020','T1','D MG 01 ','78')
		inst.oHelper.Program('GFEA096')

	def test_GFEA096_CT001(self):

		self.oHelper.SetButton('Incluir')

		self.oHelper.SetButton('OK')
		
		self.oHelper.SetValue('Filial De', 'D MG 01')
		self.oHelper.SetValue('Filial Ate', 'D MG 01')
		self.oHelper.SetValue('Período', '2020/12')
		self.oHelper.SetValue('Data De', '01/12/2020')
		self.oHelper.SetValue('Data Ate', '31/12/2020')
		self.oHelper.SetValue('Emissor', '500')

		self.oHelper.SetButton('Confirmar')

		self.oHelper.SetButton('Fechar')

		self.oHelper.SetButton('Visualizar')

		self.oHelper.SetButton('Fechar')

		self.oHelper.SetButton('Alterar')

		self.oHelper.SetValue('Data De', '01/11/2020')

		self.oHelper.SetButton('Confirmar')

		self.oHelper.SetButton('Fechar')

		self.oHelper.SetButton('Outras Ações','Montar Lote')

		self.oHelper.SetButton('OK')

		self.oHelper.SetButton('Outras Ações','Vis. Detalhada')

		self.oHelper.SetButton('Fechar')

		self.oHelper.SetButton('Outras Ações','Excluir')

		self.oHelper.SetButton('Sim')

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()
if __name__ == '__main__':
	unittest.main()