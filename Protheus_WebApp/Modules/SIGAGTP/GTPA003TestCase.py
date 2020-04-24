from tir import Webapp
import unittest

class GTPA003(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAGTP", "14/04/2020", "T1", "D MG 01 ")
        inst.oHelper.Program('GTPA003')

    def test_GTPA003_CT001(self):
        self.oHelper.ScrollGrid(column='Linha', match_value='000012')
        self.oHelper.SetButton('Outras Ações', 'Manutenção dos Trechos')
        self.oHelper.SetButton('Não')
        self.oHelper.SetButton('Outras Ações', 'Seção da Linha')
        self.oHelper.SetButton('Sair')
        self.oHelper.SetValue("Origem", "LOC001")
        self.oHelper.SetValue("Destino","LOC003")
        self.oHelper.SetButton('Pesquisar')
        self.oHelper.SetValue("GI4_MSBLQL",'2')
        self.oHelper.SetValue("GI4_TARANU",'1')
        self.oHelper.SetValue("GI4_VIGTAR",'31/12/2020')
        self.oHelper.SetValue("GI4_TAR",'120,00')
        self.oHelper.SetValue("GI4_VIGTAX",'31/12/2020')
        self.oHelper.SetValue("GI4_TAX",'5,00')
        self.oHelper.SetValue("GI4_VIGPED",'31/12/2020')
        self.oHelper.SetValue("GI4_PED",'1,00')
        self.oHelper.SetValue("GI4_VIGSGF",'31/12/2020')
        self.oHelper.SetValue("GI4_SGFACU",'1,00')
        self.oHelper.SetValue("GI4_KMPED",'800,00')
        self.oHelper.SetValue("GI4_KMASFA",'800,00')
        self.oHelper.SetValue("GI4_KMTERR",'0,00')
        self.oHelper.SetValue("GI4_KM",'1000,00')
        self.oHelper.SetValue("GI4_TEMPO",'12:00')
        self.oHelper.SetButton("Confirmar")
        self.oHelper.SetButton("Fechar")
        self.oHelper.LoadGrid()
        self.oHelper.AssertTrue()

    def test_GTPA003_CT002(self):
        self.oHelper.ScrollGrid(column='Linha', match_value='000012')
        self.oHelper.SetButton('Histórico')
        self.oHelper.SetButton('X')
        self.oHelper.LoadGrid()
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()             

if __name__ == '__main__':
        unittest.main()
