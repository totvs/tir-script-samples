from tir import Webapp
import unittest
import datetime

class TMSA060(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
       inst.oHelper = Webapp()
       dataAtual = str(datetime.datetime.now().strftime("%d/%m,%Y"))
       inst.oHelper.Setup('SIGATMS',dataAtual,'T1','M SP 04 ','43')
       inst.oHelper.Program('TMSA060') 

    def test_TMSA060_CT001(self):

        self.oHelper.SetButton('Incluir')
        self.oHelper.SetBranch('M SP 04')
        self.oHelper.SetValue('DT7_CODDES', '100103')    
        self.oHelper.SetValue('DT7_DESCRI', 'despesa mov banco')
        self.oHelper.SetValue("DT7_CONEST","2")
        self.oHelper.SetValue("DT7_MOVBCO","2")   
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.AssertTrue()

    def test_TMSA060_CT002(self):

        self.oHelper.SearchBrowse(f'M SP    100103')
        self.oHelper.SetButton('Visualizar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.AssertTrue()     

    def test_TMSA060_CT003(self): 

        self.oHelper.SearchBrowse(f'M SP    100103')
        self.oHelper.SetButton('Alterar')
        self.oHelper.SetValue("DT7_MOVBCO","1")  
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.AssertTrue()     

    def test_TMSA060_CT004(self): 

        self.oHelper.SearchBrowse(f'M SP    100103')
        self.oHelper.SetButton('Outras Ações','Excluir')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()
