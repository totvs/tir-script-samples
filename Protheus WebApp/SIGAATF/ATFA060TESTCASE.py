# coding: UTF-8
from tir import Webapp
import unittest

class ATFA060(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()

        inst.oHelper.Setup("SIGAATF", "01/06/2015", "T1", "M SP 01 ", "01")
        inst.oHelper.Program("ATFA060")

        inst.oHelper.AddParameter("MV_TIPDEPR","","0")
        inst.oHelper.AddParameter("MV_ATFCATR","","1")

        inst.oHelper.AddParameter("M SP 01 MV_ULTDEPR","","20150531")
        inst.oHelper.AddParameter("M SP 02 MV_ULTDEPR","","20150531")

        inst.oHelper.SetParameters()

    def test_ATFA060_001(self):

        chave = "M SP 01 ATF02"
        self.oHelper.SearchBrowse(f"{chave}", key=1, index=True)

        self.oHelper.SetButton("Outras Ações", "Canc. Transf.")
        self.oHelper.SetBranch("M SP 01 ")

        # Parâmetros de perguntes
        self.oHelper.SetValue("MV_PAR01", "ATF02", name_attr=True)  # Código Base de
        self.oHelper.SetValue("MV_PAR02", "001", name_attr=True)  # Item de

        self.oHelper.SetValue("MV_PAR03", "ATF02", name_attr=True)  # Código Base Ate
        self.oHelper.SetValue("MV_PAR04", "001", name_attr=True)  # Item Ate

        self.oHelper.SetValue("MV_PAR05", "", name_attr=True)  # Grupo de
        self.oHelper.SetValue("MV_PAR06", "ZZZZ", name_attr=True)  # Grupo ate

        self.oHelper.SetValue("Mostra Lanc Contab ?","Não")  # Mostra Lanc Contab
        self.oHelper.SetValue("Aglut Lancamentos ?","Não")  # Aglut Lancamentos
        self.oHelper.SetValue("Cancelamento ?", "Filial")  # Cancelamento
        self.oHelper.SetButton("OK")

        self.oHelper.WaitShow("Transferencia de Ativos - Cancelar")

        self.oHelper.ClickBox("Cod Base Bem", "ATF02")
        self.oHelper.SetButton("Confirmar")
        
        self.oHelper.WaitShow("Sair")  # ESPERAR O BOTÃO APARECER
        self.oHelper.SetButton("Sair")

        self.oHelper.SearchBrowse(f"{chave}", key=1, index=True)

        self.oHelper.AssertFalse()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
