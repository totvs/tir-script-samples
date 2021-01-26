from tir import Webapp
import unittest

class TMSA300(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGATMS','06/11/2020','T1','M SP 03 ','43')
        inst.oHelper.Program('TMSA300')  		

    def test_TMSA300_CT001(self):

        self.oHelper.SetButton('Incluir')
        self.oHelper.SetBranch('M SP 03')	

        self.oHelper.SetValue('DU4_TABSEG','TEST')
        self.oHelper.SetValue('DU4_TPTSEG','01')
        self.oHelper.SetValue('DU4_DATDE','01/01/2020')

        self.oHelper.SetValue('DU5_CODPRO','TMS-DIVERSOS000000000000000000',grid=True,grid_number=1,row=1 )
        self.oHelper.SetValue('DU5_VALOR','100,00',grid=True,grid_number=1,row=1 )
        self.oHelper.SetValue('DU5_CDRORI','100013',grid=True,grid_number=1,row=1 )
        self.oHelper.SetValue('DU5_CDRDES','100054',grid=True,grid_number=1,row=1 )
        self.oHelper.LoadGrid()
        
        self.oHelper.SetButton('Salvar')
        self.oHelper.SetButton('Cancelar')

        self.oHelper.AssertTrue()
	
		
    def test_TMSA300_CT002(self):

        self.oHelper.SearchBrowse("M SP    TEST")

        self.oHelper.SetButton('Visualizar')
        self.oHelper.SetButton('Cancelar')

        self.oHelper.SearchBrowse("M SP    TEST")
        self.oHelper.SetButton('Outras Ações', "Excluir")

        self.oHelper.SetButton('Confirmar')
        
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()

