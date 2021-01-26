from tir import Webapp
import unittest

class TMSA090(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGATMS","27/05/2020","T1","M SP 03","43")
		inst.oHelper.Program("TMSA090")

	def test_TMSA090_CT001(self):
		self.oHelper.WaitShow("Destino de Calculo")
		
		self.oHelper.SetButton('Incluir')
		
		self.oHelper.SetBranch("M SP 03")
		
		self.oHelper.SetValue("DTH_CLIDEV","TMSPRE")
		self.oHelper.SetValue("DTH_LOJDEV","01")
		self.oHelper.SetValue("DTH_CDRDES","100013")
		self.oHelper.SetValue("DTH_CDRCAL","100054")
		self.oHelper.SetValue("DTH_ATIVO","1")
		
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		
		self.oHelper.SearchBrowse("M SP    TMSPRE01100013")
		
		self.oHelper.SetButton("Visualizar")

		self.oHelper.CheckResult("DTH_CLIDEV","TMSPRE")
		self.oHelper.CheckResult("DTH_LOJDEV","01")
		self.oHelper.CheckResult("DTH_CDRDES","100013")
		self.oHelper.CheckResult("DTH_CDRCAL","100054")
		self.oHelper.CheckResult("DTH_ATIVO", "1")
		
		self.oHelper.SetButton("Fechar")

		self.oHelper.AssertTrue()
	
	def test_TMSA090_CT002(self):
		
		self.oHelper.SearchBrowse("M SP    00000101100013")

		self.oHelper.SetButton("Alterar")

		self.oHelper.SetValue("Cod.Reg.Cal.","100104")
		self.oHelper.SetValue("Ativo","2")

		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")

		self.oHelper.SearchBrowse("M SP    00000101100013")

		self.oHelper.SetButton("Visualizar")

		self.oHelper.CheckResult("DTH_ATIVO", "2")

		self.oHelper.SetButton("Fechar")

		self.oHelper.AssertTrue()
	
	def test_TMSA090_CT003(self):
		
		self.oHelper.SearchBrowse("M SP    TMSPRE01100013")

		self.oHelper.SetButton('Outras Ações', 'Excluir')
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")


		self.oHelper.AssertTrue()
			
	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == "__main__":
	unittest.main()