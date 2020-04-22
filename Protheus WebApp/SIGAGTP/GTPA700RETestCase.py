from tir import Webapp
import unittest

class GTPA700RE(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAGTP", "30/03/2020", "T1", "D MG 01 ")
		inst.oHelper.Program('GTP700AMB')

	def test_GTPA700RE_CT001(self):

		self.oHelper.SetButton("Caixa Aberto")
		self.oHelper.SetButton("Caixa Fechado")
		self.oHelper.SearchBrowse("D MG    000008", "Filial+cod. Caixa")
		self.oHelper.ClickLabel("Reabrir Caixa")
		self.oHelper.SetButton("Ok")
		self.oHelper.LoadGrid()
		self.oHelper.AssertTrue()
	
	def test_GTPA700RE_CT002(self):

		self.oHelper.SetButton("Caixa Fechado")
		#self.oHelper.SetButton("Caixa Aberto")
		self.oHelper.SetButton("Caixa Reaberto")
		self.oHelper.SearchBrowse("D MG    000008", "Filial+cod. Caixa")
		self.oHelper.SetButton("Manutenção")

		self.oHelper.SetButton("Outras Ações","Fech.Caixa")
		
		self.oHelper.SetButton("Sim")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.WaitProcessing("Aguarde a Reabertura da ficha.")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Fechar")
		self.oHelper.LoadGrid()

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()
		

if __name__ == '__main__':
	unittest.main()
