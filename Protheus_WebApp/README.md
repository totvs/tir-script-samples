# tir-script-samples

Script samples of Totvs Interface Robot (TIR) module.

Main repository: [TIR](https://github.com/totvs/tir)

Feel free to collaborate with us and share ideas, exemples and concepts

## Contents

### Protheus WebApp Samples

- **Examples**: The methods below are linked with script models.

    [AddParameter](Modules/SIGAACD/ACDA010TESTCASE.py),
    [CheckHelp](Modules/SIGACTB/CTBA011TESTCASE.py),
    [CheckResult](Modules/SIGAAGR/OGC010TESTCASE.py),
    [CheckView](Modules/SIGACTB/CTBA200TESTCASE.py),
    [ClickBox](Modules/SIGAATF/ATFA110TESTCASE.py),
    [ClickCheckBox](Modules/SIGAEST/MATA180TESTCASE.py),
    [ClickFolder](Modules/SIGAPCO/PCOA030TESTCASE.py),
    [ClickGridCell](Modules/SIGAFIN/FINA340TESTCASE.py),
    [ClickLabel](Modules/SIGABI/BIXLogTESTCASE.py),
    [ClickMenuPopUpItem](Modules/SIGAEST/MATC710TESTCASE.py),
    [ClickTree](Modules/SIGAGCP/GCPA200TESTCASE.py),
    [GetValue](Modules/SIGACTB/CTBA011TESTCASE.py),
    [LoadGrid](Modules/SIGAEST/MATA105TESTCASE.py),
    [Program](Modules/SIGATMS/TMSA200TESTCASE.py),
    [RestoreParameters](Modules/SIGAJURI/JURA094TESTCASE.py),
    [ScrollGrid](Modules/SIGAGTP/GTPA003TESTCASE.py),
    [SearchBrowse](Modules/SIGATMS/TMSA500TESTCASE.py),
    [SetBranch](Modules/SIGATAF/TAFA400TESTCASE.py),
    [SetButton](Modules/SIGACTB/CTBC403TESTCASE.py),
    [SetFilePath](Modules/SIGAJURI/ANEXOSTESTCASE.py),
    [SetFocus](Modules/SIGAEST/MATA240TESTCASE.py),
    [SetKey](Modules/SIGAEST/MATA230TESTCASE.py),
    [SetLateralMenu](Modules/SIGABI/BIXProfileTESTCASE.py),
    [SetParameters](Modules/SIGAPCO/PCOC360TESTCASE.py),
    [SetValue](Modules/SIGACTB/CTBR200TESTCASE.py),
    [Setup](Modules/SIGATMS/TMSA500TESTCASE.py),
    [SetupTSS](Modules/SIGATSS/TSSMANAGERTESTCASE.py),
    [TearDown](Modules/SIGAPCP/MATA750TESTCASE.py),
    [WaitFieldValue](Modules/SIGAJURI/JURA106TESTCASE.py),
    [WaitHide](Modules/SIGAJURI/JURA100TESTCASE.py),
    [WaitProcessing](Modules/SIGAFIN/FINA910TESTCASE.py),
    [WaitShow](Modules/SIGAACD/ACDA010TESTCASE.py)

- **More Examples**: More methods with script models.

    [ChangeEnvironment]
    [ClickGridHeader]
    [ClickIcon]

    [ClickImage]:

    def test_TMSA040_CT043(self):
		self.oHelper.Setup('SIGATMS','19/06/2019','T1','M SP 03 ','43')
		self.oHelper.Program('TMSA040') 
		self.oHelper.SearchBrowse('M SP 01 M SP 01 000003')
		self.oHelper.SetButton('Outras Ações', 'Previsao Entrega')
		self.oHelper.SetValue('cTipTrans', '1', name_attr=True)
		self.oHelper.SetValue('cCliDev', 'TMS001', name_attr=True)
		self.oHelper.SetValue('cLojDev', '01', name_attr=True)
		self.oHelper.SetValue('cCodOri', 'Q50308', name_attr=True)
		self.oHelper.SetValue('cCodDes', 'O09102', name_attr=True)
		self.oHelper.ClickImage('s4wb064n')
		self.oHelper.AssertTrue()

    [ClickListBox]
    [Finish]
    [GetText]
    [GridTree]
    [LogOff]
    [MessageBoxClick]
    [SetTabEDAPP]