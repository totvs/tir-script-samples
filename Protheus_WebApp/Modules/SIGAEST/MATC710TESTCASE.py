#//-------------------------------------------------------------------
#@author Jefferson silva de sousa
#@since 29/10/2019
#@version P12
#/*/
#//-------------------------------------------------------------------
from tir import Webapp
import unittest
import time

class MATC710(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAEST','29/10/2019','T1','D MG 01')
		inst.oHelper.Program('MATC710')		

	def test_MATC710_CT001(self):

		#self.oHelper.ClickTree("Estruturas / Produtos > ESTSE0000000000000000000000254 - ESTSE0000000000000000000000254")
		#self.oHelper.ClickTree("Estruturas / Produtos > ESTSE0000000000000000000000254 - ESTSE0000000000000000000000254", right_click=True)

		self.oHelper.ClickTree("ESTSE0000000000000000000000254 - ESTSE0000000000000000000000254")
		self.oHelper.ClickTree("ESTSE0000000000000000000000254 - ESTSE0000000000000000000000254", right_click=True)



		self.oHelper.ClickMenuPopUpItem("Detalhes do Saldo na Filial")		
		time.sleep(3)
		self.oHelper.SetButton("Voltar")		
		


		self.oHelper.ClickTree("ESTSE0000000000000000000000254 - ESTSE0000000000000000000000254", right_click=True)
		self.oHelper.ClickMenuPopUpItem("Expandir deste nível em diante")
		self.oHelper.ClickTree("ESTSE0000000000000000000000254 - ESTSE0000000000000000000000254 > ESTSE0000000001 - ESTSE0000000001")		
		time.sleep(3)
		self.oHelper.CheckResult("B1_DESC","ESTSE0000000001")
		self.oHelper.SetButton("Fechar")

		self.oHelper.AssertTrue()		


	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()