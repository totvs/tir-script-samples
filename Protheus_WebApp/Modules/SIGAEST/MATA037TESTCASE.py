from tir import Webapp
import unittest

class MATA037(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAEST','13/11/2019','T1','D MG 01')
		inst.oHelper.Program('MATA037')

	def test_MAT037_001(self):

		self.oHelper.SearchBrowse("D MG 01 EST023")
		self.oHelper.SetButton("Carregar")
		self.oHelper.SetValue("Cliente","EST006", grid=True, grid_number=2)
		self.oHelper.SetValue("Loja","01", grid=True, grid_number=2)
		self.oHelper.SetValue("Quantidade","80,00", grid=True, grid_number=2)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton("Confirmar")
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()