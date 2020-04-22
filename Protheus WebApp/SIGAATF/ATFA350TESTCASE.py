from tir import Webapp
import unittest

class ATFA350(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        # Endereço do webapp e o nome do Browser
        inst.oHelper = Webapp()

        # Parametros de inicialização
        inst.oHelper.Setup("SIGAATF", "10/10/2016", "T1", "M SP 01 ","01")

         # Nome da rotina do Caso de Teste
        inst.oHelper.Program("ATFA350")  

        inst.oHelper.AddParameter("MV_ALTLCTO","","N")
        inst.oHelper.AddParameter("MV_PRELAN","","S")
        inst.oHelper.AddParameter("MV_A350THR","","2")
        inst.oHelper.AddParameter("M SP 01 MV_ULTDEPR","","20160930")
        inst.oHelper.SetParameters()
        
    @classmethod
    def test_ATFA350_001(self):

        self.oHelper.SetButton("Incluir")
        
        self.oHelper.SetButton("Sim")

        self.oHelper.SetButton("Avançar")

        self.oHelper.SetValue("Codigo ?"                , "000001")
        self.oHelper.SetValue("Revisão ?"               , "0001")
        self.oHelper.SetValue("Períodos a Processar ?"  , "1")
        self.oHelper.SetValue("Base do Bem Modif. ?"    , "0000010001")
        self.oHelper.SetValue("Filial De ?"             , "M SP 01")
        self.oHelper.SetValue("Filial Ate ?"            , "M SP 01")
        self.oHelper.SetValue("Considera Bens ?"        , "Real")
        self.oHelper.SetValue("Tipo de Ativo ?"         , "Fiscal")
        self.oHelper.SetValue("Tipo de Saldo ?"         , "1")

        self.oHelper.SetButton("Avançar")

        self.oHelper.ClickFolder("Grupo Bens")

        self.oHelper.SetButton("Filtro")        
        self.oHelper.SetValue("Campos:" , "Grupo")
        self.oHelper.SetValue("cExpr"   , "A350",name_attr=True)

        self.oHelper.SetButton("Incluir")
        self.oHelper.SetButton("Ok")

        self.oHelper.ClickCheckBox("Seleciona Todos")

        self.oHelper.ClickFolder("Conta Depreciação")

        self.oHelper.SetButton("Filtro")        
        self.oHelper.SetValue("Campos:" , "Cod Conta")
        self.oHelper.SetValue("cExpr"   , "CTB_ATFA350_1",name_attr=True)

        self.oHelper.SetButton("Incluir")
        self.oHelper.SetButton("Ok")

        self.oHelper.ClickCheckBox("Seleciona Todos",position=2)

        self.oHelper.SetButton("Avançar")
        
        self.oHelper.SetValue("Filial"      , "M SP 01 "            ,grid=True)
        self.oHelper.SetValue("Cta Dep Acum", "CTB_ATFA350_2        ",grid=True)
        self.oHelper.SetValue("Tx.An.Depr.1", "0,80"                ,grid=True)
        self.oHelper.SetValue("Vlr. Moeda 1", "1.000,00"            ,grid=True)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Avançar")
        self.oHelper.SetButton("Sim")
        self.oHelper.SetButton("Finalizar")

        self.oHelper.WaitProcessing("Aguarde...")     

        self.oHelper.SearchBrowse("0000010001")

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):        

        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
