from tir import Webapp
import unittest
import datetime

class TMSA220(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
       inst.oHelper = Webapp()
       dataAtual = str(datetime.datetime.now().strftime("%d/%m,%Y"))
       inst.oHelper.Setup('SIGATMS',dataAtual,'T1','M SP 04 ','43')
       inst.oHelper.Program('TMSA220') 

    #Inclusão de registro
    def test_TMSA220_CT001(self):

        self.oHelper.SetButton('Incluir')
        self.oHelper.SetBranch('M SP 04')
        self.oHelper.SetValue('DTS_TABCAR', '0001')
        self.oHelper.SetValue('DTS_ROTA', 'ENTSP4')
        self.oHelper.ClickFolder("Premio") 
        self.oHelper.ClickFolder("Frete")  
        self.oHelper.SetValue('DTT_TIPVEI','01',grid=True,grid_number=1,row=1)
        self.oHelper.SetValue('DTT_TIPCAL','4',grid=True,grid_number=1,row=1)
        self.oHelper.SetValue('DTT_VALOR','100,00',grid=True,grid_number=1,row=1)
        self.oHelper.SetValue('DTT_INTERV','1,0000',grid=True,grid_number=1,row=1)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton('Salvar')
        self.oHelper.SetButton('Cancelar')
        self.oHelper.AssertTrue()

    #Visualizar registro
    def test_TMSA220_CT002(self):

        self.oHelper.SearchBrowse(f'M SP    0001ENTSP4')
        self.oHelper.SetButton('Visualizar')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.AssertTrue()     

    #Alteração de registro
    def test_TMSA220_CT003(self): 

        self.oHelper.SearchBrowse(f'M SP    0001ENTSP4')
        self.oHelper.SetButton('Alterar')
        self.oHelper.ClickFolder("Frete")  
        self.oHelper.SetValue('DTT_TIPVEI','02',grid=True,grid_number=1,row=1)
        self.oHelper.LoadGrid()
        self.oHelper.SetButton('Salvar')
        self.oHelper.AssertTrue()   

    #Copia de registro
    def test_TMSA220_CT004(self): 

        self.oHelper.SearchBrowse(f'M SP    0001ENTSP4')
        self.oHelper.SetButton('Outras Ações','Copiar')
        self.oHelper.SetValue("cRotaDe", "ENTSP4", name_attr=True)
        self.oHelper.SetValue("cRotaAte", "TM4XM3", name_attr=True)
        self.oHelper.SetValue("cNewTab", "0002", name_attr=True)
        self.oHelper.SetButton('OK')
        self.oHelper.SetButton('Confirma')
        self.oHelper.AssertTrue()

    #Exclusão de registro
    def test_TMSA220_CT005(self): 

        self.oHelper.SearchBrowse(f'M SP    0001ENTSP4')
        self.oHelper.SetButton('Outras Ações','Excluir')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SearchBrowse(f'M SP    0002COLGEN')
        self.oHelper.SetButton('Outras Ações','Excluir')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SearchBrowse(f'M SP    0002ESMG')
        self.oHelper.SetButton('Outras Ações','Excluir')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SearchBrowse(f'M SP    0002ENTSP4')
        self.oHelper.SetButton('Outras Ações','Excluir')
        self.oHelper.SetButton('Confirmar')

        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()