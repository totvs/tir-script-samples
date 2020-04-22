from tir import Webapp
import unittest

#//-------------------------------------------------------------------
#/*/{Protheus.doc} DCLEA004 - Encerra Tanques
#
#@author pedro.missaglia
#@since 02/12/2019
#@version 1.0
#/*/
#//-------------------------------------------------------------------
class DCLEA004(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		'''
		SETUP
		Test Case Initial Setup
		'''
		#Endereco do webapp e o nome do Browser
		inst.oHelper = Webapp()

		#Parametros de inicializacao
		inst.oHelper.Setup("SIGAEST","17/10/2019","T1","D MG 01 ","04")

		#Nome da rotina do Caso de Teste
		inst.oHelper.Program("DCLEA004")

	def test_DCLEA004_001(self):
		
		#TIR001 - Inclusao simples de Mestre com Produto
		#@author: pedro.missaglia
		#@date: 02/12/2019

		self.oHelper.SetValue("Tanque Inicial.... ?", "000001")
		self.oHelper.SetValue("Tanque Final...... ?", "000001")
		self.oHelper.SetValue("Modo da Consulta.. ?", "Encerra Tanque")
		self.oHelper.SetValue("Impr.Observacoes.. ?", "Sim")
		
		self.oHelper.SetButton("Ok")

		self.oHelper.SetButton("Cancelar")

		self.oHelper.Program("DCLEA004")

		self.oHelper.AssertTrue()

	def test_DCLEA004_002(self):
		
		#TIR001 - Inclusao simples de Mestre com Produto
		#@author: pedro.missaglia
		#@date: 02/12/2019

		self.oHelper.SetValue("Tanque Inicial.... ?", "000001")
		self.oHelper.SetValue("Tanque Final...... ?", "000001")
		self.oHelper.SetValue("Modo da Consulta.. ?", "Relatorio Tanqu")
		self.oHelper.SetValue("Impr.Observacoes.. ?", "Sim")
		
		self.oHelper.SetButton("Ok")

		self.oHelper.SetButton("Cancelar")

		self.oHelper.AssertTrue()
	

	@classmethod
	def tearDownClass(inst):
		'''
		Method that finishes the test case.
		'''
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()