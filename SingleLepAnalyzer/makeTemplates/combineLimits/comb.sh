#!/bin/bash

Mass=${1}

source /cvmfs/cms.cern.ch/cmsset_default.sh
cd /home/jluo48/CMSSW_10_2_13/src
eval `scramv1 runtime -sh`
cd HiggsAnalysis/CHiggs_Dirs/limits_Hptb${Mass}_M500_2021_3_2_topPtRW_allweights_UL17_Reshape_ReNorm2D_HTnj_XGBs_split_XGB${Mass}
combine -M AsymptoticLimits cmb/workspace.root --run=blind --cminDefaultMinimizerStrategy 0 &> asy_m${Mass}.txt
