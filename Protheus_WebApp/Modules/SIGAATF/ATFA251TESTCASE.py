from tir import Webapp
import unittest

class ATFA251(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGAATF','10/10/2016','T1','M SP 01 ','01')
		inst.oHelper.Program('ATFA251') 
		inst.oHelper.AddParameter("M SP 01 MV_ULTDEPR","" , "20160930")
		inst.oHelper.AddParameter("M PR 01 MV_ULTDEPR","" , "20160930")
		inst.oHelper.SetParameters()

	def test_ATFA251_CT002(self):
		codigo     = 'ATFTIR0003'
		codigonovo = 'ATFTIR0004'
		
		self.oHelper.SearchBrowse(f'M SP 01 {codigo}0001', 'Filial+cod. do Bem + Item') 
		self.oHelper.SetButton('Transfere')
		self.oHelper.SetValue('Mostra Lanc Baixa ?'         ,'Nao'          )           
		self.oHelper.SetValue('Aglutina Lanc Baixa ?'       ,'Nao'          )         
		self.oHelper.SetValue('Repete Chapa ?'              ,'Sim'          )             
		self.oHelper.SetValue('Considera Bens ?'            ,'Todos'        )           
		self.oHelper.SetValue('Descricao Estendida ?'       ,'Desconsiderar')         
		self.oHelper.SetValue('Permite adicao novos tipos ?','Nao'          ) 
		self.oHelper.SetValue('Tipo Saldo Gerencial ?'      ,'1'            )        
		self.oHelper.SetValue('Contabiliza Online ?'        ,'Não'          )         
		self.oHelper.SetButton('OK')    
		self.oHelper.SetValue('MV_PAR01',codigo )
		self.oHelper.SetValue('MV_PAR02',codigo )        
		self.oHelper.SetButton('OK')
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetValue('Codigo Base'    ,codigonovo  ,grid=True, grid_number=1)
		self.oHelper.SetValue('Item Base'      ,'0001'      ,grid=True, grid_number=1)
		self.oHelper.SetValue('Descr Sintetica','TESTE TIR' ,grid=True, grid_number=1)
		self.oHelper.SetValue('Quantd'         ,'1,000'     ,grid=True, grid_number=1)
		self.oHelper.SetValue('Chapa'          ,codigonovo  ,grid=True, grid_number=1)
		self.oHelper.SetValue('Historico'      ,codigonovo  ,grid=True, grid_number=1)
		self.oHelper.SetValue('Conta'          ,'0123456789',grid=True, grid_number=1)
		self.oHelper.SetValue('Val Orig M1'    ,'10000,00'  ,grid=True, grid_number=1)		
		self.oHelper.LoadGrid()
		self.oHelper.SetButton('Salvar')	
		self.oHelper.SearchBrowse(f'M SP 01 {codigo}0001', 'Filial+cod. do Bem + Item') 
		self.oHelper.SetButton('Outras Ações','Canc. Transf')
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SearchBrowse(f'M SP 01 {codigonovo}0001','Filial+cod. do Bem + Item')
		self.oHelper.SetButton('Visualizar')
		self.oHelper.CheckResult('N1_CBASE',codigonovo)
		self.oHelper.CheckResult('N1_ITEM' ,'0001')
		self.oHelper.SetButton("Fechar")
		self.oHelper.AssertFalse()	
	
	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()