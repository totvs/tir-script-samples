from cawebhelper import CAWebHelper
import unittest

class TAFA235(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = CAWebHelper()
		#inst.oHelper.Setup('SIGATAF','10/08/2017','99','01','05')
		inst.oHelper.Setup('SIGATAF','10/08/2017','T1','D MG 01 ','05')
		inst.oHelper.UTProgram('TAFA235')

	def test_TAFA235_CT001(self):
		
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetFilial('D MG 01')
		self.oHelper.UTSetValue('aCab','C8V_DTINI','012018')
		self.oHelper.UTSetValue('aCab','C8V_CODIGO','DMG01CRG012')
		self.oHelper.UTSetValue('aCab','C8V_DESCRI','CARGO 142515-GER PRODUCAO DE TECNOLOGIA')
		self.oHelper.UTSetValue('aCab','C8V_CODCBO','002777')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')
		
		self.oHelper.SetButton('Visualizar')
		self.oHelper.UTCheckResult('aCab','C8V_DTINI','012018')
		self.oHelper.UTCheckResult('aCab','C8V_CODIGO','DMG01CRG012')
		self.oHelper.UTCheckResult('aCab','C8V_DESCRI','CARGO 142515-GER PRODUCAO DE TECNOLOGIA')
		self.oHelper.UTCheckResult('aCab','C8V_CODCBO','002777')
		self.oHelper.SetButton('Fechar')
		self.oHelper.AssertTrue()

	def test_TAFA235_CT002(self):
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetFilial('D MG 01')
		self.oHelper.UTSetValue('aCab','C8V_DTINI','012018')
		self.oHelper.UTSetValue('aCab','C8V_CODIGO','DMG01CRG013')
		self.oHelper.UTSetValue('aCab','C8V_DESCRI','CARGO 142105 GERENTE ADMINSTRATIVO')
		self.oHelper.UTSetValue('aCab','C8V_CODCBO','002758')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SetButton('Visualizar')
		self.oHelper.UTCheckResult('aCab','C8V_DTINI','012018')
		self.oHelper.UTCheckResult('aCab','C8V_CODIGO','DMG01CRG013')
		self.oHelper.UTCheckResult('aCab','C8V_DESCRI','CARGO 142105 GERENTE ADMINSTRATIVO')
		self.oHelper.UTCheckResult('aCab','C8V_CODCBO','002758')
		self.oHelper.SetButton('Fechar')
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()