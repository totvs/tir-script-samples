from tir import Webapp
import unittest

class MATR445(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAEST','14/11/2019','T1','D MG 01')
		inst.oHelper.Program('MATR445')
	
	def test_MATR445_CT001(self):
		self.oHelper.SetButton('Outras Ações', 'Parâmetros')
		self.oHelper.SetValue('Periodo de ?','01/01/2000')
		self.oHelper.SetValue('Periodo ate ?','31/12/2020')
		self.oHelper.SetKey("DOWN")		
		self.oHelper.CheckHelp(text_help="R4096DIAS", button="Fechar")	
		self.oHelper.SetValue('Periodo ate ?','31/12/2000')
		self.oHelper.SetButton('Cancelar')
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()
