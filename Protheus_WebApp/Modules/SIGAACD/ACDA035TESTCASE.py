#//-------------------------------------------------------------------
#/*/{Protheus.doc} ACDA035 - 										
#
#@author PEDRO ANTONIO MISSAGLIA
#@since 23/09/2019
#@version P12
#
# 	CT001 - Inclusão de Lançamento de Inventário
#	CT002 - Visão de um lançamento de inventário			
#	CT003 - Visualização das legendas
#	CT004 - Alteração de Lançamento de Inventário
#	CT005 - Exclusão de Lançamento de Inventário
#   CT007 - Alteração de Lançamento de Inventário sem finalizar contagem
#
#/*/
#//-------------------------------------------------------------------
from tir import Webapp
import unittest
import time

class ACDA035(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAEST','11/07/2019','T1','D MG 01')
		inst.oHelper.Program('ACDA035')	
		inst.oHelper.AddParameter("MV_CBPE012", "", ".T.", ".T.", ".T.")
		inst.oHelper.SetParameters()


	#CT001 - Geração de uma ordem de separação por ordem de produção		
	#@author: Pedro Antonio Missaglia
	#@date: 18/09/2019

	def test_ACDA035_CT001(self):

		self.oHelper.SetButton("Incluir")
		self.oHelper.SetButton('Ok')
		self.oHelper.SetValue('Codigo Inv.', '000000005')
		self.oHelper.SetValue('Usuario', '000010')
		self.oHelper.SetValue('Quantidade', '1', grid=True)
		self.oHelper.SetValue('Endereco', 'ENDSE01', grid=True)
		self.oHelper.LoadGrid()

		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Não')
		self.oHelper.SetButton('Cancelar')

		#Definição do operação
		
		self.oHelper.AssertTrue()

	def test_ACDA035_CT002(self):

		self.oHelper.SearchBrowse("D MG 01 000000003")
		self.oHelper.SetButton("Visão")
		self.oHelper.SetButton('Confirmar')
		
		self.oHelper.AssertTrue()

	def test_ACDA035_CT003(self):

		self.oHelper.SetButton("Outras Ações", "Legenda")
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Fechar')
		
		self.oHelper.AssertTrue()	

	def test_ACDA035_CT004(self):

		self.oHelper.SearchBrowse("D MG 01 000000030")
		self.oHelper.SetButton("Alterar")
		self.oHelper.SetValue('Quantidade', '3', grid=True)
		self.oHelper.LoadGrid()

		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Não')
		
		self.oHelper.AssertTrue()		
		
	def test_ACDA035_CT005(self):

		self.oHelper.SearchBrowse("D MG 01 000000005")
		self.oHelper.SetButton("Outras Ações", "Excluir")

		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Sim')
		
		self.oHelper.AssertTrue()

	def test_ACDA035_CT006(self):

		self.oHelper.AddParameter("MV_WMSNEW ", "", ".F.", ".T.", ".T.")
		self.oHelper.SetParameters()

		self.oHelper.SearchBrowse("D MG 01 000000029")
		self.oHelper.SetButton("Alterar")
		self.oHelper.SetValue('Qtd.Original', '3', grid=True)
		self.oHelper.LoadGrid()

		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Sim')
		
		self.oHelper.AssertTrue()			

	def test_ACDA035_CT007(self):

		self.oHelper.SearchBrowse("D MG 01 000000032")
		self.oHelper.SetButton("Alterar")
		self.oHelper.SetButton("Salvar")
		self.oHelper.WaitShow("Deseja finalizar a contagem?")
		self.oHelper.SetButton("Não")
		self.oHelper.WaitHide("Deseja finalizar a contagem?")
		time.sleep(3)
		self.oHelper.SetButton("Visão")
		self.oHelper.CheckResult("Produto","ACDACDA03500000000000000000001",grid=True, line=1)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton('Confirmar')

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()