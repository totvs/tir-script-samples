from tir import Webapp
import unittest
import time
from datetime import datetime

DateSystem = datetime.today().strftime('%d/%m/%Y')
'''-------------------------------------------------------------------
/*/{Protheus.doc} FINC030TestCase
TIR - Casos de testes da rotina Consulta Posição de Fornecedores

@author TOTVS
@since 20/08/2020
@version 12
-------------------------------------------------------------------'''

class FINC030(unittest.TestCase):

	#-------------------------------------------
	# Inicialiação setUpClass para TIR - FINC030
	#-------------------------------------------
	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAFIN',DateSystem,'T1','D MG 01 ','06')
		inst.oHelper.Program('FINC030')


	#-------------------------------------------
	# Inicio dos casos de testes TIR - FINC030
	#-------------------------------------------
	'''-------------------------------------------------------------------
	/*/{Protheus.doc} TEST_FINC030_CT004
	Consultar se o título em aberto será exibido e se o totalizador irá considerar os valores acessórios

	@author Fabio Casagrande Lima
	@since 20/08/2020
	@version 12
	@See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T53606
	-------------------------------------------------------------------'''
	def test_FINC030_CT004(self):
		filial	= 'D MG    '
		fornece	= 'FAB001'
		loja	= '01'
		data	= '19/08/2020'
		self.oHelper.SearchBrowse(f"{filial}{fornece}{loja}")
		self.oHelper.SetButton('Consultar')
		
		self.oHelper.SetValue('Da Emissao ?',data)
		self.oHelper.SetValue('Ate a Emissao ?',data)
		self.oHelper.SetValue('Do Vencimento ?',data)
		self.oHelper.SetValue('Ate o Vencimento ?',data)
		self.oHelper.SetValue('Considera Provisor. ?','Nao')
		self.oHelper.SetValue('Considera Faturados ?','Nao')
		self.oHelper.SetValue('Considera Pedidos de Compra ?','Todos')		
		self.oHelper.SetValue('Historico completo ?','Nao')			
		self.oHelper.SetValue('Conv.mov. na moeda sel.pela ?','Data Movimento')			
		self.oHelper.SetValue('Seleciona Filiais ?','Nao')							
		self.oHelper.SetButton('Ok')
		
		self.oHelper.ClickFolder('Títulos Em Aberto')
		time.sleep(2)
		self.oHelper.CheckResult('Prefixo', 'TIR', grid=True, line=1)
		self.oHelper.CheckResult('Número', 'F030CT003', grid=True, line=1)		
		self.oHelper.CheckResult('Saldo a Pagar', '1.050,00', grid=True, line=1)
		self.oHelper.CheckResult('Valor acessório', '50,00', grid=True, line=1)
		self.oHelper.LoadGrid()
		
		self.oHelper.CheckView("Valor total:        1.050,00")

		self.oHelper.SetButton('Sair')

		self.oHelper.AssertTrue()

	'''-------------------------------------------------------------------
	/*/{Protheus.doc} TEST_FINC030_CT005
	Consultar se o título pago em moeda estrangeira será exibido com o totalizador em moeda forte.

	@author Fabio Casagrande Lima
	@since 21/08/2020
	@version 12
	@See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T53609
	-------------------------------------------------------------------'''
	def test_FINC030_CT005(self):
		filial	= 'D MG    '
		fornece	= 'FAB001'
		loja	= '01'
		data	= '05/08/2020'
		self.oHelper.SearchBrowse(f"{filial}{fornece}{loja}")
		self.oHelper.SetButton('Consultar')
		
		self.oHelper.SetValue('Da Emissao ?',data)
		self.oHelper.SetValue('Ate a Emissao ?',data)
		self.oHelper.SetValue('Do Vencimento ?',data)
		self.oHelper.SetValue('Ate o Vencimento ?',data)
		self.oHelper.SetValue('Considera Provisor. ?','Nao')
		self.oHelper.SetValue('Considera Faturados ?','Nao')
		self.oHelper.SetValue('Considera Pedidos de Compra ?','Todos')		
		self.oHelper.SetValue('Historico completo ?','Nao')			
		self.oHelper.SetValue('Conv.mov. na moeda sel.pela ?','Data Movimento')			
		self.oHelper.SetValue('Seleciona Filiais ?','Nao')							
		self.oHelper.SetButton('Ok')
		
		self.oHelper.ClickFolder('Títulos Pagos')
		time.sleep(2)
		self.oHelper.CheckResult('Prefixo', 'TIR', grid=True, line=1)
		self.oHelper.CheckResult('Número', 'F030CT005', grid=True, line=1)		
		self.oHelper.CheckResult('Valor Título', '200,00', grid=True, line=1)		
		self.oHelper.CheckResult('Valor Pago', '200,00', grid=True, line=1)
		self.oHelper.CheckResult('Valor Pago (R$)', '1.000,00', grid=True, line=1)
		self.oHelper.CheckResult('Taxa Moeda', '5,0000', grid=True, line=1)		
		self.oHelper.CheckResult('Moeda da Baixa', '01', grid=True, line=1)			
		self.oHelper.LoadGrid()
		
		self.oHelper.CheckView("Valor total (R$):        1.000,00")

		self.oHelper.SetButton('Sair')

		self.oHelper.AssertTrue()

	'''-------------------------------------------------------------------
	/*/{Protheus.doc} TEST_FINC030_CT006
	Consultar se o título em aberto será exibido e se o saldo estará correto

	@author Norberto Monteiro de Melo
	@since 09/10/2020
	@version 01
	@See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T54936
	-------------------------------------------------------------------'''
	def test_FINC030_CT006(self):
		filial	= 'D MG    '
		fornece	= 'FAB001'
		loja	= '01'
		data	= '12/06/2020'

		time.sleep(5)
		self.oHelper.SetButton("x")
		self.oHelper.ChangeEnvironment("13/10/2020","T1", "D MG 01 ","06")

		self.oHelper.Program("FINC030")
		self.oHelper.WaitShow("Consulta Posição Fornecedores")
		
		self.oHelper.SearchBrowse(f"{filial}{fornece}{loja}")
		self.oHelper.SetButton('Consultar')
		
		self.oHelper.SetValue('Da Emissao ?',data)
		self.oHelper.SetValue('Ate a Emissao ?',data)
		self.oHelper.SetValue('Do Vencimento ?',data)
		self.oHelper.SetValue('Ate o Vencimento ?',data)
		self.oHelper.SetValue('Considera Provisor. ?','Nao')
		self.oHelper.SetValue('Considera Faturados ?','Nao')
		self.oHelper.SetValue('Considera Pedidos de Compra ?','Todos')		
		self.oHelper.SetValue('Historico completo ?','Nao')			
		self.oHelper.SetValue('Conv.mov. na moeda sel.pela ?','Data Movimento')			
		self.oHelper.SetValue('Seleciona Filiais ?','Nao')							
		self.oHelper.SetButton('Ok')
		
		self.oHelper.ClickFolder('Títulos Em Aberto')
		time.sleep(2)

		# Taxa Contratada de R$ 3,80 -> U$ 1,00
		self.oHelper.CheckResult('Prefixo', 'FIN', grid=True, line=1)
		self.oHelper.CheckResult('Número', 'F080CT206', grid=True, line=1)		
		self.oHelper.CheckResult('Saldo a Pagar', '38.380,00', grid=True, line=1)
		self.oHelper.CheckResult('Valor Juros', '639,90', grid=True, line=1)
		# Taxa SM2 (12/06/2020) R$ 2,80 -> U$ 1,00
		self.oHelper.CheckResult('Prefixo', 'FIN', grid=True, line=2)
		self.oHelper.CheckResult('Número', 'F080CT207', grid=True, line=2)
		self.oHelper.CheckResult('Saldo a Pagar', '28.280,00', grid=True, line=2)
		self.oHelper.CheckResult('Valor Juros', '639,90', grid=True, line=3)
		# Taxa Contratada de R$ 3,80 -> U$ 1,00
		self.oHelper.CheckResult('Prefixo', 'FIN', grid=True, line=3)
		self.oHelper.CheckResult('Número', 'F080CT208', grid=True, line=3)
		self.oHelper.CheckResult('Saldo a Pagar', '38.380,00', grid=True, line=3)
		self.oHelper.CheckResult('Valor Juros', '639,90', grid=True, line=3)
		# Taxa Contratada de R$ 3,80 -> U$ 1,00
		self.oHelper.CheckResult('Prefixo', 'FIN', grid=True, line=4)
		self.oHelper.CheckResult('Número', 'F080CT210', grid=True, line=4)
		self.oHelper.CheckResult('Saldo a Pagar', '37.620,00', grid=True, line=4)
		# Taxa SM2 (12/06/2020) R$ 2,80 -> U$ 1,00
		self.oHelper.CheckResult('Prefixo', 'FIN', grid=True, line=5)
		self.oHelper.CheckResult('Número', 'F080CT211', grid=True, line=5)
		self.oHelper.CheckResult('Saldo a Pagar', '27.720,00', grid=True, line=5)
		# Taxa Contratada de R$ 3,80 -> U$ 1,00
		self.oHelper.CheckResult('Prefixo', 'FIN', grid=True, line=6)
		self.oHelper.CheckResult('Número', 'F080CT212', grid=True, line=6)
		self.oHelper.CheckResult('Saldo a Pagar', '33.820,00', grid=True, line=6)

		self.oHelper.LoadGrid()
		
		self.oHelper.CheckView("Valor total:      204.200,00")

		self.oHelper.SetButton('Sair')

		self.oHelper.AssertTrue()

	'''-------------------------------------------------------------------
	/*/{Protheus.doc} TEST_FINC030_CT007
	Consultar se o título pago em moeda estrangeira será exibido com o totalizador em moeda forte.

	@author Fabio Casagrande Lima
	@since 21/08/2020
	@version 12
	@See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T53609
	-------------------------------------------------------------------'''
	def test_FINC030_CT007(self):
		filial	= 'D MG    '
		fornece = '1605  '
		loja	= '01'
		data	= '15/10/2016'
		dataVcI	= '21/11/2016'
		dataVcF	= '23/01/2017'

		self.oHelper.SearchBrowse(f"{filial}{fornece}{loja}")
		self.oHelper.SetButton('Consultar')
		
		self.oHelper.SetValue('Da Emissao ?',data)
		self.oHelper.SetValue('Ate a Emissao ?',data)
		self.oHelper.SetValue('Do Vencimento ?', dataVcI)
		self.oHelper.SetValue('Ate o Vencimento ?',dataVcF)
		self.oHelper.SetValue('Considera Provisor. ?','Nao')
		self.oHelper.SetValue('Considera Faturados ?','Nao')
		self.oHelper.SetValue('Considera Pedidos de Compra ?','Todos')		
		self.oHelper.SetValue('Historico completo ?','Nao')			
		self.oHelper.SetValue('Conv.mov. na moeda sel.pela ?','Data Movimento')			
		self.oHelper.SetValue('Seleciona Filiais ?','Nao')							
		self.oHelper.SetButton('Ok')
		
		# Aba - Títuos em aberto ----------------------------------------------------
		self.oHelper.ClickFolder('Títulos Em Aberto')
		time.sleep(2)
		# Parcela A
		self.oHelper.CheckResult('Prefixo', '07 ', grid=True, line=1)
		self.oHelper.CheckResult('Número', '000000004', grid=True, line=1)
		self.oHelper.CheckResult('Parcela', 'A', grid=True, line=1)		
		self.oHelper.CheckResult('Data Vencimento', '21/11/2016', grid=True, line=1)		
		self.oHelper.CheckResult('Saldo a Pagar', '8.168,33', grid=True, line=1)
		# Parcela B
		self.oHelper.CheckResult('Prefixo', '07 ', grid=True, line=2)
		self.oHelper.CheckResult('Número', '000000004', grid=True, line=2)
		self.oHelper.CheckResult('Parcela', 'B', grid=True, line=2)		
		self.oHelper.CheckResult('Data Vencimento', '21/12/2016', grid=True, line=2)		
		self.oHelper.CheckResult('Saldo a Pagar', '8.168,33', grid=True, line=2)
		# Parcela C
		self.oHelper.CheckResult('Prefixo', '07 ', grid=True, line=3)
		self.oHelper.CheckResult('Número', '000000004', grid=True, line=3)
		self.oHelper.CheckResult('Parcela', 'C', grid=True, line=3)
		self.oHelper.CheckResult('Data Vencimento', '21/01/2017', grid=True, line=3)
		self.oHelper.CheckResult('Saldo a Pagar', '8.168,34', grid=True, line=3)
		self.oHelper.LoadGrid()
		self.oHelper.CheckView("Valor total:       24.505,00")
		self.oHelper.AssertTrue()

		# Aba - Faturamento ---------------------------------------------------------
		self.oHelper.ClickFolder('Faturamento')
		time.sleep(2)
		self.oHelper.CheckResult('Número', '000000004', grid=True, line=1)
		self.oHelper.CheckResult('Emissão', '15/10/2016', grid=True, line=1)
		self.oHelper.CheckResult('Valor Nota', '24.505,00', grid=True, line=1)
		self.oHelper.CheckResult('Duplicata', '000000004', grid=True, line=1)
		self.oHelper.LoadGrid()
		self.oHelper.AssertTrue()

		# Aba - Entrega -------------------------------------------------------------
		self.oHelper.ClickFolder('Entrega')
		time.sleep(2)
		self.oHelper.CheckResult('Notas', '000000004', grid=True, line=1)
		self.oHelper.CheckResult('Emissão', '14/10/2016', grid=True, line=1)
		self.oHelper.CheckResult('Pedido', 'PMS016', grid=True, line=1)
		self.oHelper.CheckResult('Produto', 'KMP02', grid=True, line=1)
		self.oHelper.CheckResult('Dt Prevista', '14/10/2016', grid=True, line=1)
		self.oHelper.CheckResult('Dt Realizada', '15/10/2016', grid=True, line=1)
		self.oHelper.LoadGrid()
		self.oHelper.AssertTrue()

		self.oHelper.SetButton('Sair')



	#-------------------------------------------
	# Fim dos casos de testes TIR - FINC030 
	#-------------------------------------------

	#-------------------------------------------
	# Encerramento class para TIR - FINC030 
	#-------------------------------------------
	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()
