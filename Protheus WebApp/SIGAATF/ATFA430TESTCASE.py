from tir import Webapp
import unittest

class ATFA430(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        # Endereço do webapp e o nome do Browser
        inst.oHelper = Webapp()

        # Parametros de inicializaçao
        inst.oHelper.Setup("SIGAATF", "10/02/2015", "T1", "D MG 01 ","01")

         # Nome da rotina do Caso de Teste
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

    def test_ATFA430_002(self):        

        self.oHelper.SearchBrowse(f'D MG 01 TESTE_TIR2',key=1,index=True)

        self.oHelper.SetButton("Outras Ações","Atualizar",position=1)       
        
        self.oHelper.SetButton("Outras Ações","Confirmar",position=2)
        self.oHelper.SetButton("Sim")
        self.oHelper.SetButton("Sair")
   
        self.oHelper.SearchBrowse(f'D MG 01 TESTE_TIR2',key=1,index=True)

        self.oHelper.AssertTrue()

    def test_ATFA430_003(self):
                
        self.oHelper.SearchBrowse(f'D MG 01 TESTE_TIR3',key=1,index=True)

        self.oHelper.SetButton("Outras Ações","Exportar CSV")
        
        self.oHelper.SetValue("MV_PAR01","\\baseline\\atfa430_tir3.csv" )
        
        self.oHelper.SetButton("Ok")

        self.oHelper.SetButton("Ok")
   
        self.oHelper.SearchBrowse(f'D MG 01 TESTE_TIR3',key=1,index=True)

        self.oHelper.AssertTrue()

    def test_ATFA430_004(self):

        self.oHelper.SetButton("Outras Ações","Importar CSV")
        
        self.oHelper.SetButton("Ok")

        self.oHelper.SetValue("MV_PAR01","\\baseline\\atfa430_tir4.csv")        
        self.oHelper.SetValue("MV_PAR02","Sim")
        self.oHelper.SetButton("Ok")
  
        self.oHelper.SearchBrowse(f'D MG 01 TESTE_TIR30002',key=1,index=True)

        self.oHelper.AssertTrue()

    def test_ATFA430_005(self):
                
        self.oHelper.SearchBrowse(f'D MG 01 TESTE_TIR4',key=1,index=True)

        self.oHelper.SetButton("Outras Ações","Rev AVP")
        
        self.oHelper.SetValue("Indice AVP" , "05")
        
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Sim")
        self.oHelper.SetButton("Fechar")
        self.oHelper.SetButton("Sair")
   
        self.oHelper.SearchBrowse(f'D MG 01 TESTE_TIR4',key=1,index=True)

        self.oHelper.AssertTrue()
        
    def test_ATFA430_006(self):
                
        self.oHelper.SearchBrowse(f'D MG 01 TESTE_TIR5',key=1,index=True)

        self.oHelper.SetButton("Outras Ações","Realizar",position=1)

        self.oHelper.WaitShow("Projeto de Imobilizado - Realização de Projeto")  
        
        self.oHelper.SetValue("C Base Exec" ,"TESTE_TIR5"       ,grid=True,grid_number=2)        
        self.oHelper.SetValue("Item Exec"   ,"0001"             ,grid=True,grid_number=2)       
        self.oHelper.SetValue("Tipo ATF Exe","01 - DEPR. FISCAL",grid=True,grid_number=2)
        self.oHelper.SetValue("Tipo SLD Exe","1 - Real"         ,grid=True,grid_number=2)        
        self.oHelper.LoadGrid()
        
        self.oHelper.SetButton("Confirmar")        
        self.oHelper.SetButton("Fechar")   
   
        self.oHelper.SearchBrowse(f'D MG 01 TESTE_TIR5',key=1,index=True)

        self.oHelper.AssertTrue()

    def test_ATFA430_007(self):
                
        self.oHelper.SearchBrowse(f'D MG 01 TESTE_TIR6',key=1,index=True)

        self.oHelper.SetButton("Outras Ações","Excluir")
        self.oHelper.SetButton("Confirmar")        
        self.oHelper.SetButton("Sim")   
        self.oHelper.SetButton("Fechar")   
   
        self.oHelper.SearchBrowse(f'D MG 01 TESTE_TIR6',key=1,index=True)
        
        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("FNB_CODPRJ", "TESTE_TIR6")
        self.oHelper.CheckResult("FNB_DESC"  , "TESTE_TIR6")      

        self.oHelper.AssertFalse()

    def test_ATFA430_008(self):
                
        self.oHelper.SearchBrowse(f'D MG 01 TESTE_TIR7',key=1,index=True)

        self.oHelper.SetButton("Outras Ações","Copiar",position=1)
        
        self.oHelper.WaitShow("Projeto de Imobilizado - Cópia")
        
        self.oHelper.SetValue("Codigo"       , "TESTE_TIR8")
        self.oHelper.SetValue("Descricao"    , "TESTE_TIR8")
        self.oHelper.SetValue("Indice AVP"   , "01"        )
        self.oHelper.SetValue("Cod Base ATF" , "TESTE_TIR8")
        self.oHelper.SetValue("Inicio Prj"   , "10/02/2015")
        self.oHelper.SetValue("Inicio Prov"  , "10/02/2015")
        self.oHelper.SetValue("Dt.Prev.Exec" , "10/02/2015")
        
        self.oHelper.SetValue("Desc.Item"  ,"TESTE_TIR8",grid=True)        
        self.oHelper.SetValue("Periodo ini","10/02/2015",grid=True)       
        self.oHelper.SetValue("Vlr. Planej","1.000,00"  ,grid=True)
        self.oHelper.LoadGrid()

        self.oHelper.ClickFolder("Etapa")

        self.oHelper.SetValue("Desc Etapa","TESTE_TIR8",grid=True)
        self.oHelper.LoadGrid()

        self.oHelper.ClickFolder("Configuração Contábil")
        
        self.oHelper.SetValue("Grupo Bem","0005",grid=True,grid_number=2)        
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Outras Ações","Calc. AVP")
        self.oHelper.SetButton("Sim")   

        self.oHelper.SetButton("Outras Ações","Copia CTB")
        self.oHelper.SetButton("Sim")   


        self.oHelper.SetButton("Confirmar")        
        self.oHelper.SetButton("Fechar")   
   
        self.oHelper.SearchBrowse(f'D MG 01 TESTE_TIR8',key=1,index=True)

        self.oHelper.AssertTrue()
    @classmethod
    def tearDownClass(inst):        

        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
