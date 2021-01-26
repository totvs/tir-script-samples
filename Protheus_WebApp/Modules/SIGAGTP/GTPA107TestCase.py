from tir import Webapp
import unittest

class GTPA107(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAGTP", "20/04/2020", "T1", "D MG 01 ")
		inst.oHelper.Program('GTPA107')

	def test_GTPA107_CT001(self):
		self.oHelper.SearchBrowse("D MG    000033", "Filial+lote Remessa")
		self.oHelper.SetButton("Visualizar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.AssertTrue()

	def test_GTPA107_CT002(self):
		self.oHelper.SearchBrowse("D MG    000033", "Filial+lote Remessa")
		self.oHelper.SetButton("Outras Ações", "Cancelar Remessa")
		self.oHelper.SetButton("OK")
		self.oHelper.SetValue('GQG_NUMINI', '000010')
		self.oHelper.SetValue('GQG_NUMFIM', '000010')
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.AssertTrue()

	def test_GTPA107_CT003(self):
		self.oHelper.SearchBrowse("D MG    000034", "Filial+lote Remessa")
		self.oHelper.SetButton("Outras Ações", "Transferir Remessa")
		self.oHelper.SetButton("OK")
		self.oHelper.SetValue('GQG_NUMINI', '000010')
		self.oHelper.SetValue('GQG_NUMFIM', '000010')
		self.oHelper.SetValue('GQG_AGENCI', 'AGREM5')
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.AssertTrue()

	def test_GTPA107_CT004(self):
		self.oHelper.SearchBrowse("D MG    000035", "Filial+lote Remessa")
		self.oHelper.SetButton("Outras Ações", "Devolução de Remessa")
		self.oHelper.SetButton("OK")
		self.oHelper.SetValue('GQG_NUMINI', '000010')
		self.oHelper.SetValue('GQG_NUMFIM', '000010')
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.AssertTrue()

	def test_GTPA107_CT006(self):
		self.oHelper.SearchBrowse("D MG    000042", "Filial+lote Remessa")
		self.oHelper.SetButton("Outras Ações", "Baixa Protocolo")
		self.oHelper.SetButton("Sim")
		self.oHelper.SetButton("Fechar")
		self.oHelper.AssertTrue()

	def test_GTPA107_CT007(self):
		self.oHelper.SearchBrowse("D MG    000043", "Filial+lote Remessa")
		self.oHelper.SetButton("Outras Ações", "Estorno Baixa Protocolo")
		self.oHelper.SetButton("Sim")
		self.oHelper.SetButton("Fechar")
		self.oHelper.AssertTrue()



	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()	

if __name__ == '__main__':
	unittest.main()
