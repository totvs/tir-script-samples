from tir import Webapp
import unittest
import time

class CTBANFS(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAFAT','14/08/2019','T1','D MG 01 ','05')
		inst.oHelper.Program('CTBANFS')

	def test_CTBANFS_CT001(self):
		self.oHelper.AddParameter("MV_CNFSTHR","D MG 01","15","15","15")
		self.oHelper.AddParameter("MV_OPTNFS" ,"D MG 01",".T.",".T.",".T.")
		self.oHelper.AddParameter("MV_ALTLCTO" ,"D MG 01","N","N","N")
		self.oHelper.AddParameter("MV_PRELAN" ,"D MG 01","S","S","S")
		self.oHelper.SetParameters()

		self.oHelper.SetButton('Param.')
		self.oHelper.SetValue('mv_par07', 'D MG 01')
		self.oHelper.SetValue('Mostra Lanç Contab ?', 'Nao')
		self.oHelper.SetValue('Aglut. Lançamentos ?', 'Nao')
		self.oHelper.SetValue('Gera Lanç. Por ?', 'Documento')
		self.oHelper.SetValue('Contb.Custo On-Line ?', 'Nao')
		self.oHelper.SetValue('Data Inicial ?', '16/08/2019')
		self.oHelper.SetValue('Data Final ?', '16/08/2019')
		self.oHelper.SetValue('Até a Filial ?', 'D MG 01')
		self.oHelper.SetValue('Cont.Notas Credito ?', 'Nao')
		self.oHelper.SetButton('Ok')
		self.oHelper.SetButton('Ok')
		time.sleep(60)
		self.oHelper.WaitHide('Contabilizando...')
		self.oHelper.AssertTrue()

		self.oHelper.RestoreParameters()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()