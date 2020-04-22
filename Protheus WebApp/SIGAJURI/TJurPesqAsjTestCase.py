from tir import Webapp
import unittest

class TJurPesqAsj(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAJURI','15/10/2018','T1','D MG 01 ','05')
		inst.oHelper.Program('JURA162')
		inst.oHelper.AddParameter("MV_JFTJURI", "", "2", "", "")
		inst.oHelper.SetParameters()

	def test_TJurPesqAsj_CT001(self):

		self.oHelper.SetValue("cValor","Contratos",name_attr=True)
		self.oHelper.SetValue("NSZ_CAREAJ","JUR01")
		self.oHelper.ClickLabel("Pesquisar")
		self.oHelper.WaitHide("Pesquisando...")
		self.oHelper.SetValue("NSZ_LCLIEN","01")
		self.oHelper.ClickLabel("Alteração em Lote")
		self.oHelper.SetValue("NSZ_CAREAJ","JUR02")
		self.oHelper.SetButton("Ok")
		self.oHelper.WaitHide("Processando...")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetValue("NSZ_CAREAJ","JUR02")
		self.oHelper.SetValue("NSZ_COD","0000000092")
		self.oHelper.ClickLabel("Pesquisar")
		self.oHelper.SetValue("NSZ_LCLIEN","01")
		self.oHelper.ClickGridCell("Area Juridica",row=1)
		self.oHelper.ClickLabel("Visualizar")
		self.oHelper.CheckResult("NSZ_CAREAJ","JUR02")
		self.oHelper.SetButton("Fechar")
		self.oHelper.ClickLabel("Sair")
		self.oHelper.AssertTrue()
		self.oHelper.RestoreParameters()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()
		

if __name__ == '__main__':
	unittest.main()
