from tir import Webapp
from datetime import datetime
DataSystem = datetime.today().strftime('%d/%m/%Y')
import unittest

class MATA415(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAFAT', DataSystem,'T1','D MG 01 ','05')
		inst.oHelper.Program('MATA415')

	def test_MATA415_CT040(self):
		self.oHelper.AddParameter("MV_BLQMAR","D MG 01",".T.",".T.",".T.")
		self.oHelper.SetParameters()

		pedido = 'TIR001'		
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetBranch("D MG 01 ")
		self.oHelper.SetValue("CJ_NUM", pedido)
		self.oHelper.SetValue("CJ_PROSPE","FAT001")
		self.oHelper.SetValue("CJ_LOJPRO","01")
		self.oHelper.SetValue("CJ_CONDPAG","000")
		self.oHelper.SetValue("CK_PRODUTO", "FAT000000000000000000000000001", grid=True)
		self.oHelper.SetValue("CK_QTDVEN", "1,00", grid=True)
		self.oHelper.LoadGrid()
		self.oHelper.SetFocus('Quantidade', grid_cell = True)
		self.oHelper.SetKey('F4')		
		self.oHelper.SetValue("CL_PRODUTO", "FAT001", grid=True)
		self.oHelper.SetValue("CL_QUANT", "1,00", grid=True)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton("Salvar")
		self.oHelper.SetKey('ENTER')		
		self.oHelper.SetFocus('Prc Unitario', grid_cell = True)
		self.oHelper.SetKey('F4')		
		self.oHelper.SetButton("Voltar")
		self.oHelper.WaitHide("Saldos em Estoque")
		self.oHelper.SetKey('ENTER')		
		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("Cancelar")	
		self.oHelper.SearchBrowse(f"D MG 01 {pedido}")	
		self.oHelper.SetButton("Visualizar")	
		self.oHelper.CheckResult("CJ_NUM", pedido)
		self.oHelper.CheckResult("CJ_PROSPE","FAT001")
		self.oHelper.CheckResult("CJ_LOJPRO","01")
		self.oHelper.CheckResult("CJ_CONDPAG","000")	
		self.oHelper.CheckResult("CK_PRODUTO", " FAT000000000000000000000000001", grid=True, line=1)
		self.oHelper.CheckResult("CK_QTDVEN", " 1,00", grid=True, line=1)	
		self.oHelper.LoadGrid()	
		self.oHelper.SetButton("Cancelar")
		self.oHelper.RestoreParameters()
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()