import os,sys,datetime,itertools,shutil
parent = os.path.dirname(os.getcwd())
sys.path.append(parent)
from utils import *

thisDir = os.getcwd()
outputDir = thisDir+'/'

region='CR' #SR,CR --> matters only when plotting kinematics
categorize=1 #==categorize into t/W/b/j, 0==only split into flavor
sigTrainedList=['500']#['300', '500', '800', '1000', '1500']#,'500','1000']

cTime=datetime.datetime.now()
date='%i_%i_%i'%(cTime.year,cTime.month,cTime.day)
time='%i_%i_%i'%(cTime.hour,cTime.minute,cTime.second)

iPlotList = [#distribution name as defined in "doHists.py"


#"NPV",
#"NJets",
#"NBJetsNoSF", 
#"JetPt",
#"Jet1Pt", 
#"Jet2Pt", 
#"Jet3Pt", 
#"Jet4Pt", 
#"lepPt",
#"lepEta"
#'AK4HTpMETpLepPt'
#'ST',
#'minMlb',
#'mass_minBBdr',
#'deltaR_lepBJet_maxpt',
#'MT_lepMet',
#'FW_momentum_2',
#'HT',
#'theJetLeadPt',
#'MET',
#'mass_lepBJet0',
#'mass_lepBJet_mindr',
#'sixthJetPt',
#'mass_maxBBmass',
#'M_allJet_W',
#'HT_bjets',
#'thirdcsvb_bb',
#'fourthcsvb_bb',
#'Sphericity',
#'Aplanarity',
#'BestTop_Disc',
#'BestTop_Pt',
#'NoTop_Jet1_CSV',
#'NoTop_Jet1_Pt',
#'NoTop_Jet2_CSV',
#'recLeptonicTopJetCSV',
#'LeptonicTB1_M',
#'LeptonicTB2_M',
#'HadronicTB2_M',
#'ST',
#'minMlb',
#'topPt',
#'mass_minBBdr',
#'deltaR_lepBJet_maxpt',
#'lepDR_minBBdr',
#'centrality',
#'deltaEta_maxBB',
#'aveCSVpt',
#'aveBBdr',
#'FW_momentum_0',
#'FW_momentum_1',
#'FW_momentum_2',
#'FW_momentum_3',
#'FW_momentum_4',
#'FW_momentum_5',
#'FW_momentum_6',
#'mass_maxJJJpt',
#'Bjet1Pt',
#'deltaR_minBB',
#'deltaR',
#'MTlmet',
#'HT',
#'hemiout',
#'theLeadJetPt',
#'MET',
#'lepPt',
#'masslepJets0',
#'masslepJets1',
#'masslepJets2',
#'MT2bb',
#'masslepBJets0',
#'mass_lepBJet_mindr',
#'secondJetPt',
#'fifthJetPt',
#'sixthJetPt',
#'PtFifthJet',
#'mass_minLLdr',
#'mass_maxBBmass',
#'deltaR_lepJetInMinMljet',
#'deltaPhi_lepJetInMinMljet',
#'deltaR_lepbJetInMinMlb',
#'deltaPhi_lepbJetInMinMlb',
#'M_allJet_W',
#'HT_bjets',
#'HTpt40',
#'ratio_HTdHT4leadjets',
#'csvJet1',
#'csvJet2',
#'csvJet3',
#'csvJet4',
#'firstcsvb_bb',
#'secondcsvb_bb',
#'thirdcsvb_bb',
#'fourthcsvb_bb',
#'NJets',
#'NBJets',
#'HT_2m',
#'Sphericity',
#'Aplanarity',
#'BestTop_Disc', 
#'BestTop_Pt', 
#'NoTop_Jet1_CSV', 
#'NoTop_Jet1_Pt', 
#'NoTop_Jet2_CSV', 
#'NoTop_Jet2_Pt',

'XGB200_SR1',
'XGB220_SR1',
'XGB250_SR1',
'XGB300_SR1',
'XGB350_SR1',
'XGB400_SR1',
'XGB500_SR1',
'XGB600_SR1',
'XGB700_SR1',
'XGB800_SR1',
'XGB1000_SR1',
'XGB1250_SR1',
'XGB1500_SR1',
'XGB1750_SR1',
'XGB2000_SR1',
'XGB2500_SR1',
'XGB3000_SR1',

'XGB200_SR2',
'XGB220_SR2',
'XGB250_SR2',
'XGB300_SR2',
'XGB350_SR2',
'XGB400_SR2',
'XGB500_SR2',
'XGB600_SR2',
'XGB700_SR2',
'XGB800_SR2',
'XGB1000_SR2',
'XGB1250_SR2',
'XGB1500_SR2',
'XGB1750_SR2',
'XGB2000_SR2',
'XGB2500_SR2',
'XGB3000_SR2',

'XGB200_SR3',
'XGB220_SR3',
'XGB250_SR3',
'XGB300_SR3',
'XGB350_SR3',
'XGB400_SR3',
'XGB500_SR3',
'XGB600_SR3',
'XGB700_SR3',
'XGB800_SR3',
'XGB1000_SR3',
'XGB1250_SR3',
'XGB1500_SR3',
'XGB1750_SR3',
'XGB2000_SR3',
'XGB2500_SR3',
'XGB3000_SR3',






# 			'minBBdr',
# 			'aveBBdr',
# 			'deltaEta_maxBB',
# 			'FW_momentum_2',
# 			'centrality',
# 			'aveCSVpt',
# 			'HT',
# 			'minMlb',
# 			'Bjet1Pt',
# 			'mass_maxJJJpt',
# 			'MTlmet',
# 			'lepDR_minBBdr',
# 			'MET',
# #  
# 			'NPV',
#       		'lepPt',
#       		'lepEta',
#       		'JetEta',
#       		'JetPt',
# 			'NJets',
# 			'NBJets',
# 			'HTpBDT',
# 			'deltaPhi_METjets',
#			'min_deltaPhi_METjets'
#
# 			'HTpDNN',	
			]

isEMlist = ['E','M']
nttaglist = ['0p']
nWtaglist = ['0p']
nbtaglist = ['1', '2', '3p']
njetslist = ['4','5','6p']
#nbtaglist = ['1','2','3p']
#njetslist = ['3','4','5','6p']

if not categorize: 
	nbtaglist = ['1p']
	njetslist = ['3p']
if not categorize and 'BDT' in region: 
	nbtaglist = ['2p']
	njetslist = ['5p']

catList = list(itertools.product(isEMlist,nttaglist,nWtaglist,nbtaglist,njetslist))


count=0
for sigTrained in sigTrainedList:
    pfix='templates'
    if not categorize: pfix='kinematics_'+region
    pfix+='_M'+sigTrained+'_'+date+"_QCDsup_XGBRED_FineBin_UL16APV"#+'_'+time
    outDir = outputDir+pfix
    if not os.path.exists(outDir): os.system('mkdir '+outDir)
    os.chdir(outputDir)
	#os.system('cp ../analyze.py doHists.py ../utils.py ../weights.py ../samples.py doCondorTemplates.py doCondorTemplates.sh '+outDir+'/')
    shutil.copy('../analyze_UL16APV.py', outDir+'/')
    shutil.copy('doHists_UL16APV.py', outDir+'/')
    shutil.copy('../utils.py', outDir+'/')
    shutil.copy('../weights_UL16APV.py', outDir+'/')
    shutil.copy('../samples_UL16APV.py', outDir+'/')
    os.chdir(outDir)

    for iplot in iPlotList:
        for cat in catList:
            if skip(cat[4],cat[3]) and categorize: continue #DO YOU WANT TO HAVE THIS??
            catDir = cat[0]+'_nT'+cat[1]+'_nW'+cat[2]+'_nB'+cat[3]+'_nJ'+cat[4]
            print(("Training: "+sigTrained+", iPlot: "+iplot+", cat: "+catDir))
            if not os.path.exists(outDir+'/'+catDir): os.system('mkdir '+catDir)
            os.chdir(catDir)
            os.system('cp '+outputDir+'/doCondorTemplates_UL16APV.sh '+outDir+'/'+catDir+'/'+cat[0]+'T'+cat[1]+'W'+cat[2]+'B'+cat[3]+'J'+cat[4]+iplot+'.sh')
            tmpDir = cat[0]+'T'+cat[1]+'W'+cat[2]+'B'+cat[3]+'J'+cat[4]+iplot
            shutil.copy('../analyze_UL16APV.py', './')
            shutil.copy('../doHists_UL16APV.py', './')
            shutil.copy('../utils.py', './')
            shutil.copy('../weights_UL16APV.py', './')
            shutil.copy('../samples_UL16APV.py', '.')						
            dict={'dir':outputDir,'iPlot':iplot,'region':region,'isCategorized':categorize,
			      'isEM':cat[0],'nttag':cat[1],'nWtag':cat[2],'nbtag':cat[3],'njets':cat[4],
                  'exeDir':outDir+'/'+catDir,'sigTrained':sigTrained, 'tmpDir':tmpDir}
            jdf=open('condor_'+iplot+'.job','w')
            jdf.write(
"""universe = vanilla
Executable = %(isEM)sT%(nttag)sW%(nWtag)sB%(nbtag)sJ%(njets)s%(iPlot)s.sh
Should_Transfer_Files = IF_NEEDED
WhenToTransferOutput = ON_EXIT
Transfer_Input_Files = analyze_UL16APV.py,doHists_UL16APV.py,utils.py,weights_UL16APV.py,samples_UL16APV.py
request_memory = 13312 
Output = condor_%(iPlot)s.out
Error = condor_%(iPlot)s.err
Log = condor_%(iPlot)s.log
Arguments = %(exeDir)s %(iPlot)s %(region)s %(isCategorized)s %(isEM)s %(nttag)s %(nWtag)s %(nbtag)s %(njets)s %(sigTrained)s %(tmpDir)s
Queue 1"""%dict)
            jdf.close()
            os.system('condor_submit condor_'+iplot+'.job')
			#os.system('sleep 0.5')
            os.chdir('..')
            count+=1

print(("Total jobs submitted:", count))
                  
