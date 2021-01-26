#//-------------------------------------------------------------------
#/*/{Protheus.doc} MATA261 - 										
#
#@author PEDRO ANTONIO MISSAGLIA
#@since 11/07/2019
#@version P12
#/*/
#//-------------------------------------------------------------------
from tir import Webapp
import unittest
import time

class MATA261(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		#inst.oHelper.Setup('SIGAEST','10/10/2019','T1','D MG 01')
	    #inst.oHelper.Program('MATA261')
		inst.oHelper.Setup("SIGAADV","10/10/2019","T1","D MG 01 ","04")		
		inst.oHelper.SetLateralMenu('Atualizações > Movimentações > Internas > Transferência Múltipla')

	# def test_MATA261_CT001(self):

	# 	self.oHelper.SetButton('Incluir')
	# 	self.oHelper.SetButton('Ok')
	# 	self.oHelper.SetValue('Numero Documento','ESTA1Z001')
	# 	self.oHelper.SetValue('Emissäo','11/10/2019')
	# 	self.oHelper.SetValue('Prod.Orig.','PA01', grid=True)
	# 	self.oHelper.SetValue('Armazem Destino','02', grid=True)
	# 	self.oHelper.SetValue('Quantidade','12,00', grid=True)

	# 	self.oHelper.SetButton('Salvar')

	# 	self.oHelper.AssertTrue()

	def test_MATA261_CT002(self):
		self.oHelper.SearchBrowse('D MG 01 pcpA1Z001',key='Filial+documento + Produto')
		self.oHelper.SetButton('Visualizar')
		self.oHelper.SetButton('Confirmar')

		self.oHelper.AssertTrue()

	def test_MATA261_CT003(self):

		self.oHelper.SetButton('Outras Ações', 'Legenda')
		self.oHelper.SetButton('Fechar')

		self.oHelper.AssertTrue()

	def test_MATA261_CT004(self):
		
		self.oHelper.SearchBrowse('D MG 01 pcpA1Z001')
		self.oHelper.SetButton('Outras Ações', 'Estornar')
		self.oHelper.SetButton('Confirmar')

		self.oHelper.AssertTrue()		


	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()