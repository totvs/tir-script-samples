from tir import Webapp
import unittest

class ATFA012(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAATF", "01/04/2016", "T1", "D MG 01 ", "01")
        inst.oHelper.Program("ATFA012")  
        inst.oHelper.AddParameter("MV_ULTDEPR","", "20160331")
        inst.oHelper.AddParameter("D RJ 02 MV_ULTDEPR", "", "19801231")
        inst.oHelper.AddParameter("MV_ALTLCTO", "", "N")
        inst.oHelper.AddParameter("MV_PRELAN", "", "S")
        inst.oHelper.SetParameters()

    def test_ATFA012_001(self):
        codigo = "ATF0000005001    "
        self.oHelper.SearchBrowse(f"D MG 01 {codigo}", "Filial+cod. do Bem + Item")
        self.oHelper.SetButton("Outras Ações", "Excluir Lote")s    
        self.oHelper.SetValue("MV_PAR01","ATF0000005"	)
        self.oHelper.SetValue("MV_PAR02","ATF0000005"	)
        self.oHelper.SetValue("MV_PAR03","001"		)	
        self.oHelper.SetValue("MV_PAR04","001"	    )	
        self.oHelper.SetValue("MV_PAR05","01/11/2015" )
        self.oHelper.SetValue("MV_PAR06","01/11/2015" )	
        self.oHelper.SetButton("OK")
        self.oHelper.ClickBox("Cod. do Bem","ATF0000005") 
        self.oHelper.SetButton("Confirmar")     
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
