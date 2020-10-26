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
import keras
from root_pandas import to_root
from ROOT import TMVA
from ROOT import RDataFrame
import xgboost as xgb
from xgboost import XGBClassifier
import sklearn 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler 

parser = argparse.ArgumentParser(description='Multivariate analysis for charged Higgs search')
parser.add_argument("-k", "--varListKey", default="BigComb", help="Input variable list")
parser.add_argument("-l", "--label", default="", help="label for output file")


args = parser.parse_args()


selList = [["NJetsCSV_JetSubCalc", ""],["NJets_JetSubCalc", ""], ["leptonPt_MultiLepCalc", ""],  ["isElectron", ""], ["isMuon", ""]]
weightList = [["pileupWeight", ""], ["lepIdSF", ""], ["EGammaGsfSF", ""], ["MCWeight_MultiLepCalc", ""]] 
varListKey = args.varListKey
varList = varsList.varList[varListKey]
inputDir = varsList.inputDir
infname = "ChargedHiggs_HplusTB_HplusToTB_M-500_13TeV_amcatnlo_pythia8_hadd.root"

print "Loading Signal Sample"

sig_tree = uproot.open(inputDir+infname)["ljmet"]
sig_df = sig_tree.pandas.df(branches=(iVar[0] for iVar in varList+selList+weightList))

#Event Selection
 
sig_selected = (sig_df["NJets_JetSubCalc"]>4)&(sig_df["NJetsCSV_JetSubCalc"]>1)&( ((sig_df["leptonPt_MultiLepCalc"]>35)&(sig_df["isElectron"]==True))|((sig_df["leptonPt_MultiLepCalc"]>30)&(sig_df["isMuon"]==True))) 

sig_df = sig_df[sig_selected]

print "Loading Background Samples"
back_dfs = []

bkgList = varsList.bkg
for ibkg in bkgList:
    print ibkg
    bkg_tree = uproot.open(inputDir+ibkg)["ljmet"]
    bkg_df = bkg_tree.pandas.df(branches=(iVar[0] for iVar in varList+selList+weightList))
    print bkg_df
    bkg_selected = (bkg_df["NJets_JetSubCalc"]>4)&(bkg_df["NJetsCSV_JetSubCalc"]>1)&( ((bkg_df["leptonPt_MultiLepCalc"]>35)&(bkg_df["isElectron"]==True))|((bkg_df["leptonPt_MultiLepCalc"]>30)&(bkg_df["isMuon"]==True)))
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


X_train_val = X[isTrain]
Y_train_val = Y[isTrain]
weight_train_val = weightall[isTrain]

X_test = X[isTrain==False]
Y_test = Y[isTrain==False]
weight_test = weightall[isTrain==False]


from keras.callbacks import EarlyStopping
early_stopping = EarlyStopping(monitor='val_loss', patience=100)

from keras.callbacks import ModelCheckpoint
model_checkpoint = ModelCheckpoint('dense_model.h5', monitor='val_loss', 
                                    verbose=0, save_best_only=True, 
                                    save_weights_only=False, mode='auto', 
                                    period=1)


from keras.models import Sequential, Model
from keras.optimizers import SGD 
from keras.layers import Input, Activation, Dense, Convolution2D, MaxPooling2D, Dropout, Flatten
from keras.utils import np_utils


inputs = Input(shape=(NDIM-1,), name = 'input')
x = Dense(100, activation='sigmoid', kernel_initializer='lecun_uniform')(inputs)
x = Dropout(0.1)(x)
x = Dense(100, activation='sigmoid', kernel_initializer='lecun_uniform')(x)
x = Dropout(0.1)(x)
x = Dense(100, activation='sigmoid', kernel_initializer='lecun_uniform')(x)
x = Dropout(0.1)(x)
x = Dense(100, activation='sigmoid', kernel_initializer='lecun_uniform')(x)
x = Dropout(0.1)(x)
x = Dense(100, activation='sigmoid', kernel_initializer='lecun_uniform')(x)
outputs = Dense(1, name = 'output', kernel_initializer='lecun_uniform', activation='sigmoid')(x)

model = Model(inputs=inputs, outputs=outputs)
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.summary()

history = model.fit(X_train_val, 
                    Y_train_val, sample_weight = weight_train_val,
                    epochs=4000, 
                    batch_size=1000, 
                    verbose=1, # switch to 1 for more verbosity 
                    callbacks=[early_stopping, model_checkpoint], 
                    validation_split=0.25)

dfall_var.loc[:, 'DNN'] = model.predict(X)

dfall_var.to_root("test_DNN_classification_"+str(args.varListKey)+"_"+args.label+".root", key="DNN_Tree") 

##X_train_val, X_test, Y_train_val, Y_test, weight_train_val, weight_test = train_test_split(X, Y, weightall, test_size=0.3, random_state=7)
#
#X_train_val = X[isTrain]
#Y_train_val = Y[isTrain]
#weight_train_val = weightall[isTrain]
#
#X_test = X[isTrain==False]
#Y_test = Y[isTrain==False]
#weight_test = weightall[isTrain==False]

#del isTrain
#del weightall
#del dfall

#dall = xgb.DMatrix(X)
#dtrain = xgb.DMatrix(X_train_val, label=Y_train_val, weight=weight_train_val)
#dtest = xgb.DMatrix(X_test, label=Y_test, weight=weight_test)
#watchlist = [(dtrain, 'train'), (dtest, 'eval')]#[(dtest, 'eval'), (dtrain, 'train')]
#param = {
#    'max_depth': 4,  # the maximum depth of each tree
#    'eta': 0.1,  # the training step for each iteration
#    'silent': 0,  # logging mode - quiet
#    'objective': 'binary:logistic',  # error evaluation for classification training
#    'scale_pos_weight': scale,
#    'eval_metric': 'auc',
#    'subsample': 0.6
#    }  # the number of classes that exist in this datset
#num_round = 500  # the number of training iterations
#
#bst = xgb.train(param, dtrain, num_round, watchlist, callbacks=[xgb.callback.print_evaluation()], early_stopping_rounds=30)
##bst = xgb.train(param, dtrain, num_round, nfold=5, metrics={'auc'}, seed=10)
#print bst
#dfall_var.loc[:, 'XGB'] = bst.predict(dall)
#bst.dump_model('dump.raw'+str(num_round)+'iterations'+"_"+str(param['max_depth'])+'depths_signal_region_'+str(args.varListKey)+'_'+args.label+'.txt')
#bst.save_model('XGB'+str(num_round)+'iterations'+"_"+str(param['max_depth'])+'depths_signal_region_'+str(args.varListKey)+'_'+args.label+'.model')
##print dfall_var
#
#dfall_var.to_root("test_XGB_classification_"+str(args.varListKey)+"_"+args.label+".root", key="XGB_Tree")






#df_sig = RDataFrame("ljmet", inputDir+infname) 
#
#data_sig = df_sig.AsNumpy(columns=(iVar[0] for iVar in varList)) 
#
#
#print "Loading Background Samples"
#bkgList = varsList.bkg
#bkgfilelist = []
#for ibkg in bkgList:
#    print ibkg
#    bkgfilelist.append(inputDir+ibkg)
#
#chain = r.TChain("ljmet")
#for bkgfile in bkgfilelist:
#    chain.Add(bkgfile)
#
#df_back = RDataFrame(chain)
#data_bkg = df_back.AsNumpy(columns=(iVar[0] for iVar in varList))
#
#
#x_sig = np.vstack([data_sig[iVar[0]] for iVar in varList]).T
#
#x_bkg = np.vstack([data_bkg[iVar[0]] for iVar in varList]).T
#
#x = np.vstack([x_sig, x_bkg])
#
#num_sig = x_sig.shape[0]
#num_bkg = x_bkg.shape[0]
#
#y = np.hstack([np.ones(num_sig), np.zeros(num_bkg)])
#
#print "Prepare Training"
#num_all = num_sig + num_bkg
#
#w = np.hstack([np.ones(num_sig) * num_all / num_sig, np.ones(num_bkg) * num_all / num_bkg])
#
#x_train, x_test, y_train, y_test, w_train, w_test = train_test_split(x, y, w, test_size=0.3, random_state=7)
#
#dall = xgb.DMatrix(x, label=y, weight=w)
#dtrain = xgb.DMatrix(x_train, label=y_train, weight=w_train)
#dtest = xgb.DMatrix(x_test, label=y_test, weight=w_test)
#watchlist = [(dtest, 'eval'), (dtrain, 'train')]
#
#param = { 
#    'max_depth': 3,  # the maximum depth of each tree
#    'eta': 0.1,  # the training step for each iteration
#    'silent': 0,  # logging mode - quiet
#    'objective': 'binary:logistic',  # error evaluation for multiclass training
#    #'scale_pos_weight': 1/weight,
#    'eval_metric': 'auc',
#    'subsample': 0.6 
#    }  # the number of classes that exist in this datset
#num_round = 600  # the number of training iterations
#bst = xgb.train(param, dtrain, num_round, watchlist, callbacks=[xgb.callback.print_evaluation()], early_stopping_rounds=30)


#bdt = XGBClassifier(max_depth=3, n_estimators=500, verbosity=2)
#print "Start Training"
#bdt.fit(x, y, w)
#TMVA.Experimental.SaveXGBoost(bdt, "myBDT", "tmva101.root")
