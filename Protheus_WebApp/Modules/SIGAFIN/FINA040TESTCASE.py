from tir import Webapp
import unittest
from datetime import datetime
DateSystem = datetime.today().strftime('%d/%m/%Y')

indice1 = "Filial+prefixo + No. Titulo + Parce..."

class FINA040(unittest.TestCase):

	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("SIGAFIN",DateSystem,"T1","D MG 01 ","06")
		inst.oHelper.Program('FINA040')

	def test_FINA040_CT001(self):
		self.oHelper.WaitShow("Contas a Receber")
		self.oHelper.SetKey("F12")
		self.oHelper.SetValue("Mostra Lanc Contab ?"  ,"Nao")
		self.oHelper.SetValue("Contabiliza on line ?" ,"Nao")
		self.oHelper.SetValue("Contab.Tit.Provisor ?" ,"Nao")
		self.oHelper.SetValue("Rateia Valor ?" ,"Bruto")
		self.oHelper.SetButton("Ok")
		self.oHelper.SetButton('Incluir')
		self.oHelper.SetBranch('D MG 01')
		self.oHelper.SetValue('E1_PREFIXO', "FIN")
		self.oHelper.SetValue('E1_NUM','FINA40133')
		self.oHelper.SetValue('E1_TIPO','NF')
		self.oHelper.SetValue('E1_NATUREZ','FINA040133')
		self.oHelper.SetValue('E1_CLIENTE','FIN184')
		self.oHelper.SetValue('E1_LOJA','01')
		self.oHelper.SetValue('E1_EMISSAO','10/10/2018')
		self.oHelper.SetValue('E1_VENCTO','10/10/2018')
		self.oHelper.SetValue('E1_VENCREA','10/10/2018')
		self.oHelper.SetValue('E1_VALOR','10.000,00')
		self.oHelper.ClickFolder('Impostos')
		self.oHelper.SetButton('Salvar')
		self.oHelper.SetButton('Cancelar')
		self.oHelper.AssertTrue()

	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()