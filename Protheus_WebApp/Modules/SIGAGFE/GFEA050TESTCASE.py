from tir import Webapp
import unittest

class GFEA050(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAGFE','30/06/2020','T1','D MG 01 ','78')
		inst.oHelper.Program('GFEA050')

	def test_GFEA050_CT001(self):

		self.oHelper.SetButton('Incluir')

		self.oHelper.SetButton('OK')

		self.oHelper.SetValue('Transp', '76887431000183')
		self.oHelper.SetValue('Tipo Oper', '1')

		self.oHelper.SetButton('Confirmar')

		self.oHelper.SetButton('Fechar')

		self.oHelper.SetButton('Alterar')

		self.oHelper.SetValue('Tipo Oper', '2')

		self.oHelper.SetButton('Confirmar')

		self.oHelper.SetButton('Fechar')

		self.oHelper.SetButton('Outras Ações','Excluir')

		self.oHelper.SetButton('Confirmar')

		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('D MG 01 00000505')

		self.oHelper.SetButton('Outras Ações','Liberar')

		self.oHelper.SetButton('OK')

		self.oHelper.SearchBrowse('D MG 01 00000505')

		self.oHelper.SetButton('Visualizar')

		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('D MG 01 00000505')

		self.oHelper.SetButton('Outras Ações','Inf. Rastr.')

		self.oHelper.SetValue('Cod Rastream', '12345')

		self.oHelper.SetButton('Confirmar')

		self.oHelper.SearchBrowse('D MG 01 00000505')

		self.oHelper.SetButton('Outras Ações','Reabrir')

		self.oHelper.SetValue('Motivo da Reabertura', 'Teste TIR de Reabertura.')

		self.oHelper.SetButton('OK')

		self.oHelper.SearchBrowse('D MG 01 00000505')

		self.oHelper.SetButton('Outras Ações','Bloq./Desbloq.')

		self.oHelper.SetButton('Sim')

		self.oHelper.SearchBrowse('D MG 01 00000505')

		self.oHelper.SetButton('Outras Ações','Bloq./Desbloq.')

		self.oHelper.SetButton('Sim')

		self.oHelper.SearchBrowse('D MG 01 00000041')

		self.oHelper.SetButton('Outras Ações','Roteiro')

		self.oHelper.SetButton('Confirmar')

		self.oHelper.SetButton('Fechar')

		self.oHelper.SetButton('Fechar')
		
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()
if __name__ == '__main__':
	unittest.main()

