from tir import Webapp
import unittest

class GFEA055(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup("SIGAGFE", "02/12/2020", "T1", "D MG 01", "78")
        inst.oHelper.Program("GFEA055")

    def test_GFEA055_CT001(self):     

        self.oHelper.SetButton('Gerar')   

        self.oHelper.SetButton('OK') 

        self.oHelper.SetValue('Tipo de Geracao ?'        ,'Geração')
        self.oHelper.SetValue('Filial de ?'              ,'D MG 01')
        self.oHelper.SetValue('Filial ate ?'             ,'D MG 01')
        self.oHelper.SetValue('Transportador de ?'       ,'500')
        self.oHelper.SetValue('Transportador ate ?'      ,'500')
        self.oHelper.SetValue('Tipo Operacao de ?'       ,'')
        self.oHelper.SetValue('Tipo Operacao ate ?'      ,'ZZZZZZZZZZ')
        self.oHelper.SetValue('Classific Frete de ?'     ,'')
        self.oHelper.SetValue('Classific Frete ate ?'    ,'ZZZZ')
        self.oHelper.SetValue('Data Calculo de ?'        ,'02/12/2020')
        self.oHelper.SetValue('Data Calculo ate ?'       ,'02/12/2020')
        self.oHelper.SetValue('Data Limite Ent/Sai ?'    ,'02/12/2020')
        self.oHelper.SetValue('Romaneio de ?'            ,'00000537')
        self.oHelper.SetValue('Romaneio ate ?'           ,'00000537')
        self.oHelper.SetValue('Tipo Normal ?'            ,'Sim')
        self.oHelper.SetValue('Tipo Compl Valor ?'       ,'Sim')
        self.oHelper.SetValue('Tipo Compl Imposto ?'     ,'Sim')
        self.oHelper.SetValue('Tipo Reentrega ?'         ,'Sim')
        self.oHelper.SetValue('Tipo Devolucao ?'         ,'Sim')
        self.oHelper.SetValue('Tipo Redespacho ?'        ,'Sim')
        self.oHelper.SetValue('Tipo Servico ?'           ,'Sim')
        self.oHelper.SetValue('Gerar log ?'              ,'Sim')
        self.oHelper.SetValue('Tipo Serviço de ?'        ,'')
        self.oHelper.SetValue('Tipo Serviço ate ?'       ,'ZZZZZZZZZZZZZZZZZZZZ')
        self.oHelper.SetValue('Exceto Transportadores ?' ,'')

        self.oHelper.SetButton('OK')

        self.oHelper.SetButton('OK')  

        self.oHelper.SetButton('Visualizar')   

        self.oHelper.SetButton('Fechar')       

        self.oHelper.SetButton('Alterar') 

        self.oHelper.SetButton('Cancelar')  

        self.oHelper.SetButton('Sim')   

        self.oHelper.SetButton('Outras Ações','Excluir')   

        self.oHelper.SetButton('Confirmar')   

        self.oHelper.SetButton('Fechar')  

        self.oHelper.AssertTrue()

    def test_GFEA055_CT002(self):     

        self.oHelper.SetButton('Gerar')   

        self.oHelper.SetButton('OK') 

        self.oHelper.SetValue('Tipo de Geracao ?'        ,'Simulacao')
        self.oHelper.SetValue('Filial de ?'              ,'D MG 01')
        self.oHelper.SetValue('Filial ate ?'             ,'D MG 01')
        self.oHelper.SetValue('Transportador de ?'       ,'500')
        self.oHelper.SetValue('Transportador ate ?'      ,'500')
        self.oHelper.SetValue('Tipo Operacao de ?'       ,'')
        self.oHelper.SetValue('Tipo Operacao ate ?'      ,'ZZZZZZZZZZ')
        self.oHelper.SetValue('Classific Frete de ?'     ,'')
        self.oHelper.SetValue('Classific Frete ate ?'    ,'ZZZZ')
        self.oHelper.SetValue('Data Calculo de ?'        ,'02/12/2020')
        self.oHelper.SetValue('Data Calculo ate ?'       ,'02/12/2020')
        self.oHelper.SetValue('Data Limite Ent/Sai ?'    ,'02/12/2020')
        self.oHelper.SetValue('Romaneio de ?'            ,'00000537')
        self.oHelper.SetValue('Romaneio ate ?'           ,'00000537')
        self.oHelper.SetValue('Tipo Normal ?'            ,'Sim')
        self.oHelper.SetValue('Tipo Compl Valor ?'       ,'Sim')
        self.oHelper.SetValue('Tipo Compl Imposto ?'     ,'Sim')
        self.oHelper.SetValue('Tipo Reentrega ?'         ,'Sim')
        self.oHelper.SetValue('Tipo Devolucao ?'         ,'Sim')
        self.oHelper.SetValue('Tipo Redespacho ?'        ,'Sim')
        self.oHelper.SetValue('Tipo Servico ?'           ,'Sim')
        self.oHelper.SetValue('Gerar log ?'              ,'Sim')
        self.oHelper.SetValue('Tipo Serviço de ?'        ,'')
        self.oHelper.SetValue('Tipo Serviço ate ?'       ,'ZZZZZZZZZZZZZZZZZZZZ')
        self.oHelper.SetValue('Exceto Transportadores ?' ,'')

        self.oHelper.SetButton('OK')

        self.oHelper.SetButton('Salvar')   

        self.oHelper.SetButton('Cancelar')       

        self.oHelper.AssertTrue()
          
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == "__main__":
    unittest.main()