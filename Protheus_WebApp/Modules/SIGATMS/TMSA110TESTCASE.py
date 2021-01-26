from tir import Webapp
import unittest

class TMSA110(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGATMS','19/06/2019','T1','M SP 03 ','43')
		inst.oHelper.Program('TMSA110')  		

	def test_TMSA110_CT001(self):		
		  
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch('M SP 03')

		self.oHelper.SetValue('DTJ_CNDREM','01')
		self.oHelper.SetValue('DTJ_CNDDES','02')
		self.oHelper.SetValue('DTJ_CNDCON','01')
		self.oHelper.SetValue('DTJ_CNDDEP','01')
		self.oHelper.SetValue('DTJ_PAGFRE', '1')

		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse("M SP    0102")

		self.oHelper.SetButton("Visualizar")
		
		self.oHelper.CheckResult("DTJ_CNDREM","01")
		self.oHelper.CheckResult("DTJ_CNDDES","02")
		self.oHelper.CheckResult("DTJ_CNDCON","01")
		self.oHelper.CheckResult("DTJ_CNDDEP","01")
		
		self.oHelper.SetButton("Fechar")
		
		self.oHelper.AssertTrue()
		
	def test_TMSA110_CT002(self):

		self.oHelper.SearchBrowse("M SP    0102")

		self.oHelper.SetButton('Alterar')

		self.oHelper.SetValue('DTJ_PAGFRE', '2')

		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SetButton("Visualizar")
		
		self.oHelper.SetValue("DTJ_CNDREM","01")
		self.oHelper.SetValue("DTJ_CNDDES","02")
		self.oHelper.SetValue("DTJ_CNDCON","01")
		self.oHelper.SetValue("DTJ_CNDDEP","01")
		self.oHelper.SetValue("DTJ_PAGFRE", '2')
		
		self.oHelper.SetButton("Fechar")
		
		self.oHelper.AssertTrue()
		
	def test_TMSA110_CT003(self):

		self.oHelper.SearchBrowse("M SP    0102")

		self.oHelper.SetButton('Outras Ações', "Excluir")

		self.oHelper.SetButton("Confirmar")
		
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()

