from tir import Webapp
from datetime import datetime
DataSystem = datetime.today().strftime('%d/%m/%Y')
import unittest
import time

class GTP115(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		#inst.oHelper.SetTIRConfig(config_name="User", value="Admin")
		#inst.oHelper.SetTIRConfig(config_name="Password", value="1234")

        #Parametros de inicializaçao
		inst.oHelper.Setup("SIGAGTP", DataSystem,"T1","D MG 01 ","88")        

        #Nome da rotina do Caso de Teste
		inst.oHelper.Program("GTPA115")

	def test_GTP115_CT001(self):
		print("test_GTP115_CT001")
	
		self.oHelper.SearchBrowse("D MG    000041", key=4, index=True)	
		self.oHelper.SetButton("Outras Ações", "Excluir")	
		time.sleep(4)				
		self.oHelper.SetKey("ENTER")		
		time.sleep(2)
			
		self.oHelper.AssertTrue()
		#self.oHelper.RestoreParameters()	
			
	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()
