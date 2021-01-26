import unittest
from tir import Webapp


class TSSLOGMONITOR(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        # Endereco do webapp e o nome do Browser
        inst.oHelper = Webapp()

        # Utilizando usuário de teste
        inst.oHelper.SetTIRConfig("User", "teste")
        inst.oHelper.SetTIRConfig("Password", "1234")

        # Parametros de inicializacao
        inst.oHelper.SetupTSS("TSSINTERFACE", "SPED")

    def test_TSSLOGMONITOR01_CT001(self):
        self.oHelper.SetButton("Monitoramento")

        self.oHelper.SetButton("Configuração")
        self.oHelper.SetButton("Ambiente")
        self.oHelper.SetButton("Tabelas")
        self.oHelper.SetButton("URL")

        self.oHelper.SetButton("Analisador")

        self.oHelper.SetButton("Central Notificações")
        self.oHelper.SetButton("Config. Notificação")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton("Sim")

        self.oHelper.SetButton("Config. E-mail")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton("Sim")

        self.oHelper.SetButton("Rastro Processos")
        self.oHelper.SetButton("Confirmar")

        self.oHelper.SetButton("Sair")
        self.oHelper.SetButton("Sim")

        self.oHelper.AssertTrue()

    def test_TSSLOGMONITOR01_CT002(self):
        self.oHelper.SetupTSS("TSSINTERFACE", "SPED")

        self.oHelper.SetButton("Configuração")

        self.oHelper.SetButton("Entidades")
        self.oHelper.SetButton("Configurar")
        self.oHelper.ClickFolder("Totvs Colaboração")
        self.oHelper.ClickTree("Fiscal > NF-e")
        self.oHelper.ClickFolder("Eventos")
        self.oHelper.ClickFolder("Totvs Colaboração")
        self.oHelper.ClickTree("Fiscal > NFS-e")
        self.oHelper.ClickTree("Fiscal > NFC-e")
        self.oHelper.ClickFolder("Eventos")
        self.oHelper.ClickTree("Fiscal > CT-e")
        self.oHelper.ClickFolder("Totvs Colaboração")
        self.oHelper.ClickTree("Fiscal > CTe-OS")
        self.oHelper.ClickTree("Fiscal > MDF-e")
        self.oHelper.ClickFolder("Eventos")
        self.oHelper.ClickTree("TSS Manager")
        self.oHelper.ClickTree("Totvs Colaboração")
        self.oHelper.ClickTree("Localizados > Argentina")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton("Sim")

        self.oHelper.SetButton("Sair")
        self.oHelper.SetButton("Sim")

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()