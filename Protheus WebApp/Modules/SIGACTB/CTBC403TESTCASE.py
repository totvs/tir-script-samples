from tir import Webapp
import unittest

class CTBC403(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGACTB','08/11/2017','T1','D MG 01 ','05')
        inst.oHelper.Program('CTBC403')

    def test_CTBC403_CT002(self):
        cContaCtb   = '1110227'
        self.oHelper.SetValue("mv_par01","08/11/2019", name_attr=True	)
        self.oHelper.SetValue("mv_par02","08/11/2019", name_attr=True	)
        self.oHelper.SetValue("mv_par03","01"		)
        self.oHelper.SetValue("mv_par04","1"	    )
        self.oHelper.SetValue("mv_par05","01" )	  
        self.oHelper.SetValue("mv_par07","05" )	
        self.oHelper.SetValue("Seleciona filiais ?", "Nao")
        self.oHelper.SetButton("OK")
        self.oHelper.SetValue("Da Conta ?","1110227")
        self.oHelper.SetValue("Ate a Conta ?","1110227")
        self.oHelper.SetValue("ENTIDADE05 De ?","005"	    )
        self.oHelper.SetValue("ENTIDADE05 Até ? ?","005"	    )		     
        self.oHelper.SetButton("OK")
        self.oHelper.SearchBrowse(f'D MG    {cContaCtb}', 'Filial+cod Conta')
        self.oHelper.SetButton("Visualizar")
        self.oHelper.SetButton("Confirmar")
               
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()