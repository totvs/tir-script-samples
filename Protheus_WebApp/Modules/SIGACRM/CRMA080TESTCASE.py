from tir import Webapp 
import unittest
from datetime import datetime

DateSystem = datetime.today().strftime("%d/%m/%Y")

class CRMA080(unittest.TestCase):

    @classmethod
    def setUpClass(self): 
        self.oHelper = Webapp()
        self.oHelper.SetTIRConfig(config_name="User",value="APICRM")
        self.oHelper.SetTIRConfig(config_name="Password",value="1")
        self.oHelper.Setup("SIGACRM", DateSystem, "T1", "D MG 01 ", "73")
        self.oHelper.Program("CRMA080")  

    def test_CRMA080_CT001(self):  
        self.oHelper.WaitShow("Configuração de Filtros - Funil de Vendas")
        self.oHelper.ScrollGrid(column="Processo",match_value="FAT004",grid_number=2)
        self.oHelper.ClickBox(fields="Processo", contents_list="FAT004", select_all=False, grid_number=2)
        self.oHelper.SetValue("Dt. Início","18/07/2019")
        self.oHelper.ClickCheckBox("Todos Vendedores")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.WaitShow("Consulta - Funil de Vendas")
        self.oHelper.ClickGridCell(column="Oportunidade",row=2,grid_number=2)
        self.oHelper.SetButton("Outras Ações","Visualizar Oportunidade")
        self.oHelper.WaitShow("Oportunidade de Venda - Visualizar Oportunidade")
        self.oHelper.SetButton("Fechar")
        self.oHelper.WaitShow("Consulta - Funil de Vendas")
        self.oHelper.SetButton("Outras Ações","Configurar Filtros")
        self.oHelper.WaitShow("Configuração de Filtros - Funil de Vendas")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.WaitShow("Consulta - Funil de Vendas")
        self.oHelper.SetButton("Cancelar")
        self.oHelper.WaitHide("Consulta - Funil de Vendas")
        self.oHelper.AssertTrue() 
        
    @classmethod
    def tearDownClass(self):
        self.oHelper.TearDown()  

if __name__ == "__main__":
    unittest.main()