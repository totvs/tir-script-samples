from tir import Webapp
import unittest


"""-------------------------------------------------------------------
/*/{Protheus.doc} PLSA814TestCase
TIR - Casos de testes da rotina Analise de Alteracoes Cadastrais

@author Silvia SantAnna
@since 09/2020
@version 12
-------------------------------------------------------------------"""
class PLSA814(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAPLS","23/09/2020","T1","M SP 01","33")
		inst.oHelper.Program("PLSA814")

	def test_PLSA814_001(self):
		## Analisar
		self.oHelper.SearchBrowse(f'{"M SP    000011"}', key=1, index=True)
		self.oHelper.SetButton("Analisar")

		self.oHelper.WaitShow('Alteracao de Dados Cadastrais - ANALISAR')

		## Pasta Passos da Análise
		self.oHelper.ClickFolder('Passos da Análise')
		self.oHelper.ClickGridCell("Passo",row=1, grid_number=1)
		self.oHelper.SetKey("Enter", grid=True,  grid_number=1)
		self.oHelper.SetValue("B5G_CODPAS","0001",check_value = False)

		self.oHelper.ClickGridCell("Status",row=1, grid_number=1)
		self.oHelper.SetKey("Enter", grid=True,  grid_number=1)
		self.oHelper.SetButton("Sim")		# Confirma a finalizacao do passo

		self.oHelper.ClickGridCell("Enviou?",row=1, grid_number=1)
		self.oHelper.SetKey("Enter", grid=True,  grid_number=1)

		# Pasta Endereço
		self.oHelper.ClickFolder('Endereço')
		self.oHelper.ClickGridCell("Deferido",row=1, grid_number=1)
		self.oHelper.SetKey("Enter", grid=True,  grid_number=1)

		# Pasta Especialidade
		self.oHelper.ClickFolder('Especialidade')
		self.oHelper.ClickGridCell("Deferido",row=1, grid_number=1)
		self.oHelper.SetKey("Enter", grid=True,  grid_number=1)

		# Pasta Informações
		self.oHelper.ClickFolder('Informações')
		self.oHelper.ClickGridCell("Deferido",row=1, grid_number=2)		# CODIGO
		self.oHelper.SetKey("Enter", grid=True,  grid_number=2)
		self.oHelper.ClickGridCell("Deferido",row=2, grid_number=2)		# LOCALIDADE
		self.oHelper.SetKey("Enter", grid=True,  grid_number=2)
		self.oHelper.ClickGridCell("Deferido",row=3, grid_number=2)		# COD. ESPEC.
		self.oHelper.SetKey("Enter", grid=True,  grid_number=2)
		#self.oHelper.ScrollGrid(column="Campo", match_value="ESTADO C.R.", grid_number=2)  
		#self.oHelper.SetKey("DOWN", grid=True, grid_number=2)
		#self.oHelper.WaitShow('ESTADO C.R.')
		#self.oHelper.ClickGridCell("Deferido",row=4, grid_number=2)		# NOME
		#self.oHelper.SetKey("Enter", grid=True,  grid_number=2)
		#self.oHelper.ClickGridCell("Deferido",row=5, grid_number=2)		# NUMERO C.R.
		#self.oHelper.SetKey("Enter", grid=True,  grid_number=2)
		#self.oHelper.ClickGridCell("Deferido",row=6, grid_number=2)		# ESTADO C.R.
		#self.oHelper.SetKey("Enter", grid=True,  grid_number=2)
		#self.oHelper.ScrollGrid(column="Campo", match_value="SIGLA", grid_number=2)   
		#self.oHelper.WaitShow('SIGLA')
		#self.oHelper.ClickGridCell("Deferido",row=7, grid_number=2)		# CPF/CNPJ
		#self.oHelper.SetKey("Enter", grid=True,  grid_number=2)
		#self.oHelper.ClickGridCell("Deferido",row=8, grid_number=2)		# SIGLA
		#self.oHelper.SetKey("Enter", grid=True,  grid_number=2)

		# Pasta Corpo Clínico
		self.oHelper.ClickFolder('Corpo Clínico')
		self.oHelper.ClickGridCell("Deferido",row=1, grid_number=2)		# CODIGO
		self.oHelper.SetKey("Enter", grid=True,  grid_number=2)
		#self.oHelper.ClickGridCell("Deferido",row=2, grid_number=2)		# LOCALIDADE
		#self.oHelper.SetKey("Enter", grid=True,  grid_number=2)
		#self.oHelper.ClickGridCell("Deferido",row=3, grid_number=2)		# COD. ESPEC.
		#self.oHelper.SetKey("Enter", grid=True,  grid_number=2)
		#self.oHelper.ScrollGrid(column="Campo", match_value="ESTADO C.R.", grid_number=2)  
		#self.oHelper.ClickGridCell("Deferido",row=4, grid_number=2)		# NOME
		#self.oHelper.SetKey("Enter", grid=True,  grid_number=2)
		#self.oHelper.ClickGridCell("Deferido",row=5, grid_number=2)		# NUMERO C.R.
		#self.oHelper.SetKey("Enter", grid=True,  grid_number=2)
		#self.oHelper.ClickGridCell("Deferido",row=6, grid_number=2)		# ESTADO C.R.
		#self.oHelper.SetKey("Enter", grid=True,  grid_number=2)
		#self.oHelper.ScrollGrid(column="Campo", match_value="SIGLA", grid_number=2)   
		#self.oHelper.ClickGridCell("Deferido",row=7, grid_number=2)		# CPF/CNPJ
		#self.oHelper.SetKey("Enter", grid=True,  grid_number=2)
		#self.oHelper.ClickGridCell("Deferido",row=8, grid_number=2)		# SIGLA
		#self.oHelper.SetKey("Enter", grid=True,  grid_number=2)


		# Pasta Procedimentos
		self.oHelper.ClickFolder('Procedimentos')
		self.oHelper.ClickGridCell("Deferido",row=1, grid_number=2)
		self.oHelper.SetKey("Enter", grid=True,  grid_number=2)

		self.oHelper.ClickFolder('Corpo Clínico')
		self.oHelper.ClickFolder('Informações')
		self.oHelper.ClickFolder('Especialidade')
		self.oHelper.ClickFolder('Endereço')
		self.oHelper.ClickFolder('Passos da Análise')

		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")

		# Visualizar
		self.oHelper.SearchBrowse(f'{"M SP    000011"}', key=1, index=True)
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("B98_CODSEQ","000011")
		self.oHelper.SetButton("Fechar")

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()