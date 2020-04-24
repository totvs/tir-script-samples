from tir import Webapp
import unittest

class TAFA400(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGATAF','09/03/2020','T1','D MG 01 ','84')
		inst.oHelper.Program('TAFA400')

	def test_TAFA400_CT001(self):

		cDtIni = '012020'
		cDtFim = '032020'
	
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch('D MG 01 ')
		self.oHelper.SetValue('T39_PERINI',cDtIni)
		self.oHelper.SetValue('T39_PERFIN',cDtFim)
		self.oHelper.SetValue('T39_TIPREG','1')
		self.oHelper.SetValue('T39_ATODEC','X')
		self.oHelper.SetValue("T38_MES","01",grid=True)
		self.oHelper.SetValue("REC. BRUTA","1000,00",grid=True)
		self.oHelper.SetValue("T38_RECEMP","1000,00",grid=True)
		self.oHelper.SetValue("T38_TIPREG","1",grid=True)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()