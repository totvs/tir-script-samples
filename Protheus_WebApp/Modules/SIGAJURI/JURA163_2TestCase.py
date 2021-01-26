from tir import Webapp
import unittest

class JURA163_2(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.SetTIRConfig(config_name="user", value="JuriCorresp")
		inst.oHelper.SetTIRConfig(config_name="password", value="juri")
		inst.oHelper.Setup('SIGAJURI','12/12/2019','T1','D MG 01 ','76')
		inst.oHelper.Program('JURA162')

	def test_JURA163_2_CT001(self):
		self.oHelper.SetValue('cValor','Contencioso',name_attr=True)
		self.oHelper.ClickLabel('Incluir com Modelo')
		self.oHelper.SearchBrowse("JURA163",key=3,index=True)
		self.oHelper.SetButton("Ok")
		self.oHelper.SetValue("NSZ_CCLIEN","JLT001")
		self.oHelper.SetValue("NSZ_LCLIEN","01")
		self.oHelper.SetValue("NSZ_CESCRI","SP100")
		self.oHelper.SetButton("Fechar",check_error=False)
		self.oHelper.F3(field='NSZ_CESCRI',name_attr=True)
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetValue("NSZ_CAREAJ","00004")
		self.oHelper.SetButton("Fechar",check_error=False)
		self.oHelper.F3(field='NSZ_CAREAJ',name_attr=True)
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetValue("NSZ_SIGLA1","CRS")
		self.oHelper.SetValue("NSZ_CFCORR","04")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("Follow-ups")
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetValue("NTA_CTIPO","00006")
		self.oHelper.SetValue("NTA_DTFLWP","12/12/2040")
		self.oHelper.SetValue("NTA_CCORRE","J163C1")
		self.oHelper.SetValue("NTA_LCORRE","01")
		self.oHelper.ClickGridCell("Sigla part",row=1)
		self.oHelper.SetValue("NTE_SIGLA","CRS",grid=True)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar",check_error=False)
		self.oHelper.SetButton("Fechar",check_error=False)
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("X")
		self.oHelper.SetButton("Fechar")
		self.oHelper.ClickLabel('Pesquisar')
		self.oHelper.SetButton("Sim")
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()
