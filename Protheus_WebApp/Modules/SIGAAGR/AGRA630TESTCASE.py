from tir import Webapp
import unittest

class AGRA630(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAAGR','05/11/2019','T1','D MG 01 ','67')		
        inst.oHelper.Program('AGRA630')

    def test_AGRA630_CT001(self): #TESTECASE CLASSIFICACAO DE MALA MANUAL COM NOVO UBA
        
        #alterando parâmetro para usar novo UBA
        self.oHelper.AddParameter("MV_AGRA001","",".T.",".T.",".T.")#Novo UBA
        self.oHelper.SetParameters()
        #incluindo a mala
        self.oHelper.SetButton('Incluir')		
        self.oHelper.SetButton('OK')						
        self.oHelper.SetValue("DXJ_SAFRA", "1920")
        self.oHelper.SetValue("DXJ_PRDTOR", "000001")
        self.oHelper.SetValue("DXJ_LJPRO", "01")
        self.oHelper.SetValue("DXJ_CODUNB", "02")
        
        #adicionando os fardos
        self.oHelper.SetButton('Outras Ações', 'Incluir Fardos')	
        self.oHelper.SetValue("MV_PAR01", "012222")
        self.oHelper.SetValue("MV_PAR02", "012223")
        self.oHelper.SetValue("MV_PAR04", "2")
        self.oHelper.SetButton('OK')
        self.oHelper.WaitShow("Fardos Sem Classificação")        
        self.oHelper.ClickBox("Etiqueta", select_all=True, grid_number=1)
        self.oHelper.SetButton('>>')		
        self.oHelper.SetButton('Salvar')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')
        
        #classificando
        self.oHelper.SetButton('Outras Ações', 'Classificar')
        self.oHelper.WaitShow("Mala de Classificação - Mala de Classificação")
        self.oHelper.ClickGridCell("Fardo", row=1, grid_number=1)
        current_value1 = self.oHelper.GetValue("Etiqueta", grid=True, grid_number=1)
        current_value2 = self.oHelper.GetValue("Etiqueta", grid=True, grid_number=1, line=2)
        self.oHelper.SetValue("cClasVis", value="11-1", name_attr=True)
        self.oHelper.SetValue("cEtiqueta", value=current_value1, name_attr=True)
        self.oHelper.SetKey("Enter")
        self.oHelper.SetValue("cClasVis", value="11-2", name_attr=True)
        self.oHelper.SetValue("cEtiqueta", value=current_value2, name_attr=True)
        self.oHelper.SetKey("Enter")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        
        #conferência dos valores
        self.oHelper.SetButton("Visualizar")
        self.oHelper.WaitShow("Mala de Classificação - VISUALIZAR")
        self.oHelper.ClickGridCell("Fardo", row=1, grid_number=1)
        self.oHelper.CheckResult("Peso Líquido", "200,00",  grid=True, line=1, grid_number=1)
        self.oHelper.LoadGrid()
        self.oHelper.CheckResult("Class. Vis.", "11-1",  grid=True, line=1, grid_number=1)
        self.oHelper.LoadGrid()
        
        self.oHelper.CheckResult("Peso Líquido", "200,00",  grid=True, line=2, grid_number=1)
        self.oHelper.LoadGrid()
        self.oHelper.CheckResult("Class. Vis.", "11-2",  grid=True, line=2, grid_number=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()
    
    def test_AGRA630_CT002(self): #TESTECASE CLASSIFICACAO DE MALA MANUAL COM ANTIGO UBA
        #alterando parâmetro para usar antigo UBA
        self.oHelper.AddParameter("MV_AGRA001","",".F.",".F.",".F.")#Novo UBA
        self.oHelper.SetParameters()
        #incluindo a mala
        self.oHelper.SetButton('Incluir')		
        self.oHelper.SetButton('OK')						
        self.oHelper.SetValue("DXJ_SAFRA", "1920")
        self.oHelper.SetValue("DXJ_PRDTOR", "000001")
        self.oHelper.SetValue("DXJ_LJPRO", "01")
        self.oHelper.SetValue("DXJ_CODUNB", "02")
        
        #adicionando os fardos
        self.oHelper.SetButton('Outras Ações', 'Incluir Fardos')	
        self.oHelper.SetValue("MV_PAR01", "012224")
        self.oHelper.SetValue("MV_PAR02", "012225")
        self.oHelper.SetValue("MV_PAR04", "2")
        self.oHelper.SetButton('OK')
        self.oHelper.WaitShow("Fardos Sem Classificação")        
        self.oHelper.ClickBox("Etiqueta", select_all=True, grid_number=1)
        self.oHelper.SetButton('>>')		
        self.oHelper.SetButton('Salvar')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')
        
        #classificando
        self.oHelper.SetButton('Outras Ações', 'Classificar')
        self.oHelper.WaitShow("Mala de Classificação - Mala de Classificação")
        self.oHelper.ClickGridCell("Fardo", row=1, grid_number=1)
        current_value1 = self.oHelper.GetValue("Etiqueta", grid=True, grid_number=1)
        current_value2 = self.oHelper.GetValue("Etiqueta", grid=True, grid_number=1, line=2)
        self.oHelper.SetValue("cClasVis", value="11-1", name_attr=True)
        self.oHelper.SetValue("cEtiqueta", value=current_value1, name_attr=True)
        self.oHelper.SetKey("Enter")
        self.oHelper.SetValue("cClasVis", value="11-2", name_attr=True)
        self.oHelper.SetValue("cEtiqueta", value=current_value2, name_attr=True)
        self.oHelper.SetKey("Enter")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        
        #conferência dos valores
        self.oHelper.SetButton("Visualizar")
        self.oHelper.WaitShow("Mala de Classificação - VISUALIZAR")
        self.oHelper.ClickGridCell("Fardo", row=1, grid_number=1)
        self.oHelper.CheckResult("Peso Líquido", "200,00",  grid=True, line=1, grid_number=1)
        self.oHelper.LoadGrid()
        self.oHelper.CheckResult("Class. Vis.", "11-1",  grid=True, line=1, grid_number=1)
        self.oHelper.LoadGrid()
        
        self.oHelper.CheckResult("Peso Líquido", "200,00",  grid=True, line=2, grid_number=1)
        self.oHelper.LoadGrid()
        self.oHelper.CheckResult("Class. Vis.", "11-2",  grid=True, line=2, grid_number=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Fechar")

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()