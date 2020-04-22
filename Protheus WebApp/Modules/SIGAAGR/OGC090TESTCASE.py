from tir import Webapp
import unittest

class OGC090(unittest.TestCase):
	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAAGR','20/09/2019','T1','D MG 01 ','67')
		inst.oHelper.Program('OGC090')

	def test_OGC090_CT001(self):		
		self.oHelper.SetButton('Simular')				
		self.oHelper.ClickBox("Romaneio", select_all=True,  grid_number=1)		
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Fechar') #fecha mensagem		
        
		#Abre outro programa para conferir os dados de processamento. Aguardar equipe de Central de Automacao
		'''
		self.oHelper.Program('OGC110')
		self.oHelper.SetValue("MV_PAR01", "000065") #Ctr Ini
		self.oHelper.SetValue("MV_PAR02", "000065") #Ctr Fim
		self.oHelper.SetValue("MV_PAR05", "ZZZZZZ") #Corretor Ini
		self.oHelper.SetValue("MV_PAR06", "ZZ") 	#Corretor Fim
		self.oHelper.SetButton('OK')	
		self.oHelper.CheckResult("Valor", "9.841,33", grid=True, line=1)		
		self.oHelper.LoadGrid()
		'''
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()