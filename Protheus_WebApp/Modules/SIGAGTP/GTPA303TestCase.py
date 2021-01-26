from tir import Webapp
import unittest
import time
from datetime import datetime
DataSystem = datetime.today().strftime('%d/%m/%Y')


class GTPA303(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAGTP', "01/03/2020", 'T1', 'D MG 01 ', '88')
        inst.oHelper.Program('GTPA303')

    def test_GTPA303_CT001(self):
        print('test_GTPA303_CT001 - VISUALIZAR')
        self.oHelper.SearchBrowse('D MG    0000000001', key=1, index=True)
        self.oHelper.SetButton('VISUALIZAR')
        self.oHelper.SetButton('Outras Ações', 'Detalhes Escala')
        self.oHelper.SetButton('Cancelar')
        self.oHelper.SetButton('Outras Ações', 'Legenda')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.AssertTrue()

    def test_GTPA303_CT002(self):
        print('test_GTPA303_CT002 - Manutenção da Alocação')
        self.oHelper.SearchBrowse('D MG    0000000001', key=1, index=True)
        self.oHelper.SetButton('Manutenção da Alocação')
        self.oHelper.SetValue('Esquema', '')

        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.AssertTrue()

    def test_GTPA303_CT003(self):
        print('test_GTPA303_CT003 - Excluir')
        self.oHelper.SearchBrowse('D MG    0000000001', key=1, index=True)
        self.oHelper.SetButton('Outras Ações', 'Exclusão de Alocação')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.AssertTrue()

    def test_GTPA303_CT004(self):
        print('test_GTPA303_CT004 - Incluir')
        self.oHelper.SetButton('Alocação')
        self.oHelper.SetBranch('D MG')

        self.oHelper.SetValue('Cód Setor', '000001')
        self.oHelper.SetValue('Cód Grupo', '0001')
        self.oHelper.SetValue('Cód.Colab.', '000001')
        self.oHelper.SetValue('Data Inicio', '15/04/2020')
        self.oHelper.SetValue('Data Fim', '17/04/2020')
        self.oHelper.SetValue('Esquema', '000001')
        self.oHelper.SetValue('Seq. Esquema', '001')
        self.oHelper.SetValue('Seq. Esquema', '')
        self.oHelper.SetValue('Esquema', '')
        self.oHelper.SetButton('Outras Ações', 'Detalhes Escala')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Outras Ações', 'Escalar')
        self.oHelper.SetButton('Salvar')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.AssertTrue()

    def test_GTPA303_CT005(self):
        print('test_GTPA303_CT005 - Incluir')
        self.oHelper.SetButton('Alocação')
        self.oHelper.SetBranch('D MG')

        self.oHelper.SetValue('Cód Setor', '000001')
        self.oHelper.SetValue('Cód Grupo', '0001')
        self.oHelper.SetValue('Cód.Colab.', '000001')
        self.oHelper.SetValue('Data Inicio', '03/07/2020')
        self.oHelper.SetValue('Data Fim', '06/07/2020')

        self.oHelper.ClickGridCell('Tipo Dia', row=1, grid_number=1)
        self.oHelper.SetValue('Tipo Dia', '2', grid=True, grid_number=1)
        self.oHelper.LoadGrid()

        self.oHelper.ClickGridCell('Tipo Dia', row=2, grid_number=1)
        self.oHelper.SetValue('Tipo Dia', '3', grid=True, grid_number=1)
        self.oHelper.LoadGrid()

        self.oHelper.ClickGridCell('Tipo Dia', row=3, grid_number=1)
        self.oHelper.SetValue('Tipo Dia', '4', grid=True, grid_number=1)
        self.oHelper.LoadGrid()

        self.oHelper.ClickGridCell('Tipo Dia', row=4, grid_number=1)
        self.oHelper.SetButton('Outras Ações', 'Escalar')
        self.oHelper.SetButton('Salvar')

        self.oHelper.SetButton('Outras Ações', 'Atualiza Total')

        self.oHelper.SetButton('Outras Ações', 'Detalhes Escala')
        self.oHelper.SetButton('Confirmar')

        self.oHelper.SetButton('Confirmar')

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
