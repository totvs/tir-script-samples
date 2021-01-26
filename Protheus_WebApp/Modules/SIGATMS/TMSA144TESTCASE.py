from tir import Webapp
import unittest
import datetime

class TMSA144(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
         # set the date
        dataAtual = str(datetime.datetime.now().strftime("%d/%m/%Y")) 
        inst.oHelper.Setup('SIGATMS',dataAtual,'T1','M SP 03 ','43')
        inst.oHelper.Program("TMSA144D")

        inst.oHelper.AddParameter("MV_CONTVEI", "", ".F.")
        inst.oHelper.AddParameter("MV_TMSALOC", "", ".F.")
        inst.oHelper.AddParameter("MV_ENVIAG", "", ".F.")
        inst.oHelper.AddParameter("MV_TMSRRE", "", "")          
        inst.oHelper.SetParameters()

    def test_TMSA144_CT186(self):
        self.oHelper.SetButton('Visualizar')
        self.oHelper.SetButton('Cancelar')
        
        self.oHelper.SetKey("F12")
        self.oHelper.SetValue("Serviço Adicional ?","1")
        self.oHelper.SetValue("Rentab. Previa Fechamento ?", "Não")
        self.oHelper.SetButton("OK")

        self.oHelper.SetButton('Incluir')

        self.oHelper.SetBranch("M SP 03")

        self.oHelper.SetButton("OK")

        self.oHelper.SetValue("DTQ_ROTA", "ENTSP3")
        self.oHelper.SetValue("DTQ_KMVGE", "120,5")
        self.oHelper.SetValue("DTQ_CDRORI", "Q50308")

        self.oHelper.SetValue("DTA_FILDOC", "M SP 03 ",grid=True,grid_number=1,row=1)
        self.oHelper.SetValue("DTA_DOC", "000000036",grid=True,grid_number=1,row=1)
        self.oHelper.SetValue("DTA_SERIE", "664",grid=True,grid_number=1,row=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Outras Ações","Comp.Via")
        self.oHelper.SetValue("DTR_CODVEI", "TMS0047",grid=True,grid_number=1,row=1)
        self.oHelper.SetValue("DTR_VALFRE", "1.100,00",grid=True,grid_number=1,row=1)
        self.oHelper.SetValue("DTR_CREADI", "TMS001",grid=True,grid_number=1,row=1)
        self.oHelper.SetValue("DTR_LOJCRE", "01",grid=True,grid_number=1,row=1)
        self.oHelper.SetValue("DTR_QTEIXV", "2",grid=True,grid_number=1,row=1)
        self.oHelper.SetValue("DTR_CIOT", "12345678901234567",grid=True,grid_number=1,row=1)
        self.oHelper.LoadGrid()

               
        self.oHelper.SetButton("Outras Ações","Mot.Viag.")
        self.oHelper.SetValue("DUP_CODMOT", "TMS047",grid=True,grid_number=1,row=1)
        #self.oHelper.SetValue("DUP_LIBSEG", "123456789012345",grid=True,grid_number=1,row=1)
        self.oHelper.SetValue("DUP_VALSEG", "100.000,00",grid=True,grid_number=1,row=1)
        self.oHelper.SetValue("DUP_CONDUT", "1",grid=True,grid_number=1,row=1)
        self.oHelper.SetValue("DUP_PAGDIA", "1",grid=True,grid_number=1,row=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Salvar")
                
        self.oHelper.SetButton("Outras Ações","Aju.Viag.")
        self.oHelper.SetValue("DUQ_CODAJU", "000002",grid=True,grid_number=1,row=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Salvar")

        self.oHelper.SetButton("Outras Ações","Lac.Veic.")
        self.oHelper.SetValue("DVB_LACRE", "0000000002",grid=True,grid_number=1,row=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Salvar")

        self.oHelper.SetButton("Outras Ações","Adiantam./Desp.")
        self.oHelper.SetValue("DG_CODDES", "100100",grid=True,grid_number=1,row=1)
        self.oHelper.SetValue("DG_TOTAL", "12,00",grid=True,grid_number=1,row=1)
        self.oHelper.LoadGrid()
                
        self.oHelper.SetButton("Salvar")

        self.oHelper.SetButton("Outras Ações","Val. Inf.")
        self.oHelper.SetValue("DVW_CODPAS", "61",grid=True,grid_number=1,row=1)
        self.oHelper.SetValue("DVW_VALOR", "1.100,0000",grid=True,grid_number=1,row=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton("Salvar")

        self.oHelper.ClickFolder("Operadoras de Frota")
        self.oHelper.SetValue("DTR_CODOPE", "01")
        self.oHelper.SetValue("DTR_TPSPDG","3")

        self.oHelper.ClickFolder("Outros")
        self.oHelper.SetValue("DTR_TIPCRG", "1")

        self.oHelper.SetButton("Salvar")

        self.oHelper.SetButton("Outras Ações","Limite")
        self.oHelper.SetButton("Salvar")

        self.oHelper.SetButton("Outras Ações","Docto.")
        self.oHelper.SetButton("Cancelar")

        self.oHelper.SetButton("Outras Ações","Redespachos da Viagem")
        self.oHelper.SetButton("Cancelar")

        self.oHelper.SetButton("Outras Ações","Docto de Carga")
        self.oHelper.SetButton("Sair")

        self.oHelper.SetButton("Salvar")
        self.oHelper.SetButton("Cancelar")

        self.oHelper.AssertTrue()

    def test_TMSA144_CT187(self):

        self.oHelper.SearchBrowse("M SP    000050")

        self.oHelper.SetButton("Outras Ações","Excluir")
        
        self.oHelper.SetButton("Confirmar")

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == "__main__":
    unittest.main()
