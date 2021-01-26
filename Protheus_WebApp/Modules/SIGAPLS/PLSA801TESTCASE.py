from tir import Webapp
import unittest


"""-------------------------------------------------------------------
/*/{Protheus.doc} PLSA801TestCase
TIR - Casos de testes da rotina Motivos de visita

@author Silvia SantAnna
@since 09/2020
@version 12
-------------------------------------------------------------------"""
class PLSA801(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAPLS","10/09/2020","T1","M SP 01","33")
		inst.oHelper.Program("PLSA801")

	def test_PLSA801_001(self):
		self.oHelper.SetButton("Incluir")
		#self.oHelper.SetBranch('M SP 01')
		self.oHelper.SetButton("OK")

		#INCLUSAO
		## 1 - RELACIONAMENTO
		self.oHelper.SetValue("B9L_DESVIS","PLS DSAUPC TIR REL INCLUSAO")
		self.oHelper.SetValue("B9L_TIPVIS","1 - RELACIONAMENTO")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")

		#ALTERACAO
		self.oHelper.SearchBrowse(f'{"M SP    0001PLS DSAUPC TIR REL INCLUSAO"}', key=5, index=True)
		self.oHelper.SetButton("Alterar")
		self.oHelper.SetValue("B9L_DESVIS","PLS DSAUPC TIR REL ALTERACAO")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		
		#VISUALIZACAO
		self.oHelper.SetButton("Visualizar")
		self.oHelper.CheckResult("B9L_DESVIS","PLS DSAUPC TIR REL ALTERACAO")
		self.oHelper.SetButton("Fechar")

		#COPIA
		## 3 - INSTITUCIONAL
		self.oHelper.SetButton("Outras Ações",sub_item='Copiar')
		self.oHelper.SetValue("B9L_DESVIS","PLS DSAUPC TIR INT COPIA")
		self.oHelper.SetValue("B9L_TIPVIS","3 - INSTITUCIONAL")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		## 0 - CAPTAÇÃO
		self.oHelper.SetButton("Outras Ações",sub_item='Copiar')
		self.oHelper.SetValue("B9L_DESVIS","PLS DSAUPC TIR CAP COPIA")
		self.oHelper.SetValue("B9L_TIPVIS","0 - CAPTAÇÃO")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		## 2 - CAPTAÇÃO/RELACIONAMENTO
		self.oHelper.SetButton("Outras Ações",sub_item='Copiar')
		self.oHelper.SetValue("B9L_DESVIS","PLS DSAUPC TIR CAP REL COPIA")
		self.oHelper.SetValue("B9L_TIPVIS","2 - CAPTAÇÃO/RELACIONAMENTO")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")

		#EXCLUSAO
		## 1 - RELACIONAMENTO
		self.oHelper.SearchBrowse(f'{"M SP    0001PLS DSAUPC TIR REL ALTERACAO"}', key=5, index=True)
		self.oHelper.SetButton("Outras Ações",sub_item='Excluir')
		self.oHelper.SetValue("B9L_DESVIS","PLS DSAUPC TIR REL ALTERACAO")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		## 3 - INSTITUCIONAL
		self.oHelper.SearchBrowse(f'{"M SP    0001PLS DSAUPC TIR INT COPIA"}', key=5, index=True)
		self.oHelper.SetButton("Outras Ações",sub_item='Excluir')
		self.oHelper.SetValue("B9L_DESVIS","PLS DSAUPC TIR INT COPIA")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		## 0 - CAPTAÇÃO
		self.oHelper.SearchBrowse(f'{"M SP    0001PLS DSAUPC TIR CAP COPIA"}', key=5, index=True)
		self.oHelper.SetButton("Outras Ações",sub_item='Excluir')
		self.oHelper.SetValue("B9L_DESVIS","PLS DSAUPC TIR CAP COPIA")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		## 2 - CAPTAÇÃO/RELACIONAMENTO
		self.oHelper.SearchBrowse(f'{"M SP    0001PLS DSAUPC TIR CAP REL COPIA"}', key=5, index=True)
		self.oHelper.SetButton("Outras Ações",sub_item='Excluir')
		self.oHelper.SetValue("B9L_DESVIS","PLS DSAUPC TIR CAP REL COPIA")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")

		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()