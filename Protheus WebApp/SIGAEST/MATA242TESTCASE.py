#//-------------------------------------------------------------------
#/*/{Protheus.doc} MATA242 - 
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

class MATA242(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAEST','21/06/2019','T1','D MG 01')
		inst.oHelper.Program('MATA242')
		#inst.oHelper.SetLateralMenu('Atualizações > Movimentações > Internas > Desmontagem')

	def test_MATA242_CT001(self):

		self.oHelper.AddParameter("MV_CUSMED", "", "O", "O", "O")
		self.oHelper.SetParameters()

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetValue('Produto Origem','ESTSE0000000000000000000000215')
		self.oHelper.SetValue('Armazem','01')
		self.oHelper.SetValue('Endereco','ENDSE01')
		
		self.oHelper.SetKey("F4")
		time.sleep(3)
		self.oHelper.SetButton('Ok')
		#self.oHelper.SetValue('Lote','LT01')
		#self.oHelper.SetValue('Sub-Lote','LT01')

		self.oHelper.SetValue('Quantidade','1,00')
		self.oHelper.SetValue('Data','21/06/2019')
		self.oHelper.SetValue('Documento','ESTSE0005')


		self.oHelper.SetButton('Outras Ações', '1o.Nivel')

		self.oHelper.SetValue("Produto", "ESTSE0000000000000000000000216", grid=True)
		self.oHelper.SetValue("Quantidade", "1,00", grid=True)
		self.oHelper.SetValue("% Rateio", "20,00", grid=True)
		self.oHelper.SetValue("Lote", "LT01", grid=True)
		self.oHelper.SetValue("Endereco", "ENDSE01", grid=True)
		self.oHelper.LoadGrid()
		
		self.oHelper.ClickGridCell("Produto", 2)

		self.oHelper.SetValue("Produto", "ESTSE0000000000000000000000217", grid=True)
		self.oHelper.SetValue("Quantidade", "2,00", grid=True)
		self.oHelper.SetValue("% Rateio", "50,00", grid=True)
		self.oHelper.SetValue("Lote", "LT01", grid=True)
		self.oHelper.SetValue("Endereco", "ENDSE01", grid=True)
		self.oHelper.LoadGrid()

		self.oHelper.SetButton('Salvar')
		time.sleep(10)
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Cancelar')
		self.oHelper.AssertTrue()
	
	def test_MATA242_CT002(self):
		filial    = "D MG 01 "
		documento = "ESTSE0006"
		produto   = "ESTSE0000000000000000000000218" 

		#Verificação de Inclusão		
		self.oHelper.SearchBrowse(f"{filial}{documento}{produto}", "Filial+documento + Produto")
		self.oHelper.SetButton('Visualizar')
		self.oHelper.SetButton('Cancelar')
		self.oHelper.AssertTrue()

	def test_MATA242_CT003(self):
		filial    = "D MG 01 "
		documento = "ESTSE0007"
		produto   = "ESTSE0000000000000000000000221"

		self.oHelper.SearchBrowse(f"{filial}{documento}{produto}", "Filial+documento + Produto")
		self.oHelper.SetButton('Outras Ações', 'Estornar')
		time.sleep(3)	
		self.oHelper.SetButton('Confirmar')				
		self.oHelper.AssertTrue()

	def test_MATA242_CT004(self):
		
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetValue("Produto Origem","ESTSE0000000000000000000000250")
		self.oHelper.SetValue("Armazem","01")
		time.sleep(2)
		self.oHelper.SetValue("Quantidade","1,00")
		self.oHelper.SetValue("Documento","MT242TST")
		self.oHelper.SetButton("Outras Ações", "1o.Nivel")		
		self.oHelper.SetButton("Salvar")
	
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()
	