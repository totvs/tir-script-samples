from tir import Webapp
import unittest
import datetime

class TMSA050(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()

        # set the date
        dataAtual = str(datetime.datetime.now().strftime("%d/%m/%Y")) 
        inst.oHelper.Setup('SIGATMS',dataAtual,'T1','M SP 01 ','43')
        inst.oHelper.Program('TMSA050')
        inst.oHelper.AddParameter("MV_CDRORI" ,"","Q50308"    )
        inst.oHelper.AddParameter("MV_TESDR"  ,"","482"       )
        inst.oHelper.AddParameter("MV_CLIGEN" ,"","TMSCLIGE"  )
        inst.oHelper.AddParameter("MV_TMSCFEC","",".T."       )
        inst.oHelper.AddParameter("MV_TMSMFAT","","2"         )
        inst.oHelper.AddParameter("MV_NATFAT" ,"","001"       )
        inst.oHelper.AddParameter("MV_COMPENT","","09"        )
        inst.oHelper.AddParameter("MV_TIPFAT" ,"","01"        )
        inst.oHelper.AddParameter("MV_FATPREF","","TMS"       )
        inst.oHelper.AddParameter("MV_CODCOMP","","10"        )
        inst.oHelper.AddParameter("MV_PROGEN" ,"","TMS_PROGEN")
        inst.oHelper.AddParameter("MV_TMSCTE" ,"",".T."       )
        inst.oHelper.AddParameter("MV_ESPECIE","","UNI=NF;117=CTE;")
        inst.oHelper.SetParameters()
    
    #+-------------------------------------------------------------------------------
    # CENARIO : C017 - Cópia de Documento de Entrada Simples
    #+-------------------------------------------------------------------------------
    def test_TMSA050_CT017(self):

        
        self.oHelper.SearchBrowse("M SP    M SP 01 000017")
        self.oHelper.SetButton('Outras Ações', 'Copiar')
        
        # start form field setting
        #self.oHelper.SetFocus("COD BAR:")
        self.oHelper.SetValue('DTC_LOTNFC','000084')
        self.oHelper.SetValue('DTC_NUMNFC','190626001',grid=True,grid_number=1,row=1)
        self.oHelper.LoadGrid()
        
        # Salve Data
        self.oHelper.SetButton('Salvar')
        self.oHelper.AssertTrue()
    #+-------------------------------------------------------------------------------
    #| Cenario 018: Fechar Lote do Documento
    #+-------------------------------------------------------------------------------
    # def test_TMSA050_CT018(self):

    #     self.oHelper.SearchBrowse("M SP".ljust(8) +"M SP 01 000084")
    #     self.oHelper.SetButton('Outras Ações',sub_item='Calculo Frete')
    #     self.oHelper.SetButton('Calculo Frete',sub_item='Fechar Lote')

    #     # self.oHelper.ClickLabel('Calculo Frete')
    #     # self.oHelper.SetKey('ENTER')
    #     self.oHelper.MessageBoxClick('Sim')
    #     self.oHelper.AssertTrue()

    #+-------------------------------------------------------------------------------
    #| Cenario 019: Alteração do Documento de Entrada informando o valor do Fr.Informado
    #+-------------------------------------------------------------------------------
    def test_TMSA050_CT019(self):
        
        self.oHelper.SearchBrowse("M SP".ljust(8)+"M SP 01 000085")
        self.oHelper.SetButton('Alterar')
        self.oHelper.SetValue('DTC_VLRINF','300,00')
        self.oHelper.SetButton('Salvar')
        self.oHelper.AssertTrue()

    #+-------------------------------------------------------------------------------
    #| Cenario 020: Excluir Documento de Entrada
    #+-------------------------------------------------------------------------------
    def test_TMSA050_CT020(self):
        
        self.oHelper.SearchBrowse("M SP".ljust(8)+"M SP 01 000085")
        self.oHelper.SetButton('Outras Ações','Estornar')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
    
        #    Test Case Ending
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
