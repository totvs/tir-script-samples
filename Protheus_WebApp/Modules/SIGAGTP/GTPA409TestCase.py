from tir import Webapp
import unittest


class GTPA409(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAGTP', '29/04/2020', 'T1', 'D MG 01 ')
        inst.oHelper.Program('GTPA409')

    def test_GTPA409_CT001(self):

     # Efetua a alocação de veículo (caso padrão)
        print('CT001 - Alocação de veículo (caso padrão)')
        self.oHelper.SetValue('Data Viagem De: ?', '04/05/2020')
        self.oHelper.SetValue('Data Viagem Até: ?', '04/05/2020')
        self.oHelper.SetValue('Escala: ?', '000004')
        self.oHelper.SetButton('OK')
        self.oHelper.ClickGridCell('Seq. Alocação', row=1, grid_number=1)
        self.oHelper.SetValue('Seq. Alocação', '01',
                              grid=True, grid_number=1, name_attr=True)
        self.oHelper.LoadGrid()
        self.oHelper.ClickGridCell('', row=1, grid_number=2)
        self.oHelper.SetValue('', True, grid=True, grid_number=2)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.AssertTrue()

    def test_GTPA409_CT004(self):

     # Efetua a alocação de veículo proveniente de uma escala com vários veículos
        print('CT004 - Alocação de veículo proveniente de uma escala com vários veículos')
        self.oHelper.Program('GTPA409')
        self.oHelper.SetValue('MV_PAR01', '03/04/2020')
        self.oHelper.SetValue('MV_PAR02', '09/04/2020')
        self.oHelper.SetValue('MV_PAR03', '000003')
        self.oHelper.SetButton('OK')
        self.oHelper.ScrollGrid(column='Cód. Veículo',
                                match_value='VEICULOGTP_001')
        self.oHelper.SetValue('Seq. Alocação', '01',
                              grid=True, grid_number=1, name_attr=True)
        self.oHelper.LoadGrid()
        self.oHelper.ScrollGrid(column='Seq. Alocação',
                                match_value='0001', grid_number=2)
        self.oHelper.SetValue('', True, grid=True, grid_number=2)
        self.oHelper.LoadGrid()
        self.oHelper.ClickGridCell('Código', row=1, grid_number=2)
        self.oHelper.CheckResult(
            'Código', '000061', grid=True, line=1, grid_number=2, name_attr=True)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
