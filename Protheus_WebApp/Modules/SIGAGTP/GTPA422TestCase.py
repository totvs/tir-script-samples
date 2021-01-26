from tir import Webapp
import unittest
import time


class GTPA422(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAGTP', '27/08/2020', 'T1', 'D MG 01 ', '88')
        inst.oHelper.Program('GTPA422')

    def test_GTPA422_CT001(self):
        print("test_GTPA422_CT001 - Visualizar")
        self.oHelper.SearchBrowse('D MG    000003', key=1, index=True)
        self.oHelper.SetButton('Visualizar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.AssertTrue()

    def test_GTPA422_CT002(self):
        print("test_GTPA422_CT002 - Alterar")
        self.oHelper.SearchBrowse('D MG    000003', key=1, index=True)
        self.oHelper.SetButton('Alterar')
        self.oHelper.SetValue('Motivo', 'Alteração Tir')
        
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.AssertTrue()       

   
    def test_GTPA422_CT003(self):
        print("test_GTPA422_CT003 - Excluir")
        self.oHelper.SearchBrowse('D MG    000003', key=1, index=True)
        self.oHelper.SetButton('Outras Ações', 'Excluir')
        self.oHelper.SetButton('Confirmar')
        time.sleep(2)
        self.oHelper.SetButton('Fechar')
        self.oHelper.AssertTrue()

    def test_GTPA422_CT004(self):
        print("test_GTPA422_CT004 - Incluir")
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetBranch('D MG')

        self.oHelper.SetValue('Tipo', '000001')
        self.oHelper.SetValue('Agência', 'GTPVAM')
        self.oHelper.F3(field='Serie')
        self.oHelper.SearchBrowse('000046', key=1, index=True)
        self.oHelper.SetButton('OK')
        
        self.oHelper.SetValue('Seq. Lote', '000012')
        self.oHelper.SetValue('Dt. Entrega', '31/08/2020')
        self.oHelper.SetValue('Emitente' , '000001')
        self.oHelper.SetValue('Cod.Acertado' , '000009')
        
        self.oHelper.SetButton('Outras Ações', 'Carrega Bilhete')    
        self.oHelper.SetValue('Dt. Emissão de: ?' , '27/08/2020')
        self.oHelper.SetValue('Dt Emissão até: ?' , '31/08/2020')
        self.oHelper.SetValue('Tipo de Documento: ?' , '000001')
        self.oHelper.SetValue('Série: ?' , '422')
        self.oHelper.SetValue('Sub Série: ?' , '111')
        self.oHelper.SetValue('Num. Complemento: ?' , '111')
        self.oHelper.SetValue('Numero Inicial: ?' , '000001')
        self.oHelper.SetValue('Numero Final: ?' , '000100')

        self.oHelper.SetButton('OK')
        time.sleep(3)

        self.oHelper.SetButton('Confirmar')

        self.oHelper.AssertTrue()


    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
