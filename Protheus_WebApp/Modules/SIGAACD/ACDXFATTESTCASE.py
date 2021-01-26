from tir import Webapp
import time
import unittest

#//-------------------------------------------------------------------
#/*/{Protheus.doc} ACDXFAT - Integração ACD x Faturamento
#
#@author SQUAD Entradas
#@since 24/02/2020
#@version 0.1
#/*/
#//-------------------------------------------------------------------
class ACDXFAT(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		'''
		SETUP
		Test Case Initial Setup
		'''
		#Endereço do webapp e o nome do Browser
		inst.oHelper = Webapp()

		#Parametros de inicializacao
		inst.oHelper.Setup("SIGAFAT","06/03/2020","T1","D MG 01 ","05")

		#Nome da rotina do Caso de Teste
		inst.oHelper.Program("MATA460A")

	def test_ACDXFAT_001(self):
		
		#TIR001 - ACDXFAT - Faturamento parcial de Pedido de Venda com OS finalizada (Passo 1)
		#@author: SQUAD Entradas
		#@date: 09/03/2020

		self.oHelper.AddParameter('MV_INTACD', '', '1', '1', '1')
		self.oHelper.SetParameters()

		self.oHelper.SetValue("Filtra ja Emitid. ?           ", "Nao")
		self.oHelper.SetValue("Estorno da Liberc. ?          ", "Marcados")
		self.oHelper.SetValue("Cons. Param. Abaixo ?         ", "Sim")
		self.oHelper.SetValue("Trazer Ped. Marc. ?           ", "Nao")
		self.oHelper.SetValue("Pedido De ?                   ", "pcpAAF")
		self.oHelper.SetValue("Pedido Ate ?                  ", "pcpAAF")
		self.oHelper.SetValue("Cliente De ?                  ", "ESTSE1")
		self.oHelper.SetValue("Cliente Ate ?                 ", "ESTSE1")
		self.oHelper.SetValue("Loja Cliente De ?             ", "01")
		self.oHelper.SetValue("Loja Cliente Ate ?            ", "01")
		self.oHelper.SetValue("Data Liberacao De ?           ", "01/01/1999")
		self.oHelper.SetValue("Data Liberacao Ate ?          ", "31/12/2999")
		self.oHelper.SetValue("Mostrar Itens Previstos ?     ", "Não")
		self.oHelper.SetButton("Ok")
		self.oHelper.ClickBox("Produto", "ESTSE0000000000000000000000387")
		self.oHelper.SetButton("Prep. Doc's")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Ok")
		self.oHelper.WaitProcessing("Aguarde")
		self.oHelper.SetButton("Visualiza Doc.")
		self.oHelper.WaitShow("Notas Fiscais de Saida - VISUALIZAR")
		self.oHelper.CheckResult("Item", "01", True)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton("Cancelar")
		self.oHelper.SetButton("x")
		self.oHelper.AssertTrue()

	def test_ACDXFAT_002(self):

		#TIR001 - ACDXFAT - Faturamento parcial de Pedido de Venda com OS finalizada (Passo 2)
		#@author: SQUAD Entradas
		#@date: 09/03/2020

		time.sleep(10)
		self.oHelper.SetLateralMenu('Atualizações > Faturamento > Documentos de Saída')
		self.oHelper.SetButton("Ok")
		self.oHelper.ClickBox("Produto", "ESTSE0000000000000000000000386")
		self.oHelper.SetButton("Prep. Doc's")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton("Ok")
		self.oHelper.WaitShow("Pedido pcpAAF com ordem de separação 000029 não concluida")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("x")
		self.oHelper.AssertTrue()

	def test_ACDXFAT_003(self):

		#TIR001 - ACDXFAT - Faturamento parcial de Pedido de Venda com OS finalizada (Passo 3)
		#@author: SQUAD Entradas
		#@date: 09/03/2020

		time.sleep(10)
		self.oHelper.SetLateralMenu('Atualizações > Pedidos > Pedidos de Venda')
		self.oHelper.SearchBrowse("D MG 01 pcpAAJ")
		self.oHelper.SetButton("Outras Ações","Prep.Doc.saída")
		self.oHelper.WaitShow("Pedido pcpAAJ possui ordem(ns) de separação não concluida(s)")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("x")
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		'''
		Method that finishes the test case.
		'''
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()