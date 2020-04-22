#//-------------------------------------------------------------------
#/*/{Protheus.doc} MATC070 - 
# 	CASO DE USO test_FIN001_CT001 - Inclusão de desmontagem:															
#	CASO DE USO test_FIN001_CT002 - Visualização de desmontagem.
#	CASO DE USO test_FIN001_CT003 - Estorno de Desmontagem.												
#	
#  - Seguintes recursos de tela: 1o Nivel, ShowF4. 
#  - Controle de Endereço, Controle de Rastro com Lote e Sub-Lote
#  - Informando uma porcentagem de rateio abaixo de 100%
#
#INCLUSÃO DE MOVIMENTACAÇÃO
#TABELA DE MOVIMENTAÇÃO SD3
#
#@author PEDRO ANTONIO MISSAGLIA
#@since 26/06/2019
#@version P12
#/*/
#//-------------------------------------------------------------------
from tir import Webapp
import unittest
import time

class MATC070(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAEST','21/06/2019','T1','D MG 01')
		inst.oHelper.Program('MATC070')
		#inst.oHelper.SetLateralMenu('Atualizações > Movimentações > Internas > Desmontagem')

	def test_MATC070_CT001(self):

		self.oHelper.SearchBrowse('D MG 01 ESTSE0000000000000000000000037')
		self.oHelper.SetButton('Consulta')
		self.oHelper.SetButton('Imprimir')
		self.oHelper.SetButton('Cancelar')
		self.oHelper.SetButton('Ordem')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Ok')
		self.oHelper.AssertTrue()



	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()
