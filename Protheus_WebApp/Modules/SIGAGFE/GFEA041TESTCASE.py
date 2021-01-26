from tir import Webapp
import unittest

class GFEA041(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAGFE','05/12/2020','T1','D MG 01 ','78')
		inst.oHelper.Program('GFEA041')

	def test_GFEA041_CT001(self):

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetValue('Tipo Docto  ', 'TST')
		self.oHelper.SetValue('Descricao   ', 'TESTE DE AUTOMACAO')
		self.oHelper.SetValue('Tipo Transp ', '1')
		self.oHelper.SetValue('Sentido     ', '0')
		self.oHelper.SetValue('Tipo Contab ', '1')
		self.oHelper.SetValue('Envia EDI?  ', '2')
		self.oHelper.SetValue('Calculo fret', '1')
		self.oHelper.SetValue('Emite PreFat', '1')
		self.oHelper.SetValue('Data Ent Aut', '0')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        TST')
		self.oHelper.SetButton('Alterar')
		self.oHelper.SetValue('Descricao   ', 'TESTE DE AUTOMACAO - ALTERADO')
		self.oHelper.SetValue('Tipo Transp ', '4')
		self.oHelper.SetValue('Sentido     ', '4')
		self.oHelper.SetValue('Tipo Contab ', '3')
		self.oHelper.SetValue('Emite PreFat', '2')
		self.oHelper.SetValue('Data Ent Aut', '1')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        TST')
		self.oHelper.SetButton('Visualizar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('        TST')
		self.oHelper.SetButton('Outras Ações','Excluir')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')
		
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()
if __name__ == '__main__':
	unittest.main()

