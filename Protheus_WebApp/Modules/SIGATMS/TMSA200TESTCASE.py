from tir import Webapp
import unittest

class TMSA200(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		
		inst.oHelper.Setup('SIGATMS','07/10/2019','T1','M SP 01 ','43')
		inst.oHelper.Program('TMSA200')

	# CT007 - Cálculo de Lote com configurações para gerar "Bloqueio de crédito"
	def test_TMSA200_CT007(self):

		self.oHelper.SearchBrowse("M SP    000086")
		self.oHelper.SetButton('Outras Ações', 'Recalculo')

		self.oHelper.SetButton('Ok')
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()