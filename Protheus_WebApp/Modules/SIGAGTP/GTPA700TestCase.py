from tir import Webapp
import unittest

class GTPA700(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAGTP", "23/03/2020", "T1", "D MG 01 ")
		inst.oHelper.Program('GTP700AMB')

	def test_GTPA700_CT001(self):
		self.oHelper.ClickLabel("Abrir Caixa")
		self.oHelper.SetValue("MV_PAR01", "000040")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Ok")
		self.oHelper.SearchBrowse("D MG    20200323000040", "Filial+dt. Abertura + Agência")
		self.oHelper.SetButton("Manutenção")
		self.oHelper.ClickGridCell("Flag Caixa", row=1)
		self.oHelper.ClickBox("Flag Caixa", contents_list='', select_all=False, grid_number=1)
		self.oHelper.SetButton("Confirmar")
		self.oHelper.WaitProcessing("Carregando movimentos...")
		self.oHelper.SetButton("Fechar")
		self.oHelper.LoadGrid()
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()		

if __name__ == '__main__':
	unittest.main()
