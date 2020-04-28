from tir import Webapp
import unittest

class OMSA010(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAFAT','14/08/2019','T1','D MG 01 ','05')
		inst.oHelper.Program('OMSA010')

	def test_OMSA010_CT035(self):
		self.oHelper.AddParameter("MV_LJECOMM","D MG 01",".T.",".T.",".T.")
		self.oHelper.AddParameter("MV_LJGRINT","D MG 01",".T.",".T.",".T.")			
		self.oHelper.SetParameters() 
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch("D MG 01 ")
		self.oHelper.SetValue('DA0_CODTAB', 'TR2')
		self.oHelper.SetValue('DA0_DESCRI', 'CASO DE TESTE TIR2')
		self.oHelper.SetValue("Cod.Produto" , "FAT000000000000000000000000002"		, grid=True,row=1)
		self.oHelper.SetValue("Vlr.Desconto", "1,00"		, grid=True,row=1)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')
		self.oHelper.SearchBrowse('D MG    TR2')
		self.oHelper.SetButton('Outras Ações', 'Visualizar')	
		self.oHelper.CheckResult('DA0_CODTAB', 'TR2')
		self.oHelper.CheckResult('DA0_DESCRI','CASO DE TESTE TIR2')	
		self.oHelper.CheckResult("Cod.Produto", " FAT000000000000000000000000002"	, grid=True)
		self.oHelper.CheckResult("Preco Venda", " 99,00"	, grid=True)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton("Fechar")
		self.oHelper.AssertTrue()
		self.oHelper.RestoreParameters()		

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()