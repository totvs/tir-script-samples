from tir import Webapp
import unittest
import datetime

class TMSA050(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
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

    def test_TMSA050_CT017(self):       
        self.oHelper.SearchBrowse("M SP    M SP 01 000017")
        self.oHelper.SetButton('Outras Ações', 'Copiar')
        self.oHelper.SetValue('DTC_LOTNFC','000084')
        self.oHelper.SetValue('DTC_NUMNFC','190626001',grid=True,grid_number=1,row=1)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton('Salvar')
        self.oHelper.AssertTrue()
   
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()
