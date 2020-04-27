from tir import Webapp
import unittest
from datetime import datetime

DateSystem = datetime.today().strftime('%d/%m/%Y')

class FINC010(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAFIN',DateSystem,'T1','D MG 01 ','06')
		inst.oHelper.Program('FINC010')

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
		self.oHelper.CheckResult('No. Titulo', 'FIN000326', grid=True, line=1)
		self.oHelper.CheckResult('Tipo', 'RA', grid=True, line=1)
		self.oHelper.CheckResult('Vlr.Titulo', '1.000,00', grid=True, line=1)
		self.oHelper.CheckResult('Saldo a Receber', '250,00', grid=True, line=1)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton('Ok')
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()