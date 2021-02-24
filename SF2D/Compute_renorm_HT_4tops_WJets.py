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


basedir = '/eos/uscms/store/group/lpcljm/FWLJMET102X_1lep2017_Oct2019_4t_02162021_step1hadds/nominal/'

filenames = {'200to400':'WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root', 
             '400to600':'WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root',
             '600to800':'WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root',
             '800to1200':'WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root',
             '1200to2500_1': 'WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8_1_hadd.root', 
             '1200to2500_2': 'WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8_2_hadd.root',
             '1200to2500_3': 'WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8_3_hadd.root',
             '2500toInf_1': 'WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8_1_hadd.root', 
             '2500toInf_2': 'WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8_2_hadd.root',
             '2500toInf_3': 'WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8_3_hadd.root',
             '2500toInf_4': 'WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8_4_hadd.root'
             }


weights = {'200to400':359.7*1.21/21192211.0*0.978569, 
           '400to600':48.91*1.21/14189363.0*0.928054,
           '600to800':12.05*1.21/21330497.0*0.856705,
           '800to1200':5.501*1.21/3089712.0*0.757463,
           '1200to2500_1':1.329*1.21/19950628.0*0.608292, 
           '1200to2500_2':1.329*1.21/19950628.0*0.608292, 
           '1200to2500_3':1.329*1.21/19950628.0*0.608292,
           '2500toInf_1':0.03216*1.21/20629585.0*0.454246,
           '2500toInf_2':0.03216*1.21/20629585.0*0.454246,
           '2500toInf_3':0.03216*1.21/20629585.0*0.454246,
           '2500toInf_4':0.03216*1.21/20629585.0*0.454246}
           
           

HT_bins = filenames.keys()



fout = ROOT.TFile("Fourtops_Weights_"+args.label+"_extended_HT_cuts.root", "RECREATE")


h2D_origin = ROOT.TH2F("h2D_origin", "h2D_origin", 6, 4, 10, 40, 150, 4000)
h2D_origin.Sumw2()
h2D_weight_dcsv = ROOT.TH2F("h2D_weight_dcsv", "h2D_weight_dcsv", 6, 4, 10, 40, 150, 4000)
h2D_weight_dcsv.Sumw2()

h2D_weight_djet = ROOT.TH2F("h2D_weight_djet", "h2D_weight_djet", 6, 4, 10, 40, 150, 4000)
h2D_weight_djet.Sumw2()

for HTbin in HT_bins:
    print "processing:", HTbin
    tfile = TFile.Open(basedir+filenames[HTbin])
    
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
        h2D_origin.Fill(njet, HT, weights[HTbin])
        h2D_weight_dcsv.Fill(njet, HT, ttree.btagCSVWeight*weights[HTbin])
        h2D_weight_djet.Fill(njet, HT, ttree.btagDeepJetWeight*weights[HTbin])
    tfile.Close()

h2D_scale_dcsv = h2D_origin.Clone()
h2D_scale_dcsv.SetTitle("h2D_scale_dcsv")
h2D_scale_dcsv.Divide(h2D_weight_dcsv)
h2D_scale_djet = h2D_origin.Clone()
h2D_scale_djet.SetTitle("h2D_scale_djet")
h2D_scale_djet.Divide(h2D_weight_djet)
fout.WriteTObject(h2D_origin, "h2D_origin")
fout.WriteTObject(h2D_weight_dcsv, "h2D_weight_dcsv")
fout.WriteTObject(h2D_scale_dcsv, "h2D_scale_dcsv")
fout.WriteTObject(h2D_weight_djet, "h2D_weight_djet")
fout.WriteTObject(h2D_scale_djet, "h2D_scale_djet")
fout.Close()
