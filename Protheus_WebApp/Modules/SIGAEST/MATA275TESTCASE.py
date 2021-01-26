#//-------------------------------------------------------------------
#/*/{Protheus.doc} MATA275
#
#@author jefferson silva de sousa 
#@since 03/12/2020
#@version P12
#/*/
#//-------------------------------------------------------------------
from tir import Webapp
import unittest
import time

class MATA275(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAEST","03/12/2020","T1","D MG 01")
		inst.oHelper.Program("MATA275")

	# Inclusão de bloqueio de lote automaçao fonte sigacus
	def test_MAT275_001(self):

		self.oHelper.SetButton("Bloquear")
		self.oHelper.SetButton("OK")
		self.oHelper.SetValue("Documento","X01")
		self.oHelper.SetValue("Produto","ESTSE0000000000000000000000339")
		self.oHelper.SetValue("Armazem","01")
		self.oHelper.SetFocus("Lote")
		self.oHelper.SetKey("F4")
		self.oHelper.SetButton("OK")
		self.oHelper.SetValue("Quantidade", "100,00")
		self.oHelper.SetValue("Motivo", "ND")		
		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("Cancelar")

		self.oHelper.AssertTrue()
	
	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()