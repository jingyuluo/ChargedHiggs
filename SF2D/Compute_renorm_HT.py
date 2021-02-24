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

fout = ROOT.TFile("CHiggs_Weights_"+args.label+"_extended_HT_cuts.root", "RECREATE")


h2D_origin = ROOT.TH2F("h2D_origin", "h2D_origin", 3, 4, 7, 40, 150, 4000)
h2D_origin.Sumw2()
h2D_weight = ROOT.TH2F("h2D_weight", "h2D_weight", 3, 4, 7, 40, 150, 4000)
h2D_weight.Sumw2()



ttree = tfile.Get("ljmet")


ttree.SetBranchStatus("*", 0)
ttree.SetBranchStatus("NJets_JetSubCalc*", 1)
ttree.SetBranchStatus("theJetPt_JetSubCalc_PtOrdered*", 1)
ttree.SetBranchStatus("AK4HT*", 1)
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
    if njet>6: njet=6
    #for ijet in range(njet):
    #    if ttree.theJetPt_JetSubCalc_PtOrdered.at(ijet)>120:
    #        n_fastjet+=1
    #    elif (ttree.theJetPt_JetSubCalc_PtOrdered.at(ijet)<=120 and ttree.theJetPt_JetSubCalc_PtOrdered.at(ijet)>40):
    #        n_slowjet+=1

    #if n_fastjet>5: n_fastjet=5
    #if n_slowjet>5: n_slowjet=5
    h2D_origin.Fill(njet, HT)
    h2D_weight.Fill(njet, HT, ttree.btagDeepJetWeight)

h2D_scale = h2D_origin.Clone()
h2D_scale.SetTitle("h2D_scale")
h2D_scale.Divide(h2D_weight)
fout.WriteTObject(h2D_origin, "h2D_origin")
fout.WriteTObject(h2D_weight, "h2D_weight")
fout.WriteTObject(h2D_scale, "h2D_scale")
fout.Close()
