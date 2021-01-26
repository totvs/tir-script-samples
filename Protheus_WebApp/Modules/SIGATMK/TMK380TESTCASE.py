from tir import Webapp
from datetime import datetime, timedelta 
import time
import unittest

class TMKA380(unittest.TestCase):

	@classmethod
	def setUpClass(self):

		self.oHelper = Webapp(autostart=False)
		self.oHelper.SetTIRConfig(config_name="User", value="televendas") 
		self.oHelper.SetTIRConfig(config_name="Password", value="1")
	
	def test_TMKA380_CT005(self):

		# Inicia o novo Webapp para logar com o User no Módulo
		self.oHelper.Start()
		self.oHelper.Setup("SIGATMK","01/04/2020","T1","D MG 01  ","13")
		self.oHelper.Program("TMKA380")
		# Posiciona o Atendimento: 000024
		self.oHelper.ClickGridCell("Nome", row=2)
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("Sim")
		self.oHelper.SetValue("UA_OPER","1 - Faturamento")
		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Sim")
		self.oHelper.SetButton("Cancela")
		self.oHelper.SetButton("Cancelar")
		self.oHelper.SetButton("Sim")

		self.oHelper.AssertTrue()
			
	def test_TMKA380_CT006(self):
		
		# Posiciona o Atendimento: 000025
		self.oHelper.ClickGridCell("Nome", row=1)	
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("Sim")
		self.oHelper.SetValue("UA_OBS","Teste")
		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("Ok")
		self.oHelper.ClickGridCell("Tipo", row=4)
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Cancela")
		self.oHelper.SetButton("Cancelar")
		self.oHelper.SetButton("Sim")
		self.oHelper.SetButton("Cancelar")

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(self):
 
		'''self.oHelper.TearDown()
		self.oHelper2.TearDown()
		self.oHelper3.TearDown()'''
		
	
if __name__ == '__main__':
	unittest.main()