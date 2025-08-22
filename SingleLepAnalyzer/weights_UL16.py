#!/usr/bin/python

targetlumi = 16726. # 1/pb

genHTweight={}
genHTweight['WJetsMG100'] = 0.998056#https://github.com/jmhogan/GenHTweight/blob/master/WJetsToLNuSFs.txt
genHTweight['WJetsMG200'] = 0.978569
genHTweight['WJetsMG400'] = 0.928054
genHTweight['WJetsMG600'] = 0.856705
genHTweight['WJetsMG800'] = 0.757463
genHTweight['WJetsMG1200']= 0.608292
genHTweight['WJetsMG2500']= 0.454246

genHTweight['DYMG100'] = 1.007516#https://github.com/jmhogan/GenHTweight/blob/master/DYJetsToLLSFs.txt
genHTweight['DYMG200'] = 0.992853
genHTweight['DYMG400'] = 0.974071
genHTweight['DYMG600'] = 0.948367
genHTweight['DYMG800'] = 0.883340
genHTweight['DYMG1200']= 0.749894
genHTweight['DYMG2500']= 0.617254


# Number of processed MC events (before selections)
nRun={}
nRun['TTJets'] = 14188545. #need negative counts
nRun['TTJetsPH'] = 111068128.

BR_TTJetsHad = 0.457
BR_TTJetsSemiLep = 0.438
BR_TTJets2L2nu = 0.105
filtEff_TTJets1000mtt = 0.02474
filtEff_TTJets700mtt = 0.0921
filtEff_TTJets0mtt = 0.8832 # 1-filtEff_TTJets700mtt-filtEff_TTJets1000mtt
filtEff_TTJetsSemiLepNjet9 = 0.0057 # from McM
nRun_TTJetsHad = 108415462.0#93137016.0 #129706300#129211204.0 # from integral 130262340.0, file TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8_Mtt0to700_hadd.root
nRun_TTJetsSemiLep = 143446896.0#133661764.0 #6837419540.0 #114058500#129706300#109124472.0 # from integral 110085096.0, file TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_Mtt0to700_hadd.root
nRun_TTJets2L2nu = 43277246.0#40819800.0 #66259900#68595608.0 # from integral 69155808.0, file TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8_Mtt0to700_hadd.root
nRun_TTJets700mtt = 38428627.0 # from 39258853, file TT_Mtt-700to1000_TuneCP5_13TeV-powheg-pythia8_hadd.root
nRun_TTJets1000mtt = 21288395.0 # from integral 22458751.0, file TT_Mtt-1000toInf_TuneCP5_PSweights_13TeV-powheg
nRun_TTJetsSemiLepNjet9 = 8752072.0 # from integral, file TTToSemiLepton_HT500Njet9_TuneCP5_PSweights_13TeV-powheg-pythia8_Mtt0to700_hadd.root
nRun['TTToHadronic'] = nRun_TTJetsHad#207187204.0#nRun_TTJetsHad
nRun['TTToSemiLeptonic'] = nRun_TTJetsSemiLep#148086112.0#nRun_TTJetsSemiLep
nRun['TTTo2L2Nu'] = nRun_TTJets2L2nu#47141720.0 #nRun_TTJets2L2nu 
nRun['TTJetsHad0']    = nRun_TTJetsHad * filtEff_TTJets0mtt 
nRun['TTJetsHad700']  = nRun_TTJetsHad * filtEff_TTJets700mtt  + nRun_TTJets700mtt  * BR_TTJetsHad
nRun['TTJetsHad1000'] = nRun_TTJetsHad * filtEff_TTJets1000mtt + nRun_TTJets1000mtt * BR_TTJetsHad
nRun['TTJetsSemiLep0']    = nRun_TTJetsSemiLep * filtEff_TTJets0mtt 
nRun['TTJetsSemiLep700']  = nRun_TTJetsSemiLep * filtEff_TTJets700mtt  + nRun_TTJets700mtt  * BR_TTJetsSemiLep
nRun['TTJetsSemiLep1000'] = nRun_TTJetsSemiLep * filtEff_TTJets1000mtt + nRun_TTJets1000mtt * BR_TTJetsSemiLep
nRun['TTJets2L2nu0']    = nRun_TTJets2L2nu * filtEff_TTJets0mtt 
nRun['TTJets2L2nu700']  = nRun_TTJets2L2nu * filtEff_TTJets700mtt  + nRun_TTJets700mtt  * BR_TTJets2L2nu
nRun['TTJets2L2nu1000'] = nRun_TTJets2L2nu * filtEff_TTJets1000mtt + nRun_TTJets1000mtt * BR_TTJets2L2nu
nRun['TTJets700mtt']  = nRun_TTJets700mtt  + nRun_TTJetsHad * filtEff_TTJets700mtt  + nRun_TTJetsSemiLep * filtEff_TTJets700mtt  + nRun_TTJets2L2nu * filtEff_TTJets700mtt
nRun['TTJets1000mtt'] = nRun_TTJets1000mtt + nRun_TTJetsHad * filtEff_TTJets1000mtt + nRun_TTJetsSemiLep * filtEff_TTJets1000mtt + nRun_TTJets2L2nu * filtEff_TTJets1000mtt

nRun['TTJets700mtt_JEC'] = nRun['TTJets700mtt']
nRun['TTJets1000mtt_JER'] = nRun['TTJets1000mtt']

#nRun['TTJetsHad'] = nRun_TTJetsHad
#nRun['TTJetsSemiLepNjet0'] = nRun_TTJetsSemiLep * ( 1. - filtEff_TTJetsSemiLepNjet9 ) 
#nRun['TTJetsSemiLepNjet9'] = nRun_TTJetsSemiLep * filtEff_TTJetsSemiLepNjet9 + nRun_TTJetsSemiLepNjet9
#nRun['TTJetsSemiLepNjet9bin'] = nRun['TTJetsSemiLepNjet9']
#nRun['TTJets2L2nu'] = nRun_TTJets2L2nu
#nRun['TTJetsSemiLep'] = nRun_TTJetsSemiLep

nRun['Ts'] = 3562866.0#3468362.0#3478306.0#19850000#6895750.0 # from integral 6898000.0, file ST_s-channel_top_leptonDecays_13TeV-PSweights_powheg-pythia_hadd.root
#nRun['Tbs'] = 2952214.0 # from integral 2953000.0, file ST_s-channel_antitop_leptonDecays_13TeV-PSweights_powheg-pythia_hadd.root
nRun['Tt'] = 59099222.0#51822600.0#52437432.0#46206600#122640200.0 # from integral 109621700.0, file ST_t-channel_top_4f_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8_hadd.root
nRun['Tbt']= 28814596.0#28810822.0#29205918.0#3695100#64818800.0 # from integral 50194500.0, file ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8_hadd.root
nRun['TtW'] = 2490860.0#2490860.0#2299880.0#10041965#7884388.0 # from integral 7945242.0, file ST_tW_top_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8_hadd.root
nRun['TbtW'] = 2553882.0#2553882.0#2299866.0#9191369#7686032.0 # from integral 7745276.0, file ST_tW_antitop_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8_hadd.root

nRun['WJets'] = 6776900. # from 9908534.
nRun['WJetsMG'] = 87960604#86731806. 
nRun['WJetsMG100'] = 79356685.
nRun['WJetsMG200'] = 15067621.0#15185376.0#17164198.0#21192211.0 # from integral 21250517.0, file WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root
nRun['WJetsMG400'] = 1781026.0#2115509.0#2302057.0#14189363.0 # from integral 14252285.0, file WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root
nRun['WJetsMG600'] = 2251807.0#2251807.0#1905536.0#21330497.0 # from integral 21455857.0, file WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root
nRun['WJetsMG800'] = 2132228.0#2132228.0#2350331.0#20272990.0 # from integral 20432728.0, file WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root
nRun['WJetsMG1200'] = 2090561.0#2090561.0#1754683.0#19950628.0 # from integral 20216830.0, file WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root
nRun['WJetsMG2500'] = 709514.0#584932.0#808649.0#20629585.0 # from integral 21495421.0, file WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root
nRun['WJetsPt100'] = 120124110.*(1.-2.*0.32) #Full =120124110, neg frac 0.32
nRun['WJetsPt250'] = 12022587.*(1.-2.*0.31555) #Full = 12022587, neg frac 0.31555 
nRun['WJetsPt400'] = 1939947.*(1.-2.*0.30952) #Full = 1939947, neg frac 0.30952
nRun['WJetsPt600'] = 1974619.*(1.-2.*0.29876) #Full = 1974619, neg frac 0.29876

nRun['DY'] = 123584520. # from 182359896, this is the ext1 sample
nRun['DYMG'] = 202549488#49082157. # from integral 49125561.0, file DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root
nRun['DYMG100'] = 10607207.
nRun['DYMG200'] = 5653782.0#5653782.0#10699051.0 # from integral 10728447.0, file DYJetsToLL_M-50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root
nRun['DYMG400'] = 2491416.0#2491416.0#10174800.0 # from integral 10219524.0, file DYJetsToLL_M-50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root
nRun['DYMG600'] = 2266996.0#2299853.0#8691608.0 # from integral 8743640.0, file DYJetsToLL_M-50_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root
nRun['DYMG800'] = 2393976.0#2393976.0#3089712.0 # from integral 3114980.0, file DYJetsToLL_M-50_HT-800to1200_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root
nRun['DYMG1200']= 1912385.0#1970857.0#616906.0 # from integral 625517.0, file DYJetsToLL_M-50_HT-1200to2500_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root
nRun['DYMG2500']= 696811.0#696811.0 #401334.0 # from integral 419308.0, file DYJetsToLL_M-50_HT-2500toInf_TuneCP5_13TeV-madgraphMLM-pythia8_hadd.root

nRun['WW'] = 15821000.0#15685000.0#7876200#7765828.0 # from integral 7765828.0, file WW_TuneCP5_13TeV-pythia8_hadd.root
nRun['WZ'] = 7584000.0#7584000.0#3970000#3928567.0 # from integral 3928630.0, file WZ_TuneCP5_13TeV-pythia8_hadd.root
nRun['ZZ'] = 1141000.0#1151000.0#1981800#1925931.0 # from integral 1925931.0, file ZZ_TuneCP5_13TeV-pythia8_hadd.root

nRun['QCDht100'] = 77775408#80684349.
nRun['QCDht200'] = 17569141.0#17569141.0#57721120#65436493.0 # from integral 59074480.0, file QCD_HT200to300_TuneCP5_13TeV-madgraph-pythia8_hadd.root
nRun['QCDht300'] = 16747056.0#16747056.0#57191140#60432501.0 # from integral 59569132.0, file QCD_HT300to500_TuneCP5_13TeV-madgraph-pythia8_hadd.root
nRun['QCDht500'] = 15222746.0#15222746.0#43589739.0#9188310#56041018.0 # from integral 56207744.0, file QCD_HT500to700_TuneCP5_13TeV-madgraph-pythia8_hadd.root
nRun['QCDht700'] = 13858616.0#13905714.0#45812757#46638985.0 # from integral 46840955.0, file QCD_HT700to1000_TuneCP5_13TeV-madgraph-pythia8_hadd.root
nRun['QCDht1000'] = 4320065.0#4365993.0#15346629#16770762.0 # from integral 16882838.0, file QCD_HT1000to1500_TuneCP5_13TeV-madgraph-pythia8_hadd.root
nRun['QCDht1500'] = 3217830.0#3217830.0#10598209#11508604.0 # from integral 11634434.0, file QCD_HT1500to2000_TuneCP5_13TeV-madgraph-pythia8_hadd.root
nRun['QCDht2000'] = 1847781.0#1847781.0#5457021#5825566.0 # from integral 5941306.0, file QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8_hadd.root

nRun['TTW'] = 5216439#9384328. # from integral 9425384.0, file ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8_hadd.root
nRun['TTZ'] = 14000000#8519074. # from integral 8536618.0, file ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8_hadd.root
nRun['TTH'] = 9580578. # from integral 9783674.0, file ttH_M125_TuneCP5_13TeV-powheg-pythia8_hadd.root
nRun['TTWl'] = 1800823.0#1800823.0#1543290.0#5216439#2742430.0 # from integral, file TTWJetsToLNu_TuneCP5_PSweights_13TeV-amcatnloFXFX-madspin-pythia8_hadd.root
nRun['TTWq'] = 168951.0#168951.0#148842.0#441560.0 # from integral 811306.0, file TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8_hadd.root
nRun['TTZlM10'] = 2982392.0#2982392.0#2856626.0#14000000# 5239484.0 # from integral, file TTZToLLNuNu_M-10_TuneCP5_PSweights_13TeV-amcatnlo-pythia8_hadd.root
nRun['TTZlM1to10'] = 177656.0#177656.0#177656.0
nRun['TTHB'] = 4834712.0#4834712.0
nRun['TTHnoB'] = 2194702.0#2194702.0 

nRun['TTTT'] = 6029906.0
nRun['TTWW'] = 309000.0#309000.0#245000.0
nRun['TTWH'] = 160000.0#160000.0#140000.0
nRun['TTHH'] = 153000.0#153000.0
nRun['TTZZ'] = 152000.0#152000.0#140000.0
nRun['TTWZ'] = 159000.0#159000.0#140000.0
nRun['TTZH'] = 160000.0#160000.0#140000.0




nRun['TTZq'] = 351164. # from 749400
#nRun['TTHB'] = 7833734.0 # from integral 8000000.0, file ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8_hadd.root
#nRun['TTHnoB'] = 7814711.0 # from integral 7161154.0, file ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8_hadd.root

#nRun['TTHH'] = 199371.0 # from integral, file TTHH_TuneCP5_13TeV-madgraph-pythia8_hadd.root
nRun['TTTJ'] = 198546.0 # from integral, file TTTJ_TuneCP5_13TeV-madgraph-pythia8_hadd.root
nRun['TTTW'] = 199699.0 # from integral, file TTTW_TuneCP5_13TeV-madgraph-pythia8_hadd.root
#nRun['TTWH'] = 198978.0 # from integral, file TTWH_TuneCP5_13TeV-madgraph-pythia8_hadd.root
#nRun['TTWW'] = 199008.0 # from integral, file TTWW_TuneCP5_13TeV-madgraph-pythia8_hadd.root
#nRun['TTWZ'] = 198756.0 # from integral, file TTWZ_TuneCP5_13TeV-madgraph-pythia8_hadd.root
#nRun['TTZH'] = 199285.0 # from integral, file TTZH_TuneCP5_13TeV-madgraph-pythia8_hadd.root
#nRun['TTZZ'] = 199363.0 # from integral, file TTZZ_TuneCP5_13TeV-madgraph-pythia8_hadd.root
#nRun['TTTT'] = 373734.0 # file TTTT_TuneCP5_13TeV-amcatnlo-pythia8_hadd.root

##### Signal samples with positive events weight only #####
nRun['Hptb180'] = 7008080
nRun['Hptb200'] = 1235862.0#1451090.0 
nRun['Hptb220'] = 1388218.0#1425804.0 
nRun['Hptb250'] = 1400920.0#1398138.0 
nRun['Hptb300'] = 1385196.0#1335810.0 
nRun['Hptb350'] = 1379522.0#1379522.0 
nRun['Hptb400'] = 1347890.0#1290532.0 
nRun['Hptb500'] = 1339084.0#1339084.0 
nRun['Hptb600'] = 1330778.0#1195906.0 
nRun['Hptb700'] = 1333518.0#1333518.0 
nRun['Hptb800'] = 1305996.0#1305996.0 
nRun['Hptb1000'] = 936160.0#1292230.0 
nRun['Hptb1250'] = 1216096.0#1223368.0 
nRun['Hptb1500'] = 1247468.0#1247468.0 
nRun['Hptb1750'] = 1245854.0#1196790.0 
nRun['Hptb2000'] = 1190734.0#1195628.0 
nRun['Hptb2500'] = 1240566.0#1208944.0 
nRun['Hptb3000'] = 1232958.0#1232958.0 


#energy scale samples (Q^2)
# nRun['TTJetsPHQ2U'] = 9933327.
# nRun['TTJetsPHQ2D'] = 9942427.
# nRun['TtWQ2U'] = 497600. #not used
# nRun['TtWQ2D'] = 499200. #not used
# nRun['TbtWQ2U'] = 500000. #not used
# nRun['TbtWQ2D'] = 497600. #not used


# Cross sections for MC samples (in pb)
xsec={}

xsec['TTJets'] = 831.76
xsec['TTJetsPH'] = 831.76 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
#xsec['TTJetsPH0to700inc'] = 831.76
#xsec['TTJetsPH700to1000inc'] = 831.76*0.0921 #(xsec*filtering coeff.)
#xsec['TTJetsPH1000toINFinc'] = 831.76*0.02474 #(xsec*filtering coeff.)
xsec['TTToHadronic'] = xsec['TTJets'] * BR_TTJetsHad
xsec['TTToSemiLeptonic'] = xsec['TTJets'] * BR_TTJetsSemiLep
xsec['TTToSemiLepNjet0'] = xsec['TTJets'] * BR_TTJetsSemiLep * ( 1. - filtEff_TTJetsSemiLepNjet9 ) 
xsec['TTToSemiLepNjet9'] = xsec['TTJets'] * BR_TTJetsSemiLep * filtEff_TTJetsSemiLepNjet9
xsec['TTTo2L2Nu'] = xsec['TTJets'] * BR_TTJets2L2nu

xsec['TTToSemiLepNjet0_1'] = xsec['TTToSemiLepNjet0']
xsec['TTToSemiLepNjet0_2'] = xsec['TTToSemiLepNjet0']
xsec['TTToSemiLepNjet0_3'] = xsec['TTToSemiLepNjet0']
xsec['TTToSemiLepNjet0_4'] = xsec['TTToSemiLepNjet0']
xsec['TTToSemiLepNjet0_5'] = xsec['TTToSemiLepNjet0']
xsec['TTToSemiLepNjet0_6'] = xsec['TTToSemiLepNjet0']
xsec['TTToSemiLepNjet0_7'] = xsec['TTToSemiLepNjet0']
xsec['TTToSemiLepNjet0_9'] = xsec['TTToSemiLepNjet0']
xsec['TTToSemiLepNjet0_10'] = xsec['TTToSemiLepNjet0']




xsec['TTJetsHad0']    = xsec['TTJets'] * BR_TTJetsHad * filtEff_TTJets0mtt # BRs from PDG Top Review 2018: 45.7%/43.8%/10.5% 0/1/2 leptons
xsec['TTJetsHad700']  = xsec['TTJets'] * BR_TTJetsHad * filtEff_TTJets700mtt
xsec['TTJetsHad1000'] = xsec['TTJets'] * BR_TTJetsHad * filtEff_TTJets1000mtt
xsec['TTJetsSemiLep0']    = xsec['TTJets'] * BR_TTJetsSemiLep * filtEff_TTJets0mtt
xsec['TTJetsSemiLep700']  = xsec['TTJets'] * BR_TTJetsSemiLep * filtEff_TTJets700mtt
xsec['TTJetsSemiLep1000'] = xsec['TTJets'] * BR_TTJetsSemiLep * filtEff_TTJets1000mtt
xsec['TTJets2L2nu0']    = xsec['TTJets'] * BR_TTJets2L2nu * filtEff_TTJets0mtt
xsec['TTJets2L2nu700']  = xsec['TTJets'] * BR_TTJets2L2nu * filtEff_TTJets700mtt
xsec['TTJets2L2nu1000'] = xsec['TTJets'] * BR_TTJets2L2nu * filtEff_TTJets1000mtt
xsec['TTJets700mtt']  = xsec['TTJets'] * filtEff_TTJets700mtt # (xsec*filtering coeff.)
xsec['TTJets1000mtt'] = xsec['TTJets'] * filtEff_TTJets1000mtt # (xsec*filtering coeff.)

xsec['TTJetsHad'] = xsec['TTJets'] * BR_TTJetsHad
#xsec['TTJetsSemiLepNjet9bin'] = xsec['TTJetsSemiLepNjet9']
xsec['TTJets2L2nu'] = xsec['TTJets'] * BR_TTJets2L2nu
xsec['TTJetsSemiLep'] = xsec['TTJets'] * BR_TTJetsSemiLep

xsec['TTJets700mtt_JEC'] = xsec['TTJets700mtt']
xsec['TTJets1000mtt_JER'] = xsec['TTJets1000mtt']


xsec['Ts'] = 11.36/3 #7.20/3 #(1/3 was suggested by Thomas Peiffer to account for the leptonic branching ratio)# https://twiki.cern.ch/twiki/bin/viewauth/CMS/SingleTopSigma
#xsec['Tbs'] = 4.16/3 #(1/3 was suggested by Thomas Peiffer to account for the leptonic branching ratio)# https://twiki.cern.ch/twiki/bin/viewauth/CMS/SingleTopSigma
xsec['Tt'] = 136.02 # https://twiki.cern.ch/twiki/bin/viewauth/CMS/SingleTopSigma
xsec['Tbt'] = 80.95 # https://twiki.cern.ch/twiki/bin/viewauth/CMS/SingleTopSigma
xsec['TtW'] = 35.83 # https://twiki.cern.ch/twiki/bin/viewauth/CMS/SingleTopSigma
xsec['TbtW'] = 35.83 # https://twiki.cern.ch/twiki/bin/viewauth/CMS/SingleTopSigma

xsec['WJets'] = 61526.7
xsec['WJetsMG'] = 61526.7
xsec['WJetsMG100'] = 1345.*1.21 # (1.21 = k-factor )# https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['WJetsMG200'] = 359.7*1.21 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['WJetsMG400'] = 48.91*1.21 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['WJetsMG600'] = 12.05*1.21 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['WJetsMG800'] = 5.501*1.21 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['WJetsMG1200'] = 1.329*1.21 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['WJetsMG2500'] = 0.03216*1.21 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns 
xsec['WJetsPt100'] = 676.3 #B2G-17-010 / AN2016_480_v5
xsec['WJetsPt250'] = 23.94 #B2G-17-010 / AN2016_480_v5
xsec['WJetsPt400'] = 3.031 #B2G-17-010 / AN2016_480_v5
xsec['WJetsPt600'] = 0.4524 #B2G-17-010 / AN2016_480_v5

xsec['DY'] = 6025.2 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['DYMG'] = 6025.2 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['DYMG100'] = 147.4*1.23 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['DYMG200'] = 40.99*1.23 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['DYMG400'] = 5.678*1.23 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['DYMG600'] = 1.367*1.23 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['DYMG800'] = 0.6304*1.23 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['DYMG1200'] = 0.1514*1.23 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns
xsec['DYMG2500'] = 0.003565*1.23 # https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns

xsec['WW'] = 118.7 # https://twiki.cern.ch/twiki/bin/viewauth/CMS/StandardModelCrossSectionsat13TeVInclusive
xsec['WZ'] = 47.13 # https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#Diboson
xsec['ZZ'] = 16.523 # https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#Diboson

xsec['QCDht100'] = 27990000. # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD
xsec['QCDht200'] = 1712000. # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD 
xsec['QCDht300'] = 347700. # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD 
xsec['QCDht500'] = 32100. # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD
xsec['QCDht700'] = 6831. # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD 
xsec['QCDht1000'] = 1207. # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD
xsec['QCDht1500'] = 119.9 # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD 
xsec['QCDht2000'] = 25.24 # from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#QCD

xsec['TTW'] = 0.4611 # from XsecDB, LO
xsec['TTZ'] = 0.5407 # from XsecDB, LO
xsec['TTH'] = 0.5269 # from XsecDB, NLO
xsec['TTWl'] = 0.2043 # from McM
xsec['TTWq'] = 0.4062 # from McM
#xsec['TTZl'] = 0.2529 # from McM
xsec['TTZlM10'] =  0.2439
xsec['TTZlM1to10'] = 0.05324

xsec['TTZq'] = 0.5297 # from McM
xsec['TTHB'] = 0.2934
xsec['TTHnoB'] = 0.215

xsec['TTHH'] = 0.0007408 # from McM
xsec['TTTJ'] = 0.0004741 # from McM
xsec['TTTW'] = 0.000733 # from McM
xsec['TTWH'] = 0.001359 # from McM
xsec['TTWW'] = 0.007883 # from McM
xsec['TTWZ'] = 0.002974 # from McM
xsec['TTZH'] = 0.001253 # from McM
xsec['TTZZ'] = 0.001572 # from McM

#4 Tops
xsec['TTTT'] = 0.008213 # from McM

#Scaling all HTB signal x-secs to 1pb as agreed with POM, 
#so we have the signal yields scaled to 1pb
xsec['Hptb180'] = 1.#((0.824531)**2/0.683584)*0.75 #interpolation using the fact that xsec proportuonal to exp(-m) http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt
xsec['Hptb200'] = 1.#0.824531*0.75 #was 0.783951 http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt
xsec['Hptb220'] = 1.#0.683584*0.75 #was 0.648629 http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt
xsec['Hptb250'] = 1.#0.524247*0.75 #was 0.4982015 interpolation using the fact that xsec proportuonal to exp(-m) http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt
xsec['Hptb300'] = 1.#0.343796*0.75 #was 0.324766 http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt
xsec['Hptb350'] = 1.#0.2312180*0.75 #was 0.2184385 interpolation using the fact that xsec proportuonal to exp(-m) http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt
xsec['Hptb400'] = 1.#0.158142*0.75 #was 0.148574 http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt
#xsec['Hptb450'] = 1.#0.1106674*0.75 #was 0.104141 interpolation using the fact that xsec proportuonal to exp(-m) http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt
xsec['Hptb500'] = 1.#0.0785572*0.75 #was 0.0735225 http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt
xsec['Hptb600'] = 1.
xsec['Hptb700'] = 1.#0.0172205*0.75 #http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt
xsec['Hptb800'] = 1.#0.0130645*0.75 #http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt
xsec['Hptb1000'] = 1.#0.00474564*0.75 #http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt
xsec['Hptb1250'] = 1.
xsec['Hptb1500'] = 1.
xsec['Hptb1750'] = 1.
xsec['Hptb2000'] = 1.#(8.70916e-05)*0.75 #http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt
xsec['Hptb2500'] = 1.
xsec['Hptb3000'] = 1.#((8.70916e-05)**2/0.00474564)*0.75 #interpolation using the fact that xsec proportuonal to exp(-m) http://www.hephy.at/user/mflechl/hp_xsec/xsec_13TeV_tHp_2016_2_5.txt

# Calculate lumi normalization weights
weight = {}
for sample in sorted(nRun.keys()): 
	weight[sample] = (targetlumi*xsec[sample]) / (nRun[sample])


weight["TTToSemiLeptonic_HT500Njet9"] = weight["TTToSemiLeptonic"]
weight["TTToSemiLeptonic_HT0Njet0"] = weight["TTToSemiLeptonic"]
weight["TTToSemiLeptonic_HT0Njet0_1"] = weight["TTToSemiLeptonic"]
weight["TTToSemiLeptonic_HT0Njet0_2"] = weight["TTToSemiLeptonic"]
weight["TTToSemiLeptonic_HT0Njet0_3"] = weight["TTToSemiLeptonic"]
weight["TTToSemiLeptonic_HT0Njet0_4"] = weight["TTToSemiLeptonic"]
weight["TTToSemiLeptonic_HT0Njet0_5"] = weight["TTToSemiLeptonic"]
weight["TTToSemiLeptonic_HT0Njet0_6"] = weight["TTToSemiLeptonic"]
weight["TTToSemiLeptonic_HT0Njet0_7"] = weight["TTToSemiLeptonic"]
weight["TTToSemiLeptonic_HT0Njet0_8"] = weight["TTToSemiLeptonic"]
weight["TTToSemiLeptonic_HT0Njet0_9"] = weight["TTToSemiLeptonic"]
weight["TTToSemiLeptonic_HT0Njet0_10"] = weight["TTToSemiLeptonic"]

  

	
#weight['TTJetsSemiLep01'] = weight['TTJetsSemiLep0']
#weight['TTJetsSemiLep02'] = weight['TTJetsSemiLep0']
#weight['TTJetsSemiLep03'] = weight['TTJetsSemiLep0']
#weight['TTJetsSemiLep04'] = weight['TTJetsSemiLep0']
weight['WJetsMG1200_1'] = weight['WJetsMG1200']
weight['WJetsMG1200_2'] = weight['WJetsMG1200']
weight['WJetsMG1200_3'] = weight['WJetsMG1200']
weight['WJetsMG1200_4'] = weight['WJetsMG1200']
weight['WJetsMG1200_5'] = weight['WJetsMG1200']
weight['WJetsMG2500_1'] = weight['WJetsMG2500'] 
weight['WJetsMG2500_2'] = weight['WJetsMG2500'] 
weight['WJetsMG2500_3'] = weight['WJetsMG2500'] 
weight['WJetsMG2500_4'] = weight['WJetsMG2500'] 
weight['WJetsMG2500_5'] = weight['WJetsMG2500'] 
weight['WJetsMG2500_6'] = weight['WJetsMG2500'] 

#weight['TTJetsHad1'] = weight['TTJetsHad']
#weight['TTJetsHad2'] = weight['TTJetsHad']
#weight['TTJetsHad3'] = weight['TTJetsHad']
#weight['TTJetsSemiLep1'] = weight['TTJetsSemiLep']
#weight['TTJetsSemiLep2'] = weight['TTJetsSemiLep']
#weight['TTJetsSemiLep3'] = weight['TTJetsSemiLep']
#weight['TTJetsSemiLep4'] = weight['TTJetsSemiLep']
#weight['TTJetsSemiLep5'] = weight['TTJetsSemiLep']
#weight['TTJetsSemiLep6'] = weight['TTJetsSemiLep']
#weight['TTJetsSemiLepNjet01'] = weight['TTJetsSemiLepNjet0']
#weight['TTJetsSemiLepNjet02'] = weight['TTJetsSemiLepNjet0']
#weight['TTJetsSemiLepNjet03'] = weight['TTJetsSemiLepNjet0']
#weight['TTJetsSemiLepNjet04'] = weight['TTJetsSemiLepNjet0']
#weight['TTJetsSemiLepNjet05'] = weight['TTJetsSemiLepNjet0']
#weight['TTJetsSemiLepNjet06'] = weight['TTJetsSemiLepNjet0']
#weight['TTJetsSemiLepNjet07'] = weight['TTJetsSemiLepNjet0']
#
#
#weight['TTJetsSemiLepNjet91'] = weight['TTJetsSemiLepNjet9']
#weight['TTJetsSemiLepNjet92'] = weight['TTJetsSemiLepNjet9']
#weight['TTJetsSemiLepNjet93'] = weight['TTJetsSemiLepNjet9']
#weight['TTJetsSemiLepNjet94'] = weight['TTJetsSemiLepNjet9']
#weight['TTJetsSemiLepNjet95'] = weight['TTJetsSemiLepNjet9']
#weight['TTJetsSemiLepNjet96'] = weight['TTJetsSemiLepNjet9']
#weight['TTJetsSemiLepNjet9bin1'] = weight['TTJetsSemiLepNjet9bin']
#weight['TTJetsSemiLepNjet9bin2'] = weight['TTJetsSemiLepNjet9bin']
#weight['TTJetsSemiLepNjet9bin3'] = weight['TTJetsSemiLepNjet9bin']
#weight['TTJets2L2nu1'] = weight['TTJets2L2nu']
#weight['TTJets2L2nu2'] = weight['TTJets2L2nu']
#weight['TTJets2L2nu3'] = weight['TTJets2L2nu']

for smp in list(weight.keys()):
	if 'TTTo' in smp:
		for hf in ['_tt2b','_ttbb','_tt1b','_ttcc','_ttjj']: 
			weight[smp+hf]=weight[smp]
