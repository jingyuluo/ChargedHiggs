import ROOT
import sys
import numpy
import argparse
import array
from ROOT import TFile, TTree

parser = argparse.ArgumentParser(description="compute the renormalization factors for charged Higgs analysis")

parser.add_argument("-f", "--file", default="", help="The path to the analysis tree")
parser.add_argument("-l", "--label", default="", help="The name of the output file")

args = parser.parse_args()

filename = args.file

tfile = TFile.Open(filename)

fout = ROOT.TFile("Fourtops_Weights_"+args.label+"_extended_HT_cuts.root", "RECREATE")


h2D_origin = ROOT.TH2F("h2D_origin", "h2D_origin", 6, 4, 10, 40, 150, 4000)
h2D_origin.Sumw2()
h2D_weight_dcsv = ROOT.TH2F("h2D_weight_dcsv", "h2D_weight_dcsv", 6, 4, 10, 40, 150, 4000)
h2D_weight_dcsv.Sumw2()

h2D_weight_djet = ROOT.TH2F("h2D_weight_djet", "h2D_weight_djet", 6, 4, 10, 40, 150, 4000)
h2D_weight_djet.Sumw2()


ttree = tfile.Get("ljmet")


ttree.SetBranchStatus("*", 0)
ttree.SetBranchStatus("NJets_JetSubCalc*", 1)
ttree.SetBranchStatus("theJetPt_JetSubCalc_PtOrdered*", 1)
ttree.SetBranchStatus("AK4HT*", 1)
ttree.SetBranchStatus("btagCSVWeight*", 1)
ttree.SetBranchStatus("btagDeepJetWeight*", 1)
ttree.SetBranchStatus("leptonPt_MultiLepCalc*", 1)
ttree.SetBranchStatus("isElectron*", 1)
ttree.SetBranchStatus("isMuon*", 1)
ttree.SetBranchStatus("corr_met_MultiLepCalc*", 1)
ttree.SetBranchStatus("MCPastTrigger*", 1)

nevents = ttree.GetEntries()

for iev in range(nevents):
    if iev%1000==1:
        print(iev)
    ttree.GetEntry(iev)
    njet = ttree.NJets_JetSubCalc
    if not ((ttree.leptonPt_MultiLepCalc > 35 and ttree.isElectron) or (ttree.leptonPt_MultiLepCalc > 30 and ttree.isMuon)): continue
    if not (ttree.corr_met_MultiLepCalc > 30): continue
    if not (ttree.MCPastTrigger): continue 
    HT = ttree.AK4HT
    if njet>9: njet=9
    #for ijet in range(njet):
    #    if ttree.theJetPt_JetSubCalc_PtOrdered.at(ijet)>120:
    #        n_fastjet+=1
    #    elif (ttree.theJetPt_JetSubCalc_PtOrdered.at(ijet)<=120 and ttree.theJetPt_JetSubCalc_PtOrdered.at(ijet)>40):
    #        n_slowjet+=1

    #if n_fastjet>5: n_fastjet=5
    #if n_slowjet>5: n_slowjet=5
    h2D_origin.Fill(njet, HT)
    h2D_weight_dcsv.Fill(njet, HT, ttree.btagCSVWeight)
    h2D_weight_djet.Fill(njet, HT, ttree.btagDeepJetWeight)

h2D_scale_dcsv = h2D_origin.Clone()
h2D_scale_dcsv.SetTitle("h2D_scale_dcsv")
h2D_scale_dcsv.Divide(h2D_weight_dcsv)
h2D_scale_djet = h2D_origin.Clone()
h2D_scale_djet.SetTitle("h2D_scale_dcsv")
h2D_scale_djet.Divide(h2D_weight_djet)
fout.WriteTObject(h2D_origin, "h2D_origin")
fout.WriteTObject(h2D_weight_dcsv, "h2D_weight_dcsv")
fout.WriteTObject(h2D_scale_dcsv, "h2D_scale_dcsv")
fout.WriteTObject(h2D_weight_djet, "h2D_weight_djet")
fout.WriteTObject(h2D_scale_djet, "h2D_scale_djet")
fout.Close()
