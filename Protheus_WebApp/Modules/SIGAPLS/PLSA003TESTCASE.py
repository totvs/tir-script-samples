from tir import Webapp
import unittest


"""-------------------------------------------------------------------
/*/{Protheus.doc} PLSA003TestCase
TIR - Casos de testes da rotina parcelamento de cobranca de guias

@author Silvia SantAnna
@since 09/2020
@version 12
-------------------------------------------------------------------"""
class PLSA003(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAPLS","11/09/2020","T1","M SP 01","33")
		inst.oHelper.Program("PLSA003")
		
	def test_PLSA003_001(self):
		#Para este cenario de teste, as guias abaixo nao devem ter parcelamento gerado.
		self.oHelper.SetButton("Novo Lote")

		#preenchendo tela de pergunte
		self.oHelper.SetValue("Mes de:","01")
		self.oHelper.SetValue("Mes ate","12")
		self.oHelper.SetValue("Ano de:","2020")
		self.oHelper.SetValue("Ano ate:","2020")
		self.oHelper.SetValue("RDA de:","")
		self.oHelper.SetValue(field = "cRDAAt", value = "ZZZZZZ", name_attr = True)
		self.oHelper.SetValue("Local Digitacao de:","0001")
		self.oHelper.SetValue(field = "cLocalAt", value = "0001", name_attr = True)
		self.oHelper.SetValue("Operadora de:","0001")
		self.oHelper.SetValue(field = "cCdOpeAte", value = "0001", name_attr = True)
		self.oHelper.SetValue("Empresa de:","")
		self.oHelper.SetValue(field = "cEmpAte", value = "ZZZZ", name_attr = True)
		self.oHelper.SetValue("Matricula de:","")
		self.oHelper.SetValue(field = "cMatAte", value = "ZZZZZZ", name_attr = True)

		self.oHelper.SetButton("Salvar")

		self.oHelper.SearchBrowse(f'{"M SP    00010113000010"}', key=5, index=True)
		self.oHelper.SetKey("Enter", grid=True, grid_number=4)
		self.oHelper.SetButton("Gerar")
		self.oHelper.SetButton("Não") 		#Deseja gerar um novo lote para as guias seleciondas
		self.oHelper.SetKey("Enter", grid=True, grid_number=4)

		self.oHelper.SearchBrowse(f'{"M SP    00010113000011"}', key=5, index=True)
		self.oHelper.SetKey("Enter", grid=True, grid_number=4)
		self.oHelper.SetButton("Gerar")
		self.oHelper.SetButton("Sim")		#Deseja gerar um novo lote para as guias seleciondas
		self.oHelper.SetButton("Cancelar")
		self.oHelper.SetButton("Fechar") 	#Acoes de parcelamento abortadas
		self.oHelper.SetKey("Enter", grid=True, grid_number=4)

		self.oHelper.SearchBrowse(f'{"M SP    00010113000006"}', key=5, index=True)
		self.oHelper.SetKey("Enter", grid=True, grid_number=4)
		self.oHelper.SetButton("Gerar")
		self.oHelper.SetButton("Sim")
		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("Cancelar") 	#Confirma o processamento
		self.oHelper.SetButton("Fechar") 	#Acoes de parcelamento abortadas
		self.oHelper.SetButton("Gerar")
		self.oHelper.SetButton("Sim")
		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("Salvar")	#Confirma o processamento
		self.oHelper.SetButton("Fechar")	#Acoes de parcelamento concluida com sucesso

		self.oHelper.SetButton("Vis. Lote")
		self.oHelper.SetValue("B0K_CODOPE","0001")
		self.oHelper.SetButton("Confirmar")

		self.oHelper.SetButton("Outras Ações", sub_item='Deb/Cre. RDA')
		self.oHelper.SetButton("Ok")		#Nao existem registros relacionados a este lote

		self.oHelper.SetButton("Outras Ações", sub_item='Deb/Cre. Benef.')
		self.oHelper.SetButton("Historico")
		self.oHelper.SetButton("OK")

		self.oHelper.SetButton('x')

		self.oHelper.SetButton("Modificar")
		self.oHelper.SetValue("BSQ_VALOR","50,00")
		self.oHelper.SetButton("Salvar")

		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("BSQ_USUARI","00010113000006010")
		self.oHelper.CheckResult("BSQ_VALOR","50,00")
		self.oHelper.SetButton("Confirmar")

		self.oHelper.SetButton("Outras Ações", sub_item='Legenda')
		self.oHelper.SetButton("OK")
		self.oHelper.SetButton("Fechar")

		self.oHelper.SetButton("Outras Ações", sub_item='Prorrogar')
		self.oHelper.SetButton("OK")
		self.oHelper.SetButton("Não")	#Deseja prorrogar o lancamento

		self.oHelper.SetButton("Outras Ações", sub_item='Prorrogar')
		self.oHelper.SetButton("OK")
		self.oHelper.SetButton("Sim")
		self.oHelper.SetButton("Fechar") #Prorrogacao concluida com sucesso

		self.oHelper.SetButton("Outras Ações", sub_item='Excluir')
		self.oHelper.SetValue("BSQ_USUARI","00010113000006010")
		self.oHelper.SetButton("Confirmar")

		self.oHelper.SetButton('x')

		self.oHelper.SetButton("Outras Ações", sub_item='Exlcuir Lote')
		self.oHelper.SetValue("B0K_CODOPE","0001")
		self.oHelper.SetButton("Confirmar")

		self.oHelper.SetButton('x')

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()