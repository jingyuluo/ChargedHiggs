import os, sys
import time
import getopt
import argparse
import ROOT
import array
import varsList
import numpy as np
import uproot
import pandas as pd
#import root_pandas
#from root_pandas import to_root
#from ROOT import TMVA
#from ROOT import RDataFrame
import xgboost as xgb
from xgboost import XGBClassifier
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

############################################################
# Copy the entire step-2 TTree, add XGB, save to a new TTree
############################################################

parser = argparse.ArgumentParser(description='Apply XGB for charged Higgs search')
parser.add_argument("-k", "--varListKey", default="NewVar", help="Input variable list")
parser.add_argument("-f", "--file", default="ChargedHiggs_HplusTB_HplusToTB_M-1000_13TeV_amcatnlo_pythia8_hadd.root", help="The name of the input file")
parser.add_argument("-o", "--output", help="The label for the output file")

args = parser.parse_args()

varListKey = args.varListKey
varList = varsList.varList[varListKey]
inputDir = varsList.inputDir
infname = args.file

print("Load Input File")

bst = xgb.Booster()
bst.load_model("XGB500iterations_4depths_signal_region_NewVar_NewVar_FeatureNamed.model")

train_var = []
for ivar in varList:
    train_var.append(ivar[0])
sig_tree = uproot.open(inputDir+infname)["ljmet"]
numentries = sig_tree.numentries

tfile = ROOT.TFile.Open(inputDir+infname)
ttree = tfile.Get("ljmet")


newfile = ROOT.TFile("NewOutput.root", "RECREATE")
newfile.cd()

newtree = ttree.CloneTree(0) 
XGB = array.array('d', [0])
newtree.Branch("XGB", XGB, "XGB/D")

iev=0
for chunk in sig_tree.iterate("*", entrysteps=1, namedecode="utf-8"):

    print(iev)
    array_var=[]
    for var in train_var:
        array_var.append(chunk[var])
    dataset = np.column_stack(array_var)
    dX = xgb.DMatrix(dataset, feature_names=train_var)
    XGB[0] = bst.predict(dX)
    ttree.GetEntry(iev)
    newtree.Fill()
    iev+=1    


newfile.WriteTObject(newtree, "ljmet")
newfile.Close()

