from tir import Webapp
import unittest

#//-------------------------------------------------------------------
#/*/{Protheus.doc} ACDI011 - Wizard de Etiquetas
#
#@author SQUAD Entradas
#@since 24/02/2020
#@version 0.1
#/*/
#//-------------------------------------------------------------------
class ACDI011(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		'''
		SETUP
		Test Case Initial Setup
		'''
		#Endereço do webapp e o nome do Browser
		inst.oHelper = Webapp()

		#Parametros de inicializacao
		inst.oHelper.Setup("SIGAEST","24/02/2020","T1","D MG 01 ","04")

		#Nome da rotina do Caso de Teste
		inst.oHelper.Program("ACDI011")

		inst.oHelper.AddParameter("MV_VLDLOTE", "", ".F.", ".F.", ".F.")
		inst.oHelper.SetParameters()

	def test_ACDI011_001(self):
		
		#TIR001 - ACDI011 - Preenchimento das informações de Endereço do Produto com F4 (Parte 1)
		#@author: SQUAD Entradas
		#@date: 24/02/2020

		self.oHelper.SetButton("Avançar")
		self.oHelper.SetValue("Produto", True)
		self.oHelper.SetButton("Avançar")
		self.oHelper.SetValue("Produto", "ESTSE0000000000000000000000384")
		self.oHelper.SetButton("Avançar")
		self.oHelper.ClickBox("Produto", "ESTSE0000000000000000000000384")
		self.oHelper.SetButton("Alterar")
		self.oHelper.SetValue("Quantidade ? ", "1,00")
		self.oHelper.SetValue("Armazém ? ", "01")
		self.oHelper.SetValue("Lote ? ", "ABC")
		self.oHelper.SetValue("Data de validade ? ", "31/12/2999")
		self.oHelper.SetFocus("Endereço ?")
		self.oHelper.SetKey("F4")
		self.oHelper.SetButton("Ok")
		self.oHelper.CheckResult("Quantidade ? ","1000")

		self.oHelper.AssertTrue()

	def test_ACDI011_002(self):
		
		#TIR002 - ACDI011 - Preenchimento das informações de Endereço do Produto com F4 (Parte 2)
		#@author: SQUAD Entradas
		#@date: 24/02/2020

		self.oHelper.SetButton("Cancelar")
		self.oHelper.SetButton("Alterar")
		self.oHelper.SetValue("Quantidade ? ", "0,00")
		self.oHelper.SetValue("Armazém ? ", "01")
		self.oHelper.SetValue("Lote ? ", "ABC")
		self.oHelper.SetValue("Data de validade ? ", "31/12/2999")
		self.oHelper.SetFocus("Endereço ?")
		self.oHelper.SetKey("F4")
		self.oHelper.SetButton("Ok")
		self.oHelper.CheckResult("Quantidade ? ","1000.00")

		self.oHelper.AssertTrue()

	def test_ACDI011_003(self):
		
		#TIR003 - ACDI011 - Impressão de etiquetas quando possui resto
		#@author: SQUAD Entradas
		#@date: 04/05/2020

		self.oHelper.SetButton("Cancelar")
		self.oHelper.SetButton("Voltar")
		self.oHelper.SetValue("Produto", "ESTSE0000000000000000000000725")
		self.oHelper.SetButton("Avançar")
		self.oHelper.ClickBox("Produto", "ESTSE0000000000000000000000725")
		self.oHelper.SetButton("Alterar")
		self.oHelper.SetValue("Quantidade ? ", "1,00")
		self.oHelper.SetValue("Qtd por Embalagem ? ", "10,00")
		self.oHelper.SetValue("Armazém ? ", "01")
		self.oHelper.SetKey("F4")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Avançar")
		self.oHelper.SetValue("Local de Impressão ? ", "000001")
		self.oHelper.SetButton("Avançar")
		self.oHelper.SetButton("Sim")

		self.oHelper.AssertTrue()		

	@classmethod
	def tearDownClass(inst):
		'''
		Method that finishes the test case.
		'''
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()