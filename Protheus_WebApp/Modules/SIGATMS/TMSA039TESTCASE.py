from tir import Webapp
import unittest
import datetime

class TMSA039(unittest.TestCase):
 
    @classmethod
    def setUpClass (inst):
        inst.oHelper = Webapp()
        dataAtual = str(datetime.datetime.now().strftime("%d/%m,%Y"))
        inst.oHelper.Setup('SIGATMS',dataAtual,'T1','M SP 04 ','43')
        inst.oHelper.Program('TMSA039')

    def test_TMSA039_CT001(self):

        self.oHelper.SetButton('Incluir')
        self.oHelper.SetBranch('M SP 04')
        self.oHelper.SetValue('DLO_CODIGO', '03')
        self.oHelper.SetValue('DLO_DESCRI', 'PERIGOSA')
        self.oHelper.SetValue("DLO_CODTPC","03")
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.AssertTrue()

    def test_TMSA039_CT002(self):

        self.oHelper.SearchBrowse(f'M SP    04')
        self.oHelper.SetButton('Visualizar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.AssertTrue()  

    def test_TMSA039_CT003(self):

        self.oHelper.SearchBrowse(f'M SP    03')
        self.oHelper.SetButton('Alterar')
        self.oHelper.SetValue("DLO_CODTPC","04")
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.AssertTrue() 

    def test_TMSA039_CT004(self): 

        self.oHelper.SearchBrowse(f'M SP    03')
        self.oHelper.SetButton('Outras Ações','Excluir')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()     