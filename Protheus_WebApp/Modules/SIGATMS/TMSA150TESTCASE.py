from tir import Webapp
import unittest
import datetime

class TMSA150(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		dataAtual = str(datetime.datetime.now().strftime("%d/%m,%Y"))
		inst.oHelper.Setup('SIGATMS',dataAtual,'T1','M SP 02 ','43')
		inst.oHelper.Program('TMSA150')

	def test_TMSA150_CT001(self):
		
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch('M SP 02')
		self.oHelper.SetValue('DUI_DOCTMS', 'M')
		self.oHelper.SetValue('DUI_SERIE','117')
		self.oHelper.SetValue('DUI_CODPRO','TMSICM120000000000000000000000')
	
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')
		
		self.oHelper.SearchBrowse(f'M SP 02 M')
		self.oHelper.SetButton('Visualizar')
		self.oHelper.CheckResult('DUI_DOCTMS', 'M')
		self.oHelper.CheckResult('DUI_SERIE','117')
		self.oHelper.CheckResult('DUI_CODPRO','TMSICM120000000000000000000000')
		self.oHelper.SetButton('Fechar')
		self.oHelper.AssertTrue()

	def test_TMSA150_CT002(self):
		
		self.oHelper.SearchBrowse(f'M SP 02 M')
		self.oHelper.SetButton('Visualizar')
		self.oHelper.CheckResult('DUI_DOCTMS', 'M')
		self.oHelper.CheckResult('DUI_SERIE','117')
		self.oHelper.CheckResult('DUI_CODPRO','TMSICM120000000000000000000000')
		self.oHelper.SetButton('Fechar')
		
		self.oHelper.SearchBrowse(f'M SP 02 M')
		self.oHelper.SetButton('Outras Ações','Excluir')
		self.oHelper.CheckResult('DUI_DOCTMS', 'M')
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


