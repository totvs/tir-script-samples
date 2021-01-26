from tir import Webapp
import unittest

class MATA093(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAPCP','22/04/2019','T1','D MG 01 ','10')
		inst.oHelper.Program('MATA093')

	def test_MATA093_001(self):

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch('D MG 01')

		self.oHelper.SetButton('Ok')

		self.oHelper.SetValue('BP_BASE', 'PCP_TIR_MATA093_CFGPRD_001')

		self.oHelper.LoadGrid()	
		self.oHelper.SetValue('BQ_ID', '0000000001', grid=True)
		self.oHelper.LoadGrid()	
		self.oHelper.SetValue('BQ_CARACT', 'COR', grid=True)
		self.oHelper.LoadGrid()	
		self.oHelper.SetValue('BQ_TAMANHO', '2', grid=True)
		self.oHelper.LoadGrid()	
		self.oHelper.SetValue('BQ_DESCR', 'COR', grid=True)
		self.oHelper.LoadGrid()	

		self.oHelper.SetKey('DOWN', grid=True)	

		self.oHelper.LoadGrid()	
		self.oHelper.SetValue('BQ_ID', '0000000002', grid=True, row=2)
		self.oHelper.LoadGrid()	
		self.oHelper.SetValue('BQ_CARACT', 'TAMANHO', grid=True, row=2)
		self.oHelper.LoadGrid()	
		self.oHelper.SetValue('BQ_TAMANHO', '2', grid=True, row=2)
		self.oHelper.LoadGrid()	
		self.oHelper.SetValue('BQ_DESCR', 'TAMANHO', grid=True, row=2)
		self.oHelper.LoadGrid()	

		self.oHelper.SetButton('Salvar')

		self.oHelper.SetButton('Cancelar')

		self.oHelper.SetButton('Visualizar')


		self.oHelper.CheckResult('BP_BASE', 'PCP_TIR_MATA093_CFGPRD_001')

		self.oHelper.LoadGrid()	
		self.oHelper.CheckResult('BQ_ID', '0000000001', grid=True, line=1)
		self.oHelper.LoadGrid()	
		self.oHelper.CheckResult('BQ_CARACT', 'COR', grid=True, line=1)
		self.oHelper.LoadGrid()	
		self.oHelper.CheckResult('BQ_TAMANHO', '2', grid=True, line=1)
		self.oHelper.LoadGrid()	
		self.oHelper.CheckResult('BQ_DESCR', 'COR', grid=True, line=1)
		self.oHelper.LoadGrid()	

		self.oHelper.SetKey('DOWN')	

		self.oHelper.LoadGrid()	
		self.oHelper.CheckResult('BQ_ID', '0000000002', grid=True, line=2)
		self.oHelper.LoadGrid()	
		self.oHelper.CheckResult('BQ_CARACT', 'TAMANHO', grid=True, line=2)
		self.oHelper.LoadGrid()	
		self.oHelper.CheckResult('BQ_TAMANHO', '2', grid=True, line=2)
		self.oHelper.LoadGrid()	
		self.oHelper.CheckResult('BQ_DESCR', 'TAMANHO', grid=True, line=2)
		self.oHelper.LoadGrid()	

		self.oHelper.SetButton('Cancelar')
		
		self.oHelper.AssertTrue()

	def test_MATA093_002(self):
    

		self.oHelper.SearchBrowse('D MG 01 PCP_TIR_MATA093_CFGPRD_002', 'Filial+conteudo')

		self.oHelper.SetButton('Alterar')

		self.oHelper.SetValue('BQ_PRISEC', '1', grid=True)
		self.oHelper.LoadGrid()	
		
		self.oHelper.SetButton('Salvar')

		self.oHelper.SetButton('Visualizar')

		self.oHelper.CheckResult('BP_BASE', 'PCP_TIR_MATA093_CFGPRD_002')

		self.oHelper.LoadGrid()	
		self.oHelper.CheckResult('BQ_ID', '0000000001', grid=True, line=1)
		self.oHelper.LoadGrid()	
		self.oHelper.CheckResult('BQ_PRISEC', 'Primario', grid=True, line=1)
		self.oHelper.LoadGrid()	

		self.oHelper.SetButton('Cancelar')
		
		self.oHelper.AssertTrue()

	def test_MATA093_003(self):
        

		self.oHelper.SearchBrowse('D MG 01 PCP_TIR_MATA093_CFGPRD_003', 'Filial+conteudo')

		self.oHelper.SetButton('Outras Ações','Excluir')
	
		self.oHelper.SetButton('Confirmar')

		self.oHelper.AssertTrue()


	def test_MATA093_004(self):
        

		self.oHelper.SearchBrowse('D MG 01 PCP_TIR_MATA093_CFGPRD_002', 'Filial+conteudo')

		self.oHelper.SetButton('Outras Ações','Dados Padrões')

		self.oHelper.SetValue('BR_DESCPRD', 'PCP_TIR_MATA093')
		self.oHelper.SetValue('BR_TIPO', 'PA')
		self.oHelper.SetValue('BR_UM', 'UN')
		self.oHelper.SetValue('BR_LOCPAD', '01')

		self.oHelper.SetButton('Confirmar')

		self.oHelper.AssertTrue()


	def test_MATA093_005(self):
        

		self.oHelper.SearchBrowse('D MG 01 PCP_TIR_MATA093_CFGPRD_004', 'Filial+conteudo')

		self.oHelper.SetButton('Outras Ações','siMulacäo')

		self.oHelper.SetValue('COR', 'AM')

		self.oHelper.SetButton('Confirmar')

		self.oHelper.SetButton('Incluir')

		self.oHelper.SetButton('Confirmar')

		self.oHelper.SetButton('Não')

		self.oHelper.AssertTrue()

	def test_MATA093_006(self):
        

		self.oHelper.SearchBrowse('D MG 01 PCP_TIR_MATA093_CFGPRD_004', 'Filial+conteudo')

		self.oHelper.SetButton('Outras Ações','Gera Autom')

		self.oHelper.WaitShow('GERA AUTOM')

		self.oHelper.SetKey('ENTER')
		self.oHelper.SetKey('DOWN')
		self.oHelper.SetKey('ENTER')

		self.oHelper.SetButton('Confirmar')

		self.oHelper.SetButton('Não')
		
		self.oHelper.AssertTrue()


	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()