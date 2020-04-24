from tir import Webapp
import unittest

class MATC070(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAEST','21/06/2019','T1','D MG 01')
		inst.oHelper.Program('MATC070')

	def test_MATC070_CT001(self):
		self.oHelper.SearchBrowse('D MG 01 ESTSE0000000000000000000000037')
		self.oHelper.SetButton('Consulta')
		self.oHelper.SetButton('Imprimir')
		self.oHelper.SetButton('Cancelar')
		self.oHelper.SetButton('Ordem')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Ok')
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()
