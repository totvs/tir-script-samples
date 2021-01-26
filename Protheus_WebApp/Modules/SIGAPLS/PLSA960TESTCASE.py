from tir import Webapp
import unittest
from tir.technologies.apw_internal import ApwInternal
import datetime
import time

DateSystem = datetime.datetime.today().strftime('%d/%m/%Y')
DateVal = datetime.datetime(2120, 5, 17)
"""-------------------------------------------------------------------
/*/{Protheus.doc} PLSA960TestCase
TIR - Casos de testes da rotina Profissionais de Saude

@author Silvia SantAnna
@since 11/2020
@version 12
-------------------------------------------------------------------"""
class PLSA960(unittest.TestCase):


	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAPLS",DateSystem,"T1","M SP 01","33")
		inst.oHelper.Program("PLSA960")

	def test_PLSA960_001(self):

		# Incluir
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetBranch("M SP 01 ")

		self.oHelper.SetValue("BB0_NOME","PLS DSAUPC TIR PLSA960")
		self.oHelper.SetValue("BB0_CODSIG","CRM")
		self.oHelper.SetValue("BB0_NUMCR","10101010")
		self.oHelper.SetValue("BB0_ESTADO","SP")
		self.oHelper.SetValue("BB0_CGC","71658342000141", check_value = False )
		self.oHelper.SetValue("BB0_CEP","05541000", check_value = False)
		self.oHelper.SetValue("BB0_TIPLOG","008")
		self.oHelper.SetValue("BB0_ENDERE","ALBERT BARTHOLOME")
		self.oHelper.SetValue("BB0_NUMERO","1000")
		self.oHelper.SetValue("BB0_COMPLE","SALA 10")
		self.oHelper.SetValue("BB0_BAIRRO","JARDIM DAS VERTENTES")
		self.oHelper.SetValue("BB0_CODMUN","3550308")
		self.oHelper.SetValue("BB0_CIDADE","SAO PAULO")
		self.oHelper.SetValue("BB0_UF","SP")
		self.oHelper.SetValue("BB0_CODOPE","0001")
		self.oHelper.SetValue("BB0_CODORI","")
		self.oHelper.SetValue("BB0_DATNAS","19/01/1985", check_value = False)
		self.oHelper.SetValue("BB0_SEXO", "2 - Feminino")
		self.oHelper.SetValue("BB0_ESTCIV","C")
		self.oHelper.SetValue("BB0_MATVID","00000015")
		self.oHelper.SetValue("BB0_DATVIN","20/11/2020", check_value = False)
		self.oHelper.SetValue("BB0_EMAIL","PRESTADORES@DSAUPC.COM.BR")
		self.oHelper.SetValue("BB0_NRCRNA","188451896120004")
		self.oHelper.SetValue("BB0_TEL","11323200000", check_value = False)
		self.oHelper.SetButton("Confirmar")

		self.oHelper.SetButton("Fechar")

		# Alterar
		self.oHelper.SearchBrowse(f'{"M SP    71658342000141"}', key=3, index=True)
		self.oHelper.SetButton("Alterar")
		self.oHelper.SetValue("BB0_NOME","PLS DSAUPC TIR ALTERADO")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")

		# Visualizar
		self.oHelper.SearchBrowse(f'{"M SP    71658342000141"}', key=3, index=True)
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("BB0_NOME","PLS DSAUPC TIR ALTERADO")
		self.oHelper.SetButton("Fechar")


		# Outras Ações > Bloquear
		self.oHelper.SearchBrowse(f'{"M SP    71658342000141"}', key=3, index=True)
		self.oHelper.SetButton("Outras Ações", sub_item='(Des)Bloquear')
		self.oHelper.SetValue("B17_DATA","20/11/2020", check_value = False)
		self.oHelper.SetValue("B17_HORA","1000", check_value = False)
		self.oHelper.SetValue("B17_MOTBLO","901")
		self.oHelper.SetValue("B17_OBS","PLS DSAUPC BLOQUEADO")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")

		# Outras Ações > Desbloquear
		self.oHelper.SearchBrowse(f'{"M SP    71658342000141"}', key=3, index=True)
		self.oHelper.SetButton("Outras Ações" , sub_item='(Des)Bloquear')
		self.oHelper.SetValue("B17_DATA","20/11/2020", check_value = False)
		self.oHelper.SetValue("B17_HORA","1100", check_value = False)
		self.oHelper.SetValue("B17_MOTBLO","905")
		self.oHelper.SetValue("B17_OBS","PLS DSAUPC DESBLOQUEADO")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")

#		# Excluir
#		self.oHelper.SearchBrowse(f'{"M SP    71658342000141"}', key=3, index=True)
#		self.oHelper.SetButton("Outras Ações",sub_item='Excluir')
#		self.oHelper.SetButton("Confirmar")
#		#Help: FWFORMCANCEL
#		#Problema: Violação de Integridade. Foi encontrada referência de Cod. Esp. (BQ1_CODESP) na tabela BE2 - Autorização e Procedimentos. Formulário BQ1Detail

		self.oHelper.AssertTrue()



	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()