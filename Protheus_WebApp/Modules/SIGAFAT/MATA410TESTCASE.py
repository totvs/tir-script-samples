from tir import Webapp
from datetime import datetime
DataSystem = datetime.today().strftime('%d/%m/%Y')
import unittest

class MATA410(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAFAT",DataSystem,"T1","D MG 01 ","05")
        inst.oHelper.Program("MATA410")

    def test_MATA410_199(self):
        order = 'FATT37'

        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("D MG 01 ")
        self.oHelper.SetValue("C5_NUM", order)
        self.oHelper.SetValue("C5_TIPO","B")
        self.oHelper.SetValue("C5_TIPO","N")
        self.oHelper.SetValue("C5_CLIENTE","FAT001")
        self.oHelper.SetValue("C5_LOJACLI","01")
        self.oHelper.SetValue("C5_LOJAENT","00")
        self.oHelper.SetValue("C5_CONDPAG","003")
        self.oHelper.SetValue("Produto", "FAT000000000000000000000000001", grid=True)
        self.oHelper.SetValue("Quantidade", "1,00", grid=True)
        self.oHelper.SetValue("C6_OPER", "01", grid=True)
        self.oHelper.SetValue("C6_DESCONT", "5,00", grid=True)
        self.oHelper.SetValue("C6_TES", "503", grid=True)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SearchBrowse(f"D MG 01 {order}", "Filial+numero")
        self.oHelper.SetButton("Visualizar")
        self.oHelper.CheckResult("C5_NUM", order)
        self.oHelper.CheckResult("C5_TIPO","N")
        self.oHelper.CheckResult("C5_CLIENTE","FAT001")
        self.oHelper.CheckResult("C5_CONDPAG","003")
        self.oHelper.CheckResult("Produto", " FAT000000000000000000000000001", grid=True, line=1)
        self.oHelper.CheckResult("C6_DESCONT", " 5,00", grid=True, line=1)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Cancelar")
        self.oHelper.AssertTrue()
    
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()