from tir import Webapp
import unittest
from tir.technologies.apw_internal import ApwInternal
import datetime
import time

DateSystem = datetime.datetime.today().strftime('%d/%m/%Y')
DateVal = datetime.datetime(2120, 5, 17)
"""-------------------------------------------------------------------
/*/{Protheus.doc} PLSA940TestCase
TIR - Casos de testes da rotina Rede de Atendimento (RDA)

@author Silvia SantAnna
@since 09/2020
@version 12
-------------------------------------------------------------------"""
class PLSA360(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAPLS",DateSystem,"T1","M SP 01","33")
		inst.oHelper.Program("PLSA360")

	def test_PLSA360_001(self):
		# Incluir
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetBranch("M SP 01 ")

		self.oHelper.SetValue("BAU_TIPPE", "F - Fisica")
		self.oHelper.SetValue("BAU_CPFCGC","48464726120",check_value = False)
		self.oHelper.SetValue("BAU_NOME","PLS DSAUPC RDA TIR INCLUSAO")			
		#self.oHelper.CheckResult("BAU_NREDUZ","PLS DSAUPC RDA TIR I")
		self.oHelper.SetValue("BAU_RECPRO","0 - Nao")
		self.oHelper.SetValue("BAU_DTINCL","01/09/2020",check_value = False)
		self.oHelper.SetValue("BAU_TIPPRE","MED")
		self.oHelper.SetValue("BAU_COPCRE", "2 - Credenciado/Contratualizado")
		self.oHelper.SetValue("BAU_CEP","05541000",check_value = False)
		#self.oHelper.CheckResult("BAU_END","ALBERT BARTHOLOME")
		self.oHelper.SetValue("BAU_NUMERO","100")
		self.oHelper.SetValue("BAU_COMPL","SALA 10")
		#self.oHelper.CheckResult("BAU_BAIRRO","JARDIM DAS VERTENTES")
		#self.oHelper.CheckResult("BAU_MUN","3550308")

		## Pasta Registro
		self.oHelper.ClickFolder("Registro")
		self.oHelper.SetValue("BAU_SIGLCR","CRM")
		self.oHelper.SetValue("BAU_ESTCR","SP")
		self.oHelper.SetValue("BAU_CONREG","12345")
		self.oHelper.SetValue("BAU_CBO","225120")
		#self.oHelper.SetValue("BAU_MATVID","")

		## Pasta Atendimento
		self.oHelper.ClickFolder("Atendimento")

		## Pasta Impostos/seguro Social
		self.oHelper.ClickFolder("Impostos/seguro Social")
		self.oHelper.SetValue("BAU_CALIMP", "1 - Pedido de Compra")
		self.oHelper.SetValue("BAU_CODRET","0297")
		#self.oHelper.SetValue("BAU_ISS","")

		## Pasta Financeiro
		self.oHelper.ClickFolder("Financeiro")
		self.oHelper.SetValue("BAU_FORPGT", "1 - Crédito em Conta")

		## Pasta Producao Medica
		self.oHelper.ClickFolder("Producao Medica")
		self.oHelper.SetValue("BAU_DIAPGT","10")
		self.oHelper.SetValue("BAU_PAGPRO","1 - Sim")
		self.oHelper.SetValue("BAU_CALPGT","001")

		## Pasta Outros
		self.oHelper.ClickFolder("Outros")
		self.oHelper.SetValue("BAU_TISVER","3.05.00")

		## Pasta Especialidades
		#self.oHelper.ClickFolder("Especialidades")
		#self.oHelper.ClickGridCell("Item",row=1, grid_number=1)
		#self.oHelper.SetKey("Enter", grid=True,  grid_number=1)
		#self.oHelper.SetValue("BBF_CODESP","0001002")
		#self.oHelper.SetValue("BBF_DATINC","/  /")
		#self.oHelper.SetValue("BBF_DATINC","01/09/2020",check_value = False)
		#self.oHelper.SetValue("BBF_DATBLO","/  /",check_value = False)
		#self.oHelper.SetButton("Salvar")

		self.oHelper.SetButton("Salvar")

		# Alterar
		self.oHelper.SearchBrowse(f'{"M SP    PLS DSAUPC RDA TIR INCLUSAO"}', key=2, index=True)
		self.oHelper.SetButton("Alterar")
		self.oHelper.SetValue("BAU_NOME","PLS DSAUPC RDA TIR ALTERACAO")	
		self.oHelper.SetButton("Salvar")

		# Visualizar
		self.oHelper.SearchBrowse(f'{"M SP    PLS DSAUPC RDA TIR ALTERACAO"}', key=2, index=True)
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("BAU_NOME","PLS DSAUPC RDA TIR ALTERACAO")	
		self.oHelper.SetButton("Confirmar")

		## Outras Acoes > Complemento
		self.oHelper.SearchBrowse(f'{"M SP    PLS DSAUPC RDA TIR ALTERACAO"}', key=2, index=True)
		self.oHelper.SetButton("Outras Ações",sub_item='Complemento')
		self.oHelper.SetButton("Cancelar")
		self.oHelper.SetButton("Sim")

		## Outras Acoes > (Des)Bloquear
		self.oHelper.SearchBrowse(f'{"M SP    PLS DSAUPC RDA TIR ALTERACAO"}', key=2, index=True)
		self.oHelper.SetButton("Outras Ações",sub_item='(Des)Bloquear')
		self.oHelper.SetValue("BC4_DATA","24/09/2020",check_value = False)
		self.oHelper.SetValue("BC4_HORA","1000",check_value = False)
		self.oHelper.SetValue("BC4_MOTBLO","901")
		self.oHelper.SetValue("BC4_OBS ","PLS DSAUPC RDA TIR BLOQUEIO")
		self.oHelper.SetValue("BC4_DTBLQ ",DateSystem)
		#self.oHelper.SetValue("BC4_MOTIVO ","1 - Suspensao")
		self.oHelper.SetButton("Salvar")

		## Outras Acoes > (Des)Bloquear
		self.oHelper.SearchBrowse(f'{"M SP    PLS DSAUPC RDA TIR ALTERACAO"}', key=2, index=True)
		self.oHelper.SetButton("Outras Ações",sub_item='(Des)Bloquear')
		self.oHelper.SetValue("BC4_DATA","24/09/2020",check_value = False)
		self.oHelper.SetValue("BC4_HORA","1400",check_value = False)
		self.oHelper.SetValue("BC4_MOTBLO","906")
		self.oHelper.SetValue("BC4_OBS ","PLS DSAUPC RDA TIR DESBLOQUEIO")
		self.oHelper.SetValue("BC4_DTBLQ ",DateSystem)
		self.oHelper.SetButton("Salvar")

		## Outras Acoes > Exceção de pagamento U.S
		self.oHelper.SearchBrowse(f'{"M SP    PLS DSAUPC RDA TIR ALTERACAO"}', key=2, index=True)
		self.oHelper.SetButton("Outras Ações",sub_item='Exceção de pagamento U.S')
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetBranch("M SP 01 ")
		self.oHelper.SetValue("B4R_CPADDE","01")
		self.oHelper.SetValue("B4R_CPRODE","30101018")
		self.oHelper.SetValue("B4R_PADATE","01")
		self.oHelper.SetValue("B4R_PROATE","30101018")
		self.oHelper.SetValue("B4R_CODLOC","001001")
		#self.oHelper.SetValue("B4R_CODESP","001")
		self.oHelper.SetValue("B4R_UNIDAD","AUX,COP")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")

		self.oHelper.SetButton("Alterar")
		self.oHelper.SetValue("B4R_UNIDAD","AUX,COP,FIL")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")

		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("B4R_UNIDAD","AUX,COP,FIL")
		self.oHelper.SetButton("Fechar")

		self.oHelper.SetButton("Outras Ações",sub_item='Excluir')
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("x")


		## Outras Acoes > Especialidades x Cadastros relacionados > Contatos
		self.oHelper.SearchBrowse(f'{"M SP    PLS DSAUPC RDA TIR ALTERACAO"}', key=2, index=True)
		self.oHelper.SetButton("Outras Ações",sub_item='Especialidades x Cadastros relacionados, Contatos')
		time.sleep(3)
		self.oHelper.SetButton("Fechar")

		## Outras Acoes > Especialidades x Cadastros relacionados > Corpo Clínico
		self.oHelper.SearchBrowse(f'{"M SP    PLS DSAUPC RDA TIR ALTERACAO"}', key=2, index=True)
		self.oHelper.SetButton("Outras Ações",'Especialidades x Cadastros relacionados, Corpo Clínico')
		time.sleep(3)
		self.oHelper.SetButton("Cancelar")

		## Outras Acoes > Especialidades x Cadastros relacionados > Rede de Atendimento
		self.oHelper.SearchBrowse(f'{"M SP    PLS DSAUPC RDA TIR ALTERACAO"}', key=2, index=True)
		self.oHelper.SetButton("Outras Ações",'Especialidades x Cadastros relacionados, Rede de Atendimento')
		self.oHelper.SetBranch("M SP 01 ")
		time.sleep(3)
		self.oHelper.SetButton("Cancelar")

		## Outras Acoes > Especialidades x Cadastros relacionados > Procedimentos
		self.oHelper.SearchBrowse(f'{"M SP    PLS DSAUPC RDA TIR ALTERACAO"}', key=2, index=True)
		self.oHelper.SetButton("Outras Ações",'Especialidades x Cadastros relacionados, Procedimentos')
		time.sleep(3)
		self.oHelper.SetButton("Cancelar")

		## Outras Acoes > Contatos CRM
		self.oHelper.SearchBrowse(f'{"M SP    PLS DSAUPC RDA TIR ALTERACAO"}', key=2, index=True)
		self.oHelper.SetButton("Outras Ações",'Contatos CRM')
		self.oHelper.ClickGridCell("Contato",row=1, grid_number=1)
		self.oHelper.SetKey("Enter", grid=True,  grid_number=1)
		self.oHelper.SetValue("AC8_CODCON","000001")
		self.oHelper.LoadGrid()
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")

		## Outras Acoes > Contrato/Aditivo
		self.oHelper.SearchBrowse(f'{"M SP    PLS DSAUPC RDA TIR ALTERACAO"}', key=2, index=True)
		self.oHelper.SetButton("Outras Ações",'Contrato/Aditivo')
		self.oHelper.SetButton("Fechar")


		# Outras Acoes > Excluir
		self.oHelper.SearchBrowse(f'{"M SP    PLS DSAUPC RDA TIR ALTERACAO"}', key=2, index=True)
		self.oHelper.SetButton("Outras Ações",sub_item='Excluir')
		time.sleep(3)
		self.oHelper.SetButton("Confirmar")

		self.oHelper.SetButton("x")

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()