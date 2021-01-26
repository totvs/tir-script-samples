from tir import Webapp
import unittest

class TMSA320(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGATMS','19/06/2019','T1','M SP 03 ','43')
        inst.oHelper.Program('TMSA320')  	

        inst.oHelper.AddParameter("MV_DESAWB", "", "DESPAWB")
        inst.oHelper.AddParameter("MV_TESAWB", "", "038")
        inst.oHelper.SetParameters()	

    def test_TMSA320_CT001(self):		
            
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetBranch('M SP 03')

        self.oHelper.SetValue('DTV_NUMAWB','000987654')
        self.oHelper.SetValue('DTV_DIGAWB','8')
        self.oHelper.SetValue('DTV_DATEMI','10/11/2020')
        self.oHelper.SetValue('DTV_VIAGEM','000069')
        self.oHelper.WaitShow('Geracao de AWB - INCLUIR')
        self.oHelper.ClickBox('No.Manifesto', '999100003')
        self.oHelper.SetButton('Salvar')
        self.oHelper.SetValue('DTV_CDRDES', 'Q48708')
        self.oHelper.SetValue('DTV_CODPRO', 'TMS-DIVERSOS000000000000000000')
        self.oHelper.SetValue('DTV_AERORI', 'GRU')
        self.oHelper.SetValue('DTV_AERDES', 'CGH')
        self.oHelper.SetValue('DTV_CODCIA', 'TMSLAT')
        self.oHelper.SetValue('DTV_LOJCIA', 'AM')
        self.oHelper.SetValue('DTV_TABFRE', 'P001')
        self.oHelper.SetValue('DTV_CODEMB', 'CX')

        self.oHelper.SetButton('Outras Ações', "Digitação do Componen.")
        self.oHelper.SetButton('Salvar')

        self.oHelper.SetButton('Outras Ações', "Atualiza Compos.")

        self.oHelper.SetButton('Outras Ações', "Cotação")
        self.oHelper.SetButton('Salvar')

        self.oHelper.SetButton('Salvar')
        
        self.oHelper.WaitProcessing('Gerando AWB ...')

        self.oHelper.SetButton('Cancelar')

        self.oHelper.AssertTrue()
	
    def test_TMSA320_CT002(self):

        self.oHelper.SearchBrowse("M SP 03 0009876548")

        self.oHelper.SetButton('Outras Ações', "Estornar")
        self.oHelper.SetButton("Confirmar")

        self.oHelper.WaitProcessing('Estornando AWB ...')
        
        self.oHelper.AssertTrue()
    
    def test_TMSA320_CT003(self):

        self.oHelper.SearchBrowse("M SP 03 P00000001") #balcao

        self.oHelper.SetButton('Outras Ações', "Efetivar")
        self.oHelper.SetValue("cNroOfic","123456789",name_attr = True)
        self.oHelper.SetValue('Dígito', '1')
        self.oHelper.SetButton("Ok")
        self.oHelper.WaitHide('AWB Oficial')

        self.oHelper.AssertTrue()

    def test_TMSA320_CT004(self):

        self.oHelper.SearchBrowse("M SP 03 123456789")
        
        self.oHelper.SetButton('Outras Ações', "Altera Efetivação?")
        self.oHelper.SetButton("Sim")
        self.oHelper.SetValue("cNroOfic","987654321",name_attr = True)
        self.oHelper.SetValue('Dígito', '9')
        self.oHelper.SetButton("Ok")

        self.oHelper.SetButton("Fechar")
        
        self.oHelper.AssertTrue()

    def test_TMSA320_CT005(self):

        self.oHelper.SearchBrowse("M SP 03 0009876548")
        
        self.oHelper.SetButton('Outras Ações', "Conf. Embarque > Confirmar")
        self.oHelper.WaitShow('Registro de Ocorrencias  ')
        self.oHelper.SetButton("Sim")
        self.oHelper.SetValue("Nr. Voo ","123456")
        self.oHelper.SetValue('Data Partida', '12/11/2020')
        self.oHelper.SetValue('Hora Partida', '12:00')
        self.oHelper.SetValue('Data Chegada', '12/11/2020')
        self.oHelper.SetValue('Hora Chegada', '15:00')
        self.oHelper.SetButton("Salvar")
        
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()

