from tir import Webapp
import unittest

class GFEA022(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAGFE','05/12/2020','T1','D MG 01 ','78')
		inst.oHelper.Program('GFEA022')

	def test_GFEA022_CT001(self):

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetValue('Ida e Volta ', '2')
		self.oHelper.SetValue('Ini Validade', '04/12/2020')
		self.oHelper.SetValue('Fim Validade', '31/12/2050')
		self.oHelper.SetValue('Cid Origem  ', '1100205')
		self.oHelper.SetValue('Cid Dest    ', '1200401')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        00081')
		self.oHelper.SetButton('Alterar')
		self.oHelper.SetValue('Tipo Oper   ', '1')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        00081')
		self.oHelper.SetButton('Visualizar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        00081')
		self.oHelper.SetButton('Outras Ações','Copiar')
		self.oHelper.SetValue('Cid Origem  ', '1200401')
		self.oHelper.SetValue('Cid Dest    ', '1501402')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        00081')
		self.oHelper.SetButton('Outras Ações','Excluir')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        00082')
		self.oHelper.SetButton('Outras Ações','Excluir')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')
		
		self.oHelper.AssertTrue()

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()
if __name__ == '__main__':
	unittest.main()

