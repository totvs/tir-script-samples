from tir import Webapp
import unittest
import time
from datetime import datetime

DateSystem = datetime.today().strftime('%d/%m/%Y')
'''-------------------------------------------------------------------
/*/{Protheus.doc} FINC050TestCase
TIR - Casos de testes da rotina Consulta Posição de Fornecedores

@author TOTVS
@since 28/08/2020
@version 12
-------------------------------------------------------------------'''

class FINC050(unittest.TestCase):

	#-------------------------------------------
	# Inicialiação setUpClass para TIR - FINC050
	#-------------------------------------------
	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAFIN',DateSystem,'T1','D MG 01 ','06')
		inst.oHelper.Program('FINC050')


	#-------------------------------------------
	# Inicio dos casos de testes TIR - FINC050
	#-------------------------------------------
	'''-------------------------------------------------------------------
	/*/{Protheus.doc} TEST_FINC050_CT004
	Consulta titulo NF em moeda 2 ($ 1.000,00), baixado parcialmente (R$ 2.500,00) 
	e o saldo residual foi compensado com PA.

	@author Fabio Casagrande Lima
	@since 28/08/2020
	@version 12
	@See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/204527
	-------------------------------------------------------------------'''
	def test_FINC050_CT004(self):
		filial	= 'D MG 01 '
		prefixo = 'TIR'
		titulo  = 'FC50CT004'
		parcela = ' '
		tipo    = 'NF '
		fornece	= 'FAB001'
		loja	= '01'

		self.oHelper.SearchBrowse(f"{filial}{prefixo}{titulo}{parcela}{tipo}{fornece}{loja}")
		self.oHelper.SetButton('Consulta')
	
		time.sleep(3)

		#Conferencia de valores na grid
		self.oHelper.CheckResult('Valor Pago', '2.500,00', grid=True, line=1)		
		self.oHelper.CheckResult('Valor em US$', '500,00', grid=True, line=1)
		self.oHelper.CheckResult('Valor Pago', '2.500,00', grid=True, line=2)		
		self.oHelper.CheckResult('Valor em US$', '500,00', grid=True, line=2)
		self.oHelper.LoadGrid()

		self.oHelper.SetButton('Confirmar')

		self.oHelper.AssertTrue()

	'''-------------------------------------------------------------------
	/*/{Protheus.doc} TEST_FINC050_CT005
	Consulta titulo PA em moeda 2 ($ 500,00) que foi compensado com NF.

	@author Fabio Casagrande Lima
	@since 28/08/2020
	@version 12
	@See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/204531
	-------------------------------------------------------------------'''
	def test_FINC050_CT005(self):
		filial	= 'D MG 01 '
		prefixo = 'TIR'
		titulo  = 'FC50CT004'
		parcela = ' '
		tipo    = 'PA '
		fornece	= 'FAB001'
		loja	= '01'

		self.oHelper.SearchBrowse(f"{filial}{prefixo}{titulo}{parcela}{tipo}{fornece}{loja}")
		self.oHelper.SetButton('Consulta')
	
		time.sleep(3)

		#Conferencia de valores na grid
		self.oHelper.CheckResult('Valor Pago', '2.500,00', grid=True, line=1)
		self.oHelper.CheckResult('Valor em US$', '500,00', grid=True, line=1)
		self.oHelper.CheckResult('Valor Pago',   '500,00', grid=True, line=2)
		self.oHelper.CheckResult('Valor em US$', '500,00', grid=True, line=2)
		self.oHelper.LoadGrid()

		self.oHelper.SetButton('Confirmar')

		self.oHelper.AssertTrue()
		
	#-------------------------------------------
	# Fim dos casos de testes TIR - FINC050 
	#-------------------------------------------

	#-------------------------------------------
	# Encerramento class para TIR - FINC050 
	#-------------------------------------------
	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()