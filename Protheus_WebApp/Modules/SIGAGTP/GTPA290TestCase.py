from tir import Webapp
import unittest

class GTPA290(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAGTP", "29/05/2020", "T1", "D MG 01 ")
		inst.oHelper.Program('GTPA290')

	def test_GTPA290_CT001(self):

		self.oHelper.ClickLabel("+ Incluir Recurso")
		self.oHelper.SetButton("Fechar")

		self.oHelper.ClickLabel("+ Substituir Recurso")
		self.oHelper.SetButton("Fechar")

		self.oHelper.ClickLabel("+ Histórico do Monitor")
		self.oHelper.SetButton("Fechar")

		self.oHelper.ClickLabel("+ Finalizar Viagens")
		self.oHelper.SetButton("Fechar")

		self.oHelper.ClickLabel("+ Reabrir Viagens Finalizadas")
		self.oHelper.SetButton("Fechar")

		self.oHelper.ClickLabel("+ Ocorrências")
		self.oHelper.SetButton("Fechar")

		self.oHelper.ClickLabel("+ Finalizar Ocorrências")
		self.oHelper.SetButton("Fechar")

		self.oHelper.ClickLabel("+ Ajustar KM Realizado")
		self.oHelper.SetButton("Fechar")

		self.oHelper.ClickLabel("+ Alocação Viagem Especial")
		self.oHelper.SetButton("Fechar")

		self.oHelper.AssertTrue()

	def test_GTPA290_CT002(self):

		self.oHelper.ClickLabel("+ Monitor")

		self.oHelper.SetValue('Data Viagem de ?              ', '03/06/2020')
		self.oHelper.SetValue('Data Viagem até ?             ', '03/06/2020')
		self.oHelper.SetValue('Remover Serviços Cancelados ? ', '2-Não')
		self.oHelper.SetValue('Remover Viagens Canceladas ?  ', '2-Não')
		self.oHelper.SetValue('Tipo de Viagem ?              ', '3-Todas')

		self.oHelper.SetButton("Ok")
		
		self.oHelper.LoadGrid()

		self.oHelper.ClickLabel("+ Alocação Viagem Especial")
		self.oHelper.SetValue('Tipo Colab.', '01')
		self.oHelper.SetValue('Hora Inicial', '10:01')
		self.oHelper.SetValue('Hora Final', '13:00')
		self.oHelper.SetButton("Outras Ações","Inclui Alocação")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")

		self.oHelper.ClickLabel("+ Monitor")
		self.oHelper.SetButton("Não")

		self.oHelper.SetValue('Data Viagem de ?              ', '02/06/2020')
		self.oHelper.SetValue('Data Viagem até ?             ', '02/06/2020')
		self.oHelper.SetValue('Remover Serviços Cancelados ? ', '2-Não')
		self.oHelper.SetValue('Remover Viagens Canceladas ?  ', '2-Não')
		self.oHelper.SetValue('Tipo de Viagem ?              ', '3-Todas')

		self.oHelper.SetButton("Ok")

		self.oHelper.LoadGrid()

		self.oHelper.ClickGridCell("Confirmado?", row=1, grid_number=1)

		self.oHelper.ClickLabel("+ Legenda")
		self.oHelper.SetButton("Fechar")

		self.oHelper.ClickLabel("+ Incluir Recurso")
		self.oHelper.SetButton("Posicionada")
		self.oHelper.SetValue('Cód Recurso', '000004')
		self.oHelper.SetValue('Tipo', '01')
		self.oHelper.SetButton("Outras Ações","Executar Filtro")
		self.oHelper.SetButton("Outras Ações","Marque/Desmarque todos")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.LoadGrid()
		
		self.oHelper.ClickLabel("+ Substituir Recurso")
		self.oHelper.SetValue('Cód Recurso', '000004')
		self.oHelper.SetValue('Tipo', '01')
		self.oHelper.SetValue('Substituto', '000001')
		self.oHelper.SetValue('Justf', 'Teste automatizado')
		self.oHelper.SetButton("Outras Ações","Executar Filtro")
		self.oHelper.SetButton("Outras Ações","Marque/Desmarque todos")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.LoadGrid()
		
		self.oHelper.ClickLabel("+ Salvar Dados")
		self.oHelper.LoadGrid()

		self.oHelper.ClickLabel("+ Remover Recurso")
		self.oHelper.SetValue('Cód. Recurso', '000001')
		self.oHelper.SetValue('Data de', '02/06/2020')
		self.oHelper.SetValue('Data até', '02/06/2020')
		self.oHelper.SetButton("Outras Ações","Executar Filtro")
		self.oHelper.SetButton("Outras Ações","Marque/Desmarque todos")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.LoadGrid()
		
		self.oHelper.ClickLabel("+ Salvar Dados")
		self.oHelper.LoadGrid()

		self.oHelper.ClickLabel("+ Incluir Recurso")
		self.oHelper.SetButton("Posicionada")
		self.oHelper.SetValue('Cód Recurso', '000004')
		self.oHelper.SetValue('Tipo', '01')
		self.oHelper.SetButton("Outras Ações","Executar Filtro")
		self.oHelper.SetButton("Outras Ações","Marque/Desmarque todos")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.LoadGrid()

		self.oHelper.ClickLabel("+ Incluir Recurso")
		self.oHelper.SetButton("Posicionada")
		self.oHelper.SetValue('Tp. Recurso', '2 - Veículo')
		self.oHelper.SetValue('Cód Recurso', 'GTPVEIC01')
		self.oHelper.SetButton("Outras Ações","Executar Filtro")
		self.oHelper.SetButton("Outras Ações","Marque/Desmarque todos")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.LoadGrid()

		self.oHelper.ClickLabel("+ Salvar Dados")
		self.oHelper.LoadGrid()

		self.oHelper.ClickLabel("+ Histórico do Monitor")
		self.oHelper.SetButton("Fechar")

		self.oHelper.ClickLabel("+ Veiculo em Manutenção")
		self.oHelper.SetButton("Fechar")

		self.oHelper.ClickLabel("+ Ajustar KM Realizado")
		self.oHelper.SetValue('Cód.Linha', '000005')
		self.oHelper.SetValue('Local Origem', 'LOC001')
		self.oHelper.SetValue('Local Destin', 'LOC002')
		self.oHelper.SetValue('Data Início', '02/06/2020')
		self.oHelper.SetValue('Data Fim', '02/06/2020')
		self.oHelper.SetButton("Outras Ações","Executar Filtro")
		self.oHelper.SetButton("Outras Ações","Salvar")
		self.oHelper.SetButton("Fechar")

		self.oHelper.ClickLabel("+ Confirmar Recurso")
		self.oHelper.SetValue('Cód. Recurso', '000004')
		self.oHelper.SetValue('Data de', '02/06/2020')
		self.oHelper.SetValue('Data até', '02/06/2020')
		self.oHelper.SetValue('Tp Confirm?', '2 - Planejamento')
		self.oHelper.SetButton("Outras Ações","Executar Filtro")
		self.oHelper.SetButton("Outras Ações","Marque/Desmarque todos")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.LoadGrid()

		self.oHelper.ClickLabel("+ Confirmar Recurso")
		self.oHelper.SetValue('Tipo Recurso', '2 - Veiculo')
		self.oHelper.SetValue('Cód. Recurso', 'GTPVEIC01')
		self.oHelper.SetValue('Data de', '02/06/2020')
		self.oHelper.SetValue('Data até', '02/06/2020')
		self.oHelper.SetValue('Tp Confirm?', '2 - Planejamento')
		self.oHelper.SetButton("Outras Ações","Executar Filtro")
		self.oHelper.SetButton("Outras Ações","Marque/Desmarque todos")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.LoadGrid()

		self.oHelper.ClickLabel("+ Finalizar Viagens")
		self.oHelper.SetButton("Posicionada")
		self.oHelper.SetButton("Fechar")
		self.oHelper.LoadGrid()

		self.oHelper.ClickLabel("+ Salvar Dados")
		self.oHelper.LoadGrid()

		#self.oHelper.SearchBrowse("000061", "Código")
		self.oHelper.ClickLabel("+ Reabrir Viagens Finalizadas")
		self.oHelper.SetButton("Posicionada")
		self.oHelper.SetButton("Fechar")
		self.oHelper.LoadGrid()

		self.oHelper.ClickLabel("+ Salvar Dados")
		self.oHelper.LoadGrid()

		self.oHelper.ClickLabel("+ Ocorrências")
		self.oHelper.SetButton("Posicionada")
		self.oHelper.SetButton("Outras Ações","Fechar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("Outras Ações","Reabrir")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("Fechar")
		
		self.oHelper.ClickLabel("+ Finalizar Ocorrências")
		self.oHelper.SetButton("Posicionada")
		self.oHelper.SetButton("Fechar")

		self.oHelper.ClickLabel("+ Alocação Viagem Especial")
		self.oHelper.SetButton("Fechar")

		self.oHelper.ClickLabel("+ Escalas Extraordinárias")
		self.oHelper.SetButton('X')
		self.oHelper.LoadGrid()
		self.oHelper.SetButton("Fechar")
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()	

if __name__ == '__main__':
	unittest.main()
