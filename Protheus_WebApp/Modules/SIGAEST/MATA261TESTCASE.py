from tir import Webapp
import unittest

class MATA261(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAEST','10/10/2019','T1','D MG 01')
		inst.oHelper.Program('MATA261')		

	def test_MATA261_CT002(self):
		self.oHelper.SearchBrowse('D MG 01 pcpA1Z001',key='Filial+documento + Produto')
		self.oHelper.SetButton('Visualizar')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.AssertTrue()

	def test_MATA261_CT003(self):
		self.oHelper.SetButton('Outras Ações', 'Legenda')
		self.oHelper.SetButton('Fechar')
		self.oHelper.AssertTrue()

	def test_MATA261_CT004(self):
		self.oHelper.SearchBrowse('D MG 01 pcpA1Z001')
		self.oHelper.SetButton('Outras Ações', 'Estornar')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.AssertTrue()		

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()