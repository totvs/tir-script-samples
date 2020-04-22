from tir import Webapp
import unittest
import time

#//-------------------------------------------------------------------
#/*/{Protheus.doc} MATA241 - Movimentacoes Multiplas
#TABELA SD3
#
#@author ADRIANO VIEIRA
#@since 11/10/2019
#@version 0.1
#/*/
#//-------------------------------------------------------------------
class MATA241(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		'''
		SETUP
		Test Case Initial Setup
		'''

		#Endereço do webapp e o nome do Browser
		inst.oHelper = Webapp()

		#Parametros de inicializacao
		inst.oHelper.Setup("SIGAEST","11/03/2020","T1","D MG 01 ","04")

		#Nome da rotina do Caso de Teste
		inst.oHelper.Program("MATA241")

	def test_MATA241_001(self):
		
		#TIR - Movimentacao Produto com Enderco e Cod. Barras
		#@author: ADRIANO VIEIRA
		#@date: 14/10/2019	

		self.oHelper.AddParameter("MV_CUSMED", "", "M", "M", "M")
		self.oHelper.SetParameters()

		self.oHelper.SetButton("Incluir")

		self.oHelper.SetBranch("D MG 01 ")

		self.oHelper.SetValue("Número Documento", "EST136")
		self.oHelper.SetValue("TM", "550")
		self.oHelper.SetValue("Centro de Custo", "ESTSE0001")
		
		self.oHelper.SetValue("Produto", "ESTSE0003000000000000000000346", grid=True)
		self.oHelper.SetValue("Quantidade","1,00", grid=True)
		self.oHelper.SetValue("Endereco","EST001", grid=True)
		self.oHelper.LoadGrid()
		
		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("Cancelar")

		self.oHelper.AssertTrue()

	def test_MATA241_002(self):
		
		#TIR - Estorno Simples
		#@author: ADRIANO VIEIRA
		#@date: 14/10/2019	

		self.oHelper.SearchBrowse("D MG 01 EST137",  key="Filial+documento + Produto")                                
		self.oHelper.SetButton('Outras Ações', "Estornar")
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Sim')

		self.oHelper.AssertTrue()
	
	def test_MATA241_003(self):
		
		#TIR - Visualizacao
		#@author: ADRIANO VIEIRA
		#@date: 14/10/2019	

		self.oHelper.SearchBrowse("D MG 01 EST138",  key="Filial+documento + Produto")                                
		self.oHelper.SetButton('Visualizar')
		self.oHelper.SetButton('Confirmar')

		self.oHelper.AssertTrue()
	
	def test_MATA241_004(self):
		
		#TIR - Requisicao para OP (Botao Outras Acoes)
		#@author: ADRIANO VIEIRA
		#@date: 14/10/2019	

		self.oHelper.SetButton("Incluir")

		self.oHelper.SetBranch("D MG 01 ")

		self.oHelper.SetValue("Número Documento", "EST139")
		self.oHelper.SetValue("TM", "550")
		self.oHelper.SetValue("Centro de Custo", "ESTSE0001")
		
		self.oHelper.SetValue("Produto", "ESTSE0000000000000000000000349", grid=True)   
		self.oHelper.SetValue("Quantidade","1,00", grid=True)
		self.oHelper.SetValue("Ord Producao","EST13901001", grid=True)
		self.oHelper.LoadGrid()
		
		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("Sim")
		self.oHelper.SetButton("Cancelar")

		self.oHelper.AssertTrue()
	
	def test_MATA241_005(self):
		
		#TIR - Visualizacao
		#@author: Nilton MK
		#@date: 11/03/2020	
	
		self.oHelper.SetButton("Incluir")

		self.oHelper.SetBranch("D MG 01 ")

		self.oHelper.SetValue("TM", "501")
		self.oHelper.SetValue("Produto", "ESTSE0000000000000000000000875", grid=True)   
		self.oHelper.SetValue("Quantidade","1,00", grid=True)
		self.oHelper.ClickGridCell("Produto", 1)
		self.oHelper.SetKey("DOWN", grid=True)
		self.oHelper.SetValue("Produto", "ESTSE0000000000000000000000875", grid=True)   
		self.oHelper.SetValue("Quantidade","1,00", grid=True) 
		self.oHelper.LoadGrid()
		self.oHelper.SetButton("Salvar")
		
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		'''
		Method that finishes the test case.
		'''
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()