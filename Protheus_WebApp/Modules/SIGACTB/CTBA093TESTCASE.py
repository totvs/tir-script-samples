from tir import Webapp
import unittest


class CTBA093(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGACTB", "01/06/2015", "T1", "D MG 01 ", "01")
        inst.oHelper.Program("CTBA093")

    def test_CTBA093_001(self):
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("D MG 01")
        self.oHelper.SetValue("CWK_CODFOR", "000000000000001")
        self.oHelper.SetValue("CWK_DESC", "CONTROL INCLUSAO")
        self.oHelper.SetValue("CWK_GRUPO",  "000001")
        self.oHelper.SetValue("CWK_TIPO",   "1 - Conta")
        self.oHelper.SetValue("CWK_TIPDAT", "1 - Numérico")
        self.oHelper.SetValue("CWK_HELP",   "Teste para TIR, Não utilizar.")
        self.oHelper.SetValue("CWK_CUENTA", "00000000000000000100")
        self.oHelper.CheckResult("CWK_CODFOR",  "000000000000001")
        self.oHelper.CheckResult("CWK_DESC", "CONTROL INCLUSAO")
        self.oHelper.CheckResult("CWK_GRUPO",   "000001")
        self.oHelper.CheckResult("CWK_TIPO",    "1 - Conta")
        self.oHelper.CheckResult("CWK_TIPDAT",  "1 - Numérico")
        self.oHelper.CheckResult("CWK_HELP",    "Teste para TIR, Não utilizar.")
        self.oHelper.CheckResult("CWK_CUENTA",  "00000000000000000100")
        self.oHelper.ClickFolder("Formulação")
        self.oHelper.SetButton("Gerar fórmula")
        self.oHelper.CheckResult("CWK_ADVPL",   "00000000000000000100")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.AssertTrue()
    
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
