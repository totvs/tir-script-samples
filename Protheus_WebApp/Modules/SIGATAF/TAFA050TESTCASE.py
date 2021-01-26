from cawebhelper import CAWebHelper
import unittest

class TAFA050(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = CAWebHelper()
		inst.oHelper.Setup('SIGATAF','10/08/2017','T1','D MG 01 ','05')
		#inst.oHelper.Setup('SIGATAF','10/08/2017','99','01','05')
		#inst.oHelper.UTProgram('TAFA050')
		inst.oHelper.SetLateralMenu("Atualizações > Empresa > Complemento Cadastral")

	def test_TAFA050_CT001(self):
		self.oHelper.SearchBrowse('Id + Id. Ver. Reg + Reg. Ativo?', '000009', True)
		
		self.oHelper.SetButton('Alterar')
		self.oHelper.ClickFolder('Complemento do Estabelecimento')
		self.oHelper.ClickFolder('Informações do Estabelecimento')
		self.oHelper.UTSetValue('aCab','C1E_DTINI','12018')
		self.oHelper.UTSetValue('aCab','C1E_NOME','TOTVS SA')
		self.oHelper.UTSetValue('aCab','C1E_CLAFIS','000019')
		self.oHelper.UTSetValue('aCab','C1E_NATJUR','000023')
		self.oHelper.UTSetValue('aCab','C1E_INCOOP','0')
		self.oHelper.UTSetValue('aCab','C1E_INCONS','0')
		self.oHelper.UTSetValue('aCab','C1E_CRT','1')
		self.oHelper.UTSetValue('aCab','C1E_DESFOL','1')
		self.oHelper.UTSetValue('aCab','C1E_REGELT','1')
		self.oHelper.UTSetValue('aCab','C1E_MATRIZ',True)
		self.oHelper.UTSetValue('aCab','C1E_ENTEDU','0')
		self.oHelper.UTSetValue('aCab','C1E_INDETT','2')
		self.oHelper.ClickFolder('Contato do Estabelecimento')
		self.oHelper.UTSetValue('aCab','C1E_EMAIL','TESTE@TESTE.COM.BR')
		self.oHelper.UTSetValue('aCab','C1E_NOMCNT','ATENDIMENTO TOTVS SA.')
		self.oHelper.UTSetValue('aCab','C1E_CPFCNT','08557176961')
		self.oHelper.UTSetValue('aCab','C1E_DDDFON','11')
		self.oHelper.UTSetValue('aCab','C1E_FONCNT','20122015')
		self.oHelper.UTSetValue('aCab','C1E_DDDCEL','11')
		self.oHelper.UTSetValue('aCab','C1E_CELCNT','998754485')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')
		
		self.oHelper.SetButton('Visualizar')
		self.oHelper.ClickFolder('Complemento do Estabelecimento')
		self.oHelper.ClickFolder('Informações do Estabelecimento')
		self.oHelper.UTCheckResult('aCab','C1E_DTINI','12018')
		self.oHelper.UTCheckResult('aCab','C1E_NOME','TOTVS SA')
		self.oHelper.UTCheckResult('aCab','C1E_CLAFIS','000019')
		self.oHelper.UTCheckResult('aCab','C1E_NATJUR','000023')
		self.oHelper.UTCheckResult('aCab','C1E_INCOOP','0 - Não é Cooperativa')
		self.oHelper.UTCheckResult('aCab','C1E_INCONS','0 - Não é Construtora')
		self.oHelper.UTCheckResult('aCab','C1E_CRT','1 - Simples Nacional')
		self.oHelper.UTCheckResult('aCab','C1E_DESFOL','1 - Empresa enquadrada nos art. 7º a 9º da Lei 12.546/201')
		self.oHelper.UTCheckResult('aCab','C1E_REGELT','1 - Optou pelo registro eletrônico de empregados')
		self.oHelper.UTCheckResult('aCab','C1E_MATRIZ',True)
		self.oHelper.UTCheckResult('aCab','C1E_ENTEDU','0 - Não é entidade educativa sem fins lucrativos')
		self.oHelper.UTCheckResult('aCab','C1E_INDETT','2 - Não')
		self.oHelper.ClickFolder('Contato do Estabelecimento')
		self.oHelper.UTCheckResult('aCab','C1E_EMAIL','TESTE@TESTE.COM.BR')
		self.oHelper.UTCheckResult('aCab','C1E_NOMCNT','ATENDIMENTO TOTVS SA.')
		self.oHelper.UTCheckResult('aCab','C1E_CPFCNT','08557176961')
		self.oHelper.UTCheckResult('aCab','C1E_DDDFON','11')
		self.oHelper.UTCheckResult('aCab','C1E_FONCNT','20122015')
		self.oHelper.UTCheckResult('aCab','C1E_DDDCEL','11')
		self.oHelper.UTCheckResult('aCab','C1E_CELCNT','998754485')
		self.oHelper.SetButton('Fechar')
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()