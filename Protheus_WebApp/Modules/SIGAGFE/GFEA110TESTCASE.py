from tir import Webapp
import unittest

class GFEA110(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAGFE", "30/06/2020", "T1", "D MG 01", "78")
        inst.oHelper.Program("GFEA110")

    def test_GFEA110_CT001(self):         
       
        self.oHelper.SetValue('Versão do Layout ?','3.1')

        self.oHelper.SetButton('OK')

        self.oHelper.SetValue('Filial de ?','')
        self.oHelper.SetValue('Filia ate ?','ZZZZZZZZ')
        self.oHelper.SetValue('Serie de ?','')
        self.oHelper.SetValue('Serie ate ?','ZZZZZ')
        self.oHelper.SetValue('Nr Docto de ?','')
        self.oHelper.SetValue('Nr Docto ate ?','ZZZZZZZZZZZZZZZZ')
        self.oHelper.SetValue('Dt Emissao de ?','01/11/2018')
        self.oHelper.SetValue('Dt Emissao ate ?','30/11/2018')
        self.oHelper.SetValue('Transportador de ?','')
        self.oHelper.SetValue('Transportador ate ?','ZZZZZZZZZZZZZZ')
        self.oHelper.SetValue('Somente Embarcados ?','Não')
        self.oHelper.SetValue('Destino ?','spool')
                        
        self.oHelper.SetButton('OK')        

        self.oHelper.SetButton('OK')       

        self.oHelper.AssertTrue()
     
    def test_GFEA110_CT002(self):

        self.oHelper.Program('GFEA110')
        
        self.oHelper.SetValue('Versão do Layout ?','5.0')

        self.oHelper.SetButton('OK')

        self.oHelper.SetValue('Filial de ?','')
        self.oHelper.SetValue('Filial até ?','ZZZZZZZZ')
        self.oHelper.SetValue('Série de ?','')
        self.oHelper.SetValue('Série até ?','ZZZZZ')
        self.oHelper.SetValue('Data Emissão de ?','01/11/2018')
        self.oHelper.SetValue('Data Emissão até ?','30/11/2018')
        self.oHelper.SetValue('Transportador de ?','')
        self.oHelper.SetValue('Transportador até ?','ZZZZZZZZZZZZZZ')
        self.oHelper.SetValue('Diretório ?','spool')
        self.oHelper.SetValue('Enviar email transportador ?','Não')
                        
        self.oHelper.SetButton('OK')

        self.oHelper.SetButton('Detalhes')

        self.oHelper.SetButton('OK')        

        self.oHelper.AssertTrue()      
            
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == "__main__":
    unittest.main()
