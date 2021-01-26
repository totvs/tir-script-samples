#//-------------------------------------------------------------------
#/*/{Protheus.doc} MATR445 - 
#/*/
#//-------------------------------------------------------------------
from tir import Webapp
import unittest
import time

class MATR445(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAEST','14/11/2019','T1','D MG 01')
		inst.oHelper.Program('MATR445')
	
	#CT001 Verifica se o bloqueio de periodo maior que 4095 dias esta funcionando ok 
	def test_MATR445_CT001(self):

		time.sleep(2)
		self.oHelper.SetButton('Outras Ações', 'Parâmetros')
		self.oHelper.SetValue('Periodo de ?','01/01/2000')
		self.oHelper.SetValue('Periodo ate ?','31/12/2020')
		self.oHelper.SetKey("DOWN")		
		self.oHelper.CheckHelp(text_help="R4096DIAS", button="Fechar")
		time.sleep(5)		
		self.oHelper.SetValue('Periodo ate ?','31/12/2000')
		self.oHelper.SetButton('Cancelar')
		
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()
