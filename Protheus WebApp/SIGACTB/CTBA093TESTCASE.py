from tir import Webapp
import unittest


class CTBA093(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()

        inst.oHelper.Setup("SIGACTB", "01/06/2015", "T1", "D MG 01 ", "01")

        inst.oHelper.Program("CTBA093")

    def test_CTBA093_001(self):
        # Inclusao Formula Conta
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
        self.oHelper.CheckResult(
            "CWK_HELP",    "Teste para TIR, Não utilizar.")
        self.oHelper.CheckResult("CWK_CUENTA",  "00000000000000000100")

        self.oHelper.ClickFolder("Formulação")
        self.oHelper.SetButton("Gerar fórmula")

        self.oHelper.CheckResult("CWK_ADVPL",   "00000000000000000100")

        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.AssertTrue()

    def test_CTBA093_002(self):
        # Copiar

        COD = "000000000000002"
        self.oHelper.SearchBrowse(
            f"D MG 01 {COD}",   "Filial+cód. Fórmula")

        self.oHelper.SetButton("Outras Ações",  "Copiar")
        self.oHelper.SetValue("CWK_CODFOR", "000000000000008")
        self.oHelper.SetValue("CWK_DESC", "CONTROL COPIADO")

        self.oHelper.CheckResult("CWK_CODFOR",  "000000000000008")
        self.oHelper.CheckResult("CWK_DESC", "CONTROL COPIADO")

        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.AssertTrue()

    def test_CTBA093_003(self):
        # Consulta

        COD = "000000000000007"
        self.oHelper.SearchBrowse(
            f"D MG 01 {COD}", "Filial+cód. Fórmula")

        self.oHelper.SetButton("Outras Ações",  "Consulta")

        self.oHelper.SetButton("Confirmar")
        self.oHelper.AssertTrue()

    def test_CTBA093_004(self):
        # Inclusao de Valor Fixo com geração de formula
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("D MG 01")

        self.oHelper.SetValue("CWK_CODFOR", "000000000000003")
        self.oHelper.SetValue("CWK_DESC",   "Valor Fixo Control")
        self.oHelper.SetValue("CWK_GRUPO",  "000001")
        self.oHelper.SetValue("CWK_TIPO",   "5 - Valor Fixo")
        self.oHelper.SetValue("CWK_TIPDAT", "2 - Caracter")
        self.oHelper.SetValue("CWK_VALOR",  "1.000")
        self.oHelper.SetValue("CWK_CONASI", "CT2->CT2_VALOR!=0")
        self.oHelper.SetValue("CWK_HELP",   "Teste para TIR, Não utilizar.")

        self.oHelper.CheckResult("CWK_CODFOR",  "000000000000003")
        self.oHelper.CheckResult("CWK_DESC",    "Valor Fixo Control")
        self.oHelper.CheckResult("CWK_GRUPO",   "000001")
        self.oHelper.CheckResult("CWK_TIPO",    "5 - Valor Fixo")
        self.oHelper.CheckResult("CWK_TIPDAT",  "2 - Caracter")
        self.oHelper.CheckResult("CWK_VALOR",   "1.000")
        self.oHelper.CheckResult("CWK_CONASI",  "CT2->CT2_VALOR!=0")
        self.oHelper.CheckResult(
            "CWK_HELP",    "Teste para TIR, Não utilizar.")

        self.oHelper.ClickFolder("Formulação")

        self.oHelper.SetButton("Gerar fórmula")
        self.oHelper.CheckResult(
            "CWK_ADVPL", "IF(CT2->CT2_VALOR!=0,1.000,")

        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.AssertTrue()

    def test_CTBA093_005(self):
        # Excluir

        COD = "000000000000004"
        self.oHelper.SearchBrowse(
            f"D MG 01 {COD}", "Filial+cód. Fórmula")
        self.oHelper.SetButton("Outras Ações",  "Excluir")

        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Sim")
        self.oHelper.SetButton("Fechar")
        self.oHelper.AssertTrue()

    def test_CTBA093_006(self):
        # Modificar, Colocando operadores e MNEMONICOS Na conta
        COD = "000000000000005"
        self.oHelper.SearchBrowse(
            f"D MG 01 {COD}", "Filial+cód. Fórmula")

        self.oHelper.SetButton("Modificar")

        self.oHelper.SetValue("CWK_CUENTA", "M_A1_CONTA")
        self.oHelper.CheckResult("CWK_CUENTA",  "M_A1_CONTA")

        self.oHelper.ClickFolder("Formulação")

        self.oHelper.SetValue("CWL_OPER",   "01 - SOMA",    grid=True)
        self.oHelper.SetValue("CWL_OPER1",  "M_B1_PRV1",    grid=True)
        self.oHelper.SetValue("CWL_OPER2",  "M_A3_COMIS",    grid=True)
        self.oHelper.LoadGrid()

        self.oHelper.CheckResult("CWL_OPER",    "SOMA", grid=True)
        self.oHelper.CheckResult("CWL_OPER1",   "M_B1_PRV1",  grid=True)
        self.oHelper.CheckResult("CWL_OPER2",   "M_A3_COMIS",   grid=True)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Gerar fórmula")
        self.oHelper.CheckResult("CWK_ADVPL",   "SA1->A1_CONTA")

        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()

    def test_CTBA093_007(self):
        # Visualizar

        COD = "000000000000007"
        self.oHelper.SearchBrowse(
            f"D MG 01 {COD}", "Filial+cód. Fórmula")
        self.oHelper.SetButton("Visualizar")
        self.oHelper.CheckResult("CWK_CODFOR",  "000000000000007")

        self.oHelper.SetButton("Fechar")
        self.oHelper.AssertTrue()

    def test_CTBA093_008(self):
         # -------------------------------------------------------------------------
        # ALTERAÇÃO 2 VALOR FIXO
        # -------------------------------------------------------------------------
        CODA = "000000000000006"
        self.oHelper.SearchBrowse(
            f"D MG 01 {CODA}", "Filial+cód. Fórmula")

        self.oHelper.SetButton("Modificar")

        self.oHelper.SetValue("CWK_VALOR",  "M_A3_COMIS")
        self.oHelper.CheckResult("CWK_VALOR",   "M_A3_COMIS")

        self.oHelper.ClickFolder("Formulação")

        self.oHelper.SetValue("CWL_OPER",   "01 - SOMA",    grid=True)
        self.oHelper.SetValue("CWL_OPER1",  "M_B1_PRV1",    grid=True)
        self.oHelper.SetValue("CWL_OPER2",  "M_A3_COMIS",   grid=True)
        self.oHelper.LoadGrid()

        self.oHelper.CheckResult("CWL_OPER",    "SOMA", grid=True)
        self.oHelper.CheckResult("CWL_OPER1",   "M_B1_PRV1",    grid=True)
        self.oHelper.CheckResult("CWL_OPER2",   "M_A3_COMIS",   grid=True)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Gerar fórmula")

        self.oHelper.CheckResult(
            "CWK_ADVPL", "SA3->A3_COMIS")

        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
