#!/bin/bash

inputfile=${1}
outputDir=${2}
fileName=${3}
vListKey=${4}
scratch=${PWD}

#source /cvmfs/cms.cern.ch/cmsset_default.sh
#
#export SCRAM_ARCH=el9_amd64_gcc12
#
##cp /isilon/export/home/jluo48/CMSSW_14_0_19.tgz .
##tar -xf CMSSW_14_0_19.tgz
##rm CMSSW_14_0_19.tgz
#scramv1 project CMSSW CMSSW_14_0_19
#cd CMSSW_14_0_19/src
##cmsenv
#eval `scramv1 runtime -sh`
#cd -

source /cvmfs/sft.cern.ch/lcg/views/LCG_107/x86_64-el9-gcc11-opt/setup.sh

#cmssw-el7 -p  --bind `pwd`  --bind /isilon/hadoop/ --bind /cvmfs -- /bin/bash -l

macroDir=${PWD}
export HOME=${PWD}
export PATH=$PATH:$macroDir

echo ${PWD}
#ls /isilon/hadoop/store/group/bruxljm/jluo48/CHiggs/
#source /cvmfs/sft.cern.ch/lcg/contrib/gcc/7.3.0/x86_64-centos7-gcc7-opt/setup.sh
#source /cvmfs/sft.cern.ch/lcg/app/releases/ROOT/6.16.00/x86_64-centos7-gcc48-opt/bin/thisroot.sh
#xrdcp -f ${haddFile} root://cmseos.fnal.gov/${outputDir//$NOM/$SHIFT}/${haddFile//${SHIFT}_hadd/} 2>&1

cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M200_SRAll.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M220_SRAll.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M250_SRAll.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M300_SRAll.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M350_SRAll.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M400_SRAll.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M500_SRAll.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M600_SRAll.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M700_SRAll.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M800_SRAll.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M1000_SRAll.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M1250_SRAll.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M1500_SRAll.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M1750_SRAll.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M2000_SRAll.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M2500_SRAll.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M3000_SRAll.json .

cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M200_SR1.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M220_SR1.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M250_SR1.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M300_SR1.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M350_SR1.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M400_SR1.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M500_SR1.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M600_SR1.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M700_SR1.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M800_SR1.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M1000_SR1.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M1250_SR1.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M1500_SR1.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M1750_SR1.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M2000_SR1.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M2500_SR1.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M3000_SR1.json .

cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M200_SR2.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M220_SR2.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M250_SR2.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M300_SR2.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M350_SR2.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M400_SR2.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M500_SR2.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M600_SR2.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M700_SR2.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M800_SR2.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M1000_SR2.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M1250_SR2.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M1500_SR2.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M1750_SR2.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M2000_SR2.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M2500_SR2.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M3000_SR2.json .

cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M200_SR3.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M220_SR3.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M250_SR3.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M300_SR3.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M350_SR3.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M400_SR3.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M500_SR3.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M600_SR3.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M700_SR3.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M800_SR3.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M1000_SR3.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M1250_SR3.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M1500_SR3.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M1750_SR3.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M2000_SR3.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M2500_SR3.json .
cp /isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/XGB_M3000_SR3.json .


python3 XGBApply_SRs.py  -l $vListKey -f $inputfile -o $fileName

cp -f ${fileName}.root $outputDir/

#rm -r CMSSW_14_0_19
rm *json
rm ${fileName}.root
