from tir import Webapp
import unittest


class GTPA106(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGAGTP', '12/08/2020', 'T1', 'D MG 01 ')
        inst.oHelper.Program('GTPA106')

     # Efetua a alocação de documentos (caso padrão)
    print('CT001 - Alocação de documentos (caso padrão)')

    def test_GTPA106_CT001(self):
        self.oHelper.SetButton('Incluir')
        self.oHelper.SetBranch('D MG')
        self.oHelper.SetValue('GQH_AGENCI', 'AGREMG')
        self.oHelper.SetValue('GQH_TIPO', 'TP9505')
        self.oHelper.SetValue('GQH_COMPLE', '1')
        self.oHelper.SetValue('GQH_TIPPAS', '1')
        self.oHelper.SetValue('GQH_SERIE', 'AA1')
        self.oHelper.SetValue('GQH_SUBSER', '3')
        self.oHelper.SetValue('GQH_NUMCOM', '3')
        self.oHelper.SetValue('GQH_NUMINI', '000001')
        self.oHelper.SetValue('GQH_NUMFIM', '000010')
        self.oHelper.SetValue('GQH_FUNPAS', '000001')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SearchBrowse("D MG    GTPLOT", "Filial+lote Remessa")
        self.oHelper.SetButton("Outras Ações", "Transferir")
        self.oHelper.SetButton('OK')
        self.oHelper.SetValue('Num.Inicial', '000009')
        self.oHelper.SetValue('Num.Final', '000009')
        self.oHelper.SetValue('Colaborador', '000005')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SearchBrowse("D MG    ALTES7", "Filial+lote Remessa")
        self.oHelper.SetButton("Outras Ações", "Devolução")
        self.oHelper.SetButton('OK')
        self.oHelper.SetValue('Num.Inicial', '000010')
        self.oHelper.SetValue('Num.Final', '000010')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.SearchBrowse("D MG    GTPLOT", "Filial+lote Remessa")
        self.oHelper.SetButton("Outras Ações", "Baixa")
        self.oHelper.SetButton('OK')
        self.oHelper.SetValue('Num.Inicial', '000008')
        self.oHelper.SetValue('Num.Final', '000008')
        self.oHelper.SetButton('Confirmar')
        self.oHelper.SetButton('Fechar')
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()


if __name__ == '__main__':
    unittest.main()
