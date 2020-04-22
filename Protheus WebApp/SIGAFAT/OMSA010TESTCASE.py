from tir import Webapp
import unittest
import time

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

	def test_OMSA010_CT036(self):
		self.oHelper.AddParameter("MV_LJGRINT","D MG 01",".T.",".T.",".T.")
		self.oHelper.SetParameters() 				

		self.oHelper.SearchBrowse('D MG    TR3')
		self.oHelper.SetButton('Alterar')

		self.oHelper.SetValue('DA0_DESCRI', 'ALTERADO')

		self.oHelper.SetValue("Cod.Produto", "FAT001"	, grid=True, row=1)
		self.oHelper.SetValue("Preco Venda", "2,00"		, grid=True, row=1)
		self.oHelper.LoadGrid()

		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('D MG    TR3')
		self.oHelper.SetButton('Outras Ações', 'Visualizar')
		
		self.oHelper.CheckResult('DA0_CODTAB', 'TR3')
		self.oHelper.CheckResult('DA0_DESCRI','ALTERADO')
		
		self.oHelper.CheckResult("Cod.Produto", " FAT001", grid=True, line=1)
		self.oHelper.CheckResult("Preco Venda", " 2,00"	, grid=True, line=1)
		self.oHelper.LoadGrid()
		
		self.oHelper.SetButton("Fechar")
		
		self.oHelper.RestoreParameters()

		self.oHelper.AssertTrue()		

	def test_OMSA010_CT037(self):
		self.oHelper.SearchBrowse('D MG    TR4')
		self.oHelper.SetButton('Outras Ações', 'Excluir')

		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')
		
		self.oHelper.AssertTrue()				

	def test_OMSA010_CT038(self):
		self.oHelper.SearchBrowse('D MG    TR5')
		self.oHelper.SetButton('Outras Ações', 'Reajuste')

		self.oHelper.SetButton('Param.')

		self.oHelper.SetValue('Fator de Reajust. ?'				, '0,5000')		
		self.oHelper.SetValue('Produto Inicial ?'				, 'FTR041')
		self.oHelper.SetValue('Produto Final ?'					, 'FTR041')
		self.oHelper.SetValue('Grupo Inicial ?'					, '')
		self.oHelper.SetValue('Grupo Final ?'					, 'ZZZZ')
		self.oHelper.SetValue('Tipo Inicial ?'					, '')
		self.oHelper.SetValue('Tipo Final ?'					, 'ZZ')
		self.oHelper.SetValue('Tabela Inicial ?'				, 'TR5')
		self.oHelper.SetValue('Tabela Final ?'					, 'TR5')		
		self.oHelper.SetValue('Número de Decimais ?'			, '2')
		self.oHelper.SetValue('Atualiza preço base(produto) ?'	, 'Sim')		

		self.oHelper.SetButton('OK')

		self.oHelper.SetButton('Ok')

		self.oHelper.SearchBrowse('D MG    TR5')
		self.oHelper.SetButton('Outras Ações', 'Visualizar')
		
		self.oHelper.CheckResult('DA0_CODTAB', 'TR5')
		self.oHelper.CheckResult("Preco Venda", " 1,00"	, grid=True, line=2)
		self.oHelper.LoadGrid()
		
		self.oHelper.SetButton("Fechar")
		
		self.oHelper.AssertTrue()			

	def test_OMSA010_CT039(self):
		
		self.oHelper.SetButton('Outras Ações', 'Gerar')

		self.oHelper.SetBranch("D MG 01 ")

		self.oHelper.SetValue('Produto de ?'				, 'FAT001')		
		self.oHelper.SetValue('Produto ate ?'				, 'FAT001')
		self.oHelper.SetValue('Grupo de ?'					, '')
		self.oHelper.SetValue('Grupo ate ?'					, 'ZZZZ')
		self.oHelper.SetValue('Tipo de ?'					, '')
		self.oHelper.SetValue('Tipo ate ?'					, 'ZZ')
		self.oHelper.SetValue('Dt.de vigencia inicial ?'	, '12/09/2019')

		self.oHelper.SetButton('OK')

		self.oHelper.SetValue('DA0_CODTAB', 'TR6')
		self.oHelper.SetValue('DA0_DESCRI', 'CASO DE TESTE TIR6')

		self.oHelper.SetValue("Preco Venda", "1,00"		, grid=True,row=1)
		self.oHelper.LoadGrid()

		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('D MG    TR6')
		self.oHelper.SetButton('Outras Ações', 'Visualizar')
		
		self.oHelper.CheckResult('DA0_CODTAB', 'TR6')
		self.oHelper.CheckResult('DA0_DESCRI','CASO DE TESTE TIR6')
		
		self.oHelper.CheckResult("Cod.Produto", " FAT001", grid=True)
		self.oHelper.CheckResult("Preco Venda", " 1,00"	, grid=True)
		
		self.oHelper.LoadGrid()
		
		self.oHelper.SetButton("Fechar")
		
		self.oHelper.AssertTrue()

	def test_OMSA010_CT040(self):
		self.oHelper.AddParameter("MV_GRADE","D MG 01",".T.",".T.",".T.")
		self.oHelper.SetParameters() 						

		self.oHelper.SearchBrowse('D MG    TR7')
		self.oHelper.SetButton('Alterar')

		self.oHelper.SetValue('DA0_DESCRI', 'ALTERADO')
        
		self.oHelper.SetFocus('Preco Venda', grid_cell = True)
		time.sleep(15)
		self.oHelper.SetKey('ENTER')
		self.oHelper.SetButton("Cancelar")

		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.SearchBrowse('D MG    TR7')
		self.oHelper.SetButton('Outras Ações', 'Visualizar')
		
		self.oHelper.CheckResult('DA0_CODTAB', 'TR7')
		
		self.oHelper.SetButton("Fechar")

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch("D MG 01 ")

		self.oHelper.SetValue('DA0_CODTAB', 'TR8')
		self.oHelper.SetValue('DA0_DESCRI', 'CASO DE TESTE TIR8')

		self.oHelper.SetValue("Cod.Produto" , "FAT00000000000000000000001"		, grid=True ,row=1)
		self.oHelper.LoadGrid()

		self.oHelper.SetFocus('Preco Venda', grid_cell = True)
		time.sleep(15)		
		self.oHelper.SetKey('ENTER')
		self.oHelper.SetButton("Cancelar")		

		self.oHelper.SetButton('Fechar')
		self.oHelper.SetButton('Sair da página')		

		self.oHelper.RestoreParameters()
		
		self.oHelper.SetButton("X")

		self.oHelper.AssertTrue()	
			
	def test_OMSA010_CT041(self):
		
		self.oHelper.Program('MATA010')

		self.oHelper.SearchBrowse('D MG 01 FAT001')
		self.oHelper.SetButton("Outras Ações", "Relacionadas, Adic. Tab. Preço")
		self.oHelper.SetBranch("D MG 01 ")

		self.oHelper.SetValue("Cod. Tabela", "001"		, grid=True, row=1)
		self.oHelper.SetValue("Preco Venda", "1,00"		, grid=True, row=1)
		self.oHelper.LoadGrid()		

		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()