from tir import Webapp
import unittest

class TMSA120(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGATMS','10/11/2020','T1','M SP 03 ','43')
        inst.oHelper.Program('TMSA120')  		

    def test_TMSA120_CT001(self):		

        self.oHelper.WaitProcessing('Construindo Estrutura...')

        self.oHelper.ClickTree('Estrutura de Regiões')
        self.oHelper.ClickTree('BRASIL-Brasil')
        self.oHelper.ClickTree('AC    -Acre')

        self.oHelper.ClickTree('100013-Acrelandia')
        self.oHelper.SetButton('Opções')
        self.oHelper.ClickMenuPopUpItem('Excluir')
        self.oHelper.SetButton('Sim')

        self.oHelper.SetButton('Opções')
        self.oHelper.ClickMenuPopUpItem('Incluir Região')
        self.oHelper.SetButton('Ok')

        self.oHelper.SetButton('Opções')
        self.oHelper.ClickMenuPopUpItem('Legenda')
        self.oHelper.SetButton('Fechar')

        self.oHelper.SetButton('Opções')
        self.oHelper.ClickMenuPopUpItem('Visualizar')
        self.oHelper.SetButton('Cancelar')

        self.oHelper.SetButton('Ok')

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()

