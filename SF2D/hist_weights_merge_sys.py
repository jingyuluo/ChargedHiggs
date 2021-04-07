import sys, os
import argparse
import math 

sys.path.append('/anaconda2/envs/fireworks/lib')
import ROOT
from ROOT import TFile, TCanvas, TH1F 
from ROOT import gStyle


fout = TFile("HT_njets_SF_sys.root", "RECREATE")

tfile_ttjj = TFile("CHiggs_Weights_ttjj_extended_HT_cuts_sys.root")
tfile_ttbb = TFile("CHiggs_Weights_ttbb_extended_HT_cuts_sys.root")
tfile_ttcc = TFile("CHiggs_Weights_ttcc_extended_HT_cuts_sys.root")
tfile_tt2b = TFile("CHiggs_Weights_tt2b_extended_HT_cuts_sys.root")
tfile_tt1b = TFile("CHiggs_Weights_tt1b_extended_HT_cuts_sys.root")
tfile_STs = TFile("CHiggs_Weights_STs_extended_HT_cuts_sys.root")
tfile_STtw = TFile("CHiggs_Weights_STtw_extended_HT_cuts_sys.root")
tfile_STt  = TFile("CHiggs_Weights_STt_extended_HT_cuts_sys.root")
tfile_WJets = TFile("CHiggs_Weights_WJets_extended_HT_cuts_sys.root")
tfile_CHM200  = TFile("CHiggs_Weights_CH-M200_extended_HT_cuts_sys.root")
tfile_CHM220  = TFile("CHiggs_Weights_CH-M220_extended_HT_cuts_sys.root")
tfile_CHM250  = TFile("CHiggs_Weights_CH-M250_extended_HT_cuts_sys.root")
tfile_CHM300  = TFile("CHiggs_Weights_CH-M300_extended_HT_cuts_sys.root")
tfile_CHM350  = TFile("CHiggs_Weights_CH-M350_extended_HT_cuts_sys.root")
tfile_CHM400  = TFile("CHiggs_Weights_CH-M400_extended_HT_cuts_sys.root")
tfile_CHM500  = TFile("CHiggs_Weights_CH-M500_extended_HT_cuts_sys.root")
tfile_CHM600  = TFile("CHiggs_Weights_CH-M600_extended_HT_cuts_sys.root")
tfile_CHM700  =  TFile("CHiggs_Weights_CH-M700_extended_HT_cuts_sys.root")
tfile_CHM800  = TFile("CHiggs_Weights_CH-M800_extended_HT_cuts_sys.root")
tfile_CHM1000 = TFile("CHiggs_Weights_CH-M1000_extended_HT_cuts_sys.root")
tfile_CHM1250 = TFile("CHiggs_Weights_CH-M1250_extended_HT_cuts_sys.root")
tfile_CHM1500 = TFile("CHiggs_Weights_CH-M1500_extended_HT_cuts_sys.root")
tfile_CHM1750 = TFile("CHiggs_Weights_CH-M1750_extended_HT_cuts_sys.root")
tfile_CHM2000 = TFile("CHiggs_Weights_CH-M2000_extended_HT_cuts_sys.root")
tfile_CHM2500 = TFile("CHiggs_Weights_CH-M2500_extended_HT_cuts_sys.root")
tfile_CHM3000 = TFile("CHiggs_Weights_CH-M3000_extended_HT_cuts_sys.root")


sys_postfix = ["", "_HFup", "_HFdn", "_LFup", "_LFdn", "_jesup", "_jesdn", "_hfstats1up", "_hfstats1dn", "_hfstats2up", "_hfstats2dn", "_cferr1up", 
        "_cferr1dn", "_cferr2up", "_cferr2dn", "_lfstats1up", "_lfstats1dn", "_lfstats2up", "_lfstats2dn"]

hscale_ttjj = {}
hscale_ttbb = {}
hscale_ttcc = {}
hscale_tt2b = {} 
hscale_tt1b = {}
hscale_STs  = {}
hscale_STtw = {}
hscale_STt  = {}
hscale_WJets= {}
hscale_CHM200  = {} 
hscale_CHM220  = {}
hscale_CHM250  = {}
hscale_CHM300  = {}
hscale_CHM350  = {}
hscale_CHM400  = {}
hscale_CHM500  = {}
hscale_CHM600  = {}
hscale_CHM700  = {}
hscale_CHM800  = {}
hscale_CHM1000 = {}
hscale_CHM1250 = {}
hscale_CHM1500 = {}
hscale_CHM1750 = {}
hscale_CHM2000 = {}
hscale_CHM2500 = {}
hscale_CHM3000 = {}


for sys in sys_postfix:

    hscale_ttjj[sys] = tfile_ttjj.Get("h2D_scale"+sys).Clone()
    hscale_ttbb[sys] = tfile_ttbb.Get("h2D_scale"+sys).Clone()
    hscale_ttcc[sys] = tfile_ttcc.Get("h2D_scale"+sys).Clone()
    hscale_tt2b[sys] = tfile_tt2b.Get("h2D_scale"+sys).Clone()
    hscale_tt1b[sys] = tfile_tt1b.Get("h2D_scale"+sys).Clone()
    hscale_STs[sys]  = tfile_STs.Get("h2D_scale"+sys).Clone()
    hscale_STtw[sys] = tfile_STtw.Get("h2D_scale"+sys).Clone()
    hscale_STt[sys]  = tfile_STt.Get("h2D_scale"+sys).Clone()
    hscale_WJets[sys] = tfile_WJets.Get("h2D_scale"+sys).Clone()
    
    hscale_CHM200[sys]  = tfile_CHM200.Get("h2D_scale"+sys).Clone()  
    hscale_CHM220[sys]  = tfile_CHM220.Get("h2D_scale"+sys).Clone() 
    hscale_CHM250[sys]  = tfile_CHM250.Get("h2D_scale"+sys).Clone() 
    hscale_CHM300[sys]  = tfile_CHM300.Get("h2D_scale"+sys).Clone() 
    hscale_CHM350[sys]  = tfile_CHM350.Get("h2D_scale"+sys).Clone() 
    hscale_CHM400[sys]  = tfile_CHM400.Get("h2D_scale"+sys).Clone() 
    hscale_CHM500[sys]  = tfile_CHM500.Get("h2D_scale"+sys).Clone() 
    hscale_CHM600[sys]  = tfile_CHM600.Get("h2D_scale"+sys).Clone() 
    hscale_CHM700[sys]  = tfile_CHM700.Get("h2D_scale"+sys).Clone() 
    hscale_CHM800[sys]  = tfile_CHM800.Get("h2D_scale"+sys).Clone() 
    hscale_CHM1000[sys] = tfile_CHM1000.Get("h2D_scale"+sys).Clone() 
    hscale_CHM1250[sys] = tfile_CHM1250.Get("h2D_scale"+sys).Clone()
    hscale_CHM1500[sys] = tfile_CHM1500.Get("h2D_scale"+sys).Clone()
    hscale_CHM1750[sys] = tfile_CHM1750.Get("h2D_scale"+sys).Clone()
    hscale_CHM2000[sys] = tfile_CHM2000.Get("h2D_scale"+sys).Clone()
    hscale_CHM2500[sys] = tfile_CHM2500.Get("h2D_scale"+sys).Clone()
    hscale_CHM3000[sys] = tfile_CHM3000.Get("h2D_scale"+sys).Clone()




    fout.WriteTObject(hscale_ttjj[sys], "hscale_ttjj"+sys)
    fout.WriteTObject(hscale_ttbb[sys], "hscale_ttbb"+sys)
    fout.WriteTObject(hscale_ttcc[sys], "hscale_ttcc"+sys)
    fout.WriteTObject(hscale_tt2b[sys], "hscale_tt2b"+sys)
    fout.WriteTObject(hscale_tt1b[sys], "hscale_tt1b"+sys)
    fout.WriteTObject(hscale_STs[sys], "hscale_STs"+sys)
    fout.WriteTObject(hscale_STtw[sys], "hscale_STtw"+sys)
    fout.WriteTObject(hscale_STt[sys], "hscale_STt"+sys)
    fout.WriteTObject(hscale_WJets[sys], "hscale_WJets"+sys)
    
    fout.WriteTObject( hscale_CHM200[sys] ,    "hscale_CHM200"+sys)  
    fout.WriteTObject( hscale_CHM220[sys] ,    "hscale_CHM220"+sys)  
    fout.WriteTObject( hscale_CHM250[sys] ,    "hscale_CHM250"+sys)  
    fout.WriteTObject( hscale_CHM300[sys] ,    "hscale_CHM300"+sys)  
    fout.WriteTObject( hscale_CHM350[sys] ,    "hscale_CHM350"+sys)  
    fout.WriteTObject( hscale_CHM400[sys] ,    "hscale_CHM400"+sys)  
    fout.WriteTObject( hscale_CHM500[sys] ,    "hscale_CHM500"+sys)  
    fout.WriteTObject( hscale_CHM600[sys] ,    "hscale_CHM600"+sys)  
    fout.WriteTObject( hscale_CHM700[sys] ,    "hscale_CHM700"+sys)  
    fout.WriteTObject( hscale_CHM800[sys] ,    "hscale_CHM800"+sys)  
    fout.WriteTObject( hscale_CHM1000[sys] ,    "hscale_CHM1000"+sys) 
    fout.WriteTObject( hscale_CHM1250[sys] ,    "hscale_CHM1250"+sys) 
    fout.WriteTObject( hscale_CHM1500[sys] ,    "hscale_CHM1500"+sys) 
    fout.WriteTObject( hscale_CHM1750[sys] ,    "hscale_CHM1750"+sys) 
    fout.WriteTObject( hscale_CHM2000[sys] ,    "hscale_CHM2000"+sys) 
    fout.WriteTObject( hscale_CHM2500[sys] ,    "hscale_CHM2500"+sys) 
    fout.WriteTObject( hscale_CHM3000[sys] ,    "hscale_CHM3000"+sys) 



fout.Close()
