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

	def test_ATFA251_CT001(self):
        
		#Posiciona no registro
		codigo     = 'ATFTIR0001'
		codigonovo = 'ATFTIR0002'

		self.oHelper.SearchBrowse(f'M SP 01 {codigo}0001', 'Filial+cod. do Bem + Item') 

        #Seleciona a opção do botão
		self.oHelper.SetButton('Outras Ações','Detalhar')

        #Preenche os perguntes    
		self.oHelper.SetValue('Mostra Lanc Baixa ?'         ,'Nao'          ) #Mostra Lanc Baixa ?             
		self.oHelper.SetValue('Aglutina Lanc Baixa ?'       ,'Nao'          ) #Aglutina Lanc Baixa ?         
		self.oHelper.SetValue('Repete Chapa ?'              ,'Sim'          ) #Repete Chapa ?                
		self.oHelper.SetValue('Considera Bens ?'            ,'Todos'        ) #Considera Bens ?              
		self.oHelper.SetValue('Descricao Estendida ?'       ,'Desconsiderar') #Descricao Estendida ?         
		self.oHelper.SetValue('Permite adicao novos tipos ?','Nao'          ) #Permite adicao novos tipos ?  
		self.oHelper.SetValue('Tipo Saldo Gerencial ?'      ,'1'             ) #Tipo Saldo Gerencial ?          
		self.oHelper.SetValue('Contabiliza Online ?'        ,'Não'          ) #Contabiliza Online ?           

        #Seleciona a opção do botão
		self.oHelper.SetButton('OK')

        #Preenche os perguntes    
		self.oHelper.SetValue('MV_PAR01',codigonovo ) #Novo Bem           
		self.oHelper.SetValue('MV_PAR02','Dados'    ) #Dados         
		self.oHelper.SetValue('MV_PAR03','Rateio'   ) #Rateio  

		self.oHelper.SetButton('OK')

		self.oHelper.SetValue('Percentual','50,00',grid=True)
		
		self.oHelper.SetKey('DOWN', grid=True)

		self.oHelper.SetValue('Percentual','50,00',grid=True)

		self.oHelper.LoadGrid()

		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Sim')
		self.oHelper.SetButton('Confirmar')

		self.oHelper.SearchBrowse(f'M SP 01 {codigonovo}0001','Filial+cod. do Bem + Item')
		self.oHelper.SetButton('Visualizar')
		self.oHelper.CheckResult('N1_CBASE',codigonovo)
		self.oHelper.CheckResult('N1_ITEM','0001')
		
		self.oHelper.SetButton('Fechar')
		self.oHelper.AssertTrue()		
		
	def test_ATFA251_CT002(self):
        
		#Posiciona no registro
		codigo     = 'ATFTIR0003'
		codigonovo = 'ATFTIR0004'
		
		self.oHelper.SearchBrowse(f'M SP 01 {codigo}0001', 'Filial+cod. do Bem + Item') 

        #Seleciona a opção do botão
		self.oHelper.SetButton('Transfere')

        #Preenche os perguntes    
		self.oHelper.SetValue('Mostra Lanc Baixa ?'         ,'Nao'          ) #Mostra Lanc Baixa ?             
		self.oHelper.SetValue('Aglutina Lanc Baixa ?'       ,'Nao'          ) #Aglutina Lanc Baixa ?         
		self.oHelper.SetValue('Repete Chapa ?'              ,'Sim'          ) #Repete Chapa ?                
		self.oHelper.SetValue('Considera Bens ?'            ,'Todos'        ) #Considera Bens ?              
		self.oHelper.SetValue('Descricao Estendida ?'       ,'Desconsiderar') #Descricao Estendida ?         
		self.oHelper.SetValue('Permite adicao novos tipos ?','Nao'          ) #Permite adicao novos tipos ?  
		self.oHelper.SetValue('Tipo Saldo Gerencial ?'      ,'1'             ) #Tipo Saldo Gerencial ?          
		self.oHelper.SetValue('Contabiliza Online ?'        ,'Não'          ) #Contabiliza Online ?           

        #Seleciona a opção do botão
		self.oHelper.SetButton('OK')

        #Preenche os perguntes    
		self.oHelper.SetValue('MV_PAR01',codigo ) #Do codigo
		self.oHelper.SetValue('MV_PAR02',codigo ) #Ate o codigo         

		self.oHelper.SetButton('OK')

		self.oHelper.SetButton('Salvar')

		#self.oHelper.ClickFolder('Dados do Bem')

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
	
	def test_ATFA251_CT003(self):
        
		#self.oHelper.ChangeEnvironment(date='10/03/2016', group = 'T1', branch = 'M PR 01', module = 'SIGAATF')

		#self.oHelper.Program('ATFA251')

		self.oHelper.WaitShow("Aquisicao por Transferencia")

		#Posiciona no registro
		codigoDe      = 'NFE0000026'		
		codigoAte     = 'NFE0000026'
		codigonovo = 'ATFA251_01'

		self.oHelper.SearchBrowse(f'M PR 01 {codigoDe}0001', 'Filial+cod. do Bem + Item') 

        #Seleciona a opção do botão
		self.oHelper.SetButton('Outras Ações','Agrupar')

        #Preenche os perguntes    
		self.oHelper.SetValue('Mostra Lanc Baixa ?'         ,'Nao'          ) #Mostra Lanc Baixa ?             
		self.oHelper.SetValue('Aglutina Lanc Baixa ?'       ,'Nao'          ) #Aglutina Lanc Baixa ?         
		self.oHelper.SetValue('Repete Chapa ?'              ,'Sim'          ) #Repete Chapa ?                
		self.oHelper.SetValue('Considera Bens ?'            ,'Adiantamentos') #Considera Bens ?              
		self.oHelper.SetValue('Descricao Estendida ?'       ,'Desconsiderar') #Descricao Estendida ?         
		self.oHelper.SetValue('Permite adicao novos tipos ?','Sim'          ) #Permite adicao novos tipos ?  
		self.oHelper.SetValue('Tipo Saldo Gerencial ?'      ,'1'             ) #Tipo Saldo Gerencial ?          
		self.oHelper.SetValue('Contabiliza Online ?'        ,'Não'          ) #Contabiliza Online ?           

        #Seleciona a opção do botão
		self.oHelper.SetButton('OK')

        #Preenche os perguntes    
		self.oHelper.SetValue('MV_PAR01',codigoDe    ) #Do codigo
		self.oHelper.SetValue('MV_PAR02',codigoAte    ) #Ate o codigo
		self.oHelper.SetValue('MV_PAR03',codigonovo ) #Novo código          
		self.oHelper.SetValue('MV_PAR04','Dados'    ) #Dados         
		self.oHelper.SetValue('MV_PAR05','Rateio'   ) #Rateio  

		self.oHelper.SetButton('OK')

		self.oHelper.ClickBox("", grid_number=1)

		self.oHelper.SetButton('Confirmar')

		self.oHelper.SetValue('Quantd','1,000', grid=True) 		
		self.oHelper.LoadGrid()

		self.oHelper.SetButton('Confirmar')
		
		self.oHelper.SearchBrowse(f'M PR 01 {codigonovo}0001', 'Filial+cod. do Bem + Item') 
		self.oHelper.SetButton('Visualizar')
		self.oHelper.CheckResult('N1_CBASE',codigonovo)
		self.oHelper.CheckResult('N1_ITEM','0001')
		self.oHelper.CheckResult('N1_ICMSAPR','5.400,00')
		
		self.oHelper.SetButton('Fechar')
		self.oHelper.AssertTrue()	

	def test_ATFA251_CT004(self):

		codigoATF = 'ATF2510001'     
		codigoNew = 'DET00001'

		self.oHelper.SearchBrowse(f'M PR 01 {codigoATF}')

		self.oHelper.SetButton("Outras Ações", "Detalhar")
		
		#Preenche os perguntes    
		self.oHelper.SetValue('Mostra Lanc Baixa ?'         ,'Nao'          ) #Mostra Lanc Baixa ?             
		self.oHelper.SetValue('Aglutina Lanc Baixa ?'       ,'Nao'          ) #Aglutina Lanc Baixa ?         
		self.oHelper.SetValue('Repete Chapa ?'              ,'Sim'          ) #Repete Chapa ?                
		self.oHelper.SetValue('Considera Bens ?'            ,'Todos') #Considera Bens ?              
		self.oHelper.SetValue('Descricao Estendida ?'       ,'Atribuir') #Descricao Estendida ?         
		self.oHelper.SetValue('Permite adicao novos tipos ?','Sim'          ) #Permite adicao novos tipos ?  
		self.oHelper.SetValue('Tipo Saldo Gerencial ?'      ,'1'             ) #Tipo Saldo Gerencial ?          
		self.oHelper.SetValue('Contabiliza Online ?'        ,'Não'          ) #Contabiliza Online ?   

		self.oHelper.SetButton("OK")

		#Preenche os perguntes    
		self.oHelper.SetValue('MV_PAR01',codigoNew ) #Novo Bem      
		self.oHelper.SetButton("Ok")

		#MENSAGEM DE VALIDAÇÃO
		self.oHelper.CheckHelp(text_help="AF251DESCEST", button="Fechar")
		self.oHelper.AssertTrue()
		

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()