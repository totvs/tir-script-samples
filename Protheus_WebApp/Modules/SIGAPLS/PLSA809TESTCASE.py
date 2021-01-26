from tir import Webapp
import unittest
from tir.technologies.apw_internal import ApwInternal
import datetime
import time

DateSystem = datetime.datetime.today().strftime('%d/%m/%Y')
DateVal = datetime.datetime(2120, 5, 17)
"""-------------------------------------------------------------------
/*/{Protheus.doc} PLSA809TestCase
TIR - Casos de testes da rotina Indicacao de Prestador via CallCenter

@author Silvia SantAnna
@since 10/2020
@version 12
-------------------------------------------------------------------"""
class PLSA809(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAPLS","13/10/2020","T1","M SP 01","33")
		inst.oHelper.Program("PLSA809")
		inst.oHelper.AddParameter("MV_PLCALPG","" , "2")
		inst.oHelper.AddParameter("MV_PL809VL","" , ".F.")
		inst.oHelper.SetParameters()

	def test_PLSA809_001(self):
		# INCLUIR
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetBranch("M SP 01 ")
		self.oHelper.SetValue("B9Y_CARTEI","00010100000001024", check_value = False)
		self.oHelper.SetValue("B9Y_CRMCGC","41226834671", check_value = False)
		time.sleep(10)
		self.oHelper.SetValue("B9Y_NOME","PLS DSAUPC TIR INCLUSAO")
		self.oHelper.SetValue("B9Y_EMAIL","DSAUPC@EMAIL.COM")
		self.oHelper.SetValue("B9Y_TEL","11332220000", check_value = False)
		self.oHelper.SetValue("B9Y_TIPOAT", "3 - Ambos")
		self.oHelper.SetValue("B9Y_OBS", "TESTE 2 TIR INCLUSAO")
		# Grid Enderecos
		self.oHelper.ClickGridCell("Cód Logr",row=1, grid_number=1)
		self.oHelper.SetKey("Enter", grid=True,  grid_number=1)
		self.oHelper.SetValue("B9V_CODLOG","008")
		self.oHelper.ClickGridCell("Endereço",row=1, grid_number=1)
		self.oHelper.SetKey("Enter", grid=True,  grid_number=1)
		time.sleep(10)
		self.oHelper.SetValue("B9V_ENDER","ALBERT BARTHOLOME")
		self.oHelper.ClickGridCell("Nº",row=1, grid_number=1)
		self.oHelper.SetKey("Enter", grid=True,  grid_number=1)
		time.sleep(10)
		self.oHelper.SetValue("B9V_NUMERO","434")
		#self.oHelper.ClickGridCell("Complemento",row=1, grid_number=1)
		#self.oHelper.SetKey("Enter", grid=True,  grid_number=1)
		time.sleep(30)
		#self.oHelper.SetValue("B9V_COMEND","SALA 10")
		#self.oHelper.ClickGridCell("Bairro",row=1, grid_number=1)
		#self.oHelper.SetKey("Enter", grid=True,  grid_number=1)
		time.sleep(30)
		#self.oHelper.SetValue("B9V_BAIRRO","BUTANTA")
		#self.oHelper.ClickGridCell("Cód Cidade",row=1, grid_number=1)
		#self.oHelper.SetKey("Enter", grid=True,  grid_number=1)
		time.sleep(30)
		#self.oHelper.SetValue("B9V_CODCID","3550308")
		#self.oHelper.ClickGridCell("CEP",row=1, grid_number=1)
		#self.oHelper.SetKey("Enter", grid=True,  grid_number=1)
		time.sleep(30)
		#self.oHelper.SetValue("B9V_CEP","05541000", check_value = False)
		# Grid Especialidades
		self.oHelper.ClickGridCell("Cod Espec",row=1, grid_number=2)
		self.oHelper.SetKey("Enter", grid=True,  grid_number=2)
		time.sleep(10)
		self.oHelper.SetValue("B9Q_CODESP","002")

		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")		# "O beneficiário não possui email cadastrado na base de dados, favor informar o protocolo a ele para que seja possível acompanhar a indicação feita"
		self.oHelper.SetButton("Fechar")		# "Registro inserido com sucesso."

		# VISUALIZAR
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("B9Y_CRMCGC","41226834671")
		self.oHelper.SetButton("Fechar")
		

		# INCLUSÃO COM MESMO CRM/CNPJ
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetBranch("M SP 01 ")
		self.oHelper.SetValue("B9Y_CARTEI","00010100000001024", check_value = False)
		self.oHelper.SetValue("B9Y_CRMCGC","41226834671", check_value = False)
		time.sleep(10)
		self.oHelper.SetValue("B9Y_NOME","PLS DSAUPC TIR INCLUSAO 2")
		self.oHelper.SetValue("B9Y_EMAIL","DSAUPC2@EMAIL.COM")
		self.oHelper.SetValue("B9Y_TEL","11333331234", check_value = False)
		self.oHelper.SetValue("B9Y_TIPOAT", "2 - Assistencial")
		self.oHelper.SetValue("B9Y_OBS", "TESTE 2 TIR INCLUSAO COM MESMO CRM/CNPJ")
		# Grid Especialidades
		self.oHelper.ClickGridCell("Indicar",row=1, grid_number=2)
		self.oHelper.SetKey("Enter", grid=True,  grid_number=2)

		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")		# "O beneficiário não possui email cadastrado na base de dados, favor informar o protocolo a ele para que seja possível acompanhar a indicação feita"
		self.oHelper.SetButton("Fechar")		# "Registro inserido com sucesso."

		self.oHelper.SetButton('x')
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()