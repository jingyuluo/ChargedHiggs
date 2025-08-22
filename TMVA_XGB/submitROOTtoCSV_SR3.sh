#!/bin/bash

outputDir=${1}
mass=${2}
vListKey=${3}
scratch=${PWD}

source /cvmfs/cms.cern.ch/cmsset_default.sh

export SCRAM_ARCH=el9_amd64_gcc12

scramv1 project CMSSW CMSSW_14_0_19
cd CMSSW_14_0_19/src
eval `scramv1 runtime -sh`
cd -

macroDir=${PWD}

export HOME=${PWD}

export PATH=$PATH:$macroDir

#source /cvmfs/sft.cern.ch/lcg/contrib/gcc/7.3.0/x86_64-centos7-gcc7-opt/setup.sh
#source /cvmfs/sft.cern.ch/lcg/app/releases/ROOT/6.16.00/x86_64-centos7-gcc48-opt/bin/thisroot.sh
#xrdcp -f ${haddFile} root://cmseos.fnal.gov/${outputDir//$NOM/$SHIFT}/${haddFile//${SHIFT}_hadd/} 2>&1

python3 UpROOTtoCSV_SR3.py  -k $vListKey -m ${mass} 

cp  dtrainM${mass}.csv $outputDir/
cp  dtestM${mass}.csv $outputDir/
cp  *txt $outputDir/
cp  *weight $outputDir/ 

rm -r CMSSW_14_0_19

rm *csv
rm *weight
