from tir import Webapp
import unittest

class ATFA430(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAATF", "10/02/2015", "T1", "D MG 01 ","01")
        inst.oHelper.Program("ATFA430")  
        inst.oHelper.AddParameter("MV_ALTLCTO","","N")
        inst.oHelper.AddParameter("MV_PRELAN","","S")
        inst.oHelper.AddParameter("D MG 01 MV_ULTDEPR","","20150131")
        inst.oHelper.SetParameters()
        
    @classmethod
    def test_ATFA430_001(self):
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetButton("Ok")
        self.oHelper.WaitShow("Projeto")       
        self.oHelper.SetValue("Codigo"       , "TESTE_TIR1")
        self.oHelper.SetValue("Descricao"    , "TESTE_TIR1")
        self.oHelper.SetValue("Indice AVP"   , "01"        )
        self.oHelper.SetValue("Cod Base ATF" , "TESTE_TIR1")
        self.oHelper.SetValue("Inicio Prj"   , "10/02/2015")
        self.oHelper.SetValue("Inicio Prov"  , "10/02/2015")
        self.oHelper.SetValue("Dt.Prev.Exec" , "10/02/2015")    
        self.oHelper.SetValue("Desc.Item"  ,"TESTE_TIR1",grid=True)        
        self.oHelper.SetValue("Periodo ini","10/02/2015",grid=True)       
        self.oHelper.SetValue("Vlr. Planej","1.000,00"  ,grid=True)
        self.oHelper.LoadGrid()
        self.oHelper.ClickFolder("Etapa")
        self.oHelper.SetValue("Desc Etapa","TESTE_TIR1",grid=True)
        self.oHelper.LoadGrid()
        self.oHelper.ClickFolder("Configuração Contábil")       
        self.oHelper.SetValue("Grupo Bem","0005",grid=True,grid_number=2)        
        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Confirmar")        
        self.oHelper.SetButton("Fechar")
        self.oHelper.SearchBrowse(f'D MG 01 TESTE_TIR1',key=1,index=True)
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):        
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
