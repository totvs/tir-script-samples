from tir import Webapp
import unittest

class GFEA030(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAGFE','05/12/2020','T1','D MG 01 ','78')
		inst.oHelper.Program('GFEA030')

	def test_GFEA030_CT001(self):

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetValue('Tipo        ', '900001')
		self.oHelper.SetValue('Descricao   ', 'TIPO OCORRENCIA TESTE AUTOMACAO')
		self.oHelper.SetValue('Evento      ', '3')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        900001')
		self.oHelper.SetButton('Alterar')
		self.oHelper.SetValue('Descricao   ', 'TIPO OCORR ALTERADO TESTE AUTOMACAO')
		self.oHelper.ClickGridCell('Motivo', 1)
		self.oHelper.SetValue('Motivo', '000001', grid=True)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        900001')
		self.oHelper.SetButton('Visualizar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        900001')
		self.oHelper.SetButton('Outras Ações','Copiar')
		self.oHelper.SetValue('Tipo        ', '900002')
		self.oHelper.SetValue('Descricao   ', 'TIPO OCORR 2 TESTE AUTOMACAO')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()
if __name__ == '__main__':
	unittest.main()

