from tir import Webapp
import unittest

class TMSA290(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGATMS','19/06/2019','T1','M SP 03 ','43')
		inst.oHelper.Program('TMSA290')  		

	def test_TMSA290_CT001(self):		
		  
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch('M SP 03')

		self.oHelper.SetValue('DU3_COMSEG','AA')
		self.oHelper.SetValue('DU3_DESCRI','TESTE AA')
		self.oHelper.SetValue('DU3_PRETPG','AAA')
		self.oHelper.SetValue('DU3_TIPTPG','PA')
		self.oHelper.SetValue('DU3_NATTPG','OUTROS')
		self.oHelper.SetValue('DU3_PREIND','001')
		self.oHelper.SetValue('DU3_TIPIND','01')
		self.oHelper.SetValue('DU3_NATIND','001')
		self.oHelper.SetValue('DU3_ATALHO','X')

		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse("M SP    AA")

		self.oHelper.SetButton("Visualizar")
		
		self.oHelper.CheckResult('DU3_COMSEG','AA')
		self.oHelper.CheckResult('DU3_DESCRI','TESTE AA')
		self.oHelper.CheckResult('DU3_PRETPG','AAA')
		self.oHelper.CheckResult('DU3_TIPTPG','PA')
		self.oHelper.CheckResult('DU3_NATTPG','OUTROS')
		self.oHelper.CheckResult('DU3_PREIND','001')
		self.oHelper.CheckResult('DU3_TIPIND','01')
		self.oHelper.CheckResult('DU3_NATIND','001')
		self.oHelper.CheckResult('DU3_ATALHO','X')
		
		self.oHelper.SetButton("Fechar")
		
		self.oHelper.AssertTrue()
		
	def test_TMSA290_CT002(self):

		self.oHelper.SearchBrowse("M SP    AA")

		self.oHelper.SetButton('Alterar')

		self.oHelper.SetValue('DU3_DESCRI', 'TESTE ABC123')

		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SetButton("Visualizar")
		
		self.oHelper.CheckResult('DU3_DESCRI', 'TESTE ABC123')
		
		self.oHelper.SetButton("Fechar")
		
		self.oHelper.AssertTrue()
		
	def test_TMSA290_CT003(self):

		self.oHelper.SearchBrowse("M SP    AA")

		self.oHelper.SetButton('Outras Ações', "Excluir")

		self.oHelper.SetButton("Confirmar")
		
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()

