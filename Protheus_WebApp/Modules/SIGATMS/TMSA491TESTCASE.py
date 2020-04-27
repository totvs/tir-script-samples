from tir import Webapp
import unittest

class TMSA491(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()	
		inst.oHelper.Setup('SIGATMS','30/05/2019','T1','M SP 01 ','43')
		inst.oHelper.Program('TMSA491')
		inst.oHelper.AddParameter("MV_FATPREF", "", "TMS")
		inst.oHelper.AddParameter("MV_CLIGEN", "", "TMSCLIGE")
		inst.oHelper.AddParameter("MV_NATFAT", "", "001")
		inst.oHelper.AddParameter("MV_TIPFAT", "", "01")
		inst.oHelper.AddParameter("MV_TMSMFAT", "", "2")
		inst.oHelper.AddParameter("MV_CODCOMP", "", "10")
		inst.oHelper.AddParameter("MV_COMPENT", "", "09")
		inst.oHelper.AddParameter("MV_PROGEN", "", "TMS_PROGEN")
		inst.oHelper.SetParameters()

	def test_TMSA491_CT005(self):
		self.oHelper.SearchBrowse("M SP 01 TMS000018      A")
		self.oHelper.SetButton("Outras Ações","Cancelar")
		self.oHelper.ClickLabel("Marca") 
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()