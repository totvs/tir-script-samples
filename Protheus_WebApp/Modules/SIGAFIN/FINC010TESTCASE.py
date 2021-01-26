from tir import Webapp
import unittest
import time
from datetime import datetime

DateSystem = datetime.today().strftime('%d/%m/%Y')
'''-------------------------------------------------------------------
/*/{Protheus.doc} FINC010TestCase
TIR - Casos de testes da rotina Consulta Posição de Clinetes

@author Renato Ito
@since 26/08/2019
@version 12
-------------------------------------------------------------------'''

class FINC010(unittest.TestCase):

	#-------------------------------------------
	# Inicialiação setUpClass para TIR - FINC010
	#-------------------------------------------
	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAFIN',DateSystem,'T1','D MG 01 ','06')
		inst.oHelper.Program('FINC010')


	#-------------------------------------------
	# Inicio dos casos de testes TIR - FINC010
	#-------------------------------------------
	'''-------------------------------------------------------------------
	/*/{Protheus.doc} TEST_FINC010_CT012
	Validar a listagem de baixas de adiantamentos na opção de títulos baixados quando configurado o pergunte Considera RA = SIM.

	@author Renato.ito
	@since 26/08/2019
	@version 12
	@See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T43229
	-------------------------------------------------------------------'''
	def test_FINC010_CT012(self):
		filial	= 'D MG    '
		cliente	= 'FIN333'
		loja	= '01'
		data	= '26/08/2019'
		self.oHelper.SearchBrowse(f"{filial}{cliente}{loja}")
		self.oHelper.SetButton('Consultar')
		
		self.oHelper.SetValue('Da Emissão ?',data)
		self.oHelper.SetValue('Até a Emissão ?',data)
		self.oHelper.SetValue('Do Vencimento ?',data)
		self.oHelper.SetValue('Até o Vencimento ?',data)
		self.oHelper.SetValue('Considera RA ?','Sim')
		self.oHelper.SetButton('Ok')
		
		self.oHelper.SetButton('Tit Baixados')
		time.sleep(2)
		self.oHelper.CheckResult('No. Titulo', 'FIN000326', grid=True, line=1)
		self.oHelper.CheckResult('Tipo', 'RA', grid=True, line=1)
		self.oHelper.CheckResult('Pago', '500,00', grid=True, line=1)
		self.oHelper.CheckResult('MOT BAIXA', 'CMP', grid=True, line=1)
		self.oHelper.LoadGrid()
		
		self.oHelper.CheckResult('No. Titulo', 'FIN000326', grid=True, line=3)
		self.oHelper.CheckResult('Tipo', 'RA', grid=True, line=3)
		self.oHelper.CheckResult('Pago', '250,00', grid=True, line=3)
		self.oHelper.CheckResult('MOT BAIXA', 'NOR', grid=True, line=3)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton('Ok')

		self.oHelper.SetButton('Tit Aberto')
		time.sleep(2)
		self.oHelper.CheckResult('No. Titulo', 'FIN000326', grid=True, line=1)
		self.oHelper.CheckResult('Tipo', 'RA', grid=True, line=1)
		self.oHelper.CheckResult('Vlr.Titulo', '1.000,00', grid=True, line=1)
		self.oHelper.CheckResult('Saldo a Receber', '250,00', grid=True, line=1)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton('Ok')

		self.oHelper.AssertTrue()
	
	
	#-------------------------------------------
	# Fim dos casos de testes TIR - FINC010 
	#-------------------------------------------


	#-------------------------------------------
	# Encerramento class para TIR - FINC010 
	#-------------------------------------------
	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()