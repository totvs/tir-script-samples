from tir import Webapp
import unittest

class TMSA330(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGATMS','06/11/2020','T1','M SP 03 ','43')
        inst.oHelper.Program('TMSA330')  	

        inst.oHelper.AddParameter("MV_CDHISAP", "", "00")
        inst.oHelper.SetParameters()


    def test_TMSA330_CT001(self):

        self.oHelper.SearchBrowse("M SP    000000001")

        self.oHelper.SetButton('Outras Ações', "Confirmar")
        self.oHelper.SetButton('Confirmar')
        
        self.oHelper.WaitProcessing('Processando...')	

        self.oHelper.AssertTrue()
	
		
    def test_TMSA330_CT002(self):

        self.oHelper.SearchBrowse("M SP    000000001")

        self.oHelper.SetButton('Visualizar')
        self.oHelper.SetButton('Cancelar')

        self.oHelper.SetButton('Outras Ações', "Estornar")
        self.oHelper.SetButton('Confirmar')
        
        self.oHelper.AssertTrue()

    def test_TMSA330_CT003(self):

        self.oHelper.SetButton('Fechar')        
        self.oHelper.SetBranch('M SP 03')

        self.oHelper.SetValue('Fil.Origem De ?','M SP 01')
        self.oHelper.SetValue('Fil.Origem Ate ?','M SP 03')
        self.oHelper.SetValue('Emissao De ?','01/04/2020')
        self.oHelper.SetValue('Emissao Ate ?','10/04/2020') 
        self.oHelper.SetButton('Ok')	

        self.oHelper.SetButton('Salvar')
        self.oHelper.SetButton('Cancelar')

        self.oHelper.SetButton('Outras Ações', "Estornar")
        self.oHelper.SetButton('Confirmar')

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()

