from tir import Webapp
import unittest

class GTPA600(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAGTP", "14/04/2020", "T1", "D MG 01 ")
		inst.oHelper.Program('GTPA600')

	def test_GTPA600_CT001(self):
		self.oHelper.SetButton("Incluir")
		self.oHelper.SetButton("OK")
		self.oHelper.SetValue('G6R_PRODUT','GTP003')
		self.oHelper.SetValue('G6R_PEDESC','10,00')
		self.oHelper.SetValue('G6R_VALACO','900,00')
		self.oHelper.SetValue('G6R_SA3COD','GTP002')
		self.oHelper.SetValue('G6R_PROCES','GTP001')
		self.oHelper.SetValue('G6R_ESTAGI','000001')
		self.oHelper.SetValue('G6R_TABELA','GTP')
		self.oHelper.SetValue('G6R_CONDPG','000')
		self.oHelper.SetValue('G6R_TES'   ,'511')
		self.oHelper.SetValue('G6R_SA1COD','GTP001')
		self.oHelper.SetValue('G6R_SA1LOJ','01')
		self.oHelper.SetValue('G6R_SUSCOD','GTP001')
		self.oHelper.SetValue('G6R_SUSLOJ','01')
		self.oHelper.SetValue('G6R_DDD'   ,'111')
		self.oHelper.SetValue('G6R_TEL'   ,'111111111111111')
		self.oHelper.SetValue('G6R_CODBEM','GTP00101')
		self.oHelper.SetValue('G6R_QUANT' ,'1')
		self.oHelper.SetValue('G6R_KMCONT','200')
		self.oHelper.SetValue('G6R_KMEXCE','1.000,00')
		self.oHelper.SetValue('G6R_POLTR' ,'45')
		self.oHelper.SetValue('G6R_PDTOT' ,'20,00')
		self.oHelper.SetValue('G6R_TOTHR' ,'22:00')
		self.oHelper.SetValue('G6R_DISPVE','1')
		self.oHelper.SetValue('G6R_DTIDA' ,'15/04/2020')
		self.oHelper.SetValue('G6R_HRIDA' ,'10:00')
		self.oHelper.SetValue('G6R_LOCORI','LOC001')
		self.oHelper.SetValue('G6R_ENDEMB','')
		self.oHelper.SetValue('G6R_DTVLTA','15/04/2020')
		self.oHelper.SetValue('G6R_HRVLTA','22:00')
		self.oHelper.SetValue('G6R_LOCDES','LOC002')
		self.oHelper.SetValue('G6R_TIPITI','2')
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.LoadGrid()
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()	

if __name__ == '__main__':
	unittest.main()
