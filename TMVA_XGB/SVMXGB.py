import os, sys
import time

import argparse
import ROOT as r
#import varsList

import xgboost as xgb


parser = argparse.ArgumentParser(description='Multivariate analysis for charged Higgs search')
parser.add_argument("-i", "--input", default=".", help="The input directory")
parser.add_argument("-m", "--mass", default="500", help="The signal mass point")

args = parser.parse_args()

dtrain = xgb.DMatrix(args.input+"/dtrainM"+args.mass+".dat#dtrainM"+args.mass+".cache")
dtest = xgb.DMatrix(args.input+"/dtestM"+args.mass+".dat#dtestM"+args.mass+".cache")

watchlist = [(dtrain, 'train'), (dtest, 'eval')]#[(dtest, 'eval'), (dtrain, 'train')]
param = {
    'max_depth': 2,  # the maximum depth of each tree
    'eta': 0.05,  # the training step for each iteration
    'silent': 0,  # logging mode - quiet
    'objective': 'binary:logistic',  # error evaluation for classification training
    #'scale_pos_weight': 30.4915530986, 
    'eval_metric': 'auc',
    'subsample': 0.8
    }  # the number of classes that exist in this datset
num_round = 700  # the number of training iterations

bst = xgb.train(param, dtrain, num_round, watchlist, callbacks=[xgb.callback.print_evaluation()], early_stopping_rounds=10)
#bst = xgb.train(param, dtrain, num_round, nfold=5, metrics={'auc'}, seed=10)
print bst

bst.dump_model('dump.raw_M'+args.mass+'.txt')
bst.save_model('XGB_test_M'+args.mass+'.model')
#bst.dump_model('dump.raw'+str(num_round)+'iterations'+"_"+str(param['max_depth'])+'depths_'+str(param['eta'])+'signal_region_'+str(args.varListKey)+'_'+args.label+'_Mtest'+'.txt')
#bst.save_model('XGB'+str(num_round)+'iterations'+"_"+str(param['max_depth'])+'depths_'+str(param['eta'])+'signal_region_'+str(args.varListKey)+'_'+args.label+'_M'+args.mass+'.model')


