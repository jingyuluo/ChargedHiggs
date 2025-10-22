#!/usr/bin/env python

import os,sys,time,math,datetime,itertools
from ROOT import gROOT,TFile,TH1F
import CombineHarvester.CombineTools.ch as ch
parent = os.path.dirname(os.getcwd())
thisdir= os.path.dirname(os.getcwd()+'/')
sys.path.append(parent)
from utils import *
gROOT.SetBatch(1)

def add_processes_and_observations(cb, prefix='Hptb'):
    print('>> Creating processes and observations...')
    for chn in chns:
        cats_chn = cats[chn]
        #if 'isCR' not in chn:
        cb.AddObservations(  ['*'],  [prefix], [era], [chn],                 cats_chn      )
        cb.AddProcesses(     ['*'],  [prefix], [era], [chn], bkg_procs[chn], cats_chn, False  )
        cb.AddProcesses(     [''], [prefix], [era], [chn], sig_procs,      cats_chn, True   )
        #else:
        #    cb.AddObservations(  ['all'],  [prefix], [era], [chn],                 cats_chn      )
        #    cb.AddProcesses(     ['all'],  [prefix], [era], [chn], bkg_procs[chn], cats_chn, False  )


def add_shapes(cb):
    print('>> Extracting histograms from input root files...')
    for chn in chns:
        bkg_pattern = iPlot+'_'+lumiStr+'_%s$BIN__$PROCESS' % chn
        cb.cp().channel([chn]).era([era]).backgrounds().ExtractShapes(
            rfile, bkg_pattern, bkg_pattern + '__$SYSTEMATIC')
        
        sig_pattern = iPlot+'_'+lumiStr+'_%s$BIN__$PROCESS$MASS' % chn
        #if 'isCR' not in chn:
        cb.cp().channel([chn]).era([era]).signals().ExtractShapes(
                rfile, sig_pattern, sig_pattern + '__$SYSTEMATIC')


def add_bbb(cb):
    print('>> Merging bin errors and generating bbb uncertainties...')
    bbb = ch.BinByBinFactory()
    bbb.SetAddThreshold(0.1).SetMergeThreshold(0.5).SetFixNorm(False)
    
    for chn in chns:
        cb_chn = cb.cp().channel([chn])
        if 'isCR' in chn:
            bbb.MergeAndAdd(cb_chn.cp().era([era]).bin_id([0,1,2,3]).process(bkg_procs[chn]), cb)
            bbb.MergeAndAdd(cb_chn.cp().era([era]).bin_id([0,1,2,3]).process(sig_procs), cb)
        else:
            bbb.MergeAndAdd(cb_chn.cp().era([era]).bin_id([0]).process(bkg_procs[chn]), cb)
            bbb.MergeAndAdd(cb_chn.cp().era([era]).bin_id([0]).process(sig_procs), cb)


def rename_and_write(cb):
    print('>> Setting standardised bin names...')
    ch.SetStandardBinNames(cb)
    
    writer = ch.CardWriter('limits_'+signal+'_'+template+saveKey+'/$TAG/$MASS/$ANALYSIS_$CHANNEL_$BINID_$ERA.txt',
                           'limits_'+signal+'_'+template+saveKey+'/$TAG/common/$ANALYSIS_$CHANNEL.input.root')
    writer.SetVerbosity(1)
    writer.WriteCards('cmb', cb)
    for chn in chns:
        print(chn)
        writer.WriteCards(chn, cb.cp().channel([chn]))
    print('>> Done!')


def print_cb(cb):
    for s in ['Obs', 'Procs', 'Systs', 'Params']:
        print('* %s *' % s)
        getattr(cb, 'Print%s' % s)()
        print


def add_standard_systematics(cb):
    print('>> Adding standard systematic uncertainties...')
    
    signal = cb.cp().signals().process_set()
    

    cb.cp().process(signal + allbkgs).channel(chns).AddSyst(cb, 'lumi_$ERA', 'lnN', ch.SystMap('era')(['R16'], 1.01)(['R16APV'], 1.01)(['R17'], 1.02)(['R18'], 1.015))
    if era!='R16' or  era!='R16APV': cb.cp().process(signal + allbkgs).channel(chns).AddSyst(cb, 'lumi_R1718', 'lnN', ch.SystMap('era')(['R16'], 1.0)(['R16APV'], 1.0)(['R17'], 1.006)(['R18'], 1.002))
    cb.cp().process(signal + allbkgs).channel(chns).AddSyst(cb, 'lumi_Run2', 'lnN', ch.SystMap('era')(['R16'], 1.006)(['R16APV'], 1.006)(['R17'], 1.009)(['R18'], 1.02)) # Full correlated part
    cb.cp().process(signal + allbkgs).channel(chnsE).AddSyst(cb, 'SFel_$ERA', 'lnN', ch.SystMap()(1.06))#('era')(['R16'], 1.06)(['R16APV'], 1.06)(['R17'], 1.06)(['R18'], 1.06)) # 1.5% el id, 2.5%** iso + 5% trigger ~ 3%, doubled trigger uncertainty during OR
    cb.cp().process(signal + allbkgs).channel(chnsM).AddSyst(cb, 'SFmu_$ERA', 'lnN', ch.SystMap()(1.06))#('era')(['R16'], 1.06)(['R16APV'], 1.06)(['R17'], 1.06)(['R18'], 1.06)) # 1% mu id, 2.5%** iso + 2.5% trigger ~ 5%, doubled trigger uncertainty during OR
    cb.cp().process(signal + allbkgs).channel(chns).AddSyst(cb, smoothAlgo+'jec_$ERA', 'shape', ch.SystMap('era')(['R16'], 1.0)(['R16APV'], 1.0)(['R17'], 1.0)(['R18'], 1.0)) # This one is being studied in B2G-19-001/AN2018_322_v7 (take the uncorrelated one to be conservative!)
    cb.cp().process(signal + allbkgs).channel(chns).AddSyst(cb, smoothAlgo+'jer_$ERA', 'shape', ch.SystMap('era')(['R16'], 1.0)(['R16APV'], 1.0)(['R17'], 1.0)(['R18'], 1.0)) # Uncorrelated; Ex: B2G-19-001/AN2018_322_v7#should be fully correlated?

    cb.cp().process(signal + allbkgs).channel(chns).AddSyst(cb, 'pileup_$ERA', 'shape', ch.SystMap('era')(['R16'], 1.0)(['R17'], 1.0)(['R18'], 1.0)) # Uncorrelated; Ex: B2G-19-001/AN2018_322_v7
    cb.cp().process(signal + allbkgs).channel(chns).AddSyst(cb, smoothAlgo+'pileup', 'shape', ch.SystMap()(1.0)) # Correlated: https://hypernews.cern.ch/HyperNews/CMS/get/b2g/1381.html
#    cb.cp().process(signal + allbkgs).channel(chns).AddSyst(cb, 'LF_$ERA', 'shape', ch.SystMap('era')(['R16'], 1.0)(['R16APV'], 1.0)(['R17'], 1.0)(['R18'], 1.0)) # B-tagging reweighting systematics, LF
    cb.cp().process(signal + allbkgs).channel(chns).AddSyst(cb, 'LF_$ERA', 'shape', ch.SystMap()( 1.0 )) # B-tagging reweighting systematics, LF

#        cb.cp().process(signal + allbkgs).channel(chns).AddSyst(cb, 'HF_$ERA', 'shape', ch.SystMap('era')(['R16'], 1.0)(['R16APV'], 1.0)(['R17'], 1.0)(['R18'], 1.0)) #B-tagging reweighting systematics, HF
    cb.cp().process(signal + allbkgs).channel(chns).AddSyst(cb, 'HF_$ERA', 'shape', ch.SystMap()( 1.0 )) #B-tagging reweighting systematics, HF

    cb.cp().process(signal + allbkgs).channel(chns).AddSyst(cb, 'LFstat1_$ERA', 'shape', ch.SystMap('era')(['R16'], 1.0)(['R16APV'], 1.0)(['R17'], 1.0)(['R18'], 1.0))
    cb.cp().process(signal + allbkgs).channel(chns).AddSyst(cb, 'LFstat2_$ERA', 'shape', ch.SystMap('era')(['R16'], 1.0)(['R16APV'], 1.0)(['R17'], 1.0)(['R18'], 1.0))
    cb.cp().process(signal + allbkgs).channel(chns).AddSyst(cb, 'HFstat1_$ERA', 'shape', ch.SystMap('era')(['R16'], 1.0)(['R16APV'], 1.0)(['R17'], 1.0)(['R18'], 1.0))
    cb.cp().process(signal + allbkgs).channel(chns).AddSyst(cb, 'HFstat2_$ERA', 'shape', ch.SystMap('era')(['R16'], 1.0)(['R16APV'], 1.0)(['R17'], 1.0)(['R18'], 1.0))
#    cb.cp().process(signal + allbkgs).channel(chns).AddSyst(cb, 'CFerr1_$ERA', 'shape', ch.SystMap('era')(['R16'], 1.0)(['R16APV'], 1.0)(['R17'], 1.0)(['R18'], 1.0))
#    cb.cp().process(signal + allbkgs).channel(chns).AddSyst(cb, 'CFerr2_$ERA', 'shape', ch.SystMap('era')(['R16'], 1.0)(['R16APV'], 1.0)(['R17'], 1.0)(['R18'], 1.0))
    cb.cp().process(signal + allbkgs).channel(chns).AddSyst(cb, 'CFerr1_$ERA', 'shape', ch.SystMap()( 1.0 ))
    cb.cp().process(signal + allbkgs).channel(chns).AddSyst(cb, 'CFerr2_$ERA', 'shape', ch.SystMap()( 1.0 ))
    cb.cp().process(signal + allbkgs).channel(chns).AddSyst(cb, 'DJjes_$ERA', 'shape', ch.SystMap('era')(['R16'], 1.0)(['R16APV'], 1.0)(['R17'], 1.0)(['R18'], 1.0))

    #for proc in allbkgs:
    #    if proc in ttbkgs: 
    #        cb.cp().process([proc]).channel(chns).AddSyst(cb, smoothAlgo+'muRF_tt', 'shape', ch.SystMap()(1.0)) # Correlated, PDF and QCD Scale (not recalculated in 2018); Ex: B2G-19-001/AN2018_322_v7 
    #        cb.cp().process([proc]).channel(chns).AddSyst(cb, smoothAlgo+'isr_tt', 'shape', ch.SystMap()(1.0)) # Uncorrelated; TOP-18-003/AN2018_062_v17 (derived from different datasets and with respect to different MC samples)
    #        cb.cp().process([proc]).channel(chns).AddSyst(cb, smoothAlgo+'fsr_tt', 'shape', ch.SystMap()(1.0)) # Uncorrelated; TOP-18-003/AN2018_062_v17 (derived from different datasets and with respect to different MC samples)
    #    else: 
    #        cb.cp().process([proc]).channel(chns).AddSyst(cb, smoothAlgo+'muRF_'+proc, 'shape', ch.SystMap()(1.0)) # Correlated, PDF and QCD Scale (not recalculated in 2018); Ex: B2G-19-001/AN2018_322_v7 
    #        cb.cp().process([proc]).channel(chns).AddSyst(cb, smoothAlgo+'isr_'+proc, 'shape', ch.SystMap()(1.0)) # Uncorrelated; TOP-18-003/AN2018_062_v17 (derived from different datasets and with respect to different MC samples)
    #        cb.cp().process([proc]).channel(chns).AddSyst(cb, smoothAlgo+'fsr_'+proc, 'shape', ch.SystMap()(1.0)) # Uncorrelated; TOP-18-003/AN2018_062_v17 (derived from different datasets and with respect to different MC samples)
    #cb.cp().process(signal + allbkgs).channel(chns).AddSyst(cb, smoothAlgo+'pdf', 'shape', ch.SystMap()(1.0)) # Correlated, PDF and QCD Scale (not recalculated in 2018); Ex: B2G-19-001/AN2018_322_v7

    #if era=='R17':
    #    cb.cp().process(signal + allbkgs).channel(chns).AddSyst(cb, 'prefire', 'shape', ch.SystMap()(1.0))
    #cb.cp().process(signal + allbkgs).channel(chns).AddSyst(cb, 'pileup', 'shape', ch.SystMap()(1.0)) # Correlated: https://hypernews.cern.ch/HyperNews/CMS/get/b2g/1381.html
    #cb.cp().process(signal + allbkgs).channel(chns).AddSyst(cb, 'btag_$ERA', 'shape', ch.SystMap('era')(['R16'], 1.0)(['R17'], 1.0)(['R18'], 1.0)) # Uncorrelated; Ex: B2G-19-001/AN2018_322_v7
    #cb.cp().process(signal + allbkgs).channel(chns).AddSyst(cb, 'mistag_$ERA', 'shape', ch.SystMap('era')(['R16'], 1.0)(['R17'], 1.0)(['R18'], 1.0)) # Uncorrelated; Ex: B2G-19-001/AN2018_322_v7
    #cb.cp().process(signal + allbkgs).channel(chns).AddSyst(cb, 'hotstat_$ERA', 'shape', ch.SystMap('era')(['R16'], 1.0)(['R17'], 1.0)(['R18'], 1.0)) # Uncorrelated; Use same logic as b-tagging?
    #cb.cp().process(signal + allbkgs).channel(chns).AddSyst(cb, 'hotcspur_$ERA', 'shape', ch.SystMap('era')(['R16'], 1.0)(['R17'], 1.0)(['R18'], 1.0)) # Uncorrelated; Use same logic as b-tagging?
    #cb.cp().process(signal + allbkgs).channel(chns).AddSyst(cb, 'hotclosure_$ERA', 'shape', ch.SystMap('era')(['R16'], 1.0)(['R17'], 1.0)(['R18'], 1.0)) # Uncorrelated; Use same logic as b-tagging?
    #for proc in allbkgs:
    #    if proc in ttbkgs: cb.cp().process([proc]).channel(chns).AddSyst(cb, 'muRF_tt', 'shape', ch.SystMap()(1.0)) # Correlated, PDF and QCD Scale (not recalculated in 2018); Ex: B2G-19-001/AN2018_322_v7 
    #    else: cb.cp().process([proc]).channel(chns).AddSyst(cb, 'muRF_'+proc, 'shape', ch.SystMap()(1.0)) # Correlated, PDF and QCD Scale (not recalculated in 2018); Ex: B2G-19-001/AN2018_322_v7 
    #cb.cp().process(signal).channel(chns).AddSyst(cb, 'muRF_tttt', 'shape', ch.SystMap()(1.0)) # Correlated, PDF and QCD Scale (not recalculated in 2018); Ex: B2G-19-001/AN2018_322_v7 
    #for proc in allbkgs:
    #    if proc in ttbkgs: cb.cp().process([proc]).channel(chns).AddSyst(cb, 'PSwgt_tt_$ERA', 'shape', ch.SystMap('era')(['R16'], 1.0)(['R17'], 1.0)(['R18'], 1.0)) # Uncorrelated; TOP-18-003/AN2018_062_v17 (derived from different datasets and with respect to different MC samples)
    #    else: cb.cp().process([proc]).channel(chns).AddSyst(cb, 'PSwgt_'+proc+'_$ERA', 'shape', ch.SystMap('era')(['R16'], 1.0)(['R17'], 1.0)(['R18'], 1.0)) # Uncorrelated; TOP-18-003/AN2018_062_v17 (derived from different datasets and with respect to different MC samples)
    #cb.cp().process(signal).channel(chns).AddSyst(cb, 'PSwgt_tttt_$ERA', 'shape', ch.SystMap('era')(['R16'], 1.0)(['R17'], 1.0)(['R18'], 1.0)) # Uncorrelated; TOP-18-003/AN2018_062_v17 (derived from different datasets and with respect to different MC samples)
    #cb.cp().process(signal + allbkgs).channel(chns).AddSyst(cb, 'pdf', 'shape', ch.SystMap()(1.0)) # Correlated, PDF and QCD Scale (not recalculated in 2018); Ex: B2G-19-001/AN2018_322_v7 
     #cb.cp().process(ttbkgs).channel(chns).AddSyst(cb, 'ue', 'shape', ch.SystMap()(1.0))
     #cb.cp().process(ttbkgs).channel(chns).AddSyst(cb, 'hdamp', 'shape', ch.SystMap()(1.0))
     #cb.cp().process(ttbkgs).channel(chns).AddSyst(cb, 'toppt', 'shape', ch.SystMap()(1.0)) # Correlated; Ex: B2G-19-003/AN2015_174_v14 (since it is assumed that the affect of this correction should be consistent across years)
    cb.cp().process( ttbkgs).channel(chns).AddSyst(cb, 'xsec_ttbar', 'lnN', ch.SystMap()([0.956,1.035])) # (scale and pdf added in quadrature) from https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO; Ex: HIG-18-004/AN2017_090_v12/Table13 and HIG-19-011/AN2019_094_v10/Table79-80
    cb.cp().process(['ewk']).channel(chns).AddSyst(cb, 'xsec_ewk', 'lnN', ch.SystMap()(1.038)) # (scale and pdf added in quadrature) from https://twiki.cern.ch/twiki/bin/viewauth/CMS/StandardModelCrossSectionsat13TeV; Ex: HIG-18-004/AN2017_090_v12/Table13 and HIG-19-011/AN2019_094_v10/Table79-80
    cb.cp().process(['top']).channel(chns).AddSyst(cb, 'xsec_top', 'lnN', ch.SystMap()(1.039)) # ttV,ttH, and tt+XY uncertainties are 50% in OSDL and SSDL analyses, so aligning it with this inflated uncertainty.
    # Additional TOP bkg group x-sec uncertainties tested:


def add_HF_systematics(cb):
    print('>> Adding HF systematic uncertainties...')
    
    signal = cb.cp().signals().process_set()
    
    cb.cp().process(['ttbb']).channel(chns).AddSyst(cb, 'ttHF', 'lnN', ch.SystMap()(1.13)) # Uncorrelated; from TOP-18-002 (v34) Table 4, sqrt(0.2^2+0.6^2)/4.7 ~ 0.134565 ~ 0.13


def add_Njet4to6p_systematics(cb):
    print('>> Adding Njet 4-6+ systematic uncertainties with measured priors...')
    
    signal = cb.cp().signals().process_set()
    
    cb.cp().process(ttbkgs).channel(chns_njet[6]+chns_njet[7]+chns_njet[8]+chns_njet[9]+chns_njet[10]).AddSyst(cb, "nJet_$ERA", "lnN", ch.SystMap('era')(['R16'], 1.0)(['R17'], 1.075)(['R18'], 1.048))


def add_Njet4to9p_systematics(cb):
    print('>> Adding Njet 4-9+ systematic uncertainties with measured priors...')
    
    signal = cb.cp().signals().process_set()
    
    cb.cp().process(ttbkgs).channel(chns_njet[6]).AddSyst(cb, "n6Jet_$ERA", "lnN", ch.SystMap('era')(['R16'], 1.0)(['R17'], 1.0517285300268)(['R18'], 1.0442383872209))
    cb.cp().process(ttbkgs).channel(chns_njet[7]).AddSyst(cb, "n7Jet_$ERA", "lnN", ch.SystMap('era')(['R16'], 1.0)(['R17'], 1.0587524161036)(['R18'], 1.0480985065135))
    cb.cp().process(ttbkgs).channel(chns_njet[8]).AddSyst(cb, "n8Jet_$ERA", "lnN", ch.SystMap('era')(['R16'], 1.0)(['R17'], 1.0662112889662)(['R18'], 1.0538322999767))
    cb.cp().process(ttbkgs).channel(chns_njet[9]+chns_njet[10]).AddSyst(cb, "n9pJet_$ERA", "lnN", ch.SystMap('era')(['R16'], 1.0)(['R17'], 1.0800438168504)(['R18'], 1.0622643813546))


def add_Njet4to9p_50p_systematics(cb):
    print('>> Adding Njet 4-9+ systematic uncertainties with 50% priors...')
    
    signal = cb.cp().signals().process_set()
    
    cb.cp().process(ttbkgs).channel(chns_njet[6]).AddSyst(cb, "n6Jet_$ERA", "lnN", ch.SystMap('era')(['R16'], 1.50)(['R17'], 1.50)(['R18'], 1.50))
    cb.cp().process(ttbkgs).channel(chns_njet[7]).AddSyst(cb, "n7Jet_$ERA", "lnN", ch.SystMap('era')(['R16'], 1.50)(['R17'], 1.50)(['R18'], 1.50))
    cb.cp().process(ttbkgs).channel(chns_njet[8]).AddSyst(cb, "n8Jet_$ERA", "lnN", ch.SystMap('era')(['R16'], 1.50)(['R17'], 1.50)(['R18'], 1.50))
    cb.cp().process(ttbkgs).channel(chns_njet[9]+chns_njet[10]).AddSyst(cb, "n9pJet_$ERA", "lnN", ch.SystMap('era')(['R16'], 1.50)(['R17'], 1.50)(['R18'], 1.50))


def add_Njet4to9p_Delta_systematics(cb):
    print('>> Adding Njet 4-9+ systematic uncertainties with Delta(SF, noSF) priors...')
    
    signal = cb.cp().signals().process_set()
    
    cb.cp().process(ttbkgs).channel(chns).AddSyst(cb, 'njetsf_$ERA', 'shape', ch.SystMap('era')(['R16'], 1.0)(['R17'], 1.0)(['R18'], 1.0))


def add_Njet4to9p_50p_centValSF_systematics(cb): #PLACEHOLDER, IT IS NOT SET UP CORRECTLY YET!!!
    print('>> Adding Njet 4-9+ systematic uncertainties with 50% priors and central value set to Njet scale factors...')
    
    signal = cb.cp().signals().process_set()
    
    cb.cp().process(ttbkgs).channel(chns_njet[6]).AddSyst(cb, "n6Jet_$ERA", "lnN", ch.SystMapAsymm('era')(['R16'], 1.0, 1.0)(['R17'], 0.57566620169, 1.57566620169)(['R18'], 0.48448056055, 1.48448056055))
    cb.cp().process(ttbkgs).channel(chns_njet[7]).AddSyst(cb, "n7Jet_$ERA", "lnN", ch.SystMapAsymm('era')(['R16'], 1.0, 1.0)(['R17'], 0.60904592910, 1.60904592910)(['R18'], 0.54462767888, 1.54462767888))
    cb.cp().process(ttbkgs).channel(chns_njet[8]).AddSyst(cb, "n8Jet_$ERA", "lnN", ch.SystMapAsymm('era')(['R16'], 1.0, 1.0)(['R17'], 0.71705307722, 1.71705307722)(['R18'], 0.59013888621, 1.59013888621))
    cb.cp().process(ttbkgs).channel(chns_njet[9]+chns_njet[10]).AddSyst(cb, "n9pJet_$ERA", "lnN", ch.SystMapAsymm('era')(['R16'], 1.0, 1.0)(['R17'], 0.7377932283, 1.7377932283)(['R18'], 0.7000888232, 1.7000888232))


def add_autoMCstat(cb):
    print('>> Adding autoMCstats...')
    cb.AddDatacardLineAtEnd('* autoMCStats 1.')


def create_workspace(cb):
    print('>> Creating workspace...')
    
    for chn in ['cmb']:#+chns:
        chnDir = os.getcwd()+'/limits_'+signal+'_'+template+saveKey+'/'+chn+'/'
        cmd = 'combineTool.py -M T2W -i '+chnDir+' -o workspace.root --parallel 4'
        os.system(cmd)
        

def go(cb):
    add_processes_and_observations(cb)
    add_standard_systematics(cb)
    add_HF_systematics(cb)
    #add_Njet4to9p_systematics(cb)
    add_shapes(cb)
    #add_bbb(cb)
    add_autoMCstat(cb)
    rename_and_write(cb)
    create_workspace(cb)
    #print_cb(cb)


if __name__ == '__main__':
    cb = ch.CombineHarvester()
    #cb.SetVerbosity(20)
    signal = 'Hptb'+sys.argv[4]
    iPlot= sys.argv[3]#'HT'
    era = sys.argv[2]#'R18'
    template = sys.argv[1]
    if era=='R16': lumiStr = '16p726fb'
    elif era=='R16APV': lumiStr = '19p52fb'
    elif era=='R17': lumiStr = '41p53fb'
    elif era=='R18': lumiStr = '59p83fb'
    #lumiStr = '41p53fb'
    #if era=='R18': lumiStr = '59p83fb'
    #if era=='R16': lumiStr = '16p726fb'
       
    smoothAlgo = '' 
    tag = '_wNegBinsCorrec_'#'_50GeV_100GeVnB2'
    saveKey = '_'+iPlot+"_QCDsup_Full"#'_Njet50pct_centValSF'
    fileDir = '/home/jluo48/ChargedHiggs/CMSSW_10_2_10/src/ChargedHiggs/SingleLepAnalyzer/makeTemplates/'#templates_M500_2023_5_1_topPtRW_NOHTWeight_Full_FixTrig_forlimit#'/uscms_data/d3/jluo/work/CMSSW_dir/CMSSW_10_2_10/src/NewCHiggs_UL/SingleLepAnalyzer/makeTemplates/'
    #template = 'M500_2020_11_23_topPtRW_NC_allweights_DJ'#era+'_'+sys.argv[3]#nonjetsf_lepPt20_2020_9_3'
    if not os.path.exists('./limits_'+signal+'_'+template+saveKey): os.system('mkdir ./limits_'+signal+'_'+template+saveKey)
    os.system('cp '+fileDir+'templates_'+template+'/templates_'+iPlot+'_'+lumiStr+tag+'_rebinned_stat0p1.root ./limits_'+signal+'_'+template+saveKey+'/')
    rfile = './limits_'+signal+'_'+template+saveKey+'/templates_'+iPlot+'_'+lumiStr+tag+'_rebinned_stat0p1.root'
    
    ttbkgs = ['ttnobb','ttbb'] # ['ttjj','ttcc','ttbb','ttbj']
    allbkgs = ttbkgs + ['top','ewk', 'qcd']
    dataName = 'data_obs'
    tfile = TFile(rfile)
    allHistNames = [k.GetName() for k in tfile.GetListOfKeys() if not (k.GetName().endswith('Up') or k.GetName().endswith('Down'))]
    tfile.Close()
    chns = [hist[hist.find('fb_')+3:hist.find('__')] for hist in allHistNames if '__'+dataName in hist]
    chnsE = [chn for chn in chns if 'isE_' in chn]
    chnsM = [chn for chn in chns if 'isM_' in chn]
    chns_njet = {}
    for i in range(4,11):
        chns_njet[i]=[chn for chn in chns if 'nJ'+str(i) in chn]
    bkg_procs = {chn:[hist.split('__')[-1] for hist in allHistNames if '_'+chn+'_' in hist and not (hist.endswith('Up') or hist.endswith('Down') or hist.endswith(dataName) or hist.find('Hptb')!=-1)] for chn in chns}
    for cat in sorted(bkg_procs.keys()):
        print(cat,bkg_procs[cat])
        #if 'qcd' in bkg_procs[cat]:
        #    print '        Removing qcd ...'
        #    bkg_procs[cat]=bkg_procs[cat][:-1]
#     if era=='R18':
#         bkg_procs['isSR_isE_nHOT1p_nT0p_nW0p_nB4p_nJ9']=['ttbb', 'ttcc', 'ttjj', 'top']
    
    sig_procs = [signal]
    
    cats = {}
    for chn in chns: cats[chn] = [(0, '')]
    
    #masses = ch.ValsFromRange('690')
    go(cb)
