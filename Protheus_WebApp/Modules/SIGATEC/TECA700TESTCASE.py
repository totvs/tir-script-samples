from tir import Webapp
import unittest

class TECA700(unittest.TestCase):


	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGATEC","11/12/2020","T1","D MG 01","28")
		inst.oHelper.Program("TECA700")
	def test_TECA700_001(self):
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetButton("OK")
		self.oHelper.SetValue("ABH_CODCLI","000001")
		self.oHelper.SetValue("ABH_LOJA","01")
		self.oHelper.SetValue("ABH_DESCRI","PROJETO TESTE")
		self.oHelper.SetValue("ABH_REFER","01/01/2020")
		self.oHelper.SetValue("ABH_ENTREG","30/12/2020")
		self.oHelper.SetValue("ABH_CODPRO","COM000000000000000000000000110")
		self.oHelper.SetValue("ABH_CPAGPV","001")

		self.oHelper.SetValue("ABI_ETAPA","00", grid=True)
		self.oHelper.SetValue("ABI_DESCRI","ETAPA 01",grid=True)
		self.oHelper.SetValue("ABI_VALOR","100,00",grid=True)
		self.oHelper.SetValue("ABI_CODPRO"," COM00000000000000000000000011",grid=True)

		self.oHelper.SetValue("ABI_CODPRB","OC01  ",grid=True)
		self.oHelper.SetValue("ABI_INIPRV","01/01/2020",grid=True)
		self.oHelper.SetValue("ABI_FIMPRV","05/01/2020",grid=True)
		self.oHelper.LoadGrid()

		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("Cancelar")
		self.oHelper.SetButton("Alterar")
		self.oHelper.SetValue("ABH_DESCRI","PROJETO TESTE2")

		self.oHelper.SetKey("F4")
		
		self.oHelper.SetValue("ABJ_TAREFA","T1",grid=True)
		self.oHelper.SetValue("ABJ_DESCRI","TAREFA 001",grid=True)
		self.oHelper.SetValue("ABJ_TPREVI","0000:59",grid=True)
		self.oHelper.SetValue("ABJ_TORCAD","0000:59",grid=True)
		self.oHelper.LoadGrid()
		
		self.oHelper.CheckResult("ABJ_TAREFA","T1",grid=True, line=1)
		self.oHelper.CheckResult("ABJ_DESCRI","TAREFA 001",grid=True,line=1)
		self.oHelper.CheckResult("ABJ_TPREVI","0000:59",grid=True, line=1)
		self.oHelper.CheckResult("ABJ_TORCAD","0000:59",grid=True, line=1)
		self.oHelper.LoadGrid()
		
		self.oHelper.SetButton("Salvar")
			
		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("ABH_CODCLI","000001")
		self.oHelper.CheckResult("ABH_LOJA","01")
		self.oHelper.CheckResult("ABH_DESCRI","PROJETO TESTE2")
		self.oHelper.CheckResult("ABH_REFER","01/01/2020")
		self.oHelper.CheckResult("ABH_ENTREG","30/12/2020")
		self.oHelper.CheckResult("ABH_CODPRO","COM000000000000000000000000110")
		self.oHelper.CheckResult("ABH_CPAGPV","001")

		self.oHelper.CheckResult("ABI_ETAPA","00", grid=True, line=1)
		self.oHelper.CheckResult("ABI_DESCRI","ETAPA 01",grid=True, line=1)
		self.oHelper.CheckResult("ABI_VALOR","100,00",grid=True, line=1)
		self.oHelper.CheckResult("ABI_CODPRO"," COM00000000000000000000000011",grid=True, line=1)
		self.oHelper.CheckResult("ABI_CODPRB","OC01  ",grid=True, line=1)
		self.oHelper.CheckResult("ABI_INIPRV","01/01/2020",grid=True, line=1)
		self.oHelper.CheckResult("ABI_FIMPRV","05/01/2020",grid=True, line=1)
		self.oHelper.LoadGrid()
		
		self.oHelper.AssertTrue()


	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()