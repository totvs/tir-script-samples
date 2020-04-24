from tir import Webapp
import unittest

class TMSA150(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGATMS','03/12/2019','T1','M SP 03 ','43')
		inst.oHelper.Program('TMSA150')

	def test_TMSA150_CT001(self):
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch('M SP 03')
		self.oHelper.SetValue('DUI_DOCTMS', 'K')
		self.oHelper.SetValue('DUI_SERIE','117')
		self.oHelper.SetValue('DUI_CODPRO','TMSICM120000000000000000000000')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')
		self.oHelper.SetButton('Visualizar')
		self.oHelper.CheckResult('DUI_DOCTMS', 'K')
		self.oHelper.CheckResult('DUI_SERIE','117')
		self.oHelper.CheckResult('DUI_CODPRO','TMSICM120000000000000000000000')
		self.oHelper.SetButton('Fechar')
		self.oHelper.AssertTrue()

	def test_TMSA150_CT002(self):
		
		self.oHelper.SearchBrowse('M SP 03 K')
		self.oHelper.SetButton('Visualizar')
		self.oHelper.CheckResult('DUI_DOCTMS', 'K')
		self.oHelper.CheckResult('DUI_SERIE','117')
		self.oHelper.CheckResult('DUI_CODPRO','TMSICM120000000000000000000000')
		self.oHelper.SetButton('Fechar')
		
		self.oHelper.SetButton('Outras Ações','Excluir')
		self.oHelper.CheckResult('DUI_DOCTMS', 'K')
		self.oHelper.CheckResult('DUI_SERIE','117')
		self.oHelper.CheckResult('DUI_CODPRO','TMSICM120000000000000000000000')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()


