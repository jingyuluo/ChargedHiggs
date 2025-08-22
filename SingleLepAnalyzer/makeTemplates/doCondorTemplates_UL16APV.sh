#!/bin/bash

condorDir=$PWD
theDir=$1
iPlot=$2
region=$3
isCategorized=$4
isEM=$5
nttag=$6
nWtag=$7
nbtag=$8
njets=$9
sigTrained=${10}

#source /cvmfs/cms.cern.ch/cmsset_default.sh
#setenv ROOTSYS /cvmfs/cms.cern.ch/slc7_amd64_gcc700/lcg/root/6.12.07-gnimlf5/
#scram p CMSSW CMSSW_10_2_10
#cd CMSSW_10_2_10
##cmsenv
##cd $theDir
#eval `scramv1 runtime -sh`
#cd ../
#rm -r CMSSW_10_2_10

source /cvmfs/sft.cern.ch/lcg/views/LCG_107/x86_64-el9-gcc11-opt/setup.sh

curDir=${PWD}

macroDir=${PWD}

export HOME=${PWD}

export PATH=$PATH:$macroDir



python3 doHists_UL16APV.py ./ $iPlot $region $isCategorized $isEM $nttag $nWtag $nbtag $njets $sigTrained
