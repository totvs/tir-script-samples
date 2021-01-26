from tir import Webapp
import unittest

class OGA455(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAAGR','04/11/2019','T1','D MG 01 ','67')
        inst.oHelper.Program('OGA455')

    def test_OGA455_CT001(self):    
        if self.oHelper.GetRelease() >= "12.1.027":
            self.oHelper.SetButton('Incluir')
            self.oHelper.SetButton('OK')
            cCodigo = self.oHelper.GetValue("Codigo")            
            self.oHelper.SetValue("NBT_LOCORI", "01", name_attr=True)
            self.oHelper.SetValue("NBT_TESORI", "501", name_attr=True)
            self.oHelper.SetValue("NBT_DTCALC", "27/11/2019", name_attr=True)
            self.oHelper.ClickFolder("Dados destino")
            self.oHelper.SetValue("NBT_CTRDES", "000107", name_attr=True)
            self.oHelper.SetValue("NBT_TABDES", "0001", name_attr=True)
            self.oHelper.SetValue("NBT_ENTDES", "000001", name_attr=True)
            self.oHelper.SetValue("NBT_LOCDES", "01", name_attr=True)
            self.oHelper.SetValue("NBT_TESDES", "004", name_attr=True)
            self.oHelper.SetValue("NBT_TPFORM", "1", name_attr=True)
            self.oHelper.SetValue("NBT_TPFRET", "C", name_attr=True)
            self.oHelper.SetValue("NBT_VLRUNI", "1,000000", name_attr=True)
            self.oHelper.SetValue("NBT_VLRTOT", "100,00", name_attr=True)
            self.oHelper.SetButton('Outras Ações',"Selecionar Contratos")
            self.oHelper.SetButton('OK')
            self.oHelper.ClickBox("Contrato","000108",grid_number = 1)
            self.oHelper.SetValue("Quantidade","100,00")
            self.oHelper.SetButton('Salvar')
            self.oHelper.SetButton('Confirmar')
            self.oHelper.SetButton('Outras Ações',"Selecionar Notas")
            self.oHelper.SetButton('Salvar')
            self.oHelper.SetButton('Confirmar')
            self.oHelper.SetButton('Fechar')
            #teste delete do vínculo
            self.oHelper.SearchBrowse("D MG 01 "+cCodigo)
            self.oHelper.SetButton('Outras Ações',"Visualizar")
            self.oHelper.ClickFolder("Dados destino")
            self.oHelper.CheckResult("NBT_VLRTOT", user_value ="100,00")
            self.oHelper.SetButton('Fechar')
            self.oHelper.AssertTrue()


    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()