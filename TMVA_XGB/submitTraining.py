import os,shutil,datetime,time
import getpass
import varsList
from ROOT import *
from XRootD import client

###############################################
runDir = os.getcwd()
start_time = time.time()

inputDir='/eos/uscms/store/user/mlukasik/CHiggs2017/step2s/'
outputDir= '/eos/uscms/store/user/mlukasik/CHiggs2017/step1s/nominal/' # or 2018
condorDir= runDir+'/condor_logs/'

inDir=inputDir[10:]
outDir=outputDir[10:]


BDTlist = ['BDT']
varListKeys = ['BigComb']#['2016AN']
massList = ['200','250','300','350','400','500','800','1000','1500','2000','2500','3000']
#massList = ['200','500','2000']
nIts = '100'

############################################

os.system('mkdir -p '+condorDir)

for mass in massList:
    note = 'M-'+mass
    #for method in methodList:
    for mDepth in ['2']:
        for vListKey in varListKeys:
            fileName = 'XGB_'+vListKey+'_'+str(len(varsList.varList[vListKey]))+'vars_mDepth'+mDepth+'_'+note
            dict={'RUNDIR':runDir,'FILENAME':fileName,'vListKey':vListKey,'mDepth':mDepth,'nIts':nIts,'sigMass':'M-'+mass}
            jdfName=condorDir+'/%(FILENAME)s.job'%dict
            print jdfName
            jdf=open(jdfName,'w')
            jdf.write(
            """use_x509userproxy = true
universe = vanilla
Executable = %(RUNDIR)s/submitTraining.sh
Should_Transfer_Files = YES
WhenToTransferOutput = ON_EXIT
Transfer_Input_Files = %(RUNDIR)s/UpROOTXGB.py, %(RUNDIR)s/varsList.py
request_memory = 8000
Output = %(FILENAME)s.out
Error = %(FILENAME)s.err
Log = %(FILENAME)s.log
Notification = Never
stream_output = True
Arguments = %(RUNDIR)s %(FILENAME)s %(vListKey)s %(nIts)s %(mDepth)s %(sigMass)s
Queue 1"""%dict)
            jdf.close()
            os.chdir('%s/'%(condorDir))
            os.system('condor_submit %(FILENAME)s.job'%dict)
            os.system('sleep 0.5')
            os.chdir('%s'%(runDir))
            

