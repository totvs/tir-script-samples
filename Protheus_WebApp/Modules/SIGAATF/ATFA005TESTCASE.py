from tir import Webapp
import unittest


class ATFA005(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()

        inst.oHelper.Setup("SIGAATF", "01/04/2016", "T1", "D MG 01 ", "01")
        inst.oHelper.Program("ATFA005")

    def test_ATFA005_001(self):
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetValue("FNI_CODIND", "02"	)  # Cod.Índice
        self.oHelper.SetValue("FNI_DSCIND", "ATFA005 CAMPO DESCRI"	)  # Descrição
        self.oHelper.SetValue("FNI_PERIOD", "2 - Mensal"	)  # Peridoo
        self.oHelper.SetValue("FNI_MSBLQL", "2 - Não"	)  # Bloqueio sim ou nao

        self.oHelper.CheckResult("FNI_CODIND", "02"	)  # Cod.Índice
        self.oHelper.CheckResult("FNI_DSCIND", "ATFA005 CAMPO DESCRI")  # Descrição
        self.oHelper.CheckResult("FNI_PERIOD", "2 - Mensal"	)  # Peridoo
        self.oHelper.CheckResult("FNI_MSBLQL", "2 - Não"	)  # Bloqueio sim ou nao
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")

        # ---------------------------------------------------------------------------
        # Inclusão 2
        # ---------------------------------------------------------------------------
        self.oHelper.SetButton("Incluir")

        self.oHelper.SetValue("FNI_CODIND", "05"	)  # Cod.Índice
        self.oHelper.SetValue("FNI_DSCIND", "ATFA005 CALCULADO"	)  # Descrição
        self.oHelper.SetValue("FNI_PERIOD", "2 - Mensal"	)  # Peridoo
        self.oHelper.SetValue("FNI_MSBLQL", "2 - Não"	)  # Bloqueio sim ou nao
        self.oHelper.SetValue("FNI_TIPO"  , "2 - Calculado"	)
        self.oHelper.SetValue("FNI_CURVIN", "01/04/2016"	)
        self.oHelper.SetValue("FNI_CURVFI", "30/04/2016"	)

        self.oHelper.CheckResult("FNI_CODIND", "05"	)  # Cod.Índice
        self.oHelper.CheckResult("FNI_DSCIND", "ATFA005 CALCULADO")  # Descrição
        self.oHelper.CheckResult("FNI_PERIOD", "2 - Mensal"	)  # Peridoo
        self.oHelper.CheckResult("FNI_MSBLQL", "2 - Não"	)
        self.oHelper.CheckResult("FNI_TIPO"  , "2 - Calculado"	)  # Bloqueio sim ou nao
        self.oHelper.CheckResult("FNI_CURVIN", "01/04/2016"	)
        self.oHelper.CheckResult("FNI_CURVFI", "30/04/2016"	)

        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()

    def test_ATFA005_002(self):
        # alterar
        COD = "030001"
        self.oHelper.SearchBrowse(
            f"{COD}")

        self.oHelper.SetButton("Alterar")
        self.oHelper.SetValue("FNI_DSCIND", "ATFA005 ALTERADE"	)
        self.oHelper.CheckResult("FNI_DSCIND", "ATFA005 ALTERADE"	)
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()

    def test_ATFA005_003(self):
        # Visualizar
        self.oHelper.SetButton("Visualizar")
        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()

    def test_ATFA005_004(self):
        # Bloquear/Desbloq#

        # Bloqueando
        COD = "020001"

        self.oHelper.SearchBrowse(
            f"{COD}")
        self.oHelper.SetButton("Outras Ações", "Bloquear/Desbloq")
        self.oHelper.SetButton("Sim")

        # Desbloqueando
        self.oHelper.SearchBrowse(
            f"{COD}")
        self.oHelper.SetButton("Outras Ações", "Bloquear/Desbloq")
        self.oHelper.SetButton("Sim")

        self.oHelper.AssertTrue()

    def test_ATFA005_005(self):
        # Excluir

        COD = "030001"
        self.oHelper.SearchBrowse(
            f"{COD}")
        self.oHelper.SetButton("Outras Ações", "Excluir")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()

    def test_ATFA005_006(self):
        # Revisao
        COD = "040001"
        REV = "040002"

        #self.oHelper.SearchBrowse("030001", "Cód.índice + Revisão")
        self.oHelper.SearchBrowse(
            f"{COD}")

        self.oHelper.SetButton("Outras Ações", "Revisão")
        self.oHelper.SetValue("FNI_DTREV", "01/04/2016")
        self.oHelper.CheckResult("FNI_DTREV", "01/04/2016")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")

        self.oHelper.SearchBrowse(
            f"{REV}")

        self.oHelper.SetButton("Visualizar")
        self.oHelper.CheckResult("FNI_REVIS", "0002")
        self.oHelper.SetButton("Fechar")
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
