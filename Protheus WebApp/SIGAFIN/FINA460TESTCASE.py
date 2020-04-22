from tir import Webapp
import unittest
import time


class FINA460(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        '''
        SETUP
        Test Case Initial Setup
        '''

        #Endereço do webapp e o nome do Browser
        inst.oHelper = Webapp()

        #Parametros de inicializaçao
        inst.oHelper.Setup("SIGAFIN","09/11/2018","T1","D MG 01 ","06")

        #Nome da rotina do Caso de Teste
        inst.oHelper.Program("FINA460")

    def test_FINA460_001(self):
        '''
        Test Case 001
        '''

        time.sleep(5)
        self.oHelper.SearchBrowse("D MG 01    000001FIN")
        self.oHelper.SetButton("Liquidar")
        self.oHelper.SetBranch("D MG 01 ")
        self.oHelper.SetValue("Natureza Liquidação", "FIN5000000")
        self.oHelper.SetButton("Ok")

        self.oHelper.SetValue("FO0_COND", "000")
        self.oHelper.SetValue("FO0_TIPO", "NF")

        self.oHelper.ClickBox("Fil Origem","D MG 01",grid_number=1)

        self.oHelper.SetValue("FO2_PREFIX" , "LIQ"       , grid=True, grid_number=2)
        self.oHelper.SetValue("FO2_NUM"    , "99AA99001" , grid=True, grid_number=2)
        self.oHelper.SetValue("FO2_PARCEL" , "A"         , grid=True, grid_number=2)
        self.oHelper.SetValue("Tp Titulo"  , "NF"        , grid=True, grid_number=2)
        self.oHelper.SetValue("FO2_VENCTO" , "09/11/2018", grid=True, grid_number=2)
        self.oHelper.SetValue("FO2_VALOR"  , "1.000,00"  , grid=True, grid_number=2)
        self.oHelper.SetValue("FO2_BANCO"  , "000"       , grid=True, grid_number=2)
        self.oHelper.SetValue("FO2_AGENCI" , "00000"     , grid=True, grid_number=2)
        self.oHelper.SetValue("FO2_CONTA"  , "0000000000", grid=True, grid_number=2)
        self.oHelper.SetValue("FO2_NUMCH"  , "123456"    , grid=True, grid_number=2)

        self.oHelper.SetKey("DOWN", grid=True, grid_number=2)

        self.oHelper.SetValue("FO2_PREFIX" , "LIQ"       , grid=True, grid_number=2)
        self.oHelper.SetValue("FO2_NUM"    , "99AA99001" , grid=True, grid_number=2)
        self.oHelper.SetValue("FO2_PARCEL" , "B"         , grid=True, grid_number=2)
        self.oHelper.SetValue("Tp Titulo"  , "NF"        , grid=True, grid_number=2)
        self.oHelper.SetValue("FO2_VENCTO" , "09/11/2018", grid=True, grid_number=2)
        self.oHelper.SetValue("FO2_VALOR"  , "280,50"    , grid=True, grid_number=2)
        self.oHelper.SetValue("FO2_BANCO"  , "000"       , grid=True, grid_number=2)
        self.oHelper.SetValue("FO2_AGENCI" , "00000"     , grid=True, grid_number=2)
        self.oHelper.SetValue("FO2_CONTA"  , "0000000000", grid=True, grid_number=2)
        self.oHelper.SetValue("FO2_NUMCH"  , "123456"    , grid=True, grid_number=2)

        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Confirmar")

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        '''
        Method that finishes the test case.
        '''
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()