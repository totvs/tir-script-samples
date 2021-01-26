from tir import Webapp
import unittest
from tir.technologies.apw_internal import ApwInternal
import datetime
import time

DateSystem = datetime.datetime.today().strftime('%d/%m/%Y')
DateVal = datetime.datetime(2120, 5, 17)
"""-------------------------------------------------------------------
/*/{Protheus.doc} PLSA940TestCase
TIR - Casos de testes da rotina Tabela Padrao

@author Silvia SantAnna
@since 09/2020
@version 12
-------------------------------------------------------------------"""
class PLSA940(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAPLS",DateSystem,"T1","M SP 01","33")
		inst.oHelper.Program("PLSA940")

	def test_PLSA940_001(self):
		# Alterar
		self.oHelper.SearchBrowse(f'{"M SP    0120103018"}', key=1, index=True)
		self.oHelper.SetButton("Alterar")

		## Pasta Cobertura Padrao
		self.oHelper.ClickFolder('Cobertura Padrao')
		self.oHelper.SetValue("BR8_BENUTL","1 - Sim")
		self.oHelper.SetValue("BR8_SEXO","3 - Ambos")
		self.oHelper.SetValue("BR8_IDAMAX","999")
		self.oHelper.SetValue("BR8_QTMAAU","999")

		## Pasta Outras Informacoes
		self.oHelper.ClickFolder('Outras Informacoes')
		self.oHelper.SetValue("BR8_PODDIG","0 - Nao")

		# Pasta Odontologico
		self.oHelper.ClickFolder('Odontologico')
		self.oHelper.SetValue("BR8_ODONTO","0 - Nao")

		## Pasta Outros
		self.oHelper.ClickFolder('Outros')
		self.oHelper.SetValue("BR8_DIFIDA","1 - Sim")

		self.oHelper.SetButton("Salvar")

		# Visualizar
		self.oHelper.SearchBrowse(f'{"M SP    0120103018"}', key=1, index=True)
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("BR8_CODPSA","20103018")
		self.oHelper.SetButton("Confirmar")

		## Outras Acoes > Period. Dif. Idade
		self.oHelper.SearchBrowse(f'{"M SP    0120103018"}', key=1, index=True)
		self.oHelper.SetButton("Outras Ações",'Period. Dif. Idade')
		self.oHelper.ClickGridCell("Alias",row=1, grid_number=1)
		self.oHelper.SetKey("Enter", grid=True,  grid_number=1)
		self.oHelper.SetValue("B1Y_IDADE ","1",check_value = False)
		self.oHelper.SetValue("B1Y_TIDADE","3 - Anos")
		self.oHelper.SetValue("B1Y_PERIOD","1",check_value = False)
		self.oHelper.SetValue("B1Y_UNPERI","4 - Anos")
		self.oHelper.SetButton("Salvar")

		self.oHelper.SetButton("Salvar")

		# Alterar
		self.oHelper.SearchBrowse(f'{"M SP    0120103018"}', key=1, index=True)
		self.oHelper.SetButton("Alterar")

		# Pasta Odontologico
		self.oHelper.ClickFolder('Odontologico')
		self.oHelper.SetValue("BR8_ODONTO","1 - Sim")
		self.oHelper.SetButton("Salvar")

		## Outras Acoes > Dente/Região
		self.oHelper.SearchBrowse(f'{"M SP    0120103018"}', key=1, index=True)
		self.oHelper.SetButton("Outras Ações",'Dente/Região')
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetBranch("M SP 01 ")
		self.oHelper.SetValue("B05_CODIGO","11")
		self.oHelper.SetValue("B05_INFORM","PLS DSAUPC TIR OBSERVACAO DENTARIO")

		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("Cancelar")

		self.oHelper.SetButton("Alterar")
		self.oHelper.SetValue("B05_CODIGO","12")
		self.oHelper.SetButton("Salvar")

		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("B05_CODIGO","12")
		self.oHelper.CheckResult("B05_INFORM","PLS DSAUPC TIR OBSERVACAO DENTARIO")
		self.oHelper.SetButton("Confirmar")

		## Outras Acoes > Faces
		self.oHelper.SetButton("Outras Ações",'Faces')
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetBranch("M SP 01 ")
		self.oHelper.SetValue("BYL_FACE","D")
		self.oHelper.SetValue("BYL_INFORM","PLS DSAUPC TIR OBSERVACAO DENTARIO")

		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("Cancelar")

		self.oHelper.SetButton("Alterar")
		self.oHelper.SetValue("BYL_FACE","DI")
		self.oHelper.SetButton("Salvar")

		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("BYL_FACE","DI")
		self.oHelper.CheckResult("BYL_INFORM","PLS DSAUPC TIR OBSERVACAO DENTARIO")
		self.oHelper.SetButton("Confirmar")

		self.oHelper.SetButton("Outras Ações",'Excluir')
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("x")

		self.oHelper.SetButton("Outras Ações",'Excluir')
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("x")



		self.oHelper.SetButton("x")

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()