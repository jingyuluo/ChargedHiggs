import sys, os
import argparse
import math 

sys.path.append('/anaconda2/envs/fireworks/lib')
import ROOT
from ROOT import TFile, TCanvas, TH1F 
from ROOT import gStyle


fout = TFile("HT_njets_SF.root", "RECREATE")

tfile_ttjj = TFile("CHiggs_Weights_ttjj_extended_HT.root")
tfile_ttbb = TFile("CHiggs_Weights_ttbb_extended_HT.root")
tfile_ttcc = TFile("CHiggs_Weights_ttcc_extended_HT.root")
tfile_tt2b = TFile("CHiggs_Weights_tt2b_extended_HT.root")
tfile_tt1b = TFile("CHiggs_Weights_tt1b_extended_HT.root")
tfile_STs = TFile("CHiggs_Weights_ST_s_extended_HT.root")
tfile_STtw = TFile("CHiggs_Weights_ST_tW_extended_HT.root")
tfile_STt  = TFile("CHiggs_Weights_ST_tW_extended_HT.root")
tfile_WJets = TFile("CHiggs_Weights_WJets_extended_HT.root")

hscale_ttjj = tfile_ttjj.Get("h2D_scale").Clone()
hscale_ttbb = tfile_ttbb.Get("h2D_scale").Clone()
hscale_ttcc = tfile_ttcc.Get("h2D_scale").Clone()
hscale_tt2b = tfile_tt2b.Get("h2D_scale").Clone()
hscale_tt1b = tfile_tt1b.Get("h2D_scale").Clone()
hscale_STs = tfile_STs.Get("h2D_scale").Clone()
hscale_STtw = tfile_STtw.Get("h2D_scale").Clone()
hscale_STt = tfile_STt.Get("h2D_scale").Clone()
hscale_WJets = tfile_WJets.Get("h2D_scale").Clone()

fout.WriteTObject(hscale_ttjj, "hscale_ttjj")
fout.WriteTObject(hscale_ttbb, "hscale_ttbb")
fout.WriteTObject(hscale_ttcc, "hscale_ttcc")
fout.WriteTObject(hscale_tt2b, "hscale_tt2b")
fout.WriteTObject(hscale_tt1b, "hscale_tt1b")
fout.WriteTObject(hscale_STs, "hscale_STs")
fout.WriteTObject(hscale_STtw, "hscale_STtw")
fout.WriteTObject(hscale_STt, "hscale_STt")
fout.WriteTObject(hscale_WJets, "hscale_WJets")


fout.Close()
