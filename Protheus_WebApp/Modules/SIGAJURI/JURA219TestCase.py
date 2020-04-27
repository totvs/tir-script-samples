from tir import Webapp
import unittest

class JURA219(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAJURI','24/10/2018','T1','D MG 01 ','76')

	def test_JURA219_CT001(self):
		self.oHelper.Program('JURA219')
		self.oHelper.SetButton("Perguntas")
		self.oHelper.SetValue("MV_PAR01","01/10/2018",name_attr=True)
		self.oHelper.SetValue("MV_PAR02","31/10/2018",name_attr=True)
		self.oHelper.SetValue("MV_PAR04","001",name_attr=True)
		self.oHelper.SetButton("Informações")
		self.oHelper.SetButton("Executar")
		self.oHelper.ClickFolder("Distribuições recebidas")
		self.oHelper.SetButton("Outras Ações","Exportar Recebidas")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("Sair da página")
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()