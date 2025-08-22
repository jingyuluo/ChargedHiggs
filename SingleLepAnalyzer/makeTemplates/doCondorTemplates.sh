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
tmpDir=${11}

#source /cvmfs/cms.cern.ch/cmsset_default.sh
source /cvmfs/sft.cern.ch/lcg/views/LCG_107/x86_64-el9-gcc11-opt/setup.sh
#export SCRAM_ARCH=el9_amd64_gcc12
curDir=${PWD}

#mkdir $tmpDir
#cd $tmpDir
#
#scramv1 project CMSSW CMSSW_14_0_19
#cd CMSSW_14_0_19/src
#eval `scramv1 runtime -sh`
#cd $curDir


macroDir=${PWD}

export HOME=${PWD}

export PATH=$PATH:$macroDir


#setenv ROOTSYS /cvmfs/cms.cern.ch/slc7_amd64_gcc700/lcg/root/6.12.07-gnimlf5/
#scram p CMSSW CMSSW_10_2_10
#cd CMSSW_10_2_10
#cmsenv
#cd $theDir
#eval `scramv1 runtime -sh`
#cd ../
#rm -r CMSSW_10_2_10


python3 doHists.py ./ $iPlot $region $isCategorized $isEM $nttag $nWtag $nbtag $njets $sigTrained

#rm -r $tmpDir
