from tir import Webapp
from datetime import datetime
DataSystem = datetime.today().strftime('%d/%m/%Y')
import unittest
import time

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

		#self.oHelper.WaitHide("Sugestäo de Orcamento")
		#time.sleep(20)

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

	def test_MATA415_CT041(self):

		pedido = 'TIR002'		

		self.oHelper.SearchBrowse(f"D MG 01 {pedido}")
		
		self.oHelper.SetButton("Alterar")
		
		self.oHelper.SetValue("CJ_CONDPAG","001")

		self.oHelper.SetValue("CK_PRODUTO", "FAT000000000000000000000000001", grid=True)
		self.oHelper.SetValue("CK_QTDVEN", " 2,00", grid=True)

		self.oHelper.SetKey('DOWN', grid=True)

		self.oHelper.SetValue("CK_PRODUTO", "FAT000000000000000000000000001", grid=True)
		self.oHelper.SetValue("CK_QTDVEN", " 3,00", grid=True)

		self.oHelper.LoadGrid()

		self.oHelper.SetFocus('Quantidade', grid_cell = True, row_number = 2)
		self.oHelper.SetKey('F4')		

		self.oHelper.SetValue("CL_PRODUTO", "FAT001", grid=True)
		self.oHelper.SetValue("CL_QUANT", "1,00", grid=True)
		self.oHelper.LoadGrid()

		self.oHelper.SetButton("Salvar")		

		self.oHelper.SetKey('ENTER')	

		self.oHelper.SetButton("Salvar")

		self.oHelper.SearchBrowse(f"D MG 01 {pedido}")
		
		self.oHelper.SetButton("Visualizar")
		
		self.oHelper.CheckResult("CJ_NUM", pedido)
		self.oHelper.CheckResult("CJ_CONDPAG","001")
		
		self.oHelper.CheckResult("CK_PRODUTO", " FAT000000000000000000000000001", grid=True, line=1)
		self.oHelper.CheckResult("CK_QTDVEN", " 2,00", grid=True, line=1)
		self.oHelper.CheckResult("CK_PRODUTO", " FAT000000000000000000000000001", grid=True, line=2)
		self.oHelper.CheckResult("CK_QTDVEN", " 3,00", grid=True, line=2)		
		
		self.oHelper.LoadGrid()
		
		self.oHelper.SetButton("Cancelar")
		
		self.oHelper.AssertTrue()
		
	def test_MATA415_CT042(self):
		
		pedido = 'TIR004'
		
		self.oHelper.SearchBrowse(f"D MG 01 {pedido}")
		
		self.oHelper.SetButton('Outras Ações','Excluir')
		
		self.oHelper.SetButton("Confirmar")
		
		self.oHelper.AssertTrue()
        #Aguardando correção da Task 1558 subir para branch Master 
        
		#self.oHelper.SearchBrowse(f"D MG 01 {pedido}")
		
		#self.oHelper.SetButton("Visualizar")
		
		#self.oHelper.CheckResult("CJ_NUM", pedido)
		
		#self.oHelper.SetButton("Cancelar")
		
		#self.oHelper.AssertFalse()   
		
		
	def test_MATA415_CT043(self):
		
		pedidoOri = 'TIR002'
		pedido 	= 'TIR006'
		
		
		self.oHelper.SearchBrowse(f"D MG 01 {pedidoOri}")
		
		self.oHelper.SetButton('Outras Ações','Copiar')
		
		self.oHelper.SetValue("CJ_NUM", pedido)

		self.oHelper.SetButton("Salvar")
		
		self.oHelper.SearchBrowse(f"D MG 01 {pedido}")
		
		self.oHelper.SetButton("Visualizar")
		
		self.oHelper.CheckResult("CJ_NUM", pedido)
		
		self.oHelper.SetButton("Cancelar")
		
		self.oHelper.AssertTrue()

	def test_MATA415_CT044(self):
		
		pedido 	= 'TIR007'
		
		self.oHelper.SearchBrowse(f"D MG 01 {pedido}")
		
		self.oHelper.SetButton('Outras Ações','CaNcelar')
		
		self.oHelper.SetButton("Confirmar")
		
		self.oHelper.SearchBrowse(f"D MG 01 {pedido}")
		
		self.oHelper.SetButton("Visualizar")
		
		self.oHelper.CheckResult("CJ_NUM", pedido)
		
		self.oHelper.SetButton("Cancelar")
		
		self.oHelper.AssertTrue()	

	def test_MATA415_CT045(self):

		self.oHelper.AddParameter("MV_GRADE","D MG 01",".T.",".T.",".T.")
		self.oHelper.SetParameters()

		pedido = 'TIR008'

		self.oHelper.SearchBrowse(f"D MG 01 {pedido}")

		self.oHelper.SetButton("Alterar")
		
		self.oHelper.SetFocus('Quantidade', grid_cell = True)
		self.oHelper.SetKey('ENTER')	
		self.oHelper.WaitShow("Grade")	
		self.oHelper.SetValue("[GG] GRANDE", "1,00", grid=True)
		self.oHelper.SetValue("[MM] MEDIO", "1,00", grid=True)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton("Salvar")

		self.oHelper.SetButton("Salvar")

		self.oHelper.RestoreParameters()

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()