from tir import Webapp
import unittest

class GTPA700H(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAGTP", "30/03/2020", "T1", "D MG 01 ")
		inst.oHelper.Program('GTP700AMB')

	def test_GTPA700H_CT001(self):
		self.oHelper.SearchBrowse("D MG    000012", "Filial+cod. Caixa")
		self.oHelper.ClickLabel("Fechar Caixa")
		self.oHelper.WaitProcessing("Aguarde o fechamento do caixa.")
		self.oHelper.ClickGridCell("Marque", row=1)
		self.oHelper.SetValue("Marque", True, grid=True, grid_number=1)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.WaitProcessing("Aguarde o fechamento do caixa.")
		self.oHelper.SetButton("Ok")
		self.oHelper.LoadGrid()
		self.oHelper.AssertTrue()
	
	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()		

if __name__ == '__main__':
	unittest.main()
