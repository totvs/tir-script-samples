from tir import Webapp
import unittest
from datetime import datetime
DateSystem = datetime.today().strftime("%d/%m/%Y")

class CRMA700(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGACRM',DateSystem,'T1','D MG 01 ','73')
        inst.oHelper.Program('CRMA700')
    
    def test_CRMA700_001(self):
        self.oHelper.SetButton("Incluir")
        self.oHelper.SetButton("Ok")
        self.oHelper.WaitShow("Prospects - INCLUIR")
        self.oHelper.SetValue("Codigo","PRO013")
        self.oHelper.SetValue("Loja","01")
        self.oHelper.SetValue("Razao Social","FABIO VEIGA LTDA")
        self.oHelper.SetValue("N Fantasia","Crm LTDA")
        self.oHelper.SetValue("Tipo","F")
        self.oHelper.SetValue("Endereço" ,"Rua dos cocais")
        self.oHelper.SetValue("Municipio","SAO PAULO")
        self.oHelper.SetValue("Bairro","Centro")
        self.oHelper.SetValue("Estado","SP")
        self.oHelper.SetValue("Cd.Municipio","50308")    
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
       inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()