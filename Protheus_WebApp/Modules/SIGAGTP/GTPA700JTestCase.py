from tir import Webapp
import unittest

class GTPA700J(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAGTP", "23/03/2020", "T1", "D MG 01 ")
		inst.oHelper.Program('GTP700AMB')

	def test_GTPA700J_CT001(self):
		self.oHelper.SearchBrowse("D MG    000016", "Filial+cod. Caixa")
		self.oHelper.ClickLabel("+ Receitas")
		self.oHelper.ClickGridCell("Aceite", grid_number=2)
		self.oHelper.SetValue("Aceite", "1 - Aceito", grid=True, grid_number=2)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.LoadGrid()
		self.oHelper.AssertTrue()
	
	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()	

if __name__ == '__main__':
	unittest.main()
