from tir import Webapp
from datetime import datetime, timedelta 
import time
import unittest

class TMKA271(unittest.TestCase):

	@classmethod
	def setUpClass(self):

		self.oHelper = Webapp(autostart=False)
		self.oHelper.SetTIRConfig(config_name="User", value="telecobranca") 
		self.oHelper.SetTIRConfig(config_name="Password", value="1")

		self.oHelper2 = Webapp(autostart=False)
		self.oHelper2.SetTIRConfig(config_name="User", value="televendas") 
		self.oHelper2.SetTIRConfig(config_name="Password", value="1")
	
		self.oHelper3 = Webapp(autostart=False)
		self.oHelper3.SetTIRConfig(config_name="User", value="telemarketing") 
		self.oHelper3.SetTIRConfig(config_name="Password", value="1")

	
	def test_TMKA271_CT007(self):

		# Inicia o novo Webapp para logar com o User no Módulo
		self.oHelper.Start()
		self.oHelper.Setup("SIGATMK","07/06/2019","T1","D MG 01  ","13")
		self.oHelper.Program("TMKA271")

		self.oHelper.WaitShow("Telecobranca")
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetBranch("D MG 01")
		self.oHelper.ClickFolder("Telecobrança")

		Atendimento = self.oHelper.GetValue("Atendimento")

		self.oHelper.SetValue("ACF_CLIENT","TMC007")
		self.oHelper.SetValue("ACF_CODCON","TMC007")

		self.oHelper.SetValue("ACF_STATUS","2 - Cobranca")

		self.oHelper.SetFocus("Titulo", grid_cell = True) 
		self.oHelper.SetKey("F3") 
		self.oHelper.ClickBox("Prefixo", "TMK")
	
		self.oHelper.LoadGrid()
		
		self.oHelper.SetButton("Salvar")

		TimeSystem = datetime.today() + timedelta(hours=2)
		HrPend =  TimeSystem.strftime("%H:%M")

		self.oHelper.SetValue("ACF_HRPEND", HrPend)

		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("Ok")
		time.sleep(10)
		self.oHelper.SetButton("Cancelar")
		self.oHelper.SetButton("Sim")

		self.oHelper.SearchBrowse(f"D MG 01 {Atendimento}", "Filial+atendimento")
		self.oHelper.SetButton("Visualizar")

		self.oHelper.WaitShow("Atendimento")
	
		self.oHelper.CheckResult("ACF_CODIGO",Atendimento) 
		self.oHelper.CheckResult("ACF_CLIENT","TMC007")

		self.oHelper.CheckResult("ACF_LOJA","01")
		
		#self.oHelper.CheckResult("ACG_TITULO", "TMKC007", grid=True, line=1)  #abrir task loadgrid
	
		#self.oHelper.LoadGrid()
		
		self.oHelper.SetButton("Cancelar")

		self.oHelper.AssertTrue()
			
	def test_TMKA271_CT008(self):
		
		Atendimento = "000009"  #=ok base congelada 28/06

		self.oHelper.SearchBrowse(f"D MG 01 {Atendimento}", "Filial+atendimento")
		
		self.oHelper.SetButton("Alterar")
		self.oHelper.ClickFolder("Telecobrança")

		self.oHelper.SetValue("ACF_STATUS","1 - Atendimento")

		TimeSystem = datetime.today() + timedelta(hours=2)
		HrPend =  TimeSystem.strftime("%H:%M")

		self.oHelper.SetValue("ACF_HRPEND", HrPend)
	
		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("Ok")

		self.oHelper.SetButton("Cancelar")
		self.oHelper.SetButton("Sim")
		
		self.oHelper.SearchBrowse(f"D MG 01 {Atendimento}", "Filial+atendimento")
		self.oHelper.SetButton("Visualizar")

		self.oHelper.WaitShow("Atendimento")
	
		self.oHelper.CheckResult("ACF_CODIGO",Atendimento) 
		self.oHelper.CheckResult("ACF_STATUS","1 - Atendimento") 
				
		self.oHelper.SetButton("Confirmar")
	
		self.oHelper.AssertTrue()

		self.oHelper.TearDown()

		
	def test_TMKA271_CT009(self):

		self.oHelper2.Start()
		self.oHelper2.Setup("SIGATMK","07/06/2019","T1","D MG 01  ","13")
		self.oHelper2.Program("TMKA271")
		self.oHelper2.WaitShow("Televendas")	
				
	
		self.oHelper2.SetButton("Incluir")
		self.oHelper2.SetBranch("D MG 01")
		self.oHelper2.ClickFolder("TeleVendas")

		Atendimento = self.oHelper2.GetValue("Atendimento")

		self.oHelper2.SetValue("UA_CLIENTE","TMC007")
		self.oHelper2.SetValue("UA_LOJA","01")
		self.oHelper2.SetValue("UA_CODCONT","TMC007")
		self.oHelper2.SetValue("UA_TMK","2 - Ativo")
		self.oHelper2.SetValue("UA_OPER","2 - Orcamento")
				
		#self.oHelper2.SetFocus("Produto", grid_cell = True) 
		#self.oHelper2.SetKey("F3")
		#self.oHelper2.SearchBrowse(f"TMK000000000000000000000000001", "Código")
		#self.oHelper2.SetButton("Ok")
		self.oHelper2.SetValue("UB_PRODUTO", "TMK000000000000000000000000001", grid=True)
		self.oHelper2.SetValue("UB_QUANT", "1,00", grid=True)
		self.oHelper2.SetValue("UB_VRUNIT" , "125,50", grid=True)  

		#self.oHelper2.SetKey("DOWN", grid=True)

		##self.oHelper2.SetFocus("Produto", grid_cell = True) 
		##self.oHelper2.SetKey("F3")
		##self.oHelper2.SearchBrowse(f"TMK000000000000000000000000002", "Código")
		##self.oHelper2.SetButton("Ok")
		#self.oHelper2.SetValue("UB_PRODUTO", "TMK000000000000000000000000002", grid=True)
		#self.oHelper2.SetValue("UB_QUANT", "1.00", grid=True)
		#self.oHelper2.SetValue("UB_VRUNIT", "1870.00", grid=True)
		
		self.oHelper2.LoadGrid()
		
		self.oHelper2.SetButton("Salvar")
		time.sleep(10)
		self.oHelper2.SetButton("Cancelar")
		time.sleep(10)
		self.oHelper2.SetButton("Cancelar")
		self.oHelper2.SetButton("Sim")

		self.oHelper2.SearchBrowse(f"D MG 01 {Atendimento}", "Filial+atendimento")
		self.oHelper2.SetButton("Visualizar")

		self.oHelper2.WaitShow("Atendimento")
	
		self.oHelper2.CheckResult("UA_NUM",Atendimento) 
		self.oHelper2.CheckResult("UA_CLIENTE","TMC007")
		self.oHelper2.CheckResult("UA_LOJA","01")

		
		self.oHelper2.CheckResult("UB_PRODUTO", "TMK000000000000000000000000001", grid=True)#, line=1)
		#self.oHelper2.CheckResult("UB_QUANT", "1.00", grid=True, line=1)
		#self.oHelper2.CheckResult("UB_VRUNIT", "125,50", grid=True, line=1)  

		#self.oHelper2.CheckResult("UB_PRODUTO", "TMK000000000000000000000000002", grid=True, line=2)
		#self.oHelper2.CheckResult("UB_QUANT", "1.00", grid=True, line=2)
		#self.oHelper2.CheckResult("UB_VRUNIT", "1870,00", grid=True, line=2)  
		
		self.oHelper2.LoadGrid()
		
		self.oHelper2.SetButton("Confirmar")
				
		self.oHelper2.AssertTrue()


	def test_TMKA271_CT010(self):
	
		Atendimento = "000012" 

		self.oHelper2.SearchBrowse(f"D MG 01 {Atendimento}", "Filial+atendimento")
		
		self.oHelper2.SetButton("Alterar")
	
		self.oHelper2.ClickFolder("TeleVendas")

		self.oHelper2.SetValue("UB_VALDESC","725,00",grid=True,row=2)
		self.oHelper2.LoadGrid()

		self.oHelper2.SetValue("UA_OPER","1 - Faturamento")
		
		self.oHelper2.SetButton("Salvar")

		#self.oHelper2.WaitShow("Forma de Pagamento")

		self.oHelper2.SetButton("Ok")

		self.oHelper2.SetButton("Sim") 

		self.oHelper2.WaitShow("Emissão do Pedido de Vendas - Televendas")
		self.oHelper2.SetButton("Cancelar")
		self.oHelper2.SetButton("Cancelar")
		
		self.oHelper2.SetButton("Sim") 

		self.oHelper2.SearchBrowse(f"D MG 01 {Atendimento}", "Filial+atendimento")
		self.oHelper2.SetButton("Visualizar")

		self.oHelper2.WaitShow("Atendimento")
	
		self.oHelper2.CheckResult("UA_NUM",Atendimento) 
		self.oHelper2.CheckResult("UA_OPER","1 - Faturamento")

		self.oHelper2.CheckResult("UB_VRUNIT","1.145,00",grid=True,line=2)
		self.oHelper2.CheckResult("UB_VALDESC","725,00",grid=True,line=2)
		self.oHelper2.LoadGrid()

		self.oHelper2.SetButton("Cancelar")

		self.oHelper2.AssertTrue()

		self.oHelper2.TearDown()


	def test_TMKA271_CT011(self):

		self.oHelper3.Start()
		self.oHelper3.Setup("SIGATMK","07/06/2019","T1","D MG 01  ","13")
		self.oHelper3.Program("TMKA271")	
		self.oHelper3.WaitShow("Telemarketing")	
		
		self.oHelper3.SetButton("Incluir")
		self.oHelper3.SetBranch("D MG 01")
		self.oHelper3.ClickFolder("TeleMarketing")

		Atendimento = self.oHelper3.GetValue("Atendimento")

		self.oHelper3.SetValue("UC_CODCONT","TMC007")
		self.oHelper3.SetButton("Ok")

		self.oHelper3.SetValue("UC_OPERACA","1 - Receptivo")
		self.oHelper3.SetValue("UC_STATUS","1 - Planejada")
		
		self.oHelper3.SetFocus("Assunto", grid_cell = True) 
		self.oHelper3.SetKey("F3",grid=True)
		self.oHelper3.SearchBrowse(f"000001", "Código")
		self.oHelper3.SetButton("Ok")
		#self.oHelper3.SetValue("UD_ASSUNTO","000001",grid=True)
		self.oHelper3.SetValue("UD_PRODUTO","TMK000000000000000000000000001",grid=True)

		self.oHelper3.SetFocus("Ocorrencia", grid_cell = True) 
		self.oHelper3.SetKey("F3",grid=True)
		self.oHelper3.SetButton("Ok")
		
		self.oHelper3.LoadGrid()
	
		self.oHelper3.SetButton("Salvar")
		self.oHelper3.SetButton("Cancelar")
		self.oHelper3.SetButton("Sim")

		self.oHelper3.SearchBrowse(f'D MG 01 {Atendimento}', 'Filial+atendimento')
		self.oHelper3.SetButton("Visualizar")

		self.oHelper3.WaitShow("Atendimento")
	
		self.oHelper3.CheckResult("UC_CODIGO",Atendimento) 
		self.oHelper3.CheckResult("UC_CODCONT","TMC007")

		self.oHelper3.CheckResult("UC_OPERACA","1 - Receptivo")
		self.oHelper3.CheckResult("UC_STATUS","1 - Planejada")

		self.oHelper3.CheckResult("UD_ASSUNTO","000001", grid=True, line=1)
		self.oHelper3.CheckResult("UD_PRODUTO","TMK000000000000000000000000001", grid=True, line=1)
		self.oHelper3.CheckResult("UD_OCORREN","000003", grid=True, line=1)  

		self.oHelper3.LoadGrid()
		
		self.oHelper3.SetButton("Confirmar")
				
		self.oHelper3.AssertTrue()
			
	def test_TMKA271_CT012(self):

		Atendimento = "000015"

		self.oHelper3.SearchBrowse(f"D MG 01 {Atendimento}", "Filial+atendimento")

		self.oHelper3.SetButton("Alterar")
		self.oHelper3.ClickFolder("TeleMarketing")

		self.oHelper3.SetValue("UC_STATUS","2 - Pendente")
		
		self.oHelper3.SetButton("Salvar")
		self.oHelper3.SetButton("Cancelar")
		self.oHelper3.SetButton("Sim")

		self.oHelper3.SearchBrowse(f'D MG 01 {Atendimento}', 'Filial+atendimento')
		self.oHelper3.SetButton("Visualizar")

		self.oHelper3.WaitShow("Atendimento")
	
		self.oHelper3.CheckResult("UC_CODIGO",Atendimento) 
		self.oHelper3.CheckResult("UC_STATUS","2 - Pendente")
		self.oHelper3.SetButton("Cancelar")

		self.oHelper3.AssertTrue()
		self.oHelper3.TearDown()
		
	@classmethod
	def tearDownClass(self):
 
		'''self.oHelper.TearDown()
		self.oHelper2.TearDown()
		self.oHelper3.TearDown()'''
		
	
if __name__ == '__main__':
	unittest.main()