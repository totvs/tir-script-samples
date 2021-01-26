#//-------------------------------------------------------------------
#/*/{Protheus.doc} MATR270 - 
#/*/
#//-------------------------------------------------------------------
from tir import Webapp
import unittest
import time

class MATR270(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAEST','30/09/2019','T1','D MG 01')
		inst.oHelper.Program('MATR270')

	def test_MATR270_CT001(self):
		
		self.oHelper.SetButton('Param.')
		self.oHelper.SetValue('Armazem de ?','01')
		self.oHelper.SetValue('Armazem ate ?','01')
		self.oHelper.SetValue('Produto de ?','')
		self.oHelper.SetValue('Produto ate ?','ZZZZZ')
		self.oHelper.SetValue('Tipo de ?','') 
		self.oHelper.SetValue('Tipo ate ?','ZZ')
		self.oHelper.SetValue('Grupo de ?','')
		self.oHelper.SetValue('Grupo ate ?','ZZZ')
		self.oHelper.SetValue('Descricao de ?','')
		self.oHelper.SetValue('Descricao ate ?','ZZZZZZ')
		self.oHelper.SetValue('Proximo Numero ?','123456')
		self.oHelper.SetValue('Data Selecao de ?','30/09/2019')
		self.oHelper.SetValue('Data Selecao ate ?','30/09/2019')
		self.oHelper.SetValue('Qual Ordem de Col. ?','123')
		self.oHelper.SetValue('Endereco De ?','')
		self.oHelper.SetValue('Endereco Ate ?','ZZZZZZ')
		self.oHelper.SetValue('Imprime etiqueta de produtos ?','Ambos')

		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Ok')		

		time.sleep(5)		
		self.oHelper.SetButton('sair')
		
		self.oHelper.AssertTrue()
		
	def test_MATR270_CT002(self):

		self.oHelper.Program('MATR270')
		self.oHelper.SetButton('Param.')
		self.oHelper.SetValue('Armazem de ?','01')
		self.oHelper.SetValue('Armazem ate ?','01')
		self.oHelper.SetValue('Produto de ?','ESTSE0000000000000000000023748')
		self.oHelper.SetValue('Produto ate ?','ESTSE0000000000000000000023748')
		self.oHelper.SetValue('Tipo de ?','')
		self.oHelper.SetValue('Tipo ate ?','ZZ')
		self.oHelper.SetValue('Grupo de ?','')
		self.oHelper.SetValue('Grupo ate ?','ZZZ')
		self.oHelper.SetValue('Descricao de ?','')
		self.oHelper.SetValue('Descricao ate ?','ZZZZZZ')
		self.oHelper.SetValue('Proximo Numero ?','123456')
		self.oHelper.SetValue('Data Selecao de ?','09/12/2019')
		self.oHelper.SetValue('Data Selecao ate ?','09/12/2019')
		self.oHelper.SetValue('Qual Ordem de Col. ?','123')
		self.oHelper.SetValue('Endereco De ?','')
		self.oHelper.SetValue('Endereco Ate ?','ZZZZZZ')
		self.oHelper.SetValue('Imprime etiqueta de produtos ?','Ambos')

		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Sim')

		time.sleep(5)		
		self.oHelper.SetButton('sair')
		
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()
