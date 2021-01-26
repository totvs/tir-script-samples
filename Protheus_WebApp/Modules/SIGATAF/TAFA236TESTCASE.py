from cawebhelper import CAWebHelper
import unittest

class TAFA236(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = CAWebHelper()
		#inst.oHelper.Setup('SIGATAF','10/08/2017','99','01','05')
		inst.oHelper.Setup('SIGATAF','10/08/2017','T1','D MG 01 ','05')
		inst.oHelper.UTProgram('TAFA236')

	def test_TAFA236_CT001(self):
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetFilial('D MG 01')
		self.oHelper.UTSetValue('aCab','C8X_DTINI','012018')
		self.oHelper.UTSetValue('aCab','C8X_CODIGO','DMG01FUNC001')
		self.oHelper.UTSetValue('aCab','C8X_DESCRI','FUNC 142510 GERENTE DESENV SISTEMAS')
		self.oHelper.UTSetValue('aCab','C8X_CODCBO','000143')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SetButton('Visualizar')
		self.oHelper.UTCheckResult('aCab','C8X_DTINI','012018')
		self.oHelper.UTCheckResult('aCab','C8X_CODIGO','DMG01FUNC001')
		self.oHelper.UTCheckResult('aCab','C8X_DESCRI','FUNC 142510 GERENTE DESENV SISTEMAS')
		self.oHelper.UTCheckResult('aCab','C8X_CODCBO','000143')
		self.oHelper.SetButton('Fechar')
		self.oHelper.AssertTrue()

	def test_TAFA236_CT002(self):
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetFilial('D MG 01')
		self.oHelper.UTSetValue('aCab','C8X_DTINI','012018')
		self.oHelper.UTSetValue('aCab','C8X_CODIGO','DMG01FUNC002')
		self.oHelper.UTSetValue('aCab','C8X_DESCRI','FUNC 142510 GERENTE DESENV SISTEMAS')
		self.oHelper.UTSetValue('aCab','C8X_CODCBO','000143')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SetButton('Visualizar')
		self.oHelper.UTCheckResult('aCab','C8X_DTINI','012018')
		self.oHelper.UTCheckResult('aCab','C8X_CODIGO','DMG01FUNC002')
		self.oHelper.UTCheckResult('aCab','C8X_DESCRI','FUNC 142510 GERENTE DESENV SISTEMAS')
		self.oHelper.UTCheckResult('aCab','C8X_CODCBO','000143')
		self.oHelper.SetButton('Fechar')
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()