from cawebhelper import CAWebHelper
import unittest

class TAFMONTES(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = CAWebHelper()
		#inst.oHelper.Setup('SIGATAF','10/08/2017','99','01','05')
		inst.oHelper.Setup('SIGATAF','10/08/2017','T1','D MG 01 ','05')
		#inst.oHelper.UTProgram('TAFMONTES')
		inst.oHelper.SetLateralMenu("Atualizações > Eventos Esocial > Monitoramento")
		
	def test_TAFMONTES_CT001(self):
		self.oHelper.UTSetValue('aCab','Data Inicial','01/01/2000')
		self.oHelper.UTSetValue('aCab','Data Fim','31/12/2019')
		self.oHelper.SetButton('Selecionar Filiais')
		self.oHelper.ClickBox('Filial','D MG 01')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Aplicar Filtro')
		self.oHelper.ClickBox('Evento','S-1000 - INFORMACOES DO EMPREGADOR/CONTRIBUINTE/ÓRGÃO PÚBLIC')
		self.oHelper.SetButton('Exportar XMLs')
		self.oHelper.UTSetValue('aCab','Todos',True)
		self.oHelper.SetButton('Confirmar')

		self.oHelper.SetFilePath("SERVIDOR\\xml\\")
		self.oHelper.MessageBoxClick('Ok')
		self.oHelper.SetButton('Sair')		

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()