import os,shutil,datetime,time
import getpass
import varsList
from ROOT import *
from XRootD import client

###############################################

runDir = os.getcwd()
start_time = time.time()

inputDir='/isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_CSV_REDNEW/SR2'#'/eos/uscms/store/user/lpcbril/MC_test/FWLJMET106X_1lep2017_UL_step2_CSV_SR2_added'
outputDir= '/isilon/hadoop/users/jluo48/CHiggs/UL17/XGB_models_REDNEW/SR2' 
condorDir= runDir+'/condor_logs_CSVtoXGB_SR2_REDNEW/'

print('Starting submission')
count=0

#inDir=inputDir[10:]
#outDir=outputDir[10:]

rootfiles = os.popen('ls '+inputDir)
os.system('mkdir -p '+outputDir)
os.system('mkdir -p '+condorDir)
#eosindir = inputDir[inputDir.find("/store"):]
#eosindir = "root://cmseos.fnal.gov/"+eosindir

#eosoutdir = outputDir[outputDir.find("/store"):]
#eosoutdir = "root://cmseos.fnal.gov/"+eosoutdir

Masses = [200, 220, 250, 300, 350, 400, 500, 600, 700, 800, 1000, 1250, 1500, 1750, 2000, 2500, 3000]
#Masses = [500]#[800, 1000, 1250, 1500, 1750, 2000, 2500, 3000]

for mass in Masses:
    #if not 'TTToSemiLeptonic' in file: continue
    #if not 'ttjj' in file: continue
#    if 'TTTo' in file: continue
    dict={'RUNDIR':runDir, 'CONDORDIR':condorDir, 'INPUTDIR':inputDir, 'MASS':mass, 'OUTPUTDIR':outputDir}
    subdir = condorDir+'/XGB_M%(MASS)s'%dict
    os.system('mkdir -p '+subdir)
    jdfName=subdir+'/M%(MASS)s.job'%dict
    print(jdfName)
    jdf=open(jdfName,'w')
    jdf.write(
"""universe = vanilla
Executable = %(RUNDIR)s/submitCSVXGB.sh
Request_memory = 4000
Should_Transfer_Files = IF_NEEDED
WhenToTransferOutput = ON_EXIT
Transfer_Input_Files = %(RUNDIR)s/CSVXGB.py
Output = M%(MASS)s.out
Error = M%(MASS)s.err
Log = M%(MASS)s.log
Notification = Never
Arguments =  %(INPUTDIR)s   %(OUTPUTDIR)s  %(MASS)s      

Queue 1"""%dict)
    jdf.close()
    os.system('cp CSVXGB.py '+subdir)
    os.system('cp submitCSVXGB.sh '+subdir)
    os.chdir('%s/'%(subdir))
    os.system('condor_submit M%(MASS)s.job'%dict)
    os.system('sleep 0.5')
    os.chdir('%s'%(runDir))
    print(count, "jobs submitted!!!")

print("--- %s minutes ---" % (round(time.time() - start_time, 2)/60))

