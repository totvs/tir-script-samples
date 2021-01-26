import unittest
from tir import Webapp


class TSSMANAGERMONITOR(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        # Endereco do webapp e o nome do Browser
        inst.oHelper = Webapp()

        # Utilizando usuário de teste
        inst.oHelper.SetTIRConfig("User", "teste")
        inst.oHelper.SetTIRConfig("Password", "1234")

        # Parametros de inicializacao
        inst.oHelper.SetupTSS("TSSMONITOR", "SPED")

    def test_TSSMANAGERMONITOR01_CT001(self):
        self.oHelper.SetButton("Eventos")
        self.oHelper.SetButton("NF-e")
        self.oHelper.SetButton("Cancelar")

        self.oHelper.SetButton("Fiscal")
        self.oHelper.SetButton("NFS-e")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton("NF-e")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton("CT-e")
        self.oHelper.SetButton("Cancelar")

        self.oHelper.SetButton("Documentos")
        self.oHelper.SetButton("EDI")

        self.oHelper.SetButton("Sair")
        self.oHelper.SetButton("Sim")

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()