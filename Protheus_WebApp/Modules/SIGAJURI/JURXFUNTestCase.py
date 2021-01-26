from tir import Webapp
import unittest

class JURXFUN(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAJURI','10/12/2020','T1','D MG 01 ','76')

	def test_JURXFUN_CT001(self):
		print("CT001 - Execução da automação do JurF3Qry")
		self.oHelper.SetLateralMenu("Atualizações > Administrativo > Clientes")
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetButton('OK')
		self.oHelper.F3(field='NUH_CRELAT',name_attr=True)
		self.oHelper.SetButton("Cancelar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("X")

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()
