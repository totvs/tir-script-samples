from tir import Webapp
import unittest
from datetime import datetime
DateSystem = datetime.today().strftime("%d/%m/%Y")

class MATA010(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAADV","25/11/2019","T1","D MG 01 ","04")
        inst.oHelper.SetLateralMenu('Atualizações > Cadastros > Produto > Produtos')

    def test_MATA010_001(self):
        self.oHelper.AddParameter("MV_CADPROD", "","|SA5|SBZ|SB5|DH5|SGI|","|SA5|SBZ|SB5|DH5|SGI|","|SA5|SBZ|SB5|DH5|SGI|")
        self.oHelper.AddParameter("MV_QALOGIX", "","0","0","0")
        self.oHelper.AddParameter("MV_RASTRO", "","S","S","S")
        self.oHelper.AddParameter("MV_LOCALIZ", "","S","S","S")
        self.oHelper.SetParameters()

        cod = 'ESTSE0001100221'
        desc = 'MATA010TIR'
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("D MG 01 ")
        self.oHelper.SetValue("B1_COD", cod)
        self.oHelper.SetValue("B1_DESC",desc)
        self.oHelper.SetValue("B1_TIPO",'PA')
        self.oHelper.SetValue("B1_UM",'UN')
        self.oHelper.SetValue("B1_LOCPAD",'01')
        self.oHelper.SetValue("B1_LOCALIZ",'S')
        self.oHelper.SetValue("B1_RASTRO",'L')
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Não")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SearchBrowse(f"D MG 01 {cod}", "Filial+codigo")
        self.oHelper.SetButton("Visualizar")
        self.oHelper.CheckResult("B1_COD", cod)
        self.oHelper.SetButton("Fechar")
        self.oHelper.SearchBrowse(f"D MG 01 {cod}", "Filial+codigo")
        self.oHelper.SetButton('Outras Ações','Excluir')
        self.oHelper.CheckResult("B1_COD", cod)
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")       
        self.oHelper.AssertTrue()
        
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()