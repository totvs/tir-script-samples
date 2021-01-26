from tir import Webapp
import unittest
from tir.technologies.apw_internal import ApwInternal
import datetime
import time

DateSystem = datetime.datetime.today().strftime('%d/%m/%Y')
DateVal = datetime.datetime(2120, 5, 17)
"""-------------------------------------------------------------------
/*/{Protheus.doc} PLSA010TestCase
TIR - Casos de testes da rotina Operadora de Saude

@author Silvia SantAnna
@since 11/2020
@version 12
-------------------------------------------------------------------"""
class PLSA010(unittest.TestCase):


	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAPLS",DateSystem,"T1","M SP 01","33")
		inst.oHelper.Program("PLSA010")


	def test_PLSA010_001(self):
		# Incluir
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetBranch("M SP 01 ")

		self.oHelper.SetValue("BA0_CODIDE","0")
		self.oHelper.SetValue("BA0_CODINT","123")
		self.oHelper.SetValue("BA0_NOMINT","PLS DSAUPC TIR")
		self.oHelper.SetValue("BA0_CLAINT","13")
		self.oHelper.SetValue("BA0_GRUOPE","01")
		self.oHelper.SetValue("BA0_SUSEP","123456")
		self.oHelper.SetValue("BA0_CGC","53226134000191", check_value = False) 

		self.oHelper.ClickFolder("Diops")
		self.oHelper.SetValue("BA0_MODALI","ADMIN")
		self.oHelper.SetValue("BA0_SEGMEN","6")

		self.oHelper.ClickFolder("Integração Carol")
		self.oHelper.ClickFolder("Outros")
		self.oHelper.SetValue("BA0_TISVER","3.05.00", check_value = False)

		self.oHelper.ClickFolder("Contatos por Depto.")
		self.oHelper.ClickFolder("Cargo Social")

		self.oHelper.ClickFolder("Vínculo entre operadoras")
		self.oHelper.ClickGridCell("Operadora",row=1, grid_number=1)
		self.oHelper.SetKey("Enter", grid=True,  grid_number=1)
		self.oHelper.SetValue("BIA_OPEREL","0001")
		self.oHelper.SetKey("F3")
		time.sleep(2)
		self.oHelper.SetKey("Enter", grid=True,  grid_number=1)
		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("Salvar")

		self.oHelper.ClickFolder("Cobrança de Identificação de Usuário")
		self.oHelper.ClickFolder("Previsão Pagamento Reembolso")
		self.oHelper.ClickFolder("Doc. obrigat. dos Usuários")
		self.oHelper.ClickFolder("Informações ANS")
		self.oHelper.ClickFolder("TISS WebService")
		self.oHelper.ClickFolder("Operadoras de Saúde")
		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("Cancelar")

		# Alterar
		self.oHelper.SearchBrowse(f'{"M SP    123456"}', key=5, index=True)
		self.oHelper.SetButton("Alterar")
		self.oHelper.SetValue("BA0_NOMINT","PLS DSAUPC TIR ALTERADO")
		self.oHelper.SetButton("Salvar")

		# Visualizar
		self.oHelper.SearchBrowse(f'{"M SP    123456"}', key=5, index=True)
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("BA0_NOMINT","PLS DSAUPC TIR ALTERADO")
		self.oHelper.SetButton("Confirmar")

		# Outras Ações > Complemento
		self.oHelper.SearchBrowse(f'{"M SP    123456"}', key=5, index=True)
		self.oHelper.SetButton("Outras Ações",sub_item='Complemento')
		self.oHelper.ClickFolder("Intercambio Eventual Especifico")
		self.oHelper.ClickFolder("Parametros para Pagamento")
		self.oHelper.ClickFolder("Tabelas de Pagamento e Recebimento")
		self.oHelper.ClickFolder("Tabelas de Reembolso")
		self.oHelper.ClickFolder("Operadora de Saude")
		self.oHelper.SetButton("Confirmar")

		# Outras Ações > Pesquisar
		self.oHelper.SetButton("Outras Ações",sub_item='Pesquisar')
		self.oHelper.SetButton("Ok")

		# Outras Ações > Excluir
		self.oHelper.SearchBrowse(f'{"M SP    123456"}', key=5, index=True)
		self.oHelper.SetButton("Outras Ações",sub_item='Excluir')
		self.oHelper.SetButton("Confirmar")

		self.oHelper.SetButton('x')
		self.oHelper.AssertTrue()


	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()