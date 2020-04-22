from cawebhelper import CAWebHelper
import unittest

class TAFA238(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = CAWebHelper()
		inst.oHelper.Setup('SIGATAF','10/08/2017','T1','D MG 01 ','05')
		inst.oHelper.UTProgram('TAFA238')

	def test_TAFA238_CT001(self):
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetFilial('D MG 01')
		self.oHelper.UTSetValue('aCab','C90_DTINI','012018')
		self.oHelper.UTSetValue('aCab','C90_CODIGO','DMG001TRN0001')
		self.oHelper.UTSetValue('aCab','C90_DESCRI','DMG001TRN0001')
		self.oHelper.UTSetValue('aCab','C90_HRENT','08:00')
		self.oHelper.UTSetValue('aCab','C90_HRSAI','17:30')
		self.oHelper.UTSetValue('aCab','C90_DURJOR','480')
		self.oHelper.UTSetValue('aCab','C90_PERFLH','1 - Sim')
		
		self.oHelper.UTSetValue('aItens','CRL_INIINT','10:30')
		self.oHelper.UTSetValue('aItens','CRL_FIMINT','10:45')
		self.oHelper.UTSetValue('aItens','CRL_TPINTE','1 - Intervalo em Horário Fixo')
		self.oHelper.UTSetValue('aItens','CRL_DURINT','15')
		self.oHelper.SetKey('DOWN')
		self.oHelper.UTSetValue('aItens','CRL_INIINT','15:30')
		self.oHelper.UTSetValue('aItens','CRL_FIMINT','15:45')
		self.oHelper.UTSetValue('aItens','CRL_TPINTE','1 - Intervalo em Horário Fixo')
		self.oHelper.UTSetValue('aItens','CRL_DURINT','15')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SetButton('Visualizar')
		self.oHelper.UTCheckResult('aCab','C90_DTINI','012018')
		self.oHelper.UTCheckResult('aCab','C90_CODIGO','DMG001TRN0001')
		self.oHelper.UTCheckResult('aCab','C90_DESCRI','DMG001TRN0001')
		self.oHelper.UTCheckResult('aCab','C90_HRENT','08:00')
		self.oHelper.UTCheckResult('aCab','C90_HRSAI','17:30')
		self.oHelper.UTCheckResult('aCab','C90_DURJOR','480')
		self.oHelper.UTCheckResult('aCab','C90_PERFLH','1 - Sim')
		self.oHelper.UTCheckResult('aItens','CRL_INIINT','10:30')
		self.oHelper.UTCheckResult('aItens','CRL_FIMINT','10:45')
		self.oHelper.UTCheckResult('aItens','CRL_TPINTE','Intervalo em Horário Fixo')
		self.oHelper.UTCheckResult('aItens','CRL_DURINT','15')
		self.oHelper.SetKey('DOWN')
		self.oHelper.UTCheckResult('aItens','CRL_INIINT','15:30')
		self.oHelper.UTCheckResult('aItens','CRL_FIMINT','15:45')
		self.oHelper.UTCheckResult('aItens','CRL_TPINTE','Intervalo em Horário Fixo')
		self.oHelper.UTCheckResult('aItens','CRL_DURINT','15')
		self.oHelper.SetButton('Fechar')
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()