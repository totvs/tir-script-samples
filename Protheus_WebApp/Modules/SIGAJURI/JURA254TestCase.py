from tir import Webapp
import unittest
import time
from datetime import datetime
today = datetime.today().strftime('%d/%m/%Y')


class JURA254(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAJURI', '24/09/202020', 'T1', 'D MG 01 ', '76')
        inst.oHelper.Program('JURA254')

    def test_JURA254_CT001(self):

        print('CT001 - Inclusão de Solicitação de Documentos')
        self.oHelper.ClickLabel('Incluir')
        self.oHelper.SetValue('O0M_CAJURI', '0000000160', name_attr=True)
        self.oHelper.SetValue('O0M_PRZSOL', today, name_attr=True)
        self.oHelper.SetValue('O0M_CENVOL', '0000000199', name_attr=True)
        self.oHelper.ClickGridCell("Cód Tip Doc", row=1)
        self.oHelper.SetValue("O0N_CTPDOC", "002", grid=True)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')

        self.oHelper.SetValue('O0M_CAJURI', '0000000160', name_attr=True)
        self.oHelper.ClickLabel("Pesquisar")
        self.oHelper.ClickGridCell("Código Assunto Juridico", row=1)
        self.oHelper.ClickLabel("Alterar")
        self.oHelper.SetButton("Outras Ações", "Anexos")
        self.oHelper.SetButton('Importar')
        self.oHelper.SetFilePath(
            r"SERVIDOR\baseline\Jur_Anexos_Importação.txt", 'Salvar')
        self.oHelper.WaitShow("Deseja importar o(s) seguinte(s) arquivo(s):")
        self.oHelper.SetButton("Sim")
        time.sleep(3)
        self.oHelper.SetButton("Fechar")
        self.oHelper.WaitShow("E-mail não enviado:")
        self.oHelper.SetButton("Fechar")
        self.oHelper.ClickGridCell("Status", row=1)
        self.oHelper.CheckResult("Status", "Entregue", grid=True, line=1)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Outras Ações", "Enviar e-mail")
        self.oHelper.WaitShow("E-mail não enviado:")
        self.oHelper.SetButton("Fechar")

        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
