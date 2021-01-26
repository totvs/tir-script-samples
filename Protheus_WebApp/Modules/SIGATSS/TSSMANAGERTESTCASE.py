import unittest
from tir import Webapp

class TSSMANAGER(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        # Endereco do webapp e o nome do Browser
        inst.oHelper = Webapp()

        # Utilizando usuário de teste
        inst.oHelper.SetTIRConfig("User", "teste")
        inst.oHelper.SetTIRConfig("Password", "1234")

        # Parametros de inicializacao
        inst.oHelper.SetupTSS("TSSMANAGER", "SPED")

    def test_TSSMANAGER01_CT001(self):
        self.oHelper.SetButton("Inicial")
        self.oHelper.SetButton("NF-e")
        self.oHelper.SetButton("NFS-e")
        self.oHelper.SetButton("EDI")

        self.oHelper.SetButton("Sair")
        self.oHelper.SetButton("Sim")

        self.oHelper.AssertTrue()

    def test_TSSMANAGER01_CT002(self):
        self.oHelper.SetupTSS("TSSMANAGER", "SPED")

        self.oHelper.SetButton("Configurações")
        self.oHelper.SetButton("Geral")
        self.oHelper.SetButton("Central Notificações")
        self.oHelper.SetButton("Config. Notificação")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton("Sim")

        self.oHelper.SetButton("Sair")
        self.oHelper.SetButton("Sim")

        self.oHelper.AssertTrue()

    def test_TSSMANAGER01_CT003(self):
        self.oHelper.SetupTSS("TSSMANAGER", "SPED")

        self.oHelper.SetButton("Ferramentas")
        self.oHelper.SetButton("Inutilizar")
        self.oHelper.SetButton("Status SEFAZ")
        self.oHelper.SetButton("Consulta Chave")

        self.oHelper.SetButton("Sair")
        self.oHelper.SetButton("Sim")

        self.oHelper.AssertTrue()

    def test_TSSMANAGER04_CT004(self):
        self.oHelper.SetupTSS("TSSMANAGER", "SPED")

        self.oHelper.SetButton("Monitor")
        self.oHelper.SetButton("NF-e")
        self.oHelper.SetButton("NFS-e")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton("EDI")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton("Eventos")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton("Manifesto")
        self.oHelper.SetButton("Cancelar")

        self.oHelper.SetButton("Sair")
        self.oHelper.SetButton("Sim")

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main() 