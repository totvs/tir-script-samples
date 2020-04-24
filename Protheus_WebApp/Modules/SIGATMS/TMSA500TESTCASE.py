from tir import Webapp
import unittest

class TMSA500(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGATMS','30/05/2019','T1','M SP 01 ','43')
		inst.oHelper.Program('TMSA500')
		inst.oHelper.AddParameter("MV_FATPREF", "", "TMS")
		inst.oHelper.AddParameter("MV_CLIGEN", "", "TMSCLIGE")
		inst.oHelper.AddParameter("MV_NATFAT", "", "001")
		inst.oHelper.AddParameter("MV_TIPFAT", "", "01")
		inst.oHelper.AddParameter("MV_TMSMFAT", "", "2")
		inst.oHelper.AddParameter("MV_CODCOMP", "", "10")
		inst.oHelper.AddParameter("MV_COMPENT", "", "05")
		inst.oHelper.AddParameter("MV_TESDR", "", "482")
		inst.oHelper.AddParameter("MV_CDRORI", "", "Q50308")
		inst.oHelper.AddParameter("MV_ESTADO", "", "SP")
		inst.oHelper.AddParameter("MV_PRCPROD", "", ".T.")
		inst.oHelper.AddParameter("MV_TMSCTE", "", ".T.")
		inst.oHelper.AddParameter("MV_TPNRNFS", "", "1")
		inst.oHelper.AddParameter("MV_DOCREE", "", ".T.")
		inst.oHelper.AddParameter("MV_OCORREE", "", "E005")
		inst.oHelper.AddParameter("MV_TMSUNFS", "", ".F.")
		inst.oHelper.AddParameter("MV_TPDCREE", "", "2,5")
		inst.oHelper.AddParameter("MV_TMSCFIS", "", ".T.")
		inst.oHelper.AddParameter("MV_ESPECIE", "", "A01=NF;117=CTR")
		inst.oHelper.SetParameters()

	def test_TMSA500_CT018(self):
		self.oHelper.SearchBrowse('M SP    M SP 01 000000133117')
		self.oHelper.SetButton('Visualizar')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.AssertTrue()	
	
	def test_TMSA500_CT019(self):
		self.oHelper.AddParameter("MV_TMSCFIS", "", ".F.")
		self.oHelper.SetParameters()
		self.oHelper.SearchBrowse('M SP    M SP 01 000000133117')
		self.oHelper.SetButton('Visualizar')
		self.oHelper.SetButton('Confirmar')		
		self.oHelper.AssertTrue()	

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()