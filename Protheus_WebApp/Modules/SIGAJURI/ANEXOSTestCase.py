import unittest
from tir import Webapp

class ANEXOS(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAJURI','03/06/2019','T1','D MG 01 ','76')
		inst.oHelper.Program('JURA162')

	def test_ANEXOS_01(self):
		self.oHelper.SetValue("cValor","Contratos",name_attr=True)
		self.oHelper.SetValue("NSZ_COD","0000000069")
		self.oHelper.ClickLabel("Pesquisar")
		self.oHelper.WaitProcessing("Pesquisando...")
		self.oHelper.SetValue("NSZ_COD","0000000069")
		self.oHelper.ClickLabel("Anexos")
		self.oHelper.SetButton("Importar")
		self.oHelper.SetFilePath(r"SERVIDOR\baseline\Jur_Anexos_Importação.txt")
		self.oHelper.SetButton("Salvar")
		self.oHelper.WaitShow("Deseja importar o(s) seguinte(s) arquivo(s):")
		self.oHelper.SetButton("Sim")
		self.oHelper.CheckResult("Descricao","jur_anexos_importacao.txt",grid=True,line=1)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton("Fechar")
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()
