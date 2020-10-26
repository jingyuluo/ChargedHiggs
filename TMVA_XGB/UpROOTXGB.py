import os, sys
import time
import getopt
import argparse
import ROOT as r
import varsList
import numpy as np
import uproot 
#import shap
import pandas as pd
import root_pandas
import matplotlib.pyplot as plt
from root_pandas import to_root
from ROOT import TMVA
from ROOT import RDataFrame
import xgboost as xgb
from xgboost import XGBClassifier
import sklearn 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler 

#parser = argparse.ArgumentParser(description='Multivariate analysis for charged Higgs search')
#parser.add_argument("-k", "--varListKey", default="NewVar", help="Input variable list")
#parser.add_argument("-l", "--label", default="", help="label for output file")
#args = parser.parse_args()

DEFAULT_OUTFNAME = "XGB.root"
DEFAULT_INFNAME  = "180"
DEFAULT_TREESIG  = "TreeS"
DEFAULT_TREEBKG  = "TreeB"
DEFAULT_NITS   = "100"
DEFAULT_MDEPTH   = "2"#str(len(varList))
DEFAULT_VARLISTKEY = "BigComb"
DEFAULT_SIGMASS = "M-1000"


shortopts  = "f:n:d:s:l:t:o:vh?"
longopts   = ["inputfile=", "nTrees=", "maxDepth=", "sigMass=", "varListKey=", "inputtrees=", "outputfile=", "verbose", "help", "usage"]
opts, args = getopt.getopt( sys.argv[1:], shortopts, longopts )
    
infname     = DEFAULT_INFNAME
treeNameSig = DEFAULT_TREESIG
treeNameBkg = DEFAULT_TREEBKG
outfname    = DEFAULT_OUTFNAME
nIts        = DEFAULT_NITS
mDepth      = DEFAULT_MDEPTH
varListKey  = DEFAULT_VARLISTKEY
sigMass     = DEFAULT_SIGMASS
verbose     = True    

for o, a in opts:
    if o in ("-?", "-h", "--help", "--usage"):
        usage()
        sys.exit(0)
    elif o in ("-d", "--maxDepth"):
        mDepth = a
    elif o in ("-l", "--varListKey"):
        varListKey = a
    elif o in ("-f", "--inputfile"):
        infname = a
    elif o in ("-n", "--nIts"):
        nIts = a
    elif o in ("-o", "--outputfile"):
        outfname = a
    elif o in ("-s", "--sigMass"):
        sigMass = a




selList = [["NJetsCSV_JetSubCalc", ""],["NJets_JetSubCalc", ""], ["leptonPt_MultiLepCalc", ""],  ["isElectron", ""], ["isMuon", ""],["DataPastTrigger",""],["MCPastTrigger"]]
weightList = [["pileupWeight", ""], ["lepIdSF", ""], ["EGammaGsfSF", ""], ["MCWeight_MultiLepCalc", ""]] 
varList = varsList.varList[varListKey]
inputDir = varsList.inputDir
infname = "ChargedHiggs_HplusTB_HplusToTB_"+sigMass+"_13TeV_amcatnlo_pythia8_hadd.root"
print "Loading Signal Sample"
sig_tree = uproot.open(inputDir+infname)["ljmet"]
sig_df = sig_tree.pandas.df(branches=(iVar[0] for iVar in varList+selList+weightList))

#Event Selection
print(sig_df[sig_df.index.duplicated()]) 
sig_selected = (sig_df["NJets_JetSubCalc"]>4)&(sig_df["NJetsCSV_JetSubCalc"]>1)&( ((sig_df["leptonPt_MultiLepCalc"]>35)&(sig_df["isElectron"]==True))|((sig_df["leptonPt_MultiLepCalc"]>30)&(sig_df["isMuon"]==True)))&(sig_df["MCPastTrigger"]==1)&(sig_df["DataPastTrigger"]==1)&(sig_df["corr_met_MultiLepCalc"]>30)

sig_df = sig_df[sig_selected]

print "Loading Background Samples"
back_dfs = []

bkgList = varsList.bkg
print bkgList
for ibkg in bkgList:
    print ibkg
    bkg_tree = uproot.open(inputDir+ibkg)["ljmet"]
    bkg_df = bkg_tree.pandas.df(branches=(iVar[0] for iVar in varList+selList+weightList))
    print bkg_df
    bkg_selected = (bkg_df["NJets_JetSubCalc"]>4)&(bkg_df["NJetsCSV_JetSubCalc"]>1)&( ((bkg_df["leptonPt_MultiLepCalc"]>35)&(bkg_df["isElectron"]==True))|((bkg_df["leptonPt_MultiLepCalc"]>30)&(bkg_df["isMuon"]==True)))&(bkg_df["MCPastTrigger"]==1)&(bkg_df["DataPastTrigger"]==1)&(bkg_df["corr_met_MultiLepCalc"]>30)
    bkg_df = bkg_df[bkg_selected]
    print bkg_df
    back_dfs.append(bkg_df)

#print back_dfs
bkgall_df = pd.concat(back_dfs)
del back_dfs

#compute Weights 
weightSig = sig_df['pileupWeight']*sig_df['lepIdSF']*sig_df['EGammaGsfSF']*sig_df['MCWeight_MultiLepCalc']/(abs(sig_df['MCWeight_MultiLepCalc']))
weightBkg = bkgall_df['pileupWeight']*bkgall_df['lepIdSF']*bkgall_df['EGammaGsfSF']*bkgall_df['MCWeight_MultiLepCalc']/(abs(bkgall_df['MCWeight_MultiLepCalc']))

sigtotalWeight = np.sum(weightSig)
bkgtotalWeight = np.sum(weightBkg)

#compute the weight ratio to balance the training for XGBoost
scale = float(bkgtotalWeight)/float(sigtotalWeight)

randnum = np.random.rand(sig_df.shape[0]+bkgall_df.shape[0])
isTrain = randnum>0.2

#assign label
sig_df.loc[:,"isSignal"] = np.ones(sig_df.shape[0])
bkgall_df.loc[:, "isSignal"] = np.zeros(bkgall_df.shape[0])

dfall = pd.concat([sig_df, bkgall_df])

weightall = np.append(weightSig, weightBkg)

print dfall

train_var = []
for ivar in varList:
    train_var.append(ivar[0])
train_var.append("isSignal")
dfall_var = dfall.loc[:, train_var]

NDIM = len(dfall_var.columns)
dataset = dfall_var.values

X = dataset[:, 0:NDIM-1]
Y = dataset[:, NDIM-1]

dfall_var.loc[:, "isTrain"] = isTrain
dfall_var.loc[:, "Weight"] = weightall
print Y


#X_train_val, X_test, Y_train_val, Y_test, weight_train_val, weight_test = train_test_split(X, Y, weightall, test_size=0.3, random_state=7)

X_train_val = X[isTrain]
Y_train_val = Y[isTrain]
weight_train_val = weightall[isTrain]

X_test = X[isTrain==False]
Y_test = Y[isTrain==False]
weight_test = weightall[isTrain==False]

features = train_var[0:NDIM-1]
print features
print len(features)
print X_test.shape[1]
#del isTrain
#del weightall
#del dfall

dall = xgb.DMatrix(X, feature_names=features)
dtrain = xgb.DMatrix(X_train_val, label=Y_train_val, weight=weight_train_val, feature_names=features)
dtest = xgb.DMatrix(X_test, label=Y_test, weight=weight_test, feature_names=features)
watchlist = [(dtrain, 'train'), (dtest, 'eval')]#[(dtest, 'eval'), (dtrain, 'train')]
param = {
    'max_depth': int(mDepth),  # the maximum depth of each tree
    'eta': 0.1,  # the training step for each iteration
    'silent': 0,  # logging mode - quiet
    'objective': 'binary:logistic',  # error evaluation for classification training
    'scale_pos_weight': scale,
    'eval_metric': 'auc',
    'subsample': 0.8
    }  # the number of classes that exist in this datset
num_round = int(nIts)  # the number of training iterations

bst = xgb.train(param, dtrain, num_round, watchlist, callbacks=[xgb.callback.print_evaluation()], early_stopping_rounds=10)
#bst = xgb.train(param, dtrain, num_round, nfold=5, metrics={'auc'}, seed=10)
dfall_var.loc[:, 'XGB'] = bst.predict(dall)
bst.dump_model('training_output/dump.raw'+str(num_round)+'iterations'+"_"+str(param['max_depth'])+'depths_signal_region_'+str(varListKey)+'_'+sigMass+'.txt')
bst.save_model('training_output/XGB'+str(num_round)+'iterations'+"_"+str(param['max_depth'])+'depths_signal_region_'+str(varListKey)+'_'+sigMass+'.model')
#print dfall_var

dfall_var.to_root("training_output/test_XGB_classification_"+str(varListKey)+"_M-"+sigMass+".root", key="XGB_Tree")


### Plot Variable Importance Information
# fig,ax = plt.subplots(figsize=(4,5))
# bst.get_score(importance_type='gain')
# xgb.plot_importance(bst, importance_type='gain', ax=ax,  max_num_features = 10, xlabel = 'Gain', ylabel = 'Var', title = 'XGB Training Output')
# ax.grid(b = False)
# plt.tight_layout()
# plt.savefig('training_output/plots/XGB'+str(num_round)+'iterations'+"_"+str(param['max_depth'])+'depths_signal_region_'+str(varListKey)+'_'+sigMass+'.png')

# t0 = time.time()
# print "Begining SHAP explainer"
# explainer = shap.TreeExplainer(bst)
# shap_values = explainer.shap_values(X)
# t1 = time.time()
# print t1-t0 + "Seconds?"
# shap.summary_plot(shap_values, "placeholder", plot_type = "bar")
