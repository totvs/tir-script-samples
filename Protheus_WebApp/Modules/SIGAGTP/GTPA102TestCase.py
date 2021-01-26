from tir import Webapp
import unittest

class GTPA102(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAGTP", "01/07/2020", "T1", "D MG 01 ")
		inst.oHelper.Program("GTPA102")

	def test_GTPA102_CT001(self):
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetBranch("D MG")
		self.oHelper.SetValue("GI8_DTINI", "01/07/2020")
		self.oHelper.SetValue("GI8_DTFIM", "31/07/2020")
		self.oHelper.SetValue("GI8_TPDOC", "000001")
		self.oHelper.SetValue("GI8_SERIE", "A")
		self.oHelper.SetValue("GI8_SUBSER","062")
		self.oHelper.SetValue("GI8_NUMCOM","001")
		self.oHelper.SetValue("GI8_NUMFIM","000005")
		self.oHelper.SetValue("GI8_DTFIM", "31/07/2020")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.WaitHide("Gerando lote de Documentos")
		self.oHelper.AssertTrue()
			
	@classmethod
	def tearDownClass(inst):
			inst.oHelper.TearDown()	

if __name__ == "__main__":
        unittest.main()
