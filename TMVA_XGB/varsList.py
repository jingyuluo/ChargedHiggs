#!/usr/bin/env python

#input variables
varList = {}

#inputDir = '/isilon/hadoop/store/user/mhadley/TTTT/LJMet94X_1lepTT_022719_step2_saraBDay/nominal/'
inputDir = '/mnt/hadoop/store/user/mlukasik/chiggs2017/step2/nominal/'
inputDir = 'root://cmseos.fnal.gov//store/user/mlukasik/CHiggs2017/step2s/'

bkg = [
### 2017
#'TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8_tt1b_hadd.root',
# 'TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8_tt2b_hadd.root',
# 'TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8_ttbb_hadd.root',
# 'TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8_ttcc_hadd.root',
# 'TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8_ttjj_hadd.root',
# 'TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8_tt1b_hadd.root',
# 'TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8_tt2b_hadd.root',
# 'TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8_ttbb_hadd.root',
# 'TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8_ttcc_hadd.root',
# 'TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8_ttjj_hadd.root',
# 'TTToSemiLepton_HT500Njet9_TuneCP5_PSweights_13TeV-powheg-pythia8_tt1b_hadd.root',
# 'TTToSemiLepton_HT500Njet9_TuneCP5_PSweights_13TeV-powheg-pythia8_tt2b_hadd.root',
# 'TTToSemiLepton_HT500Njet9_TuneCP5_PSweights_13TeV-powheg-pythia8_ttbb_hadd.root',
# 'TTToSemiLepton_HT500Njet9_TuneCP5_PSweights_13TeV-powheg-pythia8_ttcc_hadd.root',
# 'TTToSemiLepton_HT500Njet9_TuneCP5_PSweights_13TeV-powheg-pythia8_ttjj_hadd.root',
'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_HT0Njet0_tt1b_hadd.root',
 'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_HT0Njet0_tt2b_hadd.root',
 'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_HT0Njet0_ttbb_hadd.root',
 'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_HT0Njet0_ttcc_hadd.root',
 'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_HT0Njet0_ttjj_1_hadd.root',
 'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_HT0Njet0_ttjj_2_hadd.root',
 'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_HT0Njet0_ttjj_3_hadd.root',
 'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_HT0Njet0_ttjj_4_hadd.root',
 'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_HT0Njet0_ttjj_5_hadd.root',
 'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_HT500Njet9_tt1b_hadd.root',
 'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_HT500Njet9_tt2b_hadd.root',
 'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_HT500Njet9_ttbb_hadd.root',
 'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_HT500Njet9_ttcc_hadd.root',
 'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_HT500Njet9_ttjj_hadd.root',




# 'DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8_hadd.root',
# 'QCD_HT1000to1500_TuneCP5_13TeV-madgraph-pythia8_hadd.root',
# 'QCD_HT1500to2000_TuneCP5_13TeV-madgraph-pythia8_hadd.root',
# 'QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8_hadd.root',
# 'QCD_HT300to500_TuneCP5_13TeV-madgraph-pythia8_hadd.root',
# 'QCD_HT500to700_TuneCP5_13TeV-madgraph-pythia8_hadd.root',
# 'QCD_HT700to1000_TuneCP5_13TeV-madgraph-pythia8_hadd.root',
# 'ST_s-channel_4f_leptonDecays_TuneCP5_PSweights_13TeV-amcatnlo-pythia8_hadd.root',
# 'ST_t-channel_antitop_5f_TuneCP5_PSweights_13TeV-powheg-madspin-pythia8_vtd_vts_prod_hadd.root',
# 'ST_t-channel_top_5f_TuneCP5_PSweights_13TeV-powheg-madspin-pythia8_vtd_vts_prod_hadd.root',
# 'ST_tW_antitop_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8_hadd.root',
# 'ST_tW_top_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8_hadd.root',
# 'TT_Mtt-1000toInf_TuneCP5_13TeV-powheg-pythia8_hadd.root',
# 'TT_Mtt-700to1000_TuneCP5_13TeV-powheg-pythia8_hadd.root',
 #'TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8_ttbb_hadd.root',
 #'TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8_tt2b_hadd.root',
 #'TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8_tt1b_hadd.root',
 #'TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8_ttcc_hadd.root',
 #'TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8_ttjj_hadd.root',

# 'TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8_Mtt0to700_hadd.root',
# 'TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8_Mtt1000toInf_hadd.root',
# 'TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8_Mtt700to1000_hadd.root',

#'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_ttbb_hadd.root',
#'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_tt1b_hadd.root',
#'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_tt2b_hadd.root',
#'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_ttjj_hadd.root',
#'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_ttcc_hadd.root',

#'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_Mtt1000toInf_hadd.root',
#'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_Mtt700to1000_hadd.root',
# 'TTWJetsToLNu_TuneCP5_PSweights_13TeV-amcatnloFXFX-madspin-pythia8_hadd.root',
# 'TTZToLL_M-1to10_TuneCP5_13TeV-amcatnlo-pythia8_hadd.root',
# 'WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root',
# 'WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root',
# 'WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root',
# 'WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root',
# 'WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root
]
#[<variable in trees>, <variable name for axes and titles>, <unit>]
 



varList['BigComb'] = [
['AK4HTpMETpLepPt','S_{T}','GeV'],
['minMleppBjet','min[M(l,b)]','GeV'],
['mass_minBBdr','M(b,b) with min[#DeltaR(b,b)]','GeV'],
['deltaR_lepBJet_maxpt','#DeltaR(l,b)] with max[p_{T}(l,b)]',''],
['lepDR_minBBdr','#DeltaR(l,bb) with min[#DeltaR(b,b)]',''],
['centrality','Centrality',''],
['deltaEta_maxBB','max[#Delta#eta(b,b)]',''],
['aveCSVpt','p_{T} weighted CSVv2',''],
['aveBBdr','ave[#DeltaR(b,b)]',''],
#['FW_momentum_0','0^{th} FW moment','GeV'],
['FW_momentum_1','1^{st} FW moment','GeV'],
['FW_momentum_2','2^{nd} FW moment','GeV'],
['FW_momentum_3','3^{rd} FW moment','GeV'],
['FW_momentum_4','4^{th} FW moment','GeV'],
['FW_momentum_5','5^{th} FW moment','GeV'],
['FW_momentum_6','6^{th} FW moment','GeV'],
['mass_maxJJJpt','M(jjj) with max[p_{T}(jjj)]','GeV'],
['BJetLeadPt','p_{T}(b_{1})','GeV'],
['deltaR_minBB','min[#DeltaR(b,b)]',''],
['minDR_lepBJet','min[#DeltaR(l,b)]',''],
['MT_lepMet','M_{T}(lep,E_{T}^{miss})','GeV'],

['AK4HT','H_{T}','GeV'],
['hemiout','Hemiout','GeV'],
['theJetLeadPt','p_{T}(j_{1})','GeV'],
['corr_met_MultiLepCalc','E_{T}^{miss}','GeV'],
#['leptonPt_MultiLepCalc','p_{T}(lep)','GeV'],
['mass_lepJets0','M(l,j_{1})','GeV'],
['mass_lepJets1','M(l,j_{2})','GeV'],
['mass_lepJets2','M(l,j_{3})','GeV'],
['MT2bb','MT2bb','GeV'],
['mass_lepBJet0','M(l,b_{1})','GeV'],
['mass_lepBJet_mindr','M(l,b) with min[#DeltaR(l,b)]','GeV'],
['secondJetPt','p_{T}(j_{2})','GeV'],
['fifthJetPt','p_{T}(j_{5})','GeV'],
['sixthJetPt','p_{T}(j_{6})','GeV'],
['PtFifthJet','5^{th} jet p_{T}','GeV'],
['mass_minLLdr','M(j,j) with min[#DeltaR(j,j)], j #neq b','GeV'],
['mass_maxBBmass','max[M(b,b)]','GeV'],
['deltaR_lepJetInMinMljet','#DeltaR(l,j) with min M(l, j)',''],
['deltaPhi_lepJetInMinMljet','#DeltaPhi(l,j) with min M(l, j)',''],
['deltaR_lepbJetInMinMlb','#DeltaR(l,b) with min M(l, b)',''],
['deltaPhi_lepbJetInMinMlb','#DeltaPhi(l,b) with min M(l, b)',''],
['M_allJet_W','M(allJets, leptoninc W)','GeV'],
['HT_bjets','HT(bjets)','GeV'],
['ratio_HTdHT4leadjets','HT/HT(4 leading jets)',''],
['csvJet3','DeepCSV(3rdPtJet)',''],
['csvJet4','DeepCSV(4thPtJet)',''],
['thirdcsvb_bb','DeepCSV(3rdDeepCSVJet)',''],
['fourthcsvb_bb','DeepCSV(4thDeepCSVJet)',''],
#['NJets_JetSubCalc','AK4 jet multiplicity',''],
['HT_2m','HTwoTwoPtBjets','GeV'],
['Sphericity','Sphericity','Sphericity'],
['Aplanarity','Aplanarity','Aplanarity'],

# ['mass_lepJJ_minJJdr','M(l,jj) with min[#DeltaR(j,j)], j #neq b','GeV'],
# ['deltaR_lepBJets0','#DeltaR(l,b_{1})',''],
# ['minDR_lepJet','min[#DeltaR(l,j)]',''],
# ['mass_maxBBpt','M(b,b) with max[p_{T}(b,b)]','GeV'],
# ['MT2bbl','MT2bbl','GeV'],
# ['deltaR_lepJets0','#DeltaR(l,j_{1})',''],
# ['deltaR_lepJets1','#DeltaR(l,j_{2})',''],
# ['deltaR_lepJets2','#DeltaR(l,j_{3})',''],
# ['mass_lepBB_minBBdr','M(l,bb) with min[#DeltaR(b,b)]','GeV'],
# ['corr_met','E_{T}^{miss}','GeV'],
]



varList['Topological'] = [

#['deltaR_minBB','min[#DeltaR(b,b)]',''],
#['aveBBdr','ave[#DeltaR(b,b)]',''],
['deltaEta_maxBB','max[#Delta#eta(b,b)]',''],
#['FW_momentum_2','2^{nd} FW moment','GeV'],
#['centrality','Centrality',''],
#['aveCSVpt','p_{T} weighted CSVv2',''],
#['HT_bjets','HT(bjets)','GeV'],
#['minMleppBjet','min[M(l,b)]','GeV'],
#['BJetLeadPt','p_{T}(b_{1})','GeV'],
#['mass_maxJJJpt','M(jjj) with max[p_{T}(jjj)]','GeV'],
#['lepDR_minBBdr','#DeltaR(l,bb) with min[#DeltaR(b,b)]',''],
#['corr_met_MultiLepCalc','E_{T}^{miss}','GeV'],
#['MT_lepMet','M_{T}(lep,E_{T}^{miss})','GeV'],
]

varList['2016AN'] = [
['AK4HT','H_{T}','GeV'],
['deltaEta_maxBB','max[#Delta#eta(b,b)]',''],
['deltaR_minBB','min[#DeltaR(b,b)]',''],
['aveBBdr','ave[#DeltaR(b,b)]',''],
['centrality','Centrality',''],
['aveCSVpt','p_{T} weighted CSVv2',''],
['FW_momentum_2','2^{nd} FW moment','GeV'],
['minMleppBjet','min[M(l,b)]','GeV'],
['BJetLeadPt','p_{T}(b_{1})','GeV'],
['corr_met_MultiLepCalc','E_{T}^{miss}','GeV'],
['mass_maxJJJpt','M(jjj) with max[p_{T}(jjj)]','GeV'],
['MT_lepMet','M_{T}(lep,E_{T}^{miss})','GeV'],
['lepDR_minBBdr','#DeltaR(l,bb) with min[#DeltaR(b,b)]',''],
]







