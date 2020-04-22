from tir import Webapp
import unittest

class GTPA700FC(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAGTP", "30/03/2020", "T1", "D MG 01 ")
		inst.oHelper.Program('GTP700AMB')

	def test_GTPA700FC_CT001(self):

		self.oHelper.SearchBrowse("D MG    000006", "Filial+cod. Caixa")
		self.oHelper.ClickLabel("Fechar Caixa")
		self.oHelper.WaitProcessing("Aguarde o fechamento do caixa.")
		self.oHelper.SetButton("Ok")
		self.oHelper.LoadGrid()
		self.oHelper.AssertTrue()
	
	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()
		

if __name__ == '__main__':
	unittest.main()
