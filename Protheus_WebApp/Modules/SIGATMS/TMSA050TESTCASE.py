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
        
        self.oHelper.SearchBrowse("M SP    M SP 01 000085")
        self.oHelper.SetButton('Alterar')
        self.oHelper.SetValue('DTC_VLRINF','300,00')
        self.oHelper.SetButton('Salvar')
        self.oHelper.AssertTrue()

    #+-------------------------------------------------------------------------------
    #| Cenario 020: Excluir Documento de Entrada
    #+-------------------------------------------------------------------------------
    def test_TMSA050_CT020(self):
        
        self.oHelper.SearchBrowse("M SP    M SP 01 000085")
        self.oHelper.SetButton('Outras Ações','Estornar')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.AssertTrue()

    #+-------------------------------------------------------------------------------
    # CENARIO : C114 - Inclusao Entrada de Documentos
    #+-------------------------------------------------------------------------------
    def test_TMSA050_CT114(self):
        
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetBranch('M SP 01')

        self.oHelper.SetValue('DTC_LOTNFC','000155')
        self.oHelper.SetValue('DTC_FILCFS','M SP 03')
        self.oHelper.SetValue('DTC_DATENT','09/06/2020')
        self.oHelper.SetValue('DTC_CLIREM','TMS001')
        self.oHelper.SetValue('DTC_LOJREM','01')
        self.oHelper.SetValue('DTC_CLIDES','TMS002')
        self.oHelper.SetValue('DTC_LOJDES','01')
        self.oHelper.SetValue('DTC_CLICON','TMS003')
        self.oHelper.SetValue('DTC_LOJCON','01')
        self.oHelper.SetValue('DTC_CLIDPC','TMS001')
        self.oHelper.SetValue('DTC_LOJDPC','01')
        self.oHelper.SetValue('DTC_DEVFRE','3')
        self.oHelper.SetValue('DTC_SERTMS','3')
        self.oHelper.SetValue('DTC_TIPTRA','1')
        self.oHelper.SetButton('Cancelar')
        self.oHelper.SetValue('DTC_SERVIC','321')
        self.oHelper.SetValue('DTC_TIPNFC','0')
        self.oHelper.SetValue('DTC_SELORI','2')
        self.oHelper.SetValue('DTC_CDRCAL','Q48708')
        self.oHelper.SetValue('DTC_KM','11,2')
        self.oHelper.SetValue('DTC_DISTIV','2')
        self.oHelper.SetValue('DTC_RECISS','2')
        self.oHelper.SetValue('DTC_CLIEXP','TMS001')
        self.oHelper.SetValue('DTC_LOJEXP','01')
        self.oHelper.SetValue('DTC_CODNEG','01')
        self.oHelper.SetValue('DTC_INVORI','1')
        self.oHelper.SetValue('DTC_OBS','TESTE DE OBS')

        self.oHelper.SetValue('DTC_NFEID','1234569871424587741147741747455888554477',grid=True,grid_number=1,row=1)
        self.oHelper.SetValue('DTC_NUMNFC','09062020',grid=True,grid_number=1,row=1)
        self.oHelper.SetValue('DTC_SERNFC','123',grid=True,grid_number=1,row=1)
        self.oHelper.SetValue('DTC_CODPRO','001',grid=True,grid_number=1,row=1)
        self.oHelper.SetValue('DTC_CODEMB','CX',grid=True,grid_number=1,row=1)
        self.oHelper.SetValue('DTC_EMINFC','09062020',grid=True,grid_number=1,row=1)
        self.oHelper.SetValue('DTC_QTDVOL','1',grid=True,grid_number=1,row=1)
        self.oHelper.SetValue('DTC_PESO','1,2340',grid=True,grid_number=1,row=1)
        self.oHelper.SetValue('DTC_PESOM3','2,3456',grid=True,grid_number=1,row=1)
        self.oHelper.SetValue('DTC_VALOR','100,25',grid=True,grid_number=1,row=1)
        self.oHelper.SetValue('DTC_BASSEG','250,22',grid=True,grid_number=1,row=1)
        self.oHelper.SetValue('DTC_VALDPC','100,11',grid=True,grid_number=1,row=1)
        self.oHelper.SetValue('DTC_CF','5663',grid=True,grid_number=1,row=1)
        self.oHelper.SetValue('DTC_BASICM','12,01',grid=True,grid_number=1,row=1)
        self.oHelper.SetValue('DTC_VALICM','10,01',grid=True,grid_number=1,row=1)
        self.oHelper.SetValue('DTC_VALDPC','100,11',grid=True,grid_number=1,row=1)
        self.oHelper.SetValue('DTC_BASESU','20,55',grid=True,grid_number=1,row=1)
        self.oHelper.SetValue('DTC_VALIST','20,56',grid=True,grid_number=1,row=1)        
        self.oHelper.SetValue('DTC_TIPANT','0',grid=True,grid_number=1,row=1)
        self.oHelper.LoadGrid()

        self.oHelper.SetButton('Outras Ações','Vis.Frete')
        self.oHelper.SetButton('Cancelar')

        self.oHelper.SetButton('Outras Ações','Tip.Vei.')
        self.oHelper.SetValue('DVU_TIPVEI','01',grid=True,grid_number=1,row=1)
        self.oHelper.SetValue('DVU_QTDVEI','1',grid=True,grid_number=1,row=1)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton('Salvar')

        self.oHelper.SetButton('Outras Ações','Val.Inf.')
        self.oHelper.SetValue('DVR_VALOR','1,0000',grid=True,grid_number=1,row=1)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton('Salvar')

        self.oHelper.SetButton('Outras Ações','Cot.Real.')
        self.oHelper.SetButton('Sair')

        self.oHelper.SetButton('Outras Ações','Frete Inf.')
        self.oHelper.SetButton('Cancelar')

        self.oHelper.SetButton('Outras Ações','Peso Cub.')
        self.oHelper.SetValue('DTE_QTDVOL','1',grid=True,grid_number=1,row=1)
        self.oHelper.SetValue('DTE_ALTURA','1,55',grid=True,grid_number=1,row=1)
        self.oHelper.SetValue('DTE_LARGUR','1,81',grid=True,grid_number=1,row=1)
        self.oHelper.SetValue('DTE_COMPRI','1,54',grid=True,grid_number=1,row=1)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton('Salvar')

        # Salve Data
        self.oHelper.SetButton('Salvar')
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
    
        #    Test Case Ending
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
