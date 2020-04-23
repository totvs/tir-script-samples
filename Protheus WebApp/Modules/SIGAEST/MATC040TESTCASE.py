from tir import Webapp
import unittest

class MATC040(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAEST","04/07/2019","T1","D MG 01 ","04")
		inst.oHelper.Program("MATC040")

	def test_MATC040_001(self):
		self.oHelper.SearchBrowse('D MG 01 ESTSE0000000000000000000000212')
		self.oHelper.SetButton("Parametros")
		self.oHelper.SetValue('De Data de Validade ?', '01/01/2018')
		self.oHelper.SetValue('Ate Data de Validade ?', '16/09/2019')
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Rastrear")
		self.oHelper.ClickTree('ESTSE0000000000000000000000212')
		self.oHelper.SetButton("Salvar")
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()