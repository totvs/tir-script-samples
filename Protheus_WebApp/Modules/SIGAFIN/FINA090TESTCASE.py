import unittest
import time

from tir import Webapp
from datetime import datetime
DateSystem = datetime.today().strftime('%d/%m/%Y')

"""-------------------------------------------------------------------
/*/{Protheus.doc} FINA090TestCase
TIR - Casos de testes da rotina contas a pagar 

@author Matheus Ribeiro
@since 04/06/2020
@version 12
-------------------------------------------------------------------"""


class FINA090(unittest.TestCase):

    # -------------------------------------------
    # Inicialiação setUpClass para TIR - FINA090
    # -------------------------------------------
    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAFIN", "04/06/2020", "T1", "D MG 01 ", "06")
        inst.oHelper.Program('FINA090')

    # -----------------------------------------
    # {Protheus.doc} FINA090_CT041
    # Conferência de total a ser baixado com seleção de título moeda 2

    # author Matheus Ribeiro
    # since 04/06/2020
    # version 1.0
    # See https://jiraproducao.totvs.com.br/secure/Tests.jspa#/testCase/GTSER-T51565
    # -----------------------------------------
    def test_FINA090_CT041(self):

        self.oHelper.AddParameter("MV_VLTITAD","",".T.",".T.",".T.") 
        self.oHelper.SetParameters()

        self.oHelper.WaitShow("Baixa de Títulos")

        # Abre Filtro de títulos
        self.oHelper.SetButton('Automática')

        # Tela de seleção de filiais
        time.sleep(5)
        self.oHelper.SetBranch('D MG 01')

        self.oHelper.SetValue("Banco", "001")
        self.oHelper.SetValue("Agência", "00001")
        self.oHelper.SetValue("Conta", "0000000001")

        self.oHelper.SetButton('Ok')

        time.sleep(5)

        self.oHelper.WaitShow("Baixa de Títulos - AUTOMÁTICA")

        self.oHelper.CheckView("222.004,19")

        self.oHelper.SetButton('Outras Ações',sub_item='Validador')
        self.oHelper.SetButton('Não')
        self.oHelper.SetButton('Não')

        self.oHelper.SetButton('Cancelar')

        time.sleep(5)

        self.oHelper.SetButton('Cancelar')

        self.oHelper.SetButton('X')
        self.oHelper.AssertTrue()

        self.oHelper.RestoreParameters()

    # -------------------------------------------
    # Encerramento class para TIR - FINA090
    # -------------------------------------------
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
