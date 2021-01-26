#//-------------------------------------------------------------------
#/*/{Protheus.doc} MATA410EST - 
#/*/
#//-------------------------------------------------------------------
from tir import Webapp
from datetime import datetime
DataSystem = datetime.today().strftime('%d/%m/%Y')
import unittest

class MATA410EST(unittest.TestCase):

	
	@classmethod
	def setUpClass(inst):
		#Endereço do webapp e o nome do Browser
		inst.oHelper = Webapp()

		#Parametros de inicializaçao
		inst.oHelper.Setup("SIGAFAT",DataSystem,"T1","D MG 01 ","05")

		#Nome da rotina do Caso de Teste
		inst.oHelper.Program("MATA410")
	
	def test_MATA410EST_01(self):
		
		'''
			Inclusão de Pedido de Venda
		'''

		order = 'ESTSE1'

		self.oHelper.SetButton("Incluir")

		self.oHelper.SetBranch("D MG 01 ")

		self.oHelper.SetValue("C5_NUM", order)
		self.oHelper.SetValue("C5_TIPO","D")

		self.oHelper.SetValue("C5_CLIENTE","FORN01")
		self.oHelper.SetValue("C5_LOJACLI","01")
		self.oHelper.SetValue("C5_CONDPAG","000")

		self.oHelper.SetValue("Produto", "ESTSE00000000000000000024769PA", grid=True)
		self.oHelper.SetValue("Quantidade", "10,00", grid=True)
		self.oHelper.SetValue("Prc unitario", "1,00", grid=True)
		self.oHelper.SetValue("Qtd.Liberada", "10,00",grid=True)
		self.oHelper.SetValue("C6_TES", "599", grid=True)
		self.oHelper.LoadGrid()

		self.oHelper.SetFocus("N.F.Original", grid_cell=True, row_number=1)
		self.oHelper.SetKey("F4", grid=True)
		self.oHelper.LoadGrid()

		self.oHelper.WaitShow("Fornecedor/Loja: FORN01/01")
		self.oHelper.ClickGridCell("Documento", row=1)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton("Ok")
		self.oHelper.WaitHide("Fornecedor/Loja: FORN01/01")
		self.oHelper.SetKey("ENTER")

		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("Cancelar")
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()
