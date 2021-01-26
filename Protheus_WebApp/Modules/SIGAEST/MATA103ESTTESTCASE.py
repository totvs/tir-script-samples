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
			
		self.oHelper.SetButton("Salvar")	
		self.oHelper.CheckHelp("A103USARF7")
		self.oHelper.SetButton("Cancelar")
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
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Cancelar')

		self.oHelper.AssertTrue()

	def test_MATA103EST_CT003(self):

		cod3 = 'ESTSE0000000000000000000000620'
		self.oHelper.AddParameter("MV_REQAUT", "","D","D","D")
		self.oHelper.AddParameter("MV_PRNFBEN", "","T","T","T")

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
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Cancelar')

		self.oHelper.AssertTrue()

	def test_MATA103EST_CT004(self):
		
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetValue("Tipo da Nota", "D")
		self.oHelper.SetValue("Form. Prop.", "Sim")
		self.oHelper.SetValue("Cliente", "ESTSE0")
		self.oHelper.SetValue("Espec.Docum.", "NFE")
		
		#Grid
		self.oHelper.SetValue("Produto", "ESTSE00000000000000000023764PA", grid=True)		
		self.oHelper.SetValue("Quantidade", "100,00", grid=True)
		self.oHelper.SetValue("Vlr.Unitario", "1,00", grid=True)
		self.oHelper.SetValue("Vlr.Total", "100,00", grid=True)
		self.oHelper.SetValue("Tipo Entrada", "001", grid=True)
		self.oHelper.LoadGrid()
		
		self.oHelper.SetButton('Outras Ações', 'Origem')
		time.sleep(2)
		self.oHelper.SetButton("OK")
		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("OK")
		self.oHelper.SetButton("Cancelar")
		self.oHelper.SetButton("X")
		self.oHelper.AssertTrue()

	def test_MATA103EST_CT005(self):
		
		self.oHelper.SetParameters()

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetButton('Ok')
		time.sleep(3)
		
		#Validacao da mensagem de fornecedor nao informado
		self.oHelper.SetButton('Outras Ações', 'Retorno Ben.')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Cancelar')
		
		#Validacao da mensagem de tipo de documento
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetValue("Tipo da Nota", "B")
		self.oHelper.SetValue("Form. Prop.", "Sim")
		self.oHelper.SetValue("Cliente", "EST001")
		self.oHelper.SetValue("Espec.Docum.", "NFE")
		self.oHelper.SetButton('Outras Ações', 'Retorno Ben.')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Cancelar')

		#Preenchimento correto das informações
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetValue("Tipo da Nota", "N")
		self.oHelper.SetValue("Form. Prop.", "Sim")
		self.oHelper.SetValue("Fornecedor", "EST001")
		self.oHelper.SetValue("Espec.Docum.", "NFE")
				
		#Grid
		self.oHelper.ClickGridCell("Produto",1)
		self.oHelper.SetValue("Produto", "ESTSE0000000000000000000000902", grid=True)
		self.oHelper.SetValue("Quantidade", "100,00", grid=True)
		self.oHelper.SetValue("Vlr.Unitario", "1,00", grid=True)
		self.oHelper.SetValue("Vlr.Total", "100,00", grid=True)
		self.oHelper.SetValue("Tipo Entrada", "009", grid=True)
		self.oHelper.LoadGrid()
		self.oHelper.SetKey("DELETE")
		self.oHelper.LoadGrid()
		self.oHelper.SetButton('Outras Ações', 'Retorno Ben.')

		#Validacao do assistente REGNOIS
		time.sleep(3)
		self.oHelper.SetKey("DOWN")
		self.oHelper.CheckHelp(text_help="REGNOIS",button="Fechar")

		#Nao foi identificado nenhuma remessa de beneficiamento para esta ordem de produção
		self.oHelper.SetFocus("Ord Producao")
		self.oHelper.SetKey("F3")
		self.oHelper.SearchBrowse("pcpA5P")
		self.oHelper.SetButton("Ok")
		time.sleep(3)
		self.oHelper.SetKey("DOWN")
		self.oHelper.SetKey("DOWN")
		self.oHelper.SetKey("F3")
		self.oHelper.SearchBrowse("292")
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Ok')
		time.sleep(3)
		self.oHelper.SetButton('Ok')

		#Validacao de ordem de produção encerrada
		self.oHelper.SetButton('Outras Ações', 'Retorno Ben.')
		self.oHelper.SetFocus("Ord Producao")
		self.oHelper.SetKey("F3")
		self.oHelper.SearchBrowse("pcpA5V")
		self.oHelper.SetButton("Ok")
		time.sleep(3)
		self.oHelper.SetKey("DOWN")
		self.oHelper.CheckHelp(text_help="MA240OPENC",button="Fechar")
		self.oHelper.SetFocus("Ord Producao")

		self.oHelper.SetKey("F3")
		self.oHelper.SearchBrowse("pcpA5U")
		self.oHelper.SetButton("Ok")
		time.sleep(3)
		self.oHelper.SetKey("DOWN")
		self.oHelper.SetKey("DOWN")

		#Validacao do help A103TPNFOR
		time.sleep(3)
		self.oHelper.SetKey("DOWN")
		self.oHelper.CheckHelp(text_help="A103TPNFOR",button="Fechar")

		#Validaca do help A103TESNFB
		time.sleep(3)
		self.oHelper.SetKey("F3")
		self.oHelper.SearchBrowse("009")
		self.oHelper.SetButton("Ok")
		time.sleep(3)
		self.oHelper.SetKey("DOWN")
		self.oHelper.CheckHelp(text_help="A103TESNFB",button="Fechar")

		time.sleep(3)
		self.oHelper.SetKey("F3")
		self.oHelper.SearchBrowse("292")
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Ok')
		time.sleep(3)
		self.oHelper.SetValue("Ord Producao", "pcpA5W01001", grid=True, grid_number=1,ignore_case=True,row=2)
		self.oHelper.LoadGrid()
		
		#Vincula novamente a ordem de produção
		self.oHelper.SetButton('Outras Ações', 'Retorno Ben.')
		self.oHelper.SetFocus("Ord Producao")
		self.oHelper.SetKey("F3")
		self.oHelper.SearchBrowse("pcpA5U")
		self.oHelper.SetButton('Ok')
		time.sleep(3)
		self.oHelper.SetKey("DOWN")
		self.oHelper.SetKey("DOWN")
		self.oHelper.SetKey("F3")
		self.oHelper.SearchBrowse("292")
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Ok')
		time.sleep(3)
		self.oHelper.SetButton('Cancelar')
		
		#Inclui a nota diretamente
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetButton('Ok')

		self.oHelper.SetValue("Tipo da Nota", "N")
		self.oHelper.SetValue("Form. Prop.", "Sim")
		self.oHelper.SetValue("Fornecedor", "EST001")
		self.oHelper.SetValue("Espec.Docum.", "NFE")

		self.oHelper.ClickGridCell("Produto",1)
		
		self.oHelper.SetButton('Outras Ações', 'Retorno Ben.')
		self.oHelper.SetFocus("Ord Producao")
		self.oHelper.SetKey("F3")
		self.oHelper.SearchBrowse("pcpA5U")
		self.oHelper.SetButton('Ok')
		time.sleep(3)
		self.oHelper.SetKey("DOWN")
		self.oHelper.SetKey("DOWN")
		self.oHelper.SetKey("F3")
		self.oHelper.SearchBrowse("292")
		time.sleep(3)
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Ok')

		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('X')
		
		self.oHelper.AssertTrue()

	def test_MATA103EST_CT007(self):
		cod2 = 'ESTSE0000000000000000000001003'
		self.oHelper.AddParameter("MV_TMPAD", "","010","010","010")
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
		self.oHelper.SearchBrowse("pcpA63")
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
		self.oHelper.SetButton('Cancelar')
		time.sleep(2)
		self.oHelper.SetButton('X')	

		self.oHelper.Program('MATA225')	
		self.oHelper.SearchBrowse(f"D MG 01 {cod2}")
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("B2_QATU", "3000,00")
		self.oHelper.SetButton("Cancelar")
		self.oHelper.SetButton("X")
		self.oHelper.Program('MATA103')

		self.oHelper.AssertTrue()

	def test_MATA103EST_CT008(self):
		self.oHelper.AddParameter("MV_TMPAD", "","010","010","010")
		self.oHelper.AddParameter("MV_PRNFBEN", "","T","T","T")
		self.oHelper.AddParameter("MV_EMPBN", "",".T.",".T.",".T.")
		
		self.oHelper.SearchBrowse("D MG 01 FIN903")
		self.oHelper.SetButton("Outras Ações","Excluir")
		self.oHelper.SetButton("Confirmar")

		self.oHelper.AssertTrue()	

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()