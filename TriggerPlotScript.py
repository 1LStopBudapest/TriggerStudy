import os, sys
import types


sys.path.append('../')
from Sample.SampleChain import SampleChain

sL = 'SingleElectron_Data'
fileperjobData = 5
TotJobs = 4
txtline = []

if isinstance(SampleChain.samplelist[sL][0], types.ListType):
    for s in SampleChain.samplelist[sL]:
        sample = list(SampleChain.samplelist.keys())[list(SampleChain.samplelist.values()).index(s)]
        fileperjob = fileperjobData
        tfiles = len(SampleChain.getfilelist(SampleChain.samplelist[sample][0]))
        for i in range(0, tfiles, fileperjob):
            txtline.append("python TrigHistMaker.py --sample %s --startfile %i --nfiles %i --pJobs True\n"%(sample, i, fileperjob))
else:
    tfiles = len(SampleChain.getfilelist(SampleChain.samplelist[sL][0]))
    fileperjob = fileperjobData
    for i in range(0, tfiles, fileperjob):
        txtline.append("python TrigHistMaker.py --sample %s --startfile %i --nfiles %i--pJobs True\n"%(sL, i, fileperjob))
                
fout = open("parallelJobsubmit.txt", "w")
fout.write(''.join(txtline))
fout.close()

bashline = []    
bashline.append('parallel --jobs %i < parallelJobsubmit.txt\n'%TotJobs)
fsh = open("parallelTrigHist.sh", "w")
fsh.write(''.join(bashline))
fsh.close()

os.system('chmod 744 parallelTrigHist.sh')
os.system('./parallelTrigHist.sh')

