#//-------------------------------------------------------------------
#@author Jefferson Silva 
#@since 19/11/2019
#@version 1.00
#/*/
#//-------------------------------------------------------------------
from tir import Webapp
import unittest
import time

class MATA103(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAEST','19/11/2019','T1','D MG 01')
		inst.oHelper.Program('MATA103')		

	def test_MATA103EST_CT001(self):

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetButton('Ok')
		
		self.oHelper.SetValue("Form. Prop.", "Sim")
		self.oHelper.SetValue("Fornecedor", "EST001")
		self.oHelper.SetValue("Espec.Docum.", "NFE")
		
		#Grid
		self.oHelper.SetValue("Produto", "ESTSE0000000000000000000000365", grid=True)		
		self.oHelper.SetValue("Quantidade", "30,00", grid=True)
		self.oHelper.SetValue("Vlr.Unitario", "1,00", grid=True)
		self.oHelper.SetValue("Vlr.Total", "30,00", grid=True)
		self.oHelper.SetValue("Tipo Entrada", "052", grid=True)
		self.oHelper.SetValue("Cod. Fiscal", "1101", grid=True)	
		self.oHelper.SetValue("Docto. Orig.", "FIN449", grid=True)	
		self.oHelper.SetValue("Serie Orig.", "001", grid=True)
		self.oHelper.SetValue("It.Doc Orig.", "01", grid=True)				
		self.oHelper.LoadGrid()
		
		self.oHelper.SetKey("F7", grid=True)		
		self.oHelper.SetButton("OK")
		self.oHelper.CheckView("A103USARF7", element_type='help')
		

		if self.oHelper.CheckHelp("A103USARF7"):
			self.oHelper.AssertTrue()

			
		time.sleep(3)
		self.oHelper.ClickGridCell("Quantidade",1)
		self.oHelper.SetKey("DOWN",grid=True)
		self.oHelper.LoadGrid()
		#Grid
		self.oHelper.SetValue("Produto", "ESTSE0000000000000000000000365", grid=True,row=2)				
		self.oHelper.SetValue("Quantidade", "20,00", grid=True,row=2)
		self.oHelper.SetValue("Vlr.Unitario","1,00", grid=True,row=2)
		self.oHelper.SetValue("Vlr.Total", "20,00", grid=True,row=2)
		self.oHelper.SetValue("Tipo Entrada", "052", grid=True,row=2)
		self.oHelper.SetValue("Cod. Fiscal", "1101", grid=True,row=2)	
		self.oHelper.SetValue("Docto. Orig.", "FIN449", grid=True,row=2)	
		self.oHelper.SetValue("Serie Orig.", "001", grid=True,row=2)
		self.oHelper.SetValue("It.Doc Orig.", "02", grid=True,row=2)			
		self.oHelper.LoadGrid()
		time.sleep(4)
		#Origem 
		
		self.oHelper.SetKey("F7")
		time.sleep(4)		
		self.oHelper.SetButton("OK")
		self.oHelper.CheckView("A103USARF7", element_type='help')

		if self.oHelper.CheckHelp("A103USARF7"):
			self.oHelper.AssertTrue()
		
		self.oHelper.SetButton("Salvar")
		time.sleep(2)	
		self.oHelper.SetButton("OK")
		
		self.oHelper.AssertTrue()

	def test_MATA103EST_CT002(self):

		cod2 = 'ESTSE0000000000000000000000616'
		self.oHelper.AddParameter("MV_TMPAD", "","393","393","393")
		self.oHelper.AddParameter("MV_PRNFBEN", "","T","T","T")
		self.oHelper.AddParameter("MV_EMPBN", "",".T.",".T.",".T.")

		self.oHelper.SetParameters()

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetButton('Ok')
		
		self.oHelper.SetValue("Form. Prop.", "Sim")
		self.oHelper.SetValue("Fornecedor", "EST001")
		self.oHelper.SetValue("Espec.Docum.", "NFE")
		self.oHelper.SetKey("F2")	
		
		#Grid
		self.oHelper.SetButton('Outras Ações', 'Retorno Ben.')
		self.oHelper.SetFocus("Ord Producao")
		self.oHelper.SetKey("F3")
		self.oHelper.SearchBrowse("pcpA31")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetFocus("Ord Producao")
		self.oHelper.SetKey("DOWN")
		self.oHelper.SetKey("DOWN")

		self.oHelper.SetKey("F3")
		self.oHelper.SearchBrowse("292")
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Ok')
		time.sleep(3)
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('X')
		self.oHelper.SetButton('X')	

		self.oHelper.Program('MATA225')	
		self.oHelper.SearchBrowse(f"D MG 01 {cod2}")
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("B2_QATU", "0,00")
		self.oHelper.SetButton("Cancelar")
		self.oHelper.SetButton("X")
		self.oHelper.Program('MATA103')

		self.oHelper.AssertTrue()

	def test_MATA103EST_CT003(self):

		cod3 = 'ESTSE0000000000000000000000620'
		self.oHelper.AddParameter("MV_REQAUT", "","D","D","D")

		self.oHelper.SetParameters()

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetButton('Ok')
		
		self.oHelper.SetValue("Form. Prop.", "Sim")
		self.oHelper.SetValue("Fornecedor", "EST001")
		self.oHelper.SetValue("Espec.Docum.", "NFE")
		self.oHelper.SetKey("F2")	
		
		#Grid
		self.oHelper.SetButton('Outras Ações', 'Retorno Ben.')
		self.oHelper.SetFocus("Ord Producao")
		self.oHelper.SetKey("F3")
		self.oHelper.SearchBrowse("pcpA32")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetFocus("Ord Producao")
		self.oHelper.SetKey("DOWN")
		self.oHelper.SetKey("DOWN")

		self.oHelper.SetKey("F3")
		self.oHelper.SearchBrowse("292")
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Ok')
		time.sleep(3)
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('X')
		self.oHelper.SetButton('X')	

		self.oHelper.Program('MATA225')	
		self.oHelper.SearchBrowse(f"D MG 01 {cod3}")
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("B2_QATU", "1,00")
		self.oHelper.SetButton("Cancelar")
		self.oHelper.SetButton("X")
		self.oHelper.Program('MATA103')

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()