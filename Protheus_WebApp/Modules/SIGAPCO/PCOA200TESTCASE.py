from tir import Webapp
import unittest

class PCOA200(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAPCO", "05/09/2019", "T1", "M SP 01 ", "57")
        inst.oHelper.Program("PCOA200")
        inst.oHelper.AddParameter("MV_PCOTHRD", "", "2")
        inst.oHelper.AddParameter("MV_PCOMTHR", "", "1")
        inst.oHelper.SetParameters()
            
    def test_PCOA200_001(self):
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("D MG 01 ")
        self.oHelper.SetValue("Planilha Orc", "PCOAUT_A22")
        self.oHelper.SetValue("Versao Sim.", "0002")
        self.oHelper.SetValue("Descricao", "AUTOMACAO PCOA122 - MULTITHR")
        self.oHelper.SetButton("Salvar")
        self.oHelper.WaitProcessing("Processando...")
        self.oHelper.WaitProcessing("Processando...")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SearchBrowse("D MG 01 PCOAUT_A22")
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
