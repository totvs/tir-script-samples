from tir import Webapp
import unittest

class GFEA044(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAGFE','26/06/2020','T1','D MG 01 ','78')
		inst.oHelper.Program('GFEA044')

	def test_GFEA044_CT001(self):

		self.oHelper.SearchBrowse('D MG 01 NFS  001           1  3011            ')

		self.oHelper.SetButton('Outras Ações','Copiar')
		
		self.oHelper.SetValue('Numero', '2606202001')

		self.oHelper.SetButton('Confirmar')

		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('D MG 01 NFS  001           1  2606202001      ')

		self.oHelper.SetButton('Outras Ações','Bloquear')

		self.oHelper.SetButton('Sim')

		self.oHelper.SearchBrowse('D MG 01 NFS  001           1  2606202001      ')

		self.oHelper.SetButton('Outras Ações','Liberar')

		self.oHelper.SetButton('Sim')

		self.oHelper.SearchBrowse('D MG 01 NFS  001           1  2606202001      ')

		self.oHelper.SetButton('Visualizar')

		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('D MG 01 NFS  001           1  2606202001      ')

		self.oHelper.SetButton('Outras Ações','Excluir')

		self.oHelper.SetButton('Confirmar')

		self.oHelper.SetButton('Fechar')
		
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()
if __name__ == '__main__':
	unittest.main()

