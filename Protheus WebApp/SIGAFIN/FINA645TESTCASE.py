from tir import Webapp
import unittest
import time

class FINA645(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		'''
		SETUP
		Test Case Initial Setup
		'''

		#EndereÃƒÂ§o do webapp e o nome do Browser
		inst.oHelper = Webapp()

		#Parametros de inicializaÃƒÂ§ao
		inst.oHelper.Setup('SIGAFIN','12/05/2019','T1','D MG 01 ','06')

		#Nome da rotina do Caso de Teste
		inst.oHelper.Program("FINA645")

	def test_FINA645_CT001(self):
		'''
		Test Case 001
		'''
		self.oHelper.SetButton("Constituição")
		self.oHelper.SetValue('Data Referencia ?','12/05/2019')
		self.oHelper.SetValue('Dias de Atraso ?','1')
		self.oHelper.SetValue('Transferir para Provisao ?', 'Vct apos atraso')                
		self.oHelper.SetValue('Cliente De ?','PDD001')
		self.oHelper.SetValue('Loja De ?','01')
		self.oHelper.SetValue('Cliente Ate ?','PDD001')
		self.oHelper.SetValue('Loja Ate ?','01')
		self.oHelper.SetValue('Emissao De ?','10/05/2019')
		self.oHelper.SetValue('Emissao Ate ?','10/06/2019')
		self.oHelper.SetValue('Seleciona Filial ?','Não')
		self.oHelper.SetValue('Sit Cobranca PDD ?','8')
		self.oHelper.SetValue('Seleciona Sit. de Cobrança ?','Não')
		self.oHelper.SetValue('Considera Negociados ? ','Não')

		self.oHelper.SetButton("OK")

		self.oHelper.WaitShow("Transferência PDD\\PPSC - Provisão PDD")
		self.oHelper.SetButton("Confirmar")

		self.oHelper.SetButton("Fechar")

		self.oHelper.SetButton("Visualizar")

		self.oHelper.CheckResult('FJX_DTPROC','12052019')
		self.oHelper.CheckResult('FJX_DTREF','12052019')
		self.oHelper.CheckResult('FJX_TIPO','1')

		self.oHelper.AssertTrue()

		self.oHelper.SetButton("Fechar")

	def test_FINA645_CT002(self):
		'''
		Test Case 002
		'''

		self.oHelper.SetButton("Efetivação")
		self.oHelper.SetValue('Mostra Lançamento ?','Não')
		self.oHelper.SetValue('Aglutina Lançamento ?','Não')
		self.oHelper.SetValue('Movimen. Posterior Processo ?', 'Não')
		self.oHelper.SetButton("OK")

		self.oHelper.CheckResult('FJX_DTPROC','12/05/2019')
		self.oHelper.CheckResult('FJX_DTREF','12/05/2019')
		self.oHelper.CheckResult('FJX_TIPO','1')
		self.oHelper.CheckResult('FJY_FILCLI','D MG    ', grid=True, line=1, grid_number=1)
		self.oHelper.CheckResult('FJY_CLIENT','PDD001', grid=True, line=1, grid_number=1)
		self.oHelper.CheckResult('FJY_LOJA','01', grid=True, line=1, grid_number=1)
		self.oHelper.CheckResult('FJY_QTDMAX','2', grid=True, line=1, grid_number=1)
		self.oHelper.CheckResult('FJY_VLRPRO','10.000,00', grid=True, line=1, grid_number=1)
		self.oHelper.LoadGrid()

		self.oHelper.AssertTrue()

		self.oHelper.ClickFolder('Titulos')

		self.oHelper.CheckResult('FJZ_ITEM','0001', grid=True, line=1, grid_number=2)
		self.oHelper.CheckResult('FJZ_FILTIT','D MG 01 ', grid=True, line=1, grid_number=2)
		self.oHelper.CheckResult('FJZ_PREFIX','PDD', grid=True, line=1, grid_number=2)
		self.oHelper.CheckResult('FJZ_NUM','FINPDD001', grid=True, line=1, grid_number=2)
		self.oHelper.CheckResult('FJZ_PARCEL',' ', grid=True, line=1, grid_number=2)
		self.oHelper.CheckResult('FJZ_TIPO','NF ', grid=True, line=1, grid_number=2)
		self.oHelper.CheckResult('FJZ_SALDO','10.000,00', grid=True, line=1, grid_number=2)
		self.oHelper.CheckResult('FJZ_EMISS','10/05/2019', grid=True, line=1, grid_number=2)
		self.oHelper.CheckResult('FJZ_VENCTO','10/05/2019', grid=True, line=1, grid_number=2)
		self.oHelper.CheckResult('FJZ_QTDATR','2', grid=True, line=1, grid_number=2)
		#self.oHelper.CheckResult('Venc Real   ','10/05/2019', grid=True, line=1, grid_number=2)
		self.oHelper.LoadGrid()
		
		self.oHelper.AssertTrue()

		self.oHelper.SetButton("Confirmar")

		self.oHelper.SetButton("Fechar")

	@classmethod
	def tearDownClass(inst):
		'''
		Method that finishes the test case.
		'''
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()