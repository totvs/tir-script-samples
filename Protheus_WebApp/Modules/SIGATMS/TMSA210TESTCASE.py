from tir import Webapp
import unittest

class TMSA210(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGATMS','15/11/2020','T1','M SP 01 ','43')
        inst.oHelper.Program('TMSA210C')  	

        inst.oHelper.AddParameter("MV_TESDR",   "", "482")
        inst.oHelper.AddParameter("MV_CDRORI"  , "", "Q50308"  )
        inst.oHelper.AddParameter("MV_CLIGEN"  , "", "TMSCLIGE")
        inst.oHelper.AddParameter("MV_ESTADO"  , "", "SP")
        inst.oHelper.AddParameter("MV_CALNORI" , "", ".T.")
        inst.oHelper.AddParameter("MV_PRCPROD" , "", ".T.")
        inst.oHelper.AddParameter("MV_TMSCTE"  , "", ".T.")
        inst.oHelper.AddParameter("MV_TPNRNFS" , "", "1")
        inst.oHelper.AddParameter("MV_TMSMFAT" , "", "2")
        inst.oHelper.AddParameter("MV_ESPECIE" , "", "A01=NF;117=CTR")
        inst.oHelper.AddParameter("MV_ATIVCHG" , "", "050")
        inst.oHelper.AddParameter("MV_ATIVDCA" , "", "051")
        inst.oHelper.AddParameter("MV_COMPENT" , "", "05")
        inst.oHelper.AddParameter("MV_CONTVEI" , "", ".F.")
        inst.oHelper.AddParameter("MV_MOTGEN"  , "TMSGEN")
        inst.oHelper.AddParameter("MV_OCORREE" , "", ".T.")
        inst.oHelper.AddParameter("MV_PCANOP"  , "", "1")
        inst.oHelper.AddParameter("MV_TMSOPDG" , "", "0")
        inst.oHelper.AddParameter("MV_TMSPERC" , "", ".F.")
        inst.oHelper.AddParameter("MV_TMSUNFS" , "", ".T.")
        inst.oHelper.AddParameter("MV_VEIGEN"  , "", "TMSVGEN")
        inst.oHelper.AddParameter("MV_ATIVRTA" , "", "052")
        inst.oHelper.AddParameter("MV_SVCENT"  , "", "022")
        inst.oHelper.AddParameter("MV_DOCVGE"  , "", ".T.")
        inst.oHelper.AddParameter("MV_ALOCVEI" , "",  ".F.")
        inst.oHelper.AddParameter("MV_TMSALOC" , "", ".F.")
        inst.oHelper.AddParameter("MV_TPDCREE" , "", "2,5")
        inst.oHelper.AddParameter("MV_TMSRRE" , "", "")
        inst.oHelper.SetParameters()	

    def test_TMSA210_CT001(self):		
            
        self.oHelper.SetButton('Carregar')

        self.oHelper.SetValue('DTA_FILORI','M SP 01')
        self.oHelper.SetValue('DTA_VIAGEM','000009')
        self.oHelper.SetValue('DTA_CODVEI','TMSVEMM')


        self.oHelper.SetValue('DTA_FILDOC','M SP 01 ',grid=True,grid_number=1,row=1)
        self.oHelper.SetValue('DTA_DOC','000000040',grid=True,grid_number=1,row=1)
        self.oHelper.SetValue('DTA_SERIE','117',grid=True,grid_number=1,row=1)
        self.oHelper.SetValue('DTA_QTDVOL','100',grid=True,grid_number=1,row=1)
        self.oHelper.SetValue('DTA_DATAGD','15/11/2020',grid=True,grid_number=1,row=1)        
        self.oHelper.LoadGrid()

        self.oHelper.SetButton('Outras Ações', 'Viagem')
        self.oHelper.WaitShow('Geração de Viagens de Entrega')
        self.oHelper.SetButton('Cancelar')

        self.oHelper.SetButton('Salvar')

        self.oHelper.AssertTrue()
	
    def test_TMSA210_CT002(self):

        self.oHelper.SetButton('Outras Ações', "Pesquisar")
        self.oHelper.SetValue("cCampo","31M SP 01 000009M SP 01 000000040117",name_attr = True)
        self.oHelper.SetButton("Ok")
           
        self.oHelper.SetButton("Estornar")
        self.oHelper.SetButton("Salvar")
        
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()

