from tir import Webapp
import unittest

class FINA340(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAFIN","06/04/2020","T1","M SP 01 ","06")
		inst.oHelper.Program("FINA340")
	
	"""============================================================
	/*/{Protheus.doc} test_FINA340_CT043
	Seleção de título (DIC com valor maior do que o saldo da NF)

	@author pedro.alencar
	@since 06/04/2020
	@version 1.0
	@See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T50157
	============================================================"""
	def test_FINA340_CT043(self):
		chaveTit = "M SP 01 TIRF340T1NF1 NF F340T101"
		
		self.oHelper.SearchBrowse(f'{chaveTit}', key=1, index=True)
		
		self.oHelper.SetButton("Compensar")
		self.oHelper.SetBranch("M SP 01")
		self.oHelper.SetButton("Ok")

		self.oHelper.WaitShow("Compensaçäo de Titulos")
		
		#Posiciona no item da grid de seleção de DIC e simula um "Enter", para selecionar o item
		#O método de marcação de checkbox não funuciona aqui, por conta da janela de definição de valor que o FINA340 abre ao marcar o título.
		self.oHelper.ClickGridCell("Prefixo", 1, 1)
		self.oHelper.SetKey("Enter", grid=True, grid_number=1)

		#Clica em ok na tela de definição de valor a compensar para o título selecionado
		self.oHelper.SetButton("Ok")

		#Fecha o alerta indicando que não pode selecionar o DIC e fecha as demais telas.
		self.oHelper.SetButton("Fechar")
		
		#Volta pra browse
		self.oHelper.SetButton("Cancelar")
		self.oHelper.SetButton("Cancelar")

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == "__main__":
	unittest.main()