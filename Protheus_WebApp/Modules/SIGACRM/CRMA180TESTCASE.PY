from tir import Webapp
import unittest
import time

class CRMA180(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()

		inst.oHelper.SetTIRConfig(config_name="user", value="aline.toyoda")
		inst.oHelper.SetTIRConfig(config_name="password", value="1")

		inst.oHelper.Setup('SIGAADV','26/08/2019','T1','D MG 01 ','73')
		inst.oHelper.Program('CRMA180')

	#CT012 - TIR - Incluir Atividade do tipo Tarefa - Campos Obrigatórios
	def test_CRMA180_CT012(self):
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch("D MG 01 ")
		self.oHelper.ClickLabel("Tarefa")
		self.oHelper.SetButton("Sim")

		self.oHelper.SetValue("AOF_ASSUNT", "Tarefa CT012")
		self.oHelper.SetValue("AOF_DTINIC", "26/08/2019")
		self.oHelper.SetValue("AOF_DTFIM", "26/10/2019")

		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")

		self.oHelper.AssertTrue()

	#CT013 - TIR - Alterar uma Atividade do tipo Tarefa
	def test_CRMA180_CT013(self):
		self.oHelper.SearchBrowse("D MG 01 000009", key=1, index=True)
		self.oHelper.SetButton("Alterar")

		self.oHelper.SetValue("AOF_ASSUNT", "Tarefa CT013 ALTERADO")

		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")

		self.oHelper.AssertTrue()

	#CT014 - TIR - Visualizar uma Atividade do tipo Tarefa
	def test_CRMA180_CT014(self):
		self.oHelper.SearchBrowse("D MG 01 000009")
		self.oHelper.SetButton("Visualizar")
		time.sleep(10)
		self.oHelper.SetButton("Fechar")

		self.oHelper.AssertTrue()

	#CT015 - TIR - Excluir uma Atividade do tipo Tarefa
	def test_CRMA180_CT015(self):
		self.oHelper.SearchBrowse("D MG 01 000010")
		self.oHelper.SetButton("Outras Ações", "Excluir")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")

		self.oHelper.SetButton("Visualizar")
		tarefa = self.oHelper.GetValue("AOF_CODIGO")
		if tarefa == '000010':
			self.oHelper.AssertFalse()
		else:
			self.oHelper.SetButton("Fechar")
			self.oHelper.AssertTrue()

	#CT016 - TIR - Visualizar uma Atividade do tipo Compromisso
	def test_CRMA180_CT016(self):
		self.oHelper.SearchBrowse("D MG 01 000011")
		self.oHelper.SetButton("Visualizar")
		time.sleep(10)
		self.oHelper.SetButton("Fechar")

		self.oHelper.AssertTrue()
	
	#CT017 - TIR - Visualizar uma Atividade do tipo E-mail
	def test_CRMA180_CT017(self):
		self.oHelper.SearchBrowse("D MG 01 000013")
		self.oHelper.SetButton("Visualizar")
		time.sleep(10)
		self.oHelper.SetButton("Fechar")

		self.oHelper.AssertTrue()

	#CT018 - TIR - Adicionar anexos do Banco de Conhecimento na Atividade de E-mail
	def test_CRMA180_CT018(self):
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch("D MG 01 ")
		self.oHelper.ClickLabel("E-mail")
		self.oHelper.SetButton("Sim")

		self.oHelper.SetValue("AOF_DESTIN", "teste@hotmail.com")
		self.oHelper.SetValue("AOF_ANEXO", "1 - Sim")
		self.oHelper.SetButton("Confirmar")

		self.oHelper.SetValue("AC9_OBJETO", "0000000046", grid=True)
		self.oHelper.LoadGrid()
		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("Fechar")

		self.oHelper.AssertTrue()
	
	#CT019 - TIR - Abrir o Banco de Conhecimento de uma Atividade do tipo Tarefa
	def test_CRMA180_CT019(self):
		self.oHelper.SearchBrowse("D MG 01 000013")
		self.oHelper.SetButton("Outras Ações", "Relacionadas, Conhecimento")
		time.sleep(10)
		self.oHelper.SetButton("Cancelar")

		self.oHelper.AssertTrue()

	#CT020 - TIR - Incluir um Modelo de E-mail em uma Atividade do tipo E-mail
	def test_CRMA180_CT020(self):
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch("D MG 01 ")
		self.oHelper.ClickLabel("E-mail")
		self.oHelper.SetButton("Sim")

		self.oHelper.SetValue("AOF_DESTIN", "teste@hotmail.com")
		self.oHelper.SetValue("AOF_ENTIDA", "ACH")
		self.oHelper.SetValue("AOF_CHAVE", "TMK02001")

		self.oHelper.SetButton("Outras Ações", "Modelo de E-mail")
		self.oHelper.ClickGridCell("Título", 1)
		self.oHelper.SetButton("Pré-Visualizar")
		time.sleep(10)
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton("Ok")

		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()