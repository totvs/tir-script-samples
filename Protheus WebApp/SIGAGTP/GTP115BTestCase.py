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
		inst.oHelper.Program("GTPA421")

	def test_GTP115B_CT001(self):
		print("test_GTP115B_CT001")
	
		codigo = "AG950020200327"	
		self.oHelper.SearchBrowse("D MG    AG950020200327", key="Filial+agência + Número Ficha")		
		self.oHelper.SetButton("Outras Ações", "Conferência de Bilhetes")	
		time.sleep(6)
		
		self.oHelper.SetValue("Origem", "1")
		self.oHelper.SetValue("Tipo", "E")
		self.oHelper.SetValue("Status", "V")
		self.oHelper.SetButton("Pesquisar")
		self.oHelper.SetButton("Outras Ações", "Conferir Todos")

		time.sleep(5)
		self.oHelper.SetButton("Todos")
		time.sleep(3)
		self.oHelper.SetButton("Outras Ações", "Conferir Todos")
		time.sleep(3)
		self.oHelper.SetButton("Outras Ações", "Altera Contr. Docto.")
		self.oHelper.SetValue("Tipo de Documento ?", "TP9500")
		self.oHelper.SetValue("Série ?", "CDD")
		self.oHelper.SetValue("Sub Série ?", "500")
		self.oHelper.SetValue("Complemento ?", "009")
		self.oHelper.SetValue("Número Documento ?", "000001")
		self.oHelper.SetButton("OK")
		time.sleep(2)
		self.oHelper.SetKey("ENTER", grid=False)

		
		self.oHelper.SetKey("ENTER", grid=True)
		self.oHelper.ClickGridCell("CCF", 1)
		self.oHelper.SetKey("ENTER", grid=True)
		
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetKey("ENTER")
		self.oHelper.SetButton("Fechar")
		time.sleep(5)
			
		self.oHelper.AssertTrue()
		#self.oHelper.RestoreParameters()
		# 	

	def test_GTP115B_CT002(self):
		print("test_GTP115B_CT002")
	
		codigo = "AG950020200327"	
		self.oHelper.SearchBrowse("CAG950020200327", key="Filial+agência + Número Ficha")		
		self.oHelper.SetButton("Outras Ações", "Conferência de Bilhetes")	
		time.sleep(6)
		
		self.oHelper.SetButton("Todos")
		time.sleep(3)
		self.oHelper.SetButton("Outras Ações", "Conferir Todos")	
		time.sleep(2)
				
		self.oHelper.SetKey("ENTER", grid=True)
		self.oHelper.ClickGridCell("CCF", 1)
		self.oHelper.SetKey("ENTER", grid=True)

		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetKey("ENTER")
		self.oHelper.SetButton("Fechar")
		time.sleep(5)
			
		self.oHelper.AssertTrue()
		#self.oHelper.RestoreParameters()

	def test_GTP115B_CT003(self):
		print("test_GTP115B_CT003")
	
		codigo = "AG950020200327"	
		self.oHelper.SearchBrowse("D MG    00000120200227", key="Filial+agência + Número Ficha")		
		self.oHelper.SetButton("Outras Ações", "Conferência de Bilhetes")	
		time.sleep(4)				
		self.oHelper.SetKey("ENTER")
		self.oHelper.SetButton("Fechar")
		time.sleep(2)
			
		self.oHelper.AssertTrue()
		#self.oHelper.RestoreParameters()	
			
	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()
