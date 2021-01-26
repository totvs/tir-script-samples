from tir import Webapp
import unittest
import time


class GTPA004(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAGTP', '15/04/2020', 'T1', 'D MG 01 ', '88')
        inst.oHelper.Program('GTPA004')

    def test_GTPA004_CT001(self):
        print("test_GTPA004_CT001 - Visualizar")
        self.oHelper.SearchBrowse('D MG    00000000009', key=1, index=True)
        self.oHelper.SetButton('Visualizar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.AssertTrue()

    def test_GTPA004_CT002(self):
        print("test_GTPA004_CT002 - Alterar")
        self.oHelper.SearchBrowse('D MG    00000000009', key=1, index=True)
        self.oHelper.SetButton('Outras Ações', 'Alterar')
        time.sleep(2)
        self.oHelper.SetButton('Sim')
        time.sleep(2)
        self.oHelper.SetValue('Lotação', '55')
        
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.AssertTrue()       

   
    def test_GTPA004_CT003(self):
        print("test_GTPA004_CT003 - Excluir")
        self.oHelper.SearchBrowse('D MG    00000000009', key=1, index=True)
        self.oHelper.SetButton('Outras Ações', 'Excluir')
        self.oHelper.SetButton('Confirmar')
        time.sleep(2)
        self.oHelper.SetButton('Sim')
        time.sleep(2)
        self.oHelper.SetButton('Fechar')
        self.oHelper.AssertTrue()

    def test_GTPA004_CT004(self):
        print("test_GTPA004_CT004 - Incluir")
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetBranch('D MG')

        self.oHelper.SetValue('Cód. Linha', '000001')
        self.oHelper.SetValue('Sentido', '1')
        self.oHelper.SetValue('Hora Inicio', '10:00')
        time.sleep(2)
        self.oHelper.SetValue('Vigência de', '01/05/2020')
        self.oHelper.SetValue('Vigência até', '30/05/2020')
        self.oHelper.SetValue('Lotação', '50')

        self.oHelper.ClickCheckBox('Segunda', 1)        
        self.oHelper.ClickCheckBox('Terça', 1)
        self.oHelper.ClickCheckBox('Quarta', 1)
        self.oHelper.ClickCheckBox('Quinta', 1)
        self.oHelper.ClickCheckBox('Sexta', 1)
        self.oHelper.ClickCheckBox('Sábado', 1)
        self.oHelper.ClickCheckBox('Domingo', 1)

      
        self.oHelper.SetButton('Outras Ações', 'Seleção de Localidade')        
        self.oHelper.SetButton('Confirmar')
        time.sleep(2)
        self.oHelper.SetButton('Fechar')
        self.oHelper.ClickGridCell("Hora destino", row=1, grid_number=1)
        self.oHelper.SetValue("Hora destino","12:00",grid=True, grid_number=1) 
        self.oHelper.ClickGridCell("Tempo Exec.", row=1, grid_number=1)
        self.oHelper.SetValue("Tempo Exec.","01:00",grid=True, grid_number=1) 
        self.oHelper.LoadGrid()       
        time.sleep(2)

        self.oHelper.SetButton('Confirmar')
        time.sleep(2)
        self.oHelper.AssertTrue()


    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
