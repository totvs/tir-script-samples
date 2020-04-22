from tir import Webapp
from datetime import datetime
DataSystem = datetime.today().strftime('%d/%m/%Y')
import unittest


class FATA400(unittest.TestCase):
    Contr = ""

    @classmethod
    def setUpClass(inst):
        '''
        SETUP
        Test Case Initial Setup
        '''

        #Endereço do webapp e o nome do Browser
        inst.oHelper = Webapp()

        #Parametros de inicializaçao
        inst.oHelper.Setup("SIGAFAT", DataSystem,"T1","D MG 01 ","05")

        #Nome da rotina do Caso de Teste
        inst.oHelper.Program("FATA400")

    def test_FATA400_CT001(self):
        '''
        Test Case 001
        '''
        global Contr

        self.oHelper.SetButton("Incluir")
        self.oHelper.SetBranch("D MG 01 ")

        Contr = self.oHelper.GetValue("ADA_NUMCTR")
        self.oHelper.SetValue("ADA_NUMCTR", Contr)
        self.oHelper.SetValue("ADA_EMISSA","04/07/2019")
        self.oHelper.SetValue("ADA_CODCLI","000001")
        self.oHelper.SetValue("ADA_LOJCLI","01")
        self.oHelper.SetValue("ADA_CONDPG","000")

        self.oHelper.SetValue("ADB_CODPRO", "FAT000000000000000000000000001", grid=True)
        self.oHelper.SetValue("ADB_QUANT", "1,00", grid=True)
        self.oHelper.SetValue("ADB_PRCVEN", "1,00", grid=True)
        self.oHelper.SetValue("ADB_TES", "501", grid=True)
        self.oHelper.SetValue("ADB_TESCOB", "503", grid=True)

        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Cancelar")
        
        self.oHelper.SearchBrowse(f"D MG 01 {Contr}", "Filial+contrato N.")
        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("ADA_NUMCTR", Contr)
        self.oHelper.CheckResult("ADA_CODCLI","000001")
        self.oHelper.CheckResult("ADA_LOJCLI","01")
        self.oHelper.CheckResult("ADA_CONDPG","000")

        self.oHelper.CheckResult("ADB_CODPRO", " FAT000000000000000000000000001", grid=True, line=1)
        self.oHelper.CheckResult("ADB_QUANT", "1,00", grid=True, line=1)
        self.oHelper.CheckResult("ADB_PRCVEN", "1,00", grid=True, line=1)
        self.oHelper.CheckResult("ADB_TES", "501", grid=True, line=1)
        self.oHelper.CheckResult("ADB_TESCOB", "503", grid=True, line=1)

        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Cancelar")
        self.oHelper.AssertTrue()

    def test_FATA400_CT002(self):
        '''
        Test Case 002
        '''
        global Contr
        self.oHelper.SearchBrowse(f"D MG 01 {Contr}", "Filial+contrato N.")
        self.oHelper.SetButton("Alterar")

        self.oHelper.SetValue("ADA_EMISSA","04/07/2019")
        self.oHelper.SetValue("ADA_CODCLI","000001")
        self.oHelper.SetValue("ADA_LOJCLI","01")
        self.oHelper.SetValue("ADA_CONDPG","000")

        self.oHelper.SetValue("ADB_CODPRO", "FAT000000000000000000000000001", grid=True)
        self.oHelper.SetValue("ADB_QUANT", "1,00", grid=True)
        self.oHelper.SetValue("ADB_PRCVEN", "1,00", grid=True)
        self.oHelper.SetValue("ADB_TES", "501", grid=True)
        self.oHelper.SetValue("ADB_TESCOB", "518", grid=True)

        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Salvar")

        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("ADA_NUMCTR", Contr)
        self.oHelper.CheckResult("ADA_CODCLI","000001")
        self.oHelper.CheckResult("ADA_LOJCLI","01")
        self.oHelper.CheckResult("ADA_CONDPG","000")

        self.oHelper.CheckResult("ADB_CODPRO", "FAT000000000000000000000000001", grid=True, line=1)
        self.oHelper.CheckResult("ADB_QUANT", "1,00", grid=True, line=1)
        self.oHelper.CheckResult("ADB_PRCVEN", "1,00", grid=True, line=1)
        self.oHelper.CheckResult("ADB_TES", "501", grid=True, line=1)
        self.oHelper.CheckResult("ADB_TESCOB", "518", grid=True, line=1)

        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Confirmar")
        self.oHelper.AssertTrue()

    def test_FATA400_CT003(self):
        '''
        Test Case 003
        '''
        Contr       = '000016'
        NovoContr   = 'TIR901'
        self.oHelper.SearchBrowse(f"D MG 01 {Contr}", "Filial+contrato N.")
        self.oHelper.SetButton("Outras Ações","Copia")

        self.oHelper.SetValue("ADA_NUMCTR", NovoContr)
        self.oHelper.SetButton("Confirmar")

        self.oHelper.SearchBrowse(f"D MG 01 {NovoContr}", "Filial+contrato N.")

        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("ADA_CODCLI","000001")
        self.oHelper.CheckResult("ADA_NUMCTR", NovoContr)

        self.oHelper.LoadGrid()
        self.oHelper.SetButton("Cancelar")

        self.oHelper.LoadGrid()

        self.oHelper.AssertTrue()

    def test_FATA400_CT004(self):
        '''
        Test Case 004
        '''
        NumContr = '000017'
        self.oHelper.SearchBrowse(f"D MG 01 {NumContr}", "Filial+contrato N.")
        self.oHelper.SetButton("Outras Ações","Excluir")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.AssertTrue()

        '''
        #Aguardando correção da Task 1558 subir para branch Master
        self.oHelper.SearchBrowse(f"D MG 01 {NumContr}", "Filial+contrato N.")

        self.oHelper.SetButton("Visualizar")

        self.oHelper.CheckResult("ADA_NUMCTR",NumContr)

        self.oHelper.SetButton("Cancelar")

        self.oHelper.AssertFalse()
        '''
    def test_FATA400_CT005(self):
        '''
        Test Case 005
        '''
        NumContr = '000015'
        self.oHelper.SearchBrowse(f"D MG 01 {NumContr}", "Filial+contrato N.")
        self.oHelper.SetButton("Outras Ações","Remessa")

        self.oHelper.SetButton("Cancelar")

        self.oHelper.AssertTrue()

    def test_FATA400_CT006(self):
        '''
        Test Case 006
        '''
        NumContr = '000018'
        self.oHelper.SearchBrowse(f"D MG 01 {NumContr}", "Filial+contrato N.")
        self.oHelper.SetButton("Outras Ações","AProvar")

        self.oHelper.SetButton("Salvar")

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        '''
        Method that finishes the test case.
        '''
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
