from tir import Webapp
import unittest

class GFEC001(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAGFE", "24/06/2020", "T1", "D MG 01", "78")
        inst.oHelper.Program("GFEC001")

    def test_GFEC001_CT001(self):         
        filial_de = 'D MG 01'
        filial_ate = 'D MG 01'
        data_ini = '01/01/2010'
        data_fim = '31/12/2020'

        self.oHelper.SetButton('Parâmetros')

        self.oHelper.SetValue('Filial de ?',filial_de)
        self.oHelper.SetValue('Filial ate ?',filial_ate)
        self.oHelper.SetValue('Data de ?',data_ini)
        self.oHelper.SetValue('Data ate ?',data_fim)
        
        self.oHelper.SetButton('Ok')

        self.oHelper.SearchBrowse("111")

        self.oHelper.SetButton('Visualizar')

        self.oHelper.SetButton('Fechar')

        self.oHelper.SetButton('Outras Ações','Recursos')

        self.oHelper.SetButton('X')
       
        self.oHelper.AssertTrue()
        
    def test_GFEC001_CT002(self):         
        filial_de = 'D MG 01'
        filial_ate = 'D MG 01'
        data_ini = '01/01/2010'
        data_fim = '31/12/2020'

        self.oHelper.SetButton('Parâmetros')

        self.oHelper.SetValue('Filial de ?',filial_de)
        self.oHelper.SetValue('Filial ate ?',filial_ate)
        self.oHelper.SetValue('Data de ?',data_ini)
        self.oHelper.SetValue('Data ate ?',data_fim)
        
        self.oHelper.SetButton('Ok')

        self.oHelper.SearchBrowse("111")

        self.oHelper.SetButton('Outras Ações','Doc Cargas')

        self.oHelper.SetButton('Sair')
       
        self.oHelper.AssertTrue()

    def test_GFEC001_CT003(self):         
        filial_de = 'D MG 01'
        filial_ate = 'D MG 01'
        data_ini = '01/01/2010'
        data_fim = '31/12/2020'

        self.oHelper.SetButton('Parâmetros')

        self.oHelper.SetValue('Filial de ?',filial_de)
        self.oHelper.SetValue('Filial ate ?',filial_ate)
        self.oHelper.SetValue('Data de ?',data_ini)
        self.oHelper.SetValue('Data ate ?',data_fim)
        
        self.oHelper.SetButton('Ok')

        self.oHelper.SearchBrowse("111")
        
        self.oHelper.SetButton('Outras Ações','Romaneios')

        self.oHelper.SetButton('X')
       
        self.oHelper.AssertTrue()
    
    def test_GFEC001_CT004(self):         
        filial_de = 'D MG 01'
        filial_ate = 'D MG 01'
        data_ini = '01/01/2010'
        data_fim = '31/12/2020'

        self.oHelper.SetButton('Parâmetros')

        self.oHelper.SetValue('Filial de ?',filial_de)
        self.oHelper.SetValue('Filial ate ?',filial_ate)
        self.oHelper.SetValue('Data de ?',data_ini)
        self.oHelper.SetValue('Data ate ?',data_fim)
        
        self.oHelper.SetButton('Ok')

        self.oHelper.SearchBrowse("111")

        self.oHelper.SetButton('Outras Ações','Agendamentos')

        self.oHelper.SetButton('X')
       
        self.oHelper.AssertTrue()

    def test_GFEC001_CT005(self):         
        filial_de = 'D MG 01'
        filial_ate = 'D MG 01'
        data_ini = '01/01/2010'
        data_fim = '31/12/2020'

        self.oHelper.SetButton('Parâmetros')

        self.oHelper.SetValue('Filial de ?',filial_de)
        self.oHelper.SetValue('Filial ate ?',filial_ate)
        self.oHelper.SetValue('Data de ?',data_ini)
        self.oHelper.SetValue('Data ate ?',data_fim)
        
        self.oHelper.SetButton('Ok')

        self.oHelper.SearchBrowse("111")

        self.oHelper.SetButton('Outras Ações','Reprovações')

        self.oHelper.SetButton('X')
       
        self.oHelper.AssertTrue()

    def test_GFEC001_CT006(self):         
        filial_de = 'D MG 01'
        filial_ate = 'D MG 01'
        data_ini = '01/01/2010'
        data_fim = '31/12/2020'

        self.oHelper.SetButton('Parâmetros')

        self.oHelper.SetValue('Filial de ?',filial_de)
        self.oHelper.SetValue('Filial ate ?',filial_ate)
        self.oHelper.SetValue('Data de ?',data_ini)
        self.oHelper.SetValue('Data ate ?',data_fim)
        
        self.oHelper.SetButton('Ok')

        self.oHelper.SearchBrowse("111")

        self.oHelper.SetButton('Outras Ações','Entregas')

        self.oHelper.SetButton('Sair')
       
        self.oHelper.AssertTrue()
    
    def test_GFEC001_CT007(self):         
        filial_de = 'D MG 01'
        filial_ate = 'D MG 01'
        data_ini = '01/01/2010'
        data_fim = '31/12/2020'

        self.oHelper.SetButton('Parâmetros')

        self.oHelper.SetValue('Filial de ?',filial_de)
        self.oHelper.SetValue('Filial ate ?',filial_ate)
        self.oHelper.SetValue('Data de ?',data_ini)
        self.oHelper.SetValue('Data ate ?',data_fim)
        
        self.oHelper.SetButton('Ok')

        self.oHelper.SearchBrowse("300")

        self.oHelper.SetButton('Outras Ações','Ocorrências')

        self.oHelper.SetButton('X')
       
        self.oHelper.AssertTrue()
    
    def test_GFEC001_CT008(self):         
        filial_de = 'D MG 01'
        filial_ate = 'D MG 01'
        data_ini = '01/01/2010'
        data_fim = '31/12/2020'

        self.oHelper.SetButton('Parâmetros')

        self.oHelper.SetValue('Filial de ?',filial_de)
        self.oHelper.SetValue('Filial ate ?',filial_ate)
        self.oHelper.SetValue('Data de ?',data_ini)
        self.oHelper.SetValue('Data ate ?',data_fim)
        
        self.oHelper.SetButton('Ok')

        self.oHelper.SearchBrowse("300")
       
        self.oHelper.SetButton('Outras Ações','Doc Fretes')

        self.oHelper.SetButton('X')
       
        self.oHelper.AssertTrue()
    
    def test_GFEC001_CT009(self):         
        filial_de = 'D MG 01'
        filial_ate = 'D MG 01'
        data_ini = '01/01/2010'
        data_fim = '31/12/2020'

        self.oHelper.SetButton('Parâmetros')

        self.oHelper.SetValue('Filial de ?',filial_de)
        self.oHelper.SetValue('Filial ate ?',filial_ate)
        self.oHelper.SetValue('Data de ?',data_ini)
        self.oHelper.SetValue('Data ate ?',data_fim)
        
        self.oHelper.SetButton('Ok')

        self.oHelper.SearchBrowse("300")

        self.oHelper.SetButton('Outras Ações','Pré-Faturas')

        self.oHelper.SetButton('X')
       
        self.oHelper.AssertTrue()
    
    def test_GFEC001_CT010(self):         
        filial_de = 'D MG 01'
        filial_ate = 'D MG 01'
        data_ini = '01/01/2010'
        data_fim = '31/12/2020'

        self.oHelper.SetButton('Parâmetros')

        self.oHelper.SetValue('Filial de ?',filial_de)
        self.oHelper.SetValue('Filial ate ?',filial_ate)
        self.oHelper.SetValue('Data de ?',data_ini)
        self.oHelper.SetValue('Data ate ?',data_fim)
        
        self.oHelper.SetButton('Ok')

        self.oHelper.SearchBrowse("300")

        self.oHelper.SetButton('Outras Ações','Negociações')

        self.oHelper.SetButton('Aplicar')

        self.oHelper.SetButton('X')
       
        self.oHelper.AssertTrue()
    
    def test_GFEC001_CT011(self):         
        filial_de = 'D MG 01'
        filial_ate = 'D MG 01'
        data_ini = '01/01/2010'
        data_fim = '31/12/2020'

        self.oHelper.SetButton('Parâmetros')

        self.oHelper.SetValue('Filial de ?',filial_de)
        self.oHelper.SetValue('Filial ate ?',filial_ate)
        self.oHelper.SetValue('Data de ?',data_ini)
        self.oHelper.SetValue('Data ate ?',data_fim)
        
        self.oHelper.SetButton('Ok')

        self.oHelper.SearchBrowse("300")

        self.oHelper.SetButton('Outras Ações','Estatísticas')

        self.oHelper.SetButton('Sair')
       
        self.oHelper.AssertTrue()
    
    def test_GFEC001_CT012(self):         
        filial_de = 'D MG 01'
        filial_ate = 'D MG 01'
        data_ini = '01/01/2010'
        data_fim = '31/12/2020'

        self.oHelper.SetButton('Parâmetros')

        self.oHelper.SetValue('Filial de ?',filial_de)
        self.oHelper.SetValue('Filial ate ?',filial_ate)
        self.oHelper.SetValue('Data de ?',data_ini)
        self.oHelper.SetValue('Data ate ?',data_fim)
        
        self.oHelper.SetButton('Ok')

        self.oHelper.SearchBrowse("161")

        self.oHelper.SetButton('Outras Ações','Contratos')

        self.oHelper.SetButton('X')
       
        self.oHelper.AssertTrue()
    
    def test_GFEC001_CT013(self):         
        filial_de = 'D MG 01'
        filial_ate = 'D MG 01'
        data_ini = '01/11/2018'
        data_fim = '30/11/2018'

        self.oHelper.SetButton('Parâmetros')

        self.oHelper.SetValue('Filial de ?',filial_de)
        self.oHelper.SetValue('Filial ate ?',filial_ate)
        self.oHelper.SetValue('Data de ?',data_ini)
        self.oHelper.SetValue('Data ate ?',data_fim)
        
        self.oHelper.SetButton('Ok')

        self.oHelper.SearchBrowse("300")

        self.oHelper.SetButton('Outras Ações','Despesas')          
       
        self.oHelper.AssertTrue()
    
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == "__main__":
    unittest.main()
