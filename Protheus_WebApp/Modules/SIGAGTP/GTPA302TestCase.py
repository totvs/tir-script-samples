from tir import Webapp
import unittest

class GTPA302(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAGTP', '26/03/2020', 'T1', 'D MG 01 ', '05')
        inst.oHelper.Program('GTPA302')

    def test_GTPA302_CT001(self):
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetBranch('D MG')
        self.oHelper.SetValue('Vigência de', '19/03/2020')
        self.oHelper.SetValue('Vigência ate', '31/03/2020')
        self.oHelper.SetValue('Filtra por', '1')
        self.oHelper.SetValue('GY4_SETOR', '000001')
        self.oHelper.SetValue('Descrição', 'CT001 - ESCALA COLABORADOR')
        self.oHelper.SetValue('Tipo Recurso', '01')
        self.oHelper.ClickCheckBox('Seg-Feira', 1)
        self.oHelper.ClickCheckBox('Terça-Feira', 1)
        self.oHelper.ClickCheckBox('Quarta-Feira', 1)
        self.oHelper.ClickCheckBox('Quinta-Feira', 1)
        self.oHelper.ClickCheckBox('Sexta-Feira', 1)
        self.oHelper.ClickCheckBox('Sábado', 1)
        self.oHelper.ClickCheckBox('Domingo', 1)
        self.oHelper.SetValue('GYO_SETOR', '000001')
        self.oHelper.SetKey('F5')
        self.oHelper.ScrollGrid(column='Código', match_value='00000000004')
        self.oHelper.SetButton('Outras Ações', 'Copia o horário selecionado')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.AssertTrue()

    def test_GTPA302_CT002(self):

        self.oHelper.SearchBrowse('D MG    000007', key='Filial+cód.escala')
        self.oHelper.SetButton('Alterar')
        self.oHelper.ClickCheckBox('Sábado', 1)
        self.oHelper.ClickCheckBox('Domingo', 1)
        self.oHelper.ScrollGrid(column='Linha', match_value='000004', grid_number=2)
        self.oHelper.SetButton('Outras Ações', 'Voltar o horário selecionado')
        self.oHelper.ScrollGrid(column='Código', match_value='00000000007', grid_number=1)
        self.oHelper.SetKey('F5')
        self.oHelper.SetButton('Sim')
        self.oHelper.ScrollGrid(column='Código', match_value='00000000007')
        self.oHelper.SetButton('Outras Ações', 'Copia o horário selecionado')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
