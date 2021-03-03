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

xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M200_SRAll.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M220_SRAll.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M250_SRAll.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M300_SRAll.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M350_SRAll.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M400_SRAll.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M500_SRAll.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M600_SRAll.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M700_SRAll.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M800_SRAll.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M1000_SRAll.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M1250_SRAll.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M1500_SRAll.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M1750_SRAll.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M2000_SRAll.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M2500_SRAll.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M3000_SRAll.model .

xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M200_SR1.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M220_SR1.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M250_SR1.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M300_SR1.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M350_SR1.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M400_SR1.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M500_SR1.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M600_SR1.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M700_SR1.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M800_SR1.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M1000_SR1.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M1250_SR1.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M1500_SR1.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M1750_SR1.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M2000_SR1.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M2500_SR1.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M3000_SR1.model .

xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M200_SR2.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M220_SR2.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M250_SR2.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M300_SR2.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M350_SR2.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M400_SR2.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M500_SR2.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M600_SR2.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M700_SR2.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M800_SR2.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M1000_SR2.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M1250_SR2.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M1500_SR2.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M1750_SR2.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M2000_SR2.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M2500_SR2.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M3000_SR2.model .

xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M200_SR3.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M220_SR3.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M250_SR3.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M300_SR3.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M350_SR3.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M400_SR3.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M500_SR3.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M600_SR3.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M700_SR3.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M800_SR3.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M1000_SR3.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M1250_SR3.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M1500_SR3.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M1750_SR3.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M2000_SR3.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M2500_SR3.model .
xrdcp root://cmseos.fnal.gov//store/user/jluo/ChargeHiggs/SRmodels_splited/XGB_M3000_SR3.model .


python XGBApply_SRs.py  -l $vListKey -f ${fileName}.root -o $fileName

xrdcp -f ${fileName}.root $outputDir/

rm *model
rm ${fileName}.root
