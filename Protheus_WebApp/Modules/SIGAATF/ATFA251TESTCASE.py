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

		self.oHelper.SetValue('Codigo Base'    ,codigonovo  ,grid=True, grid_number=1,row=1)
		self.oHelper.SetValue('Item Base'      ,'0001'      ,grid=True, grid_number=1,row=1)
		self.oHelper.SetValue('Descr Sintetica','TESTE TIR' ,grid=True, grid_number=1,row=1)
		self.oHelper.SetValue('Quantd'         ,'1,000'     ,grid=True, grid_number=1,row=1)
		self.oHelper.SetValue('Chapa'          ,codigonovo  ,grid=True, grid_number=1,row=1)
		self.oHelper.SetValue('Historico'      ,codigonovo  ,grid=True, grid_number=1,row=1)
		self.oHelper.SetValue('Conta'          ,'0123456789',grid=True, grid_number=1,row=1)
		self.oHelper.SetValue('Val Orig M1'    ,'10000,00'  ,grid=True, grid_number=1,row=1)		
		self.oHelper.LoadGrid()

		#Aba Complementos
		self.oHelper.ClickFolder('Complementos')

		self.oHelper.SetValue('Tipo'        , '10'                   , grid=True, grid_number=1,row=1)
		self.oHelper.SetValue('Data Aquisic', "10/10/2016"             , grid=True, grid_number=1,row=1)
		self.oHelper.SetValue('Historico'   , 'TESTE COMPLEMENTO TIR', grid=True, grid_number=1,row=1)
		self.oHelper.SetValue('Conta'       , '0123456789'           , grid=True, grid_number=1,row=1)
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
		self.oHelper.SetValue('Permite adicao novos tipos ?','Nao'          ) #Permite adicao novos tipos ?  
		self.oHelper.SetValue('Tipo Saldo Gerencial ?'      ,''             ) #Tipo Saldo Gerencial ?          
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



	def test_ATFA251_CT005(self):

		# #codigoATF = 'ATF2510001'   
		codigoATF = '0000000001' 
		###mudo para a filial d mg 01 para conseguir setar o parametro
		self.oHelper.SetButton('x')
		self.oHelper.ChangeEnvironment("10/10/2016","T1", "D MG 01 ","01")  
		self.oHelper.Program("ATFA251") 
		
		self.oHelper.AddParameter("MV_ULTDEPR" ,'', "20160930")
		self.oHelper.SetParameters()
		###volto para a filial m sp 01 para corrigir posicionamento do item
		self.oHelper.SetButton('x')
		self.oHelper.ChangeEnvironment("10/10/2016","T1", "M SP 01 ","01") 

		self.oHelper.Program("ATFA251")

		self.oHelper.WaitShow("Aquisicao por Transferencia")

		self.oHelper.SearchBrowse(f'D MG 01 {codigoATF}001', 'Filial+cod. do Bem + Item') 

		self.oHelper.SetButton("Transfere")
		
		###Preenche os perguntes    
		self.oHelper.SetValue('Mostra Lanc Baixa ?'         ,'Nao'          ) #Mostra Lanc Baixa ?             
		self.oHelper.SetValue('Aglutina Lanc Baixa ?'       ,'Nao'          ) #Aglutina Lanc Baixa ?         
		self.oHelper.SetValue('Repete Chapa ?'              ,'Sim'          ) #Repete Chapa ?                
		self.oHelper.SetValue('Considera Bens ?'            ,'Todos') #Considera Bens ?              
		self.oHelper.SetValue('Descricao Estendida ?'       ,'Desconsiderar') #Descricao Estendida ?         
		self.oHelper.SetValue('Permite adicao novos tipos ?','Sim'          ) #Permite adicao novos tipos ?  
		self.oHelper.SetValue('Tipo Saldo Gerencial ?'      ,'1'             ) #Tipo Saldo Gerencial ?          
		self.oHelper.SetValue('Contabiliza Online ?'        ,'Não'          ) #Contabiliza Online ?   

		self.oHelper.SetButton("OK")

		#Preenche os perguntes    
		self.oHelper.SetValue('MV_PAR01',codigoATF ) #Do codigo 
		self.oHelper.SetValue('MV_PAR02',codigoATF )    #ate o codigo
		self.oHelper.SetButton("Ok")

		self.oHelper.ClickBox('Codigo Item ', contents_list='001', select_all=False, grid_number=1)
		self.oHelper.SetButton('Cancelar')

		self.oHelper.SetButton("Transfere")
		self.oHelper.SetButton("OK")
		self.oHelper.SetButton("Ok")

		self.oHelper.ClickBox('Codigo Item ', contents_list='001', select_all=False, grid_number=1)
		self.oHelper.ClickBox('Codigo Item ', contents_list='001', select_all=False, grid_number=1)
		self.oHelper.SetButton('Salvar')
		
		self.oHelper.SetValue('Tipo deprec'    ,'7' ,grid=True, grid_number=1,row=1)
		self.oHelper.SetValue('Per Deprec','2',grid=True, grid_number=1,row=1)
		self.oHelper.LoadGrid()
		self.oHelper.CheckHelp(text='AF010FDNTUS',button='Fechar')
		self.oHelper.SetValue('Vl Max Depre','2,00',grid=True, grid_number=1,row=1)
		self.oHelper.LoadGrid()
		self.oHelper.CheckHelp(text='AF010VMXDEPR',button='Fechar')
		self.oHelper.AssertTrue()


	def test_ATFA251_CT006(self):
        

		self.oHelper.WaitShow("Aquisicao por Transferencia")

		#Posiciona no registro
		#codigoATF =    '0000000001' 
		codigoDe      = 'ATF100    '
		codigoAte     = 'ATF100'
		codigonovo = 'ATF100RATE'

		self.oHelper.SearchBrowse(f'M SP 01 {codigoDe}0001', 'Filial+cod. do Bem + Item') 

        #Seleciona a opção do botão
		self.oHelper.SetButton('Outras Ações','Agrupar')

        ##Preenche os perguntes    
		self.oHelper.SetValue('Mostra Lanc Baixa ?'         ,'Nao'          ) #Mostra Lanc Baixa ?             
		self.oHelper.SetValue('Aglutina Lanc Baixa ?'       ,'Nao'          ) #Aglutina Lanc Baixa ?         
		self.oHelper.SetValue('Repete Chapa ?'              ,'Sim'          ) #Repete Chapa ?                
		self.oHelper.SetValue('Considera Bens ?'            ,'Todos') #Considera Bens ?                 
		self.oHelper.SetValue('Descricao Estendida ?'       ,'Desconsiderar') #Descricao Estendida ?         
		self.oHelper.SetValue('Permite adicao novos tipos ?','Sim'          ) #Permite adicao novos tipos ?  
		self.oHelper.SetValue('Tipo Saldo Gerencial ?'      ,''             ) #Tipo Saldo Gerencial ?          
		self.oHelper.SetValue('Contabiliza Online ?'        ,'Não'          ) #Contabiliza Online ?        

		self.oHelper.SetButton('Ok')   

        ####Preenche os perguntes    
		self.oHelper.SetValue('MV_PAR01',codigoDe    ) #Do codigo
		self.oHelper.SetValue('MV_PAR02',codigoAte    ) #Ate o codigo
		self.oHelper.SetValue('MV_PAR03',codigonovo ) #Novo código          
		self.oHelper.SetValue('MV_PAR04','Dados'    ) #Dados         
		self.oHelper.SetValue('MV_PAR05','Rateio'   ) #Rateio  

		self.oHelper.SetButton('Ok')
		
		self.oHelper.SetButton('Confirmar')
		
		self.oHelper.SetButton('Outras Ações','Rateio')
		self.oHelper.SetValue('Percentual','49,96',grid=True,row=1)
		self.oHelper.SetValue('C. Custo','000000001',grid=True,row=1)
		self.oHelper.SetKey('DOWN',grid=True)
		self.oHelper.SetValue('Percentual','50,04',grid=True,row=2)
		self.oHelper.SetValue('C. Custo','000000002',grid=True,row=2)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton('Confirmar')

		self.oHelper.SetValue('Val Orig M1','1000,00', grid=True,row=1) 	
		self.oHelper.SetValue('Quantd','1,000', grid=True,row=1) 	
		self.oHelper.SetValue('Icms do Item','0,00', grid=True,row=1) 
		self.oHelper.SetKey('DOWN',grid=True)		
		self.oHelper.SetValue('Percentual % ','50,0000',grid=True,grid_number=1,row=2)
		self.oHelper.LoadGrid()

		self.oHelper.ClickFolder('Complementos')

		self.oHelper.SetFocus('Crit. Deprec',grid_cell=True,row_number=1)
		self.oHelper.SetValue('Tipo deprec','1 - Linear', grid=True,row=1)
		self.oHelper.SetValue('Vl Max Depre','0,00', grid=True,row=1)
		self.oHelper.LoadGrid()
		self.oHelper.SetKey('Delete',grid=True)
		
		self.oHelper.ClickFolder('Dados do Bem')

		self.oHelper.SetButton('Cancelar')
		
		self.oHelper.AssertTrue()

	def test_ATFA251_CT010(self):
        

		self.oHelper.WaitShow("Aquisicao por Transferencia")

		#Posiciona no registro
		#codigoATF =    '0000000001' 
		codigoDe      = 'ATF100    '
		codigoAte     = 'ATF100'
		codigonovo = 'ATF100RATE'

		self.oHelper.SearchBrowse(f'M SP 01 {codigoDe}0001', 'Filial+cod. do Bem + Item') 

        #Seleciona a opção do botão
		self.oHelper.SetButton('Outras Ações','Agrupar')

        ##Preenche os perguntes    
		self.oHelper.SetValue('Mostra Lanc Baixa ?'         ,'Nao'          ) #Mostra Lanc Baixa ?             
		self.oHelper.SetValue('Aglutina Lanc Baixa ?'       ,'Nao'          ) #Aglutina Lanc Baixa ?         
		self.oHelper.SetValue('Repete Chapa ?'              ,'Sim'          ) #Repete Chapa ?                
		self.oHelper.SetValue('Considera Bens ?'            ,'Todos') #Considera Bens ?                 
		self.oHelper.SetValue('Descricao Estendida ?'       ,'Desconsiderar') #Descricao Estendida ?         
		self.oHelper.SetValue('Permite adicao novos tipos ?','Sim'          ) #Permite adicao novos tipos ?  
		self.oHelper.SetValue('Tipo Saldo Gerencial ?'      ,'2'             ) #Tipo Saldo Gerencial ?          
		self.oHelper.SetValue('Contabiliza Online ?'        ,'Não'          ) #Contabiliza Online ?        

		self.oHelper.SetButton('Ok')   

        ####Preenche os perguntes    
		self.oHelper.SetValue('MV_PAR01',codigoDe    ) #Do codigo
		self.oHelper.SetValue('MV_PAR02',codigoAte    ) #Ate o codigo
		self.oHelper.SetValue('MV_PAR03',codigonovo ) #Novo código          
		self.oHelper.SetValue('MV_PAR04','Dados'    ) #Dados         
		self.oHelper.SetValue('MV_PAR05','Rateio'   ) #Rateio  

		self.oHelper.SetButton('Ok')
		
		self.oHelper.SetButton('Confirmar')

		self.oHelper.ClickFolder('Complementos')

		self.oHelper.SetValue('Tipo Saldo  ',    '2 - Previsto'   , grid=True, grid_number=1,row=1)
		self.oHelper.SetValue('Val Orig M1',     "5.000,00"       , grid=True, grid_number=1,row=1)
		self.oHelper.SetValue('Tx Anual Dep M1', '25,0000'        , grid=True, grid_number=1,row=1)
		self.oHelper.LoadGrid()

		self.oHelper.SetButton('Confirmar')

		self.oHelper.CheckHelp(text='AF251VLRC',button='Fechar')
		self.oHelper.CheckHelp(text='OBRIGAT2',button='Fechar')

		self.oHelper.SetButton('Cancelar')

		self.oHelper.WaitShow("Aquisicao por Transferencia")
		
		self.oHelper.AssertTrue()

	def test_ATFA251_CT007(self):
        

		self.oHelper.WaitShow("Aquisicao por Transferencia")

		#Posiciona no registro
		#codigoATF =    '0000000001' 
		codigoDe      = 'ATF100    '
		codigoAte     = 'ATF100'
		codigonovo = 'ATF100RATE'

		self.oHelper.SearchBrowse(f'M SP 01 {codigoDe}0001', 'Filial+cod. do Bem + Item') 

        #Seleciona a opção do botão
		self.oHelper.SetButton('Outras Ações','Agrupar')

        ##Preenche os perguntes    
		self.oHelper.SetValue('Mostra Lanc Baixa ?'         ,'Nao'          ) #Mostra Lanc Baixa ?             
		self.oHelper.SetValue('Aglutina Lanc Baixa ?'       ,'Nao'          ) #Aglutina Lanc Baixa ?         
		self.oHelper.SetValue('Repete Chapa ?'              ,'Sim'          ) #Repete Chapa ?                
		self.oHelper.SetValue('Considera Bens ?'            ,'Todos') #Considera Bens ?                 
		self.oHelper.SetValue('Descricao Estendida ?'       ,'Desconsiderar') #Descricao Estendida ?         
		self.oHelper.SetValue('Permite adicao novos tipos ?','Sim'          ) #Permite adicao novos tipos ?  
		self.oHelper.SetValue('Tipo Saldo Gerencial ?'      ,''             ) #Tipo Saldo Gerencial ?          
		self.oHelper.SetValue('Contabiliza Online ?'        ,'Não'          ) #Contabiliza Online ?        

		self.oHelper.SetButton('Ok')   

        ####Preenche os perguntes    
		self.oHelper.SetValue('MV_PAR01',codigoDe    ) #Do codigo
		self.oHelper.SetValue('MV_PAR02',codigoAte    ) #Ate o codigo
		self.oHelper.SetValue('MV_PAR03',codigonovo ) #Novo código          
		self.oHelper.SetValue('MV_PAR04','Dados'    ) #Dados         
		self.oHelper.SetValue('MV_PAR05','Rateio'   ) #Rateio  

		self.oHelper.SetButton('Ok')
		
		self.oHelper.SetButton('Confirmar')
		
	
		self.oHelper.SetValue('Icms do Item','0,00', grid=True,row=1) 
		self.oHelper.SetValue('Grupo       ','0005', grid=True,row=1) 
		self.oHelper.SetValue('Quantd','1,000', grid=True,row=1) 
		self.oHelper.SetValue('Chapa','RATE',grid=True,grid_number=1,row=1)
		self.oHelper.SetValue('Val Orig M1','1000,00', grid=True,row=1) 
		self.oHelper.SetKey('DOWN',grid=True)		
		self.oHelper.SetValue('Codigo Base','ATF100RATE', grid=True,row=2) 
		self.oHelper.SetValue('Item Base','0002', grid=True,row=2) 
		self.oHelper.SetValue('Tipo','01', grid=True,row=2) 
		self.oHelper.SetValue('Data Aquisic','10/10/2016', grid=True,row=2) 
		self.oHelper.SetValue('Descr Sintetica','TESTE TIR', grid=True,row=2) 
		self.oHelper.SetValue('Grupo       ','0005', grid=True,row=2) 
		self.oHelper.SetValue('Percentual % ','50,0000',grid=True,grid_number=1,row=2)
		self.oHelper.SetValue('Quantd','1,000', grid=True,row=2) 
		self.oHelper.SetValue('Chapa','RATE2',grid=True,grid_number=1,row=2)
		self.oHelper.SetValue('Historico','TESTE TIR',grid=True,grid_number=1,row=2)
		self.oHelper.SetValue('Val Orig M1','1000,00', grid=True,row=2) 
		
		self.oHelper.LoadGrid()

		self.oHelper.SetButton('Confirmar')

		self.oHelper.CheckHelp(text='AF251VALOR',button='Fechar')

		self.oHelper.SetButton('Cancelar')

		self.oHelper.WaitShow("Aquisicao por Transferencia")
		
		self.oHelper.AssertTrue()

	def test_ATFA251_CT008(self):
        
		self.oHelper.ChangeEnvironment(date='10/03/2016', group = 'T1', branch = 'D MG 01', module = 'SIGAATF')

		self.oHelper.Program('ATFA251')

		self.oHelper.WaitShow("Aquisicao por Transferencia")

		#Posiciona no registro
		
		cBem = 'BMCONTR01'

		#Seleciona a opção do botão
		self.oHelper.SetButton('Outras Ações','Bem Construc.')

        #Preenche os perguntes    
		self.oHelper.SetValue('Mostra Lanc Baixa ?'         ,'Nao'          ) #Mostra Lanc Baixa ?             
		self.oHelper.SetValue('Aglutina Lanc Baixa ?'       ,'Nao'          ) #Aglutina Lanc Baixa ?         
		self.oHelper.SetValue('Repete Chapa ?'              ,'Sim'          ) #Repete Chapa ?                
		self.oHelper.SetValue('Considera Bens ?'            ,'Adiantamentos') #Considera Bens ?              
		self.oHelper.SetValue('Descricao Estendida ?'       ,'Desconsiderar') #Descricao Estendida ?         
		self.oHelper.SetValue('Permite adicao novos tipos ?','Nao'          ) #Permite adicao novos tipos ?  
		self.oHelper.SetValue('Tipo Saldo Gerencial ?'      ,''             ) #Tipo Saldo Gerencial ?          
		self.oHelper.SetValue('Contabiliza Online ?'        ,'Não'          ) #Contabiliza Online ?           

        #Seleciona a opção do botão
		self.oHelper.SetButton('OK')

        #Preenche os perguntes    
		
		self.oHelper.SetValue('MV_PAR01',cBem ) #Novo código          
		self.oHelper.SetValue('MV_PAR02','Dados'    ) #Dados         
		self.oHelper.SetButton('OK')

		self.oHelper.SetButton('Confirmar')

		self.oHelper.SetValue('Tx Anual Dep M1','10,000', grid=True) 		
		self.oHelper.LoadGrid()

		self.oHelper.SetButton('Confirmar')
		
		self.oHelper.SearchBrowse(f'M PR 01 {cBem}0001', 'Filial+cod. do Bem + Item') 
		self.oHelper.SetButton('Visualizar')
		self.oHelper.CheckResult('N1_CBASE',cBem)
		self.oHelper.CheckResult('N1_ITEM','0001')
		self.oHelper.CheckResult('N1_ICMSAPR','5400,00')
		
		self.oHelper.SetButton('Fechar')
		self.oHelper.AssertTrue()	

	def test_ATFA251_CT009(self):

        
		self.oHelper.WaitShow("Aquisicao por Transferencia")

		cBem = 'BMCONTR02'

		self.oHelper.SearchBrowse(f'D MG 01 {cBem}0001', 'Filial+cod. do Bem + Item') 

        #Seleciona a opção do botão

		self.oHelper.SetButton('Outras Ações','Canc. Transf')
		self.oHelper.SetButton('Confirmar')

		self.oHelper.WaitShow("Aquisicao por Transferencia")

		self.oHelper.SearchBrowse(f'D MG 01 {cBem}0001', 'Filial+cod. do Bem + Item') 
		
		self.oHelper.AssertTrue()


	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()