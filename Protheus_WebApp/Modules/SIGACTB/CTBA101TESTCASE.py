from tir import Webapp
import unittest


class CTBA101(unittest.TestCase):

    @classmethod
    def setUpClass(inst):

        inst.oHelper = Webapp()

        inst.oHelper.Setup("SIGACTB", "01/01/2019", "T1", "D MG 01", "34")

        inst.oHelper.Program("CTBA101")

    def test_CTBA101_001(self):
        # Estorno
        self.oHelper.WaitShow("Lançamento Contábil")

        COD = "000000004           01/06/2015"
        self.oHelper.SearchBrowse(
            f"D MG 01 {COD}", "Filial+cta Debito + Data Lcto")

        self.oHelper.SetButton("Outras Ações", "Estornar")
        self.oHelper.SetButton("Ok")
        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Sim")

        self.oHelper.AssertTrue()

    def test_CTBA101_002(self):
        # Excluir
        COD = "000000005           02/06/2015"
        self.oHelper.SearchBrowse(
            f"D MG 01 {COD}", "Filial+cta Credito + Data Lcto")

        self.oHelper.SetButton("Outras Ações", "Excluir")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Sim")

        self.oHelper.SearchBrowse(
            f"D MG 01 {COD}", "Filial+cta Credito + Data Lcto")

        self.oHelper.AssertTrue()

    def test_CTBA101_003(self):
        # Visualizar
        self.oHelper.SetButton("Visualizar")
        self.oHelper.SetButton("Confirmar")
        self.oHelper.AssertTrue()

    def test_CTBA101_004(self):
        # Alterar
        COD = "000000003           02/01/2020"
        self.oHelper.SearchBrowse(
            f"D MG 01 {COD}", "Filial+cta Credito + Data Lcto")

        self.oHelper.SetButton("Alterar")
        self.oHelper.SetButton("Ok")        
        
        self.oHelper.ClickFolder("Conversoes")

        self.oHelper.CheckResult(
            "crit", "Informada", grid=True, line=1)

        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Sim")

        self.oHelper.AssertTrue()

    def test_CTBA101_006(self):
        # Incluir PARTIDA DOBRADA

        self.oHelper.SetButton("Incluir")

        self.oHelper.SetBranch("D MG 01")

        self.oHelper.SetValue("Data","27062015") 

        self.oHelper.SetValue("Lote","CBA101") 

        self.oHelper.SetButton("Ok")

        self.oHelper.SetValue("cTipoCTB","3 - Partida Dobrada",name_attr=True) 

        self.oHelper.SetValue("cHistPad","005",name_attr=True)  

        self.oHelper.SetValue("cDebito","CTBA101D",name_attr=True) 

        self.oHelper.SetValue("cCredit","CTBA101C",name_attr=True) 

        self.oHelper.SetValue("nValorCTB","500,00",name_attr=True) 

        self.oHelper.SetButton("Salvar")

        self.oHelper.SetButton("Sim")

        self.oHelper.SetButton("Cancelar")

        self.oHelper.AssertTrue()

    def test_CTBA101_007(self):
        # Alterar

        self.oHelper.SearchBrowse(f"D MG 01 28/06/2015211EDC001000001001", "Filial+data Lcto + Numero Lote + Sub Lote + Numero Doc + Numero Linha + Tipo")

        # self.oHelper.SearchBrowse(f"D MG 01 {codigo}",key=1,index=True)

        self.oHelper.SetButton("Alterar")
        self.oHelper.SetButton("Ok") 

        self.oHelper.SetValue("cHistPad","005",name_attr=True)       
        
        self.oHelper.ClickFolder("Conversoes")

        self.oHelper.SetValue("Crit", "5 - Nao tem Conversao", grid=True, grid_number=1, row=1)
        self.oHelper.SetValue("Crit", "5 - Nao tem Conversao", grid=True, grid_number=1, row=2)
        self.oHelper.SetValue("Crit", "5 - Nao tem Conversao", grid=True, grid_number=1, row=3)
        self.oHelper.SetValue("Crit", "5 - Nao tem Conversao", grid=True, grid_number=1, row=4)
        # self.oHelper.ClickFolder("Conversoes")
        # self.oHelper.ClickFolder("Lançamento")
        self.oHelper.LoadGrid()

        self.oHelper.ClickFolder("Outras Informaçäes")#VERIFICA OUTRAS INFORMAÇÃES

        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Sim")

        self.oHelper.AssertTrue()

    def test_CTBA101_008(self):
        # Incluir DEBITO 

        self.oHelper.SetButton("Incluir")

        self.oHelper.SetBranch("D MG 01")

        self.oHelper.SetValue("Data","23062015") 

        self.oHelper.SetValue("Lote","CTINDE") 

        self.oHelper.SetButton("Ok")

        self.oHelper.SetValue("cTipoCTB","1 - Debito",name_attr=True) 

        self.oHelper.SetValue("cDebito","CTBA101D",name_attr=True) 

        self.oHelper.SetValue("cCustoCrd","000000003",name_attr=True) 

        self.oHelper.SetValue("cItemCrd","000000001",name_attr=True) 
        
        self.oHelper.SetValue("cCLVLCrd","000002",name_attr=True) 

        self.oHelper.SetButton("Salvar")

        self.oHelper.CheckHelp(text_help="NOCTADEB", button="Fechar")

        self.oHelper.SetValue("cCustoCrd","",name_attr=True) 

        self.oHelper.SetButton("Salvar")

        self.oHelper.CheckHelp(text_help="NOCTADEB", button="Fechar")

        self.oHelper.SetValue("cItemCrd","",name_attr=True) 

        self.oHelper.SetButton("Salvar")

        self.oHelper.CheckHelp(text_help="NOCTADEB", button="Fechar")

        self.oHelper.SetValue("cCLVLCrd","",name_attr=True)

        self.oHelper.SetButton("Salvar")

        self.oHelper.CheckHelp(text_help="NOVALOR", button="Fechar")

        self.oHelper.SetValue("nValorCTB","500,00",name_attr=True) 

        self.oHelper.SetButton("Salvar")

        self.oHelper.CheckHelp(text_help="NOHIST", button="Fechar")

        self.oHelper.SetValue("cHistPad","005",name_attr=True) 

        self.oHelper.SetButton("Salvar")

        self.oHelper.CheckHelp(text_help="CT2DEB", button="Fechar")

        self.oHelper.SetValue("cTpSald","9",name_attr=True)

        self.oHelper.SetButton("Salvar")
        
        self.oHelper.SetButton("Sim")

        self.oHelper.SetButton("Cancelar")

        self.oHelper.AssertTrue()

    def test_CTBA101_009(self):
        # Incluir CREDITO 

        self.oHelper.SetButton("Incluir")

        self.oHelper.SetBranch("D MG 01")

        self.oHelper.SetValue("Data","24062015") 

        self.oHelper.SetValue("Lote","CTINCR") 

        self.oHelper.SetButton("Ok")

        self.oHelper.SetValue("cTpSald","9",name_attr=True)

        self.oHelper.SetValue("cTipoCTB","2 - Credito",name_attr=True) 

        self.oHelper.SetValue("cCredit","CTBA101C",name_attr=True) 

        self.oHelper.SetValue("cCustoDeb","000000003",name_attr=True) 

        self.oHelper.SetValue("cItemDeb","000000001",name_attr=True) 
        
        self.oHelper.SetValue("cCLVLDeb","000002",name_attr=True) 

        self.oHelper.SetValue("nValorCTB","500,00",name_attr=True) 

        self.oHelper.SetValue("cHistPad","500",name_attr=True) 

        self.oHelper.CheckHelp(text_help="NOHISTPAD", button="Fechar")

        self.oHelper.SetValue("cHistPad","005",name_attr=True) 

        self.oHelper.SetButton("Salvar")

        self.oHelper.CheckHelp(text_help="NOCTACRD", button="Fechar")

        self.oHelper.SetValue("cCustoDeb","",name_attr=True) 

        self.oHelper.SetButton("Salvar")

        self.oHelper.CheckHelp(text_help="NOCTACRD", button="Fechar")

        self.oHelper.SetValue("cItemDeb","",name_attr=True) 

        self.oHelper.SetButton("Salvar")

        self.oHelper.CheckHelp(text_help="NOCTACRD", button="Fechar")

        self.oHelper.SetValue("cCLVLDeb","",name_attr=True)

        self.oHelper.SetButton("Salvar")

        self.oHelper.SetButton("Sim")

        self.oHelper.SetButton("Cancelar")

        self.oHelper.AssertTrue()

    def test_CTBA101_010(self):
        # Incluir PARTIDA DOBRADA
        self.oHelper.WaitShow("Lançamento Contábil")

        self.oHelper.SetKey("F12")
        self.oHelper.WaitShow("Parametros")
        
        self.oHelper.SetValue("Repete lcto anter. ?","Nao")

        self.oHelper.SetButton("Ok")

        self.oHelper.SetButton("Incluir")

        self.oHelper.SetBranch("D MG 01")

        self.oHelper.SetValue("Data","25062015") 

        self.oHelper.SetValue("Lote","CTNRPT") 

        self.oHelper.SetButton("Ok")

        self.oHelper.SetValue("cTipoCTB","3 - Partida Dobrada",name_attr=True) 

        self.oHelper.SetValue("cHistPad","005",name_attr=True)  

        self.oHelper.SetValue("cDebito","CTBA101D",name_attr=True) 

        self.oHelper.SetValue("cCredit","CTBA101C",name_attr=True) 

        self.oHelper.SetValue("nValorCTB","1000,00",name_attr=True) 

        self.oHelper.SetButton("Salvar")

        self.oHelper.SetButton("Sim")

        self.oHelper.SetButton("Cancelar")

        self.oHelper.AssertTrue()

    def test_CTBA101_011(self):
        # Alterar

        self.oHelper.WaitShow("Lançamento Contábil")
        self.oHelper.SearchBrowse(f"D MG 01 29/06/2015211EDH001000001001", "Filial+data Lcto + Numero Lote + Sub Lote + Numero Doc + Numero Linha + Tipo")

        self.oHelper.SetButton("Alterar")
        self.oHelper.SetButton("Ok") 

        self.oHelper.SetValue("cHistPad","003",name_attr=True)       
        
        self.oHelper.ClickFolder("Conversoes")

        self.oHelper.SetValue("Crit", "1 - Diaria", grid=True, grid_number=1, row=1)
        self.oHelper.SetValue("Crit", "1 - Diaria", grid=True, grid_number=1, row=2)
        self.oHelper.SetValue("Crit", "1 - Diaria", grid=True, grid_number=1, row=3)
        self.oHelper.SetValue("Crit", "1 - Diaria", grid=True, grid_number=1, row=4)
        # self.oHelper.ClickFolder("Conversoes")
        # self.oHelper.ClickFolder("Lançamento")
        self.oHelper.LoadGrid()

        self.oHelper.ClickFolder("Lançamento")#VERIFICA OUTRAS INFORMAÇÃES

        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Sim")

        self.oHelper.AssertTrue()

    def test_CTBA101_012(self):
        # Copiar

        self.oHelper.WaitShow("Lançamento Contábil")
        self.oHelper.SearchBrowse(f"D MG 01 30/06/2015COPIAR001000001001", "Filial+data Lcto + Numero Lote + Sub Lote + Numero Doc + Numero Linha + Tipo")

        self.oHelper.SetButton("Outras Ações", "Copiar")

        self.oHelper.SetValue("Lote","CPMSMA")


        self.oHelper.SetButton("Ok") 

        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Sim")

        self.oHelper.AssertTrue()

    def test_CTBA101_013(self):
        # Copiar

        self.oHelper.WaitShow("Lançamento Contábil")
        self.oHelper.SearchBrowse(f"D MG 01 30/06/2015COPIAR001000001001", "Filial+data Lcto + Numero Lote + Sub Lote + Numero Doc + Numero Linha + Tipo")

        self.oHelper.SetButton("Outras Ações", "Cópia Filial")

        self.oHelper.SetValue("MV_PAR01","D MG 02",name_attr=True) 

        self.oHelper.SetButton("Ok") 
        
        self.oHelper.SetValue("Lote","CPOTFI")

        self.oHelper.SetButton("Ok") 

        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Sim")

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
