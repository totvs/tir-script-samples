from tir import Webapp
import unittest

class GFEA013(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAGFE','03/11/2020','T1','D MG 01 ','78')
		inst.oHelper.Program('GFEA013')

	def test_GFEA013_CT001(self):

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetValue('Unid Feder  ', 'AC')
		self.oHelper.SetValue('Trib Est Ctb', '2')
		self.oHelper.SetValue('Trib Est NC ', '2')
		self.oHelper.SetValue('Trib Int Ctb', '2')
		self.oHelper.SetValue('Trib Int NC ', '2')
		self.oHelper.SetValue('Aliq Est Ctb', '4', check_value = False)
		self.oHelper.SetValue('Aliq Est NC ', '4', check_value = False)
		self.oHelper.SetValue('Aliq Int Ctb', '4', check_value = False)
		self.oHelper.SetValue('Aliq Int NC ', '4', check_value = False)
		self.oHelper.SetValue('% Cred ICMS ', '10', check_value = False)
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        AC')
		self.oHelper.SetButton('Alterar')
		self.oHelper.SetValue('Trib Est Ctb', '1')
		self.oHelper.SetValue('Trib Est NC ', '1')
		self.oHelper.SetValue('Trib Int Ctb', '1')
		self.oHelper.SetValue('Trib Int NC ', '1')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        AC')
		self.oHelper.SetButton('Visualizar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        AC')
		self.oHelper.SetButton('Outras Ações','Copiar')
		self.oHelper.SetValue('Unid Feder  ', 'GO')
		self.oHelper.SetValue('Trib Est Ctb', '1')
		self.oHelper.SetValue('Trib Est NC ', '1')
		self.oHelper.SetValue('Trib Int Ctb', '1')
		self.oHelper.SetValue('Trib Int NC ', '1')
		self.oHelper.SetValue('Aliq Est Ctb', '10', check_value = False)
		self.oHelper.SetValue('Aliq Est NC ', '10', check_value = False)
		self.oHelper.SetValue('Aliq Int Ctb', '10', check_value = False)
		self.oHelper.SetValue('Aliq Int NC ', '10', check_value = False)
		self.oHelper.SetValue('% Cred ICMS ', '10', check_value = False)
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        AC')
		self.oHelper.SetButton('Outras Ações','Excluir')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        GO')
		self.oHelper.SetButton('Outras Ações','Excluir')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')
		
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()
if __name__ == '__main__':
	unittest.main()
