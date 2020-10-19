import os, sys
import time
import getopt
import argparse
import ROOT as r
import varsList
import numpy as np
import uproot
import pandas as pd
import root_pandas
from root_pandas import to_root
from ROOT import TMVA
from ROOT import RDataFrame
import xgboost as xgb
from xgboost import XGBClassifier
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


#Light version of the XGB application, only saving training variables and XGB in the output TTree

parser = argparse.ArgumentParser(description='Apply XGB for charged Higgs search')
parser.add_argument("-k", "--varListKey", default="NewVar", help="Input variable list")
parser.add_argument("-f", "--file", default="ChargedHiggs_HplusTB_HplusToTB_M-300_13TeV_amcatnlo_pythia8_hadd.root", help="The name of the input file")
parser.add_argument("-o", "--output", help="The label for the output file")

args = parser.parse_args()

varListKey = args.varListKey
varList = varsList.varList[varListKey]
inputDir = varsList.inputDir
infname = args.file#"ChargedHiggs_HplusTB_HplusToTB_M-500_13TeV_amcatnlo_pythia8_hadd.root"

train_var = []
for ivar in varList:
    train_var.append(ivar[0])

print "Load Input File"

sig_tree = uproot.open(inputDir+infname)["ljmet"]
sigdf_var = sig_tree.pandas.df(branches=train_var)


#print "Loading Background Samples"
#back_dfs = []
#
#bkgList = varsList.bkg
#for ibkg in bkgList:
#    print ibkg
#    bkg_tree = uproot.open(inputDir+ibkg)["ljmet"]
#    bkg_df = bkg_tree.pandas.df(branches=(iVar[0] for iVar in varList+selList+weightList))
#    print bkg_df
#    bkg_selected = (bkg_df["NJets_JetSubCalc"]>4)&(bkg_df["NJetsCSV_JetSubCalc"]>1)&( ((bkg_df["leptonPt_MultiLepCalc"]>35)&(bkg_df["isElectron"]==True))|((bkg_df["leptonPt_MultiLepCalc"]>30)&(bkg_df["isMuon"]==True)))
#    bkg_df = bkg_df[bkg_selected]
#    print bkg_df
#    back_dfs.append(bkg_df)
#
#bkgall_df = pd.concat(back_dfs)
#del back_dfs

#bkgall_df.loc[:, "isSignal"] = np.zeros(bkgall_df.shape[0])

#dfall = pd.concat([sig_df, bkgall_df])


NDIM = len(sigdf_var.columns)
X = sigdf_var.values
 

dX = xgb.DMatrix(X, feature_names=train_var)

bst = xgb.Booster()
bst.load_model("XGB500iterations_4depths_signal_region_NewVar_NewVar_FeatureNamed.model")

sigdf_var.loc[:, "XGB"] = bst.predict(dX)

print sigdf_var

sigdf_var.to_root(args.output+".root", key="ljmet")

