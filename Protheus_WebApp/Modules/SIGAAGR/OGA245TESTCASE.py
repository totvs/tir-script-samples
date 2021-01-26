from tir import Webapp
import unittest

class OGA245(unittest.TestCase):
	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAAGR','06/11/2019','T1','D MG 01 ','67')		
		inst.oHelper.Program('OGA245')		
	
	def test_OGA245_CT001(self): 	#estonar	
		
		self.oHelper.WaitShow("Ordens de Trânsito")		
		self.oHelper.SetKey("F12", grid=True)		
		self.oHelper.SetValue("cPar1","001", name_attr=True)
		self.oHelper.SetValue("cPar2","501", name_attr=True)
		self.oHelper.SetButton('Confirmar')			
		self.oHelper.SearchBrowse("D MG 01 000002", key="Filial+ordem Trans.")										
		self.oHelper.SetButton('Outras Ações', 'Estornar NFT')									
		self.oHelper.SetButton('Sim')									
		self.oHelper.WaitShow("Serie / Nota")
		self.oHelper.SetButton('Ok')									

		self.oHelper.SetButton('Visualizar')									
		self.oHelper.WaitHide("Ordens de Transito - VISUALIZAR")				
		self.oHelper.CheckResult("NK2_STATUS", "4", name_attr=True)								
		self.oHelper.SetButton("Fechar")
		self.oHelper.AssertTrue() 
	
	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()