from tir import Webapp
import unittest

class MATA098(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAPCP','25/04/2019','T1','D MG 01 ','10')
		inst.oHelper.Program('MATA098')

	def test_MATA098_001(self):
		self.oHelper.SearchBrowse('D MG 01 PCP_TIR_MATA098_CFGPRD_001001', 'Filial+codigo Base + Item')
		self.oHelper.SetButton('Definir')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetValue('BS_DESCR','ROSA', grid=True)
		self.oHelper.SetValue('BS_DESCPRD','ROSA', grid=True)
		self.oHelper.SetValue('BS_CODIGO','RS', grid=True)
		self.oHelper.SetKey('ESC', grid=True)
		self.oHelper.SetKey('DOWN', grid=True)
		self.oHelper.SetValue('BS_DESCR','ROXO', grid=True)
		self.oHelper.SetValue('BS_DESCPRD','ROXO', grid=True)
		self.oHelper.SetValue('BS_CODIGO','RX', grid=True)
		self.oHelper.SetKey('ESC', grid=True)
		self.oHelper.SetKey('DOWN', grid=True)
		self.oHelper.SetValue('BS_DESCR','LARANJA', grid=True)
		self.oHelper.SetValue('BS_DESCPRD','LARANJA', grid=True)
		self.oHelper.SetValue('BS_CODIGO','LJ', grid=True)
		self.oHelper.LoadGrid()
		self.oHelper.SetKey('ESC', grid=True)
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Definir')
		self.oHelper.LoadGrid()
		self.oHelper.CheckResult('BS_CODIGO','LJ', grid=True, line=1)
		self.oHelper.LoadGrid()
		self.oHelper.CheckResult('BS_DESCR','LARANJA', grid=True, line=1)
		self.oHelper.LoadGrid()
		self.oHelper.CheckResult('BS_DESCPRD','LARANJA', grid=True, line=1)
		self.oHelper.LoadGrid()
		self.oHelper.CheckResult('BS_CODIGO','RS', grid=True, line=2)
		self.oHelper.LoadGrid()
		self.oHelper.CheckResult('BS_DESCR','ROSA', grid=True, line=2)
		self.oHelper.LoadGrid()
		self.oHelper.CheckResult('BS_DESCPRD','ROSA', grid=True, line=2)
		self.oHelper.LoadGrid()
		self.oHelper.CheckResult('BS_CODIGO','RX', grid=True, line=3)
		self.oHelper.LoadGrid()
		self.oHelper.CheckResult('BS_DESCR','ROXO', grid=True, line=3)
		self.oHelper.LoadGrid()
		self.oHelper.CheckResult('BS_DESCPRD','ROXO', grid=True, line=3)		
		self.oHelper.LoadGrid()
		self.oHelper.SetButton('Cancelar')

		self.oHelper.AssertTrue()

	def test_MATA098_002(self):
    		
		self.oHelper.SearchBrowse('D MG 01 PCP_TIR_MATA098_CFGPRD_002001', 'Filial+codigo Base + Item')
		self.oHelper.SetButton('Outras Ações', 'Limpar')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Sim')
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()