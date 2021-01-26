from tir import Webapp
import unittest


"""-------------------------------------------------------------------
/*/{Protheus.doc} PLSA807TestCase
TIR - Casos de testes da rotina Visita de Relacionamento

@author Silvia SantAnna
@since 09/2020
@version 12
-------------------------------------------------------------------"""
class PLSA807(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAPLS","10/09/2020","T1","M SP 01","33")
		inst.oHelper.Program("PLSA807")

	def test_PLSA807_001(self):
		# Inclusao
		self.oHelper.SetButton("Incluir")

		self.oHelper.SetButton("OK")


		## Primeira Pasta
		self.oHelper.ClickFolder('Formulário Visita')

		self.oHelper.SetValue("B9W_AGENTE","000001")
		self.oHelper.SetValue("B9W_CODPRE","000133")
		self.oHelper.SetButton("Fechar")	#Verifique o prestador informado, pois nao sera permitida alteracao deste campo apos a gravacao
		self.oHelper.SetValue("B9W_DATAAG","01/01/2050")
		self.oHelper.SetValue("B9W_HORAAG","10:00")
		self.oHelper.SetValue("B9W_DESCON","PLS DSAUPC TIR INCLUSAO")
		self.oHelper.SetValue("B9W_TELCON","11332220000",check_value = False)
		self.oHelper.SetValue("B9W_EMAIL","PRESTADORES@EMAIL.COM")
		self.oHelper.SetValue("B9W_MOTVIS","01")
		self.oHelper.SetValue("B9W_CODOBS","001")
		self.oHelper.SetValue("B9W_CODSOL","000000")
		self.oHelper.SetValue("B9W_END2","1 - Sim")	

		## Segunda pasta
		self.oHelper.ClickFolder('Dados Prestador')

		self.oHelper.ClickGridCell("Item",row=1, grid_number=3)
		self.oHelper.SetKey("Enter", grid=True,  grid_number=3)
		self.oHelper.SetValue("B9V_CODSEQ","001")
		self.oHelper.SetButton("Fechar")	#Verifique o local informado pois nao sera permitida a alteracao deste campo apos a gravacao
		self.oHelper.SetValue("B9W_OBSERV","OBSERVACAO TESTE TIR")
		
		## Primeira Pasta
		self.oHelper.ClickFolder('Formulário Visita')
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")

		#self.oHelper.LoadGrid()
		
		# Alteracao
		self.oHelper.SearchBrowse(f'{"M SP    000100001201/01/2050"}', key=3, index=True)
		self.oHelper.SetButton("Alterar")
		self.oHelper.SetValue("B9W_DESCON","PLS DSAUPC TIR ALTERACAO")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		
		# Visualizacao
		self.oHelper.SearchBrowse(f'{"M SP    000100001201/01/2050"}', key=3, index=True)
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("B9W_DESCON","PLS DSAUPC TIR ALTERACAO")
		self.oHelper.SetButton("Fechar")

		# Copiar
		self.oHelper.SearchBrowse(f'{"M SP    000100001201/01/2050"}', key=3, index=True)
		self.oHelper.SetButton("Outras Ações",sub_item='Copiar')
		## Primeira Pasta
		self.oHelper.ClickFolder('Formulário Visita')
		self.oHelper.SetValue("B9W_DESCON","PLS DSAUPC TIR COPIA")
		self.oHelper.SetValue("B9W_CODPRE","000007")
		self.oHelper.SetButton("Fechar")	#Verifique o prestador informado, pois nao sera permitida alteracao deste campo apos a gravacao
		self.oHelper.SetValue("B9W_DATAAG","01/01/2040")
		## Segunda pasta
		self.oHelper.ClickFolder('Dados Prestador')
		self.oHelper.ClickGridCell("Item",row=1, grid_number=3)
		self.oHelper.SetKey("Enter", grid=True,  grid_number=3)
		self.oHelper.SetValue("B9V_CODSEQ","001")
		self.oHelper.SetButton("Fechar")	#Verifique o local informado pois nao sera permitida a alteracao deste campo apos a gravacao
		self.oHelper.SetValue("B9W_OBSERV","OBSERVACAO TIR COPIA")
		## Primeira Pasta
		self.oHelper.ClickFolder('Formulário Visita')
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")

		# Conhecimento
		self.oHelper.SearchBrowse(f'{"M SP    000100001201/01/2040"}', key=3, index=True)
		self.oHelper.SetButton("Outras Ações",sub_item='Conhecimento')
		self.oHelper.SetButton("Cancelar")

		# Exclusao
		## Copia
		self.oHelper.SearchBrowse(f'{"M SP    000100001201/01/2040"}', key=3, index=True)
		self.oHelper.SetButton("Outras Ações",sub_item='Excluir')
		self.oHelper.SetValue("B9W_DESCON","PLS DSAUPC TIR COPIA")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		## Original
		self.oHelper.SearchBrowse(f'{"M SP    000100001201/01/2050"}', key=3, index=True)
		self.oHelper.SetButton("Outras Ações",sub_item='Excluir')
		self.oHelper.SetValue("B9W_DESCON","PLS DSAUPC TIR ALTERACAO")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()