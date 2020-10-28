from tir import Webapp
from MATA030TESTCASE import MATA030
from MATA010TESTCASE import MATA010
import unittest

class PROCESSOVENDA(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.grupo = "T1"

		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAFAT','09/06/2020', inst.grupo, 'D MG 01 ', '05')

	def test_MATA010_CT001(self):
		# self.oHelper.SetLateralMenu("Atualizações > Cadastros > Produtos")
		self.oHelper.Program("MATA010")
		MATA010().test_MATA010_CT001(self.oHelper)

	def test_MATA030_CT001(self):
		# self.oHelper.SetLateralMenu("Atualizações > Cadastros > Clientes")
		self.oHelper.Program("MATA030")
		MATA030().test_MATA030_CT001(self.oHelper)

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()