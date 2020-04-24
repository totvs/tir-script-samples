from tir import Webapp
import unittest

class FINA340(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAFIN","06/04/2020","T1","M SP 01 ","06")
		inst.oHelper.Program("FINA340")

	def test_FINA340_CT043(self):
		chaveTit = "M SP 01 TIRF340T1NF1 NF F340T101"
		
		self.oHelper.SearchBrowse(f'{chaveTit}', key=1, index=True)
		self.oHelper.SetButton("Compensar")
		self.oHelper.SetBranch("M SP 01")
		self.oHelper.SetButton("Ok")
		self.oHelper.WaitShow("Compensaçäo de Titulos")
		self.oHelper.ClickGridCell("Prefixo", 1, 1)
		self.oHelper.SetKey("Enter", grid=True, grid_number=1)
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("Cancelar")
		self.oHelper.SetButton("Cancelar")
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == "__main__":
	unittest.main()