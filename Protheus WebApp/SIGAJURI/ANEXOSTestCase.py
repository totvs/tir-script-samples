import time
import unittest

from tir import Webapp

class ANEXOS(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAJURI','03/06/2019','T1','D MG 01 ','76')
		inst.oHelper.Program('JURA162')

	# IMPORTAR
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
		time.sleep(3)
		self.oHelper.CheckResult("Descricao","jur_anexos_importacao.txt",grid=True,line=1)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton("Fechar")
		self.oHelper.AssertTrue()
		print("test_ANEXOS_01 finalizado")

		# EXPORTAR
	def test_ANEXOS_02(self):
		self.oHelper.ClickLabel("Anexos")
		#self.oHelper.ClickBox("Descricao","Jur_Anexos_Exportação.txt")
		self.oHelper.SetButton("Exportar")
		self.oHelper.WaitShow("Documentos exportados com sucesso!")
		self.oHelper.SetButton("Fechar")
		time.sleep(3)
		self.oHelper.SetButton("Fechar")
		self.oHelper.AssertTrue()
		print("test_ANEXOS_02 finalizado")

		# EXCLUIR
	def test_ANEXOS_03(self):
		self.oHelper.ClickLabel("Anexos")
		#self.oHelper.ClickBox("Descricao","jur_anexos_exclusao.txt")
		self.oHelper.SetButton("Excluir")
		self.oHelper.WaitShow("Documento(s) excluído(s) com sucesso!")
		self.oHelper.SetButton("Fechar")
		time.sleep(3)
		self.oHelper.SetButton("Fechar")
		self.oHelper.AssertTrue()
		print("test_ANEXOS_03 finalizado")

	@classmethod
	def tearDownClass(inst):
		print("TearDown")
		inst.oHelper.TearDown()


if __name__ == '__main__':
	unittest.main()
