from tir import Webapp
import unittest

class CTBA102(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGACTB", "15/04/2015", "T1", "M SP 01 ", "34")
        inst.oHelper.Program("CTBA102")
        inst.oHelper.AddParameter("MV_CTBAPLA","","4")
        inst.oHelper.AddParameter("MV_ATUSAL" ,"","N")
        inst.oHelper.AddParameter("MV_CONTBAT","","S")
        inst.oHelper.AddParameter("MV_CONTSB" ,"","N")
        inst.oHelper.AddParameter("MV_CTBLIMC","","0.20;0.20;0.20;0.20;0.20")
        inst.oHelper.AddParameter("MV_CTBCENC","","10101010003")
        inst.oHelper.SetParameters()

    @classmethod
    def test_CTBA102_001(self):
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("M SP 01 ")
        self.oHelper.SetValue("Lote", "000001")
        self.oHelper.SetButton("Ok")
        self.oHelper.SetValue("Tipo Lcto" ,"3 - Partida Dobrada",grid=True)
        self.oHelper.SetValue("CT2_DEBITO","101030105" ,grid=True)
        self.oHelper.SetValue("CT2_CREDIT","2130205"   ,grid=True)
        self.oHelper.SetValue("CT2_VALOR" ,"1000,00"   ,grid=True)
        self.oHelper.SetValue("Hist Lanc" ,"TESTE INC.",grid=True) 
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.SetButton("Visualizar")
        self.oHelper.CheckResult("CT2_VALOR", "1.000,00", grid=True, line=1)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Cancelar")
        self.oHelper.AssertTrue()
   
    @classmethod
    def tearDownClass(inst):        
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
