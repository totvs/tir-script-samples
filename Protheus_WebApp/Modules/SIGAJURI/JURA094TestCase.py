from tir import Webapp
import unittest

class JURA094(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAJURI','20/02/2019','T1','D MG 01 ','05')
		inst.oHelper.Program('JURA162')
		inst.oHelper.AddParameter("MV_JVLHIST", "", "1", "", "")
		inst.oHelper.SetParameters()

	def test_JURA094_CT001(self):
		self.oHelper.SetValue("cValor","Contencioso",name_attr=True)
		self.oHelper.SetValue("NSZ_COD","0000000124")
		self.oHelper.ClickLabel("Pesquisar")
		self.oHelper.WaitHide("Pesquisando...")
		self.oHelper.SetValue("NSZ_LCLIEN","01")
		self.oHelper.ClickLabel("Alterar")
		self.oHelper.WaitHide("Carregando...")
		self.oHelper.SetValue("NSZ_LCLIEN","01")
		self.oHelper.SetButton("Outras Ações","Objetos")
		self.oHelper.ClickGridCell("Pedido",row=1)
		self.oHelper.SetButton("Alterar")
		self.oHelper.F3(field="NSY_CJUIZ",name_attr=True)
		self.oHelper.ClickGridCell("Código",row=1)
		self.oHelper.SetButton("Confirmar")
		self.oHelper.F3(field="NSY_CENVOL",name_attr=True)
		self.oHelper.ClickGridCell("Código",row=1)
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Sim")
		self.oHelper.SetValue("NUV_CMOTIV","0002")
		self.oHelper.SetValue("NUV_JUSTIF","TIR JURA094 - Alteração dos campos Cod. Juiz e Cod. Envolvido")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("Fechar")

		self.oHelper.SetButton("Outras Ações","Correção Valores,Correção Valores")
		self.oHelper.SetButton("Sim")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("Outras Ações","Histórico Objetos")
		self.oHelper.ClickGridCell("Cod Valor",row=5)
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("NZ1_ANOMES","201910",name_attr=True)
		self.oHelper.ClickFolder("Pedidos")
		self.oHelper.CheckResult("NZ1_PEVLRA","10.018,00",name_attr=True)
		self.oHelper.CheckResult("NZ1_CCORPE","18,00",name_attr=True)
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("X")

		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("NSY_CJUIZ","001",name_attr=True)
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("X")

		self.oHelper.AssertTrue()
		self.oHelper.RestoreParameters()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()