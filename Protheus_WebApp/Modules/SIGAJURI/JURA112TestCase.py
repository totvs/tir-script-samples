from tir import Webapp
import unittest
from datetime import datetime
today = datetime.today().strftime('%d/%m/%Y')


class JURA112(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAJURI', '19/11/2019', 'T1', 'D MG 01 ', '76')
        inst.oHelper.Program('JURA112')
        inst.oHelper.AddParameter('MV_JFTJURI', '', '2', '', '')
        inst.oHelper.AddParameter('MV_JINTVAL', '', '1', '', '')
        inst.oHelper.SetParameters()

    def test_JURA112_CT001(self):

        # Efetua a Contabilização de Provisão
        print('CT001 - Contabilização de Provisão')
        self.oHelper.SetValue('A1_COD', 'TIR112', name_attr=True)
        self.oHelper.SetValue('A1_LOJA', '02', name_attr=True)
        self.oHelper.SetValue('NSZ_CAREAJ', '00004', name_attr=True)
        self.oHelper.SetButton('Contabilizar')
        self.oHelper.SetButton('Perguntas')
        self.oHelper.SetButton('Informações')
        self.oHelper.SetButton('Executar')

        # Tela do contábil para informar histórico
        self.oHelper.LoadGrid()
        self.oHelper.CheckResult('Valor', '10.000,00', grid=True, line=1)
        self.oHelper.LoadGrid()
        self.oHelper.SetFocus('Hist Pad', grid_cell=True, row_number=1)
        self.oHelper.SetKey('F3', grid=True)
        self.oHelper.SetButton('OK')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Sim')
        self.oHelper.SetButton('Sim')
        self.oHelper.WaitHide('Aguarde processando...')
        self.oHelper.WaitShow('Contabilização realizada com sucesso')
        self.oHelper.SetButton('Fechar')

        # Efetua a geração do relatório de contabilização
        self.oHelper.SetValue('cValor', 'Sim', name_attr=True)
        self.oHelper.SetValue('NSZ_DTINCL', today, name_attr=True)
        self.oHelper.SetValue('NSZ_DTENTR', today, name_attr=True)
        self.oHelper.SetButton('Relatório')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('Sair')

        self.oHelper.AssertTrue()

        self.oHelper.RestoreParameters()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
