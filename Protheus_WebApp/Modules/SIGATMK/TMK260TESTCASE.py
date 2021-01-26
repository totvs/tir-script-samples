from tir import Webapp
from datetime import datetime, timedelta 
import time
import unittest

class TMKA260(unittest.TestCase):

	@classmethod
	def setUpClass(self):

		self.oHelperA = Webapp(autostart=False)
		self.oHelperA.SetTIRConfig(config_name="User", value="teleatendimento") 
		self.oHelperA.SetTIRConfig(config_name="Password", value="1")

		#self.oHelperC = Webapp(autostart=False)
		#self.oHelperC.SetTIRConfig(config_name="User", value="telecobranca") 
		#self.oHelperC.SetTIRConfig(config_name="Password", value="1")

		#self.oHelperV = Webapp(autostart=False)
		#self.oHelperV.SetTIRConfig(config_name="User", value="televendas") 
		#self.oHelperV.SetTIRConfig(config_name="Password", value="1")
	
		#self.oHelperM = Webapp(autostart=False)
		#self.oHelperM.SetTIRConfig(config_name="User", value="telemarketing") 
		#self.oHelperM.SetTIRConfig(config_name="Password", value="1")

	def test_TMKA260_CT015(self):
		'''
		#GTSER-T52717 - CT015 - Prospects (Consulta Perfil)
		'''

		prospect = "FAT001"
		loja = "01"

		# Inicia o novo Webapp para logar com o User no Módulo
		self.oHelperA.Start()
		self.oHelperA.Setup("SIGATMK","17/07/2020","T1","D MG 01  ","13")
		self.oHelperA.Program("TMKA260")

		self.oHelperA.SearchBrowse(f"D MG    {prospect}{loja}", "Filial+codigo + loja")

		self.oHelperA.SetButton("Visualizar")

		self.oHelperA.WaitShow("Prospects - VISUALIZAR")
		self.oHelperA.SetButton("Outras Ações","Perfil")

		self.oHelperA.WaitShow("Consulta dos ultimos")
		self.oHelperA.ClickLabel("A partir de")
		self.oHelperA.SetValue("dCorte","01/01/2018", name_attr = True)

		self.oHelperA.SetButton("Financ.")
		self.oHelperA.SetValue("Da Emissão ?","01/01/2018")
		self.oHelperA.SetValue("Até a Emissão ?","31/12/2018")
		self.oHelperA.SetValue("Do Vencimento ?","01/01/2018")
		self.oHelperA.SetValue("Até o Vencimento ?","31/12/2018")
		self.oHelperA.SetValue("Considera Provisor. ?","Sim")
		#self.oHelperA.SetValue("Do Prefixo ?","   ", check_value=False)
		self.oHelperA.SetValue("Até Prefixo ?","ZZZ")
		self.oHelperA.SetValue("Considera Faturados ?","Sim")
		self.oHelperA.SetValue("Considera Liquidados ?","Sim")
		self.oHelperA.SetValue("Pedidos com Itens Bloqueados ?","Nao")
		self.oHelperA.SetValue("Tit. Gerados por Liquidação ?","Sim")
		self.oHelperA.SetValue("Considera Saldo ?","Normal")
		self.oHelperA.SetValue("Considera Lojas ?","Sim")
		self.oHelperA.SetValue("TES gera duplicata ?","Todas")
		self.oHelperA.SetValue("Considera RA ?","Nao")
		self.oHelperA.SetValue("Exibe dias a vencer ?","Nao")
		self.oHelperA.SetValue("Seleciona Filiais ?","Nao")
		self.oHelperA.SetButton("OK")

		self.oHelperA.SetButton("Ok")

		self.oHelperA.ClickTree("Perfil do Prospect > Empresa > Oportunidades")

		self.oHelperA.AssertTrue()

	@classmethod
	def tearDownClass(self):
 
		self.oHelperA.TearDown()
		#self.oHelperC.TearDown()
		#self.oHelperV.TearDown()
		#self.oHelperM.TearDown()
	
if __name__ == '__main__':
	unittest.main()