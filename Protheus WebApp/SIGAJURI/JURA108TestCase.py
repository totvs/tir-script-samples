from tir import Webapp
import unittest
import time

class JURA108(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.SetTIRConfig(config_name="user", value="daniel.frodrigues")
		inst.oHelper.SetTIRConfig(config_name="password", value="1")
		inst.oHelper.Setup('SIGAJURI','','T1','D MG 01 ','76')
		inst.oHelper.Program('JURA106')
		inst.oHelper.AddParameter("MV_JHBPESF", "", "1", "", "")
		inst.oHelper.SetParameters()

	def test_JURA108_CT001(self):
		print('CT001 - Exp. FOLLOW UP - MULTIPLOS RESPONSAVEIS')
		
		# Preenche os dados para filtro
		self.oHelper.SetValue("cValor","Contencioso - Fup",name_attr=True)
		self.oHelper.WaitFieldValue("NTA_CTIPO","")
		self.oHelper.SetValue('NTA_CTIPO', '00001')
		
		# Realiza a pesquisa e posiciona em um registro e inicia a rotina de exportação personalizada
		self.oHelper.ClickLabel('Pesquisar')
		self.oHelper.ClickGridCell("Código Assunto Jurídico",row=1)
		time.sleep(3)
		self.oHelper.ClickLabel('Exportação Personalizada')
		time.sleep(3)

		# Preenche o combo de tabelas
		self.oHelper.SetValue("cCmbTabela","000011 - Acordos (NYP001)",name_attr=True)
		time.sleep(3)
		
		# Clica no botão para Adicionar todos os campos
		self.oHelper.SetButton("Add. Todos >>")
		time.sleep(2)

		# Clica no botão sim do pergunte
		self.oHelper.SetButton("Sim")

		# Clica no botão para Remover todos
		self.oHelper.SetButton("<< Rem. Todos")
		time.sleep(2)

		# Clica no botão sim do pergunte
		self.oHelper.SetButton("Sim")

		# Preenche o combo de tabelas
		self.oHelper.SetValue("cCmbTabela","000005 - Follow-ups (NTA001)",name_attr=True)
		time.sleep(3)
		''
		# Preenche o campo de Pesquisa e adiciona o campo pesquisado
		self.oHelper.SetValue("cGetSearch","HORA",name_attr=True)
		self.oHelper.SetButton("Pesquisar")
		self.oHelper.SetButton("Adicionar >>")
		time.sleep(2)

		# Preenche o campo de Pesquisa e adiciona o campo pesquisado
		self.oHelper.SetValue("cGetSearch","DT FOLLOW-UP",name_attr=True)
		self.oHelper.SetButton("Pesquisar")
		self.oHelper.SetButton("Adicionar >>")
		time.sleep(2)

		# Preenche o campo de Pesquisa e adiciona o campo pesquisado
		self.oHelper.SetValue("cGetSearch","NOME DO PARTICI",name_attr=True)
		self.oHelper.SetButton("Pesquisar")
		self.oHelper.SetButton("Adicionar >>")
		time.sleep(2)

		# Clica no botão mover para baixo
		self.oHelper.SetButton("Mover para Baixo")
		time.sleep(2)

		# Clica no botão mover para Cima
		self.oHelper.SetButton("Mover para Cima")
		time.sleep(2)

		# Altera a linha Hora
		self.oHelper.SetValue("cGetRename","Hora F-Up",name_attr=True)
		self.oHelper.SetButton("Renomear")
		time.sleep(2)

		# Clica no botão mover para Remove
		self.oHelper.SetButton("<< Remove")
		time.sleep(2)
		
		# Realiza a exportação do arquivo
		self.oHelper.SetButton("Filt. Agrup.")
		self.oHelper.SetButton("Ok")

		# Realiza a exportação do arquivo
		self.oHelper.SetButton("Exportar")

		# Clica no botão salvar como
		self.oHelper.SetValue("cGetNewConfig","FOLLOW UP - MULTIPLOS RESPONSAVEIS",name_attr=True)
		self.oHelper.SetButton("Salvar Como")

		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")

		# Clica no botão sair da tela de exportação
		self.oHelper.SetButton("Sair")
		self.oHelper.ClickLabel("Sair")

		# Valida se tudo deu certo
		self.oHelper.AssertTrue()
		print('CT001 - Fim')
	
	def test_JURA108_CT002(self):
		print('CT002 - Atualização de configuração precadastrada')

		self.oHelper.Program('JURA106')
		# Preenche os dados para filtro
		self.oHelper.SetValue("cValor","Contencioso - Fup",name_attr=True)
		self.oHelper.WaitFieldValue("NTA_CTIPO","")
		self.oHelper.SetValue('NTA_CTIPO', '00001')
		
		# Realiza a pesquisa e posiciona em um registro e inicia a rotina de exportação personalizada
		self.oHelper.ClickLabel('Pesquisar')
		self.oHelper.ClickGridCell("Código Assunto Jurídico",row=1)
		time.sleep(3)
		self.oHelper.ClickLabel('Exportação Personalizada')
		time.sleep(3)

		# Preenche o combo de tabelas
		self.oHelper.SetValue("cCmbConfig","0007 - JURA108_TIR - Caso automatizado oficial 002",name_attr=True)
		time.sleep(3)

		# Preenche o combo de tabelas
		self.oHelper.SetValue("cCmbTabela","000009 - Andamento (NT4001)",name_attr=True)
		time.sleep(3)

		# Preenche o campo de Pesquisa e adiciona o campo pesquisado
		self.oHelper.SetValue("cGetSearch","DESC FASE",name_attr=True)
		self.oHelper.SetButton("Pesquisar")
		self.oHelper.SetButton("Adicionar >>")
		time.sleep(2)
		
		# Clique em atualizar para salvar o novo layout
		self.oHelper.SetButton("Atualizar")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Sim")
		self.oHelper.SetButton("Fechar")
		
		# Preenche o combo de Configurações
		self.oHelper.SetValue("cCmbConfig","0007 - JURA108_TIR - Caso automatizado oficial 002",name_attr=True)
		time.sleep(3)

		# Realiza a exportação do arquivo
		self.oHelper.SetButton("Exportar")
		self.oHelper.SetButton("Sim")
		self.oHelper.SetButton("Sim")
		
		# Encerra a rotina
		self.oHelper.SetButton("Sair")
		self.oHelper.ClickLabel("Sair")
		self.oHelper.AssertTrue()
		self.oHelper.RestoreParameters()
		print('CT002 - Fim')
		
	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()
