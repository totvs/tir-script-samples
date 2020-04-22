#//-------------------------------------------------------------------
#/*/{Protheus.doc} MATA240 - 										
#
#@author PEDRO ANTONIO MISSAGLIA
#@since 11/07/2019
#@version P12
#/*/
#//-------------------------------------------------------------------
from tir import Webapp
import unittest
import time

class MATA240(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAEST','11/07/2019','T1','D MG 01')
		inst.oHelper.Program('MATA240')		

	def test_MATA240_CT001(self):

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetValue('TP Movimento','501')
		self.oHelper.SetValue('Produto','ESTSE0000000000000000000000332')
		self.oHelper.SetValue('Quantidade','12,00')
		self.oHelper.SetValue('Documento','ESTEA001')
		self.oHelper.SetValue('DT Emissao', '01/10/2019')

		self.oHelper.SetFocus('Lote')
		self.oHelper.SetValue('Lote', 'LT01')

		self.oHelper.SetFocus('Endereco')
		self.oHelper.SetValue('Endereco', 'ENDSE01')
	
		self.oHelper.SetButton('Outras Ações','R.Frota')
		self.oHelper.SetValue('Codigo da Despesa', '01')
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Cancelar')	

		self.oHelper.AssertTrue()

	def test_MATA240_CT002(self):	
   
		self.oHelper.SearchBrowse("D MG 01 ESTEA001",  key="Filial+documento + Produto")                           
		self.oHelper.SetButton('Visualizar')
		self.oHelper.SetButton('Confirmar')

		self.oHelper.AssertTrue()

	def test_MATA240_CT004(self):	
   
		self.oHelper.SearchBrowse("D MG 01 ESTEA001",  key="Filial+documento + Produto")                                
		self.oHelper.SetButton('Outras Ações', "Estornar")
		self.oHelper.SetButton('Confirmar')

		self.oHelper.AssertTrue()	

	def test_MATA240_CT005(self):	
                                 
		self.oHelper.SetButton('Outras Ações', "Legenda")
		self.oHelper.SetButton('Fechar')

		self.oHelper.AssertTrue()		



	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()