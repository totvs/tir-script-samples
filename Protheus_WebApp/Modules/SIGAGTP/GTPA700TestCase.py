from tir import Webapp
import unittest

class GTPA700(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAGTP", "30/03/2020", "T1", "D MG 01 ")
		inst.oHelper.Program('GTP700AMB')

	def test_GTPA700_CT002(self):

		self.oHelper.SearchBrowse("D MG    000006", "Filial+cod. Caixa")
		self.oHelper.ClickLabel("Fechar Caixa")
		self.oHelper.WaitProcessing("Aguarde o fechamento do caixa.")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Sim")
		self.oHelper.SetButton("Ok")
		self.oHelper.LoadGrid()
		self.oHelper.AssertTrue()

	def test_GTPA700_CT003(self):

		self.oHelper.SearchBrowse("D MG    000014", "Filial+cod. Caixa")
		self.oHelper.ClickLabel("+ Vendas Cartão")
		self.oHelper.SetButton("Fechar")
		self.oHelper.LoadGrid()
		self.oHelper.AssertTrue()

	def test_GTPA700_CT004(self):

		self.oHelper.SearchBrowse("D MG    000014", "Filial+cod. Caixa")
		self.oHelper.ClickLabel("Fechar Caixa")
		self.oHelper.WaitProcessing("Aguarde o fechamento do caixa.")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Sim")
		self.oHelper.SetButton("Ok")
		self.oHelper.LoadGrid()
		self.oHelper.AssertTrue()

	def test_GTPA700_CT005(self):

		self.oHelper.SetButton("Caixa Aberto")
		self.oHelper.SetButton("Caixa Fechado")
		self.oHelper.SearchBrowse("D MG    000008", "Filial+cod. Caixa")
		self.oHelper.ClickLabel("Reabrir Caixa")
		self.oHelper.SetButton("Ok")
		self.oHelper.LoadGrid()
		self.oHelper.AssertTrue()
	
	def test_GTPA700_CT006(self):

		self.oHelper.SetButton("Caixa Fechado")
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

	def test_GTPA700_CT007(self):

		self.oHelper.SearchBrowse("D MG    000016", "Filial+cod. Caixa")
		self.oHelper.ClickLabel("+ Receitas")

		self.oHelper.SetButton("Fechar")
		self.oHelper.LoadGrid()

		self.oHelper.AssertTrue()
	
	def test_GTPA700_CT008(self):

		self.oHelper.SearchBrowse("D MG    000016", "Filial+cod. Caixa")
		self.oHelper.ClickLabel("+ Despesas")
		
		self.oHelper.SetButton("Fechar")
		self.oHelper.LoadGrid()

		self.oHelper.AssertTrue()
	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()
		

if __name__ == '__main__':
	unittest.main()
