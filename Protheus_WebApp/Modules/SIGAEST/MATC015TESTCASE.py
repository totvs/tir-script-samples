#//-------------------------------------------------------------------
#@author PEDRO ANTONIO MISSAGLIA
#@since 26/06/2019
#@version P12
#/*/
#//-------------------------------------------------------------------
from tir import Webapp
import unittest
import time

class MATC015(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAEST','21/06/2019','T1','D MG 01')
		inst.oHelper.Program('MATC015')		

	def test_MATC015_CT001(self):

		self.oHelper.SetButton('Ok')
		self.oHelper.SearchBrowse('D MG 01 ESTSE0000000000000000000000212')
		self.oHelper.SetButton('POsicionado')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.AssertTrue()
	def test_MATC015_CT002(self):

		#self.oHelper.SetButton('Ok')
		self.oHelper.SearchBrowse('D MG 01 ESTSE0000000000000000000000212')
		self.oHelper.SetButton('POsicionado')

		self.oHelper.ClickTree('ESTSE0000000000000000000000212 - ESTSE0000000000000000000000212 > Roteiros de Operacao')	
		time.sleep(2)
		self.oHelper.ClickTree('ESTSE0000000000000000000000212 - ESTSE0000000000000000000000212 > Ordens de Producao')	
		time.sleep(2)
		self.oHelper.ClickTree('ESTSE0000000000000000000000212 - ESTSE0000000000000000000000212 > Estruturas')	
		time.sleep(2)
		self.oHelper.ClickTree('ESTSE0000000000000000000000212 - ESTSE0000000000000000000000212 > Estruturas > Revisão')	
		time.sleep(2)
		self.oHelper.ClickTree('ESTSE0000000000000000000000212 - ESTSE0000000000000000000000212 > Painel de custos')	
		time.sleep(2)

		self.oHelper.SetButton('Confirmar')
		self.oHelper.AssertTrue()


	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()