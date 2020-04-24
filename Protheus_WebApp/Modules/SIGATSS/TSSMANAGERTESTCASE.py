import unittest
from tir import Webapp

class TSSMANAGER(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.oHelper = Webapp()
        inst.oHelper.SetTIRConfig("User", "teste")
        inst.oHelper.SetTIRConfig("Password", "1234")
        inst.oHelper.SetupTSS("TSSMANAGER", "SPED")

    def test_TSSMANAGER01_CT001(self):
        self.oHelper.SetButton("Inicial")
        self.oHelper.SetButton("NF-e")
        self.oHelper.SetButton("NFS-e")
        self.oHelper.SetButton("EDI")
        self.oHelper.SetButton("Sair")
        self.oHelper.SetButton("Sim")
        self.oHelper.AssertTrue()

    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main() 