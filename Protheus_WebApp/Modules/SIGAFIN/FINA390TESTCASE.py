import unittest
import time
from tir import Webapp
from datetime import datetime

class FINA390(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAFIN","06/04/2020","T1","M SP 01 ","06")
		inst.oHelper.Program("FINA390")
	
	"""============================================================
	/*/{Protheus.doc} test_FINA390_CT006
	N�o preenchimento de algum campo obrigat�rio (Banco, Ag�ncia, Conta, Cheque, Natureza)
	por n�o passar no campo (os campos possuem valida��o caso n�o sejam preeenchidos)

	@author pequim
	@since 27/07/2020
	@version 1.0
	@See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T50157
	============================================================"""
	def test_FINA390_CT006(self):
		
		self.oHelper.SetButton("Cheque sobre títulos")

		#Posiciona no item da grid de seleção de DIC e simula um "Enter", para selecionar o item
		#O método de marcação de checkbox não funuciona aqui, por conta da janela de definição de valor que o FINA340 abre ao marcar o título.
		self.oHelper.SetValue('Banco','001')
		self.oHelper.SetValue('Fornecedor', 'TIR001')
		self.oHelper.SetValue('Natureza','PEQ001')

		#Clica em ok na tela de definição de valor a compensar para o título selecionado
		self.oHelper.SetButton("Ok")

		#Fecha o alerta indicando que não pode selecionar o DIC e fecha as demais telas.
		self.oHelper.CheckHelp(text_help="FA390ERRO1", button="Fechar")
		
		#Volta pra browse
		self.oHelper.SetButton("Cancelar")

		self.oHelper.AssertTrue()
	

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == "__main__":
	unittest.main()