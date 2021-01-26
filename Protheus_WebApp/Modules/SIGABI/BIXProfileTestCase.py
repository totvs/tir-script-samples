# -*- coding: utf-8 -*-

import unittest

from tir import Webapp


class BIXPROFILE(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup('SIGACFG','11/12/2018','T1','D MG 01 ')
		inst.oHelper.SetLateralMenu('Ambiente > Extrator Bi > Perfil de Extração')

	def test_BIXPROFILE_CT001(self):

		self.oHelper.SetButton('Incluir')
		self.oHelper.SetValue("Código", "000001")
		self.oHelper.SetValue("Descrição", "Extracao 000001")
		self.oHelper.ClickLabel("Marcar / Desmarcar" ) # desmarcar
		self.oHelper.ScrollGrid(column="Tabela", match_value="HL2", grid_number=2)
		self.oHelper.ClickBox("Tabela", contents_list="HL2", grid_number=2)
		self.oHelper.SetButton("Sim")
		self.oHelper.SetButton("Salvar")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")

		self.oHelper.AssertTrue()
	
	def test_BIXPROFILE_CT002(self):
		
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetValue("Código", "000000")
		self.oHelper.SetValue("Descrição", "Extracao 00000")
		self.oHelper.SetButton('Confirmar')
		self.oHelper.SetButton('Fechar')

		self.oHelper.AssertTrue()

	def test_BIXPROFILE_CT003(self):

		self.oHelper.SetButton("Visualizar") # Perfil de extração - VISUALIZAR
		self.oHelper.SetButton("Fechar")

		self.oHelper.AssertTrue()

	def test_BIXPROFILE_CT004(self):
		
		self.oHelper.SetButton("Alterar") # Perfil de Extração - ALTERAR
		self.oHelper.SetValue("Descrição", "BIXPROFILE")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton('Fechar')

		self.oHelper.AssertTrue()
	
	def test_BIXPROFILE_CT005(self):
		
		self.oHelper.SetButton("Outras Ações", sub_item="Executar Perfil") # Executar Perfil
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton('Não')

		self.oHelper.AssertTrue()

	def test_BIXPROFILE_CT006(self):

		self.oHelper.SetButton("Outras Ações", sub_item="Excluir") # Excluir
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()
