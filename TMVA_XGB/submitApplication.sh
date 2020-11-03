#!/bin/bash

inputfile=${1}
outputDir=${2}
fileName=${3}
vListKey=${4}
scratch=${PWD}

source /cvmfs/cms.cern.ch/cmsset_default.sh

export SCRAM_ARCH=slc7_amd64_gcc820

scramv1 project CMSSW CMSSW_11_1_0_pre7
cd CMSSW_11_1_0_pre7
eval `scramv1 runtime -sh`
cd -

macroDir=${PWD}
export PATH=$PATH:$macroDir

#source /cvmfs/sft.cern.ch/lcg/contrib/gcc/7.3.0/x86_64-centos7-gcc7-opt/setup.sh
#source /cvmfs/sft.cern.ch/lcg/app/releases/ROOT/6.16.00/x86_64-centos7-gcc48-opt/bin/thisroot.sh
#xrdcp -f ${haddFile} root://cmseos.fnal.gov/${outputDir//$NOM/$SHIFT}/${haddFile//${SHIFT}_hadd/} 2>&1

xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/models/XGB700iterations_3depths_0.05signal_region_NewVar_test_M1500.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/models/XGB700iterations_3depths_0.05signal_region_NewVar_test_M1000.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/models/XGB700iterations_3depths_0.05signal_region_NewVar_test_M800.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/models/XGB700iterations_3depths_0.05signal_region_NewVar_test_M500.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/models/XGB700iterations_3depths_0.05signal_region_NewVar_test_M300.model .

xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/models/XGB700iterations_2depths_0.05signal_region_NewVar_Re_M15003b6j.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/models/XGB700iterations_2depths_0.05signal_region_NewVar_Re_M10003b6j.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/models/XGB700iterations_2depths_0.05signal_region_NewVar_Re_M8003b6j.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/models/XGB700iterations_2depths_0.05signal_region_NewVar_Re_M5003b6j.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/models/XGB400iterations_2depths_0.05signal_region_NewVar_Re_M3003b6j.model .

python XGBApply.py  -l $vListKey -f ${fileName}.root -o $fileName

xrdcp -f ${fileName}.root $outputDir/

rm *model
rm ${fileName}.root
