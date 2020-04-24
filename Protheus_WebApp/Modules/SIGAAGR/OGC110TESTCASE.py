from tir import Webapp
import unittest

class OGC110(unittest.TestCase):
	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAAGR','20/09/2019','T1','D MG 01 ','67')		
		inst.oHelper.Program('OGC110')
		
		inst.oHelper.AddParameter("MV_AGRO016","","001","001","001")#Parametro grupo aprovação alçada
		inst.oHelper.AddParameter("MV_AGRO020","","001","001","001")#Parametro TES entrada
		inst.oHelper.AddParameter("MV_AGRO021","","PROD002","PROD002","PROD002") #Parâmetro código do produto serviço
		inst.oHelper.AddParameter("MV_AGRO022","","001","001","001") #Parâmetro Condição de pagamento
		inst.oHelper.SetParameters()
		

	def test_OGC110_CT001(self): #confirma comissão e gera pedido						        		
		
		
		self.oHelper.SetValue("MV_PAR01", "000066") #Ctr Ini
		self.oHelper.SetValue("MV_PAR02", "000066") #Ctr Fim
		self.oHelper.SetValue("MV_PAR05", "ZZZZZZ") #Corretor Ini
		self.oHelper.SetValue("MV_PAR06", "ZZ") 	#Corretor Fim
		self.oHelper.SetButton('OK')	
		
		self.oHelper.SetButton('Detalhes')			
		self.oHelper.SetButton('Outras Ações', 'Incluir')	
		self.oHelper.SetValue("Vl. Comissão",  "200,00")
		self.oHelper.SetValue("Tx. Calculo", "1,000000")
		self.oHelper.SetButton('Confirmar')		
		self.oHelper.SetButton('Fechar')		
		self.oHelper.SetButton('Outras Ações', 'Alterar')	
		self.oHelper.SetValue("N89_VRCALC", "220,00")
		self.oHelper.SetButton('Confirmar')		
		self.oHelper.SetButton('Fechar')		
		self.oHelper.SetButton('Outras Ações', 'Excluir')	
		self.oHelper.SetButton('Confirmar')		
		self.oHelper.SetButton('Fechar')		
		self.oHelper.SetButton('Fechar')		

		self.oHelper.ClickGridCell("Contrato", row=1, grid_number=1)
		self.oHelper.SetButton('Confirmar Comissão')	
		self.oHelper.SetButton('Fechar')			
		self.oHelper.SetButton('Outras Ações', 'Gerar Pedido')	
		self.oHelper.WaitProcessing("Processando")		
		self.oHelper.SetButton('Fechar')		
		self.oHelper.SetButton('Detalhes')			
		self.oHelper.ClickGridCell("Pedido", row=1, grid_number=1)	
		pedido = self.oHelper.GetValue("Pedido", grid=True, line=1, grid_number=1)
		if pedido == "    ":
			self.oHelper.AssertFalse()	
		else:
			self.oHelper.AssertTrue()	
		self.oHelper.SetButton('Fechar')			

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()