from tir import Webapp
import unittest

class GFEA048(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAGFE','29/12/2020','T1','D MG 01 ','78')
		inst.oHelper.Program('GFEA048')

	def test_GFEA048_CT001(self):

		self.oHelper.SetButton('Incluir')

		self.oHelper.SetButton('OK')
		
		self.oHelper.SetValue('Campo', 'GW1_TPFRET')
		self.oHelper.SetValue('Valor', 'NFE')
				
		self.oHelper.SetButton('Confirmar')
		
		self.oHelper.SetButton('Fechar')

		self.oHelper.SetButton('Visualizar')
		
		self.oHelper.SetButton('Fechar')

		self.oHelper.SetButton('Alterar')

		self.oHelper.SetButton('Outras Ações','Montar Expressão')

		self.oHelper.SetButton('Incluir')

		self.oHelper.SetButton('OK')

		self.oHelper.SetButton('Confirmar')
		
		self.oHelper.SetButton('Fechar')

		self.oHelper.SetButton('Outras Ações','Excluir')

		self.oHelper.SetButton('Confirmar')
		
		self.oHelper.SetButton('Fechar')

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()
if __name__ == '__main__':
	unittest.main()