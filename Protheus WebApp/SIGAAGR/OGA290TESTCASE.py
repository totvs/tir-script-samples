from tir import Webapp
import unittest

class OGA290(unittest.TestCase):
	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAAGR','20/09/2019','T1','D MG 01 ','67')		
		inst.oHelper.Program('OGA290')
		inst.oHelper.AddParameter("MV_AGRA001","",".T.",".T.",".T.")#Novo UBA
		inst.oHelper.AddParameter("MV_AGRO002","",".T.",".T.",".T.")#Nova comercialização
		inst.oHelper.SetParameters()

	def test_OGA290_CT001(self): 
		
		self.oHelper.SearchBrowse("D MG 01 000069", key="Filial+contrato")
		self.oHelper.SetButton('Outras Ações', 'Gerar Previsão Financeira')									
		self.oHelper.WaitProcessing("Processando...")
		self.oHelper.SetButton('Visualizar')							
		self.oHelper.WaitShow("Contratos - VISUALIZAR")						
		self.oHelper.ClickFolder("Financeiro")		
		self.oHelper.CheckResult("NN7_VALOR", "139.624,70", grid=True, line=1)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton('Outras Ações', 'Demonstrativo de Preços')							
		self.oHelper.SetButton('Close')					
		self.oHelper.SetButton('Fechar')						
		self.oHelper.AssertTrue()
	
	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()