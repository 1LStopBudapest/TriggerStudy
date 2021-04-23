import ROOT
import math
import os, sys
import collections as coll

sys.path.append('../')
from Helper.VarCalc import *


class TrigVarSel():

    def __init__(self, tr, sample):
        self.tr = tr
        self.sample = sample
        
    def TrigExist(self, tr, trig):
       return True if trig in [br.GetName() for br in tr.GetListOfBranches()] else False
    
    def passEleTrig(self, trig):
        if trig=='HLT_Ele27_eta2p1_WPTight_Gsf' and hasattr(self.tr, 'HLT_Ele27_eta2p1_WPTight_Gsf'): return self.tr.HLT_Ele27_eta2p1_WPTight_Gsf

    def passMuTrig(self, trig):
        if trig=='HLT_IsoMu27' and hasattr(self.tr, 'HLT_IsoMu27'): return self.tr.HLT_IsoMu27

    def passLepTrig(self, trig, opt):
        return self.passEleTrig(trig) if opt=='Ele' else self.passMuTrig(trig)
    
    def passMETTrig(self, trig):
        if trig=='HLT_PFMET90_PFMHT90_IDTight' and hasattr(self.tr, 'HLT_PFMET90_PFMHT90_IDTight'): return self.tr.HLT_PFMET90_PFMHT90_IDTight
        if trig=='HLT_PFMET100_PFMHT100_IDTight' and hasattr(self.tr, 'HLT_PFMET100_PFMHT100_IDTight'): return self.tr.HLT_PFMET100_PFMHT100_IDTight
        if trig=='HLT_PFMET110_PFMHT110_IDTight' and hasattr(self.tr, 'HLT_PFMET110_PFMHT110_IDTight'): return self.tr.HLT_PFMET110_PFMHT110_IDTight
        if trig=='HLT_PFMET120_PFMHT120_IDTight' and hasattr(self.tr, 'HLT_PFMET120_PFMHT120_IDTight'): return self.tr.HLT_PFMET120_PFMHT120_IDTight
        if trig=='HLT_MET_Inclusive': return (self.tr.HLT_PFMET90_PFMHT90_IDTight if hasattr(self.tr, 'HLT_PFMET90_PFMHT90_IDTight') else False) or (self.tr.HLT_PFMET100_PFMHT100_IDTight if hasattr(self.tr, 'HLT_PFMET100_PFMHT100_IDTight') else False) or (self.tr.HLT_PFMET110_PFMHT110_IDTight if hasattr(self.tr, 'HLT_PFMET110_PFMHT110_IDTight') else False) or (self.tr.HLT_PFMET120_PFMHT120_IDTight if hasattr(self.tr, 'HLT_PFMET120_PFMHT120_IDTight') else False)
        if trig=='HLT_PFMETNoMu90_PFMHTNoMu90_IDTight' and hasattr(self.tr, 'HLT_PFMETNoMu90_PFMHTNoMu90_IDTight'): return self.tr.HLT_PFMETNoMu90_PFMHTNoMu90_IDTight
        if trig=='HLT_PFMETNoMu100_PFMHTNoMu100_IDTight' and hasattr(self.tr, 'HLT_PFMETNoMu100_PFMHTNoMu100_IDTight'): return self.tr.HLT_PFMETNoMu100_PFMHTNoMu100_IDTight
        if trig=='HLT_PFMETNoMu110_PFMHTNoMu110_IDTight' and hasattr(self.tr, 'HLT_PFMETNoMu110_PFMHTNoMu110_IDTight'): return self.tr.HLT_PFMETNoMu110_PFMHTNoMu110_IDTight
        if trig=='HLT_PFMETNoMu120_PFMHTNoMu120_IDTight' and hasattr(self.tr, 'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight'): return self.tr.HLT_PFMETNoMu120_PFMHTNoMu120_IDTight
        if trig=='HLT_METNoMu_Inclusive': return (self.tr.HLT_PFMETNoMu90_PFMHTNoMu90_IDTight if hasattr(self.tr, 'HLT_PFMETNoMu90_PFMHTNoMu90_IDTight') else False) or (self.tr.HLT_PFMETNoMu100_PFMHTNoMu100_IDTight if hasattr(self.tr, 'HLT_PFMETNoMu100_PFMHTNoMu100_IDTight') else False) or (self.tr.HLT_PFMETNoMu110_PFMHTNoMu110_IDTight if hasattr(self.tr, 'HLT_PFMETNoMu110_PFMHTNoMu110_IDTight') else False) or (self.tr.HLT_PFMETNoMu120_PFMHTNoMu120_IDTight if hasattr(self.tr, 'HLT_PFMETNoMu120_PFMHTNoMu120_IDTight') else False)

        else: return False

    def passfilters(self):
        return (self.tr.Flag_goodVertices if hasattr(self.tr, 'Flag_goodVertices') else True) and (self.tr.Flag_globalSuperTightHalo2016Filter if hasattr(self.tr, 'Flag_globalSuperTightHalo2016Filter') else True) and (self.tr.Flag_HBHENoiseFilter if hasattr(self.tr, 'Flag_HBHENoiseFilter') else True) and (self.tr.Flag_HBHENoiseIsoFilter if hasattr(self.tr, 'Flag_HBHENoiseIsoFilter') else True) and (self.tr.Flag_EcalDeadCellTriggerPrimitiveFilter if hasattr(self.tr, 'Flag_EcalDeadCellTriggerPrimitiveFilter') else True) and (self.tr.Flag_BadPFMuonFilter if hasattr(self.tr, 'Flag_BadPFMuonFilter') else True) and (self.tr.Flag_eeBadScFilter if hasattr(self.tr, 'Flag_eeBadScFilter') else True)
        
    def passFakeRateJetTrig(self):
        return (self.tr.HLT_PFHT800 if hasattr(self.tr, 'HLT_PFHT800') else False) or (self.tr.HLT_PFJet450 if hasattr(self.tr, 'HLT_PFJet450') else False) or (self.tr.HLT_AK8PFJet450 if hasattr(self.tr, 'HLT_AK8PFJet450') else False)
                                                                                                                                                                
    def passFakeRateMuTrig(self):
        return self.tr.HLT_Mu50 if hasattr(self.tr, 'HLT_Mu50') else False
                                                                                                                                                                
    ##Event object selection
    
    def getEleVar(self, eId):
        Llist = []
        for id in eId:
            Llist.append({'pt':self.tr.Electron_pt[id], 'eta':self.tr.Electron_eta[id], 'phi':self.tr.Electron_phi[id], 'mass':self.tr.Electron_mass[id], 'idx': id})
        return sortedlist(Llist)

    def getMuVar(self, muId):
        Llist = []
        for id in muId:
            Llist.append({'pt':self.tr.Muon_pt[id], 'eta':self.tr.Muon_eta[id], 'phi':self.tr.Muon_phi[id], 'mass':self.tr.Muon_mass[id], 'idx': id})
        return sortedlist(Llist)
    
    def getLepVar(self, muId, eId):
        Llist = []
        for id in muId:
            Llist.append({'pt':self.tr.Muon_pt[id], 'eta':self.tr.Muon_eta[id], 'phi':self.tr.Muon_phi[id], 'mass':self.tr.Muon_mass[id], 'idx': id})
        for id in eId:
            Llist.append({'pt':self.tr.Electron_pt[id], 'eta':self.tr.Electron_eta[id], 'phi':self.tr.Electron_phi[id], 'mass':self.tr.Electron_mass[id], 'idx': id})
        return sortedlist(Llist)


    def Elecut(self, thr=30, IdOpt='tight'):
        eid = self.EleIDconv(IdOpt)
        ele = self.getEleVar(self.selectEleIdx(eid))
        return ele[0]['pt'] > thr if len(ele) else False
        
    def Mucut(self, thr=30, IdOpt='tight'):
        Mu = self.getMuVar(self.selectMuIdx(IdOpt))
        return Mu[0]['pt'] > thr if len(Mu) else False

    def Lepcut(self, lep):
        return self.Elecut() if 'Ele' in lep else self.Mucut()
    
    def XtraLepVeto(self, lep, thr=10, IdOpt='loose'):
        cut = True
        eid = self.EleIDconv(IdOpt)
        if 'Ele' in lep:
            lid = self.getEleVar(self.selectEleIdx(4))[0]['idx'] # assuming this func applied after Elecut
            eleidx = self.selectEleIdx(eid)
            eleidx.remove(lid)
            lepvar = self.getLepVar(self.selectMuIdx(IdOpt), eleidx)
            if len(lepvar) and lepvar[0]['pt']>thr:
                cut = False
        if 'Mu' in lep:
            lid = getMuVar(selectMuIdx('tight'))[0]['idx'] # assuming this func applied after Mucut
            muidx = self.selectMuIdx(IdOpt)
            muidx.remove(lid)
            lepvar = self.getLepVar(muidx, self.selectEleIdx(eid))
            if len(lepvar) and lepvar[0]['pt']>thr:
                cut = False
        return cut
            
    def selectEleIdx(self, IdOpt):
        idx = []
        for i in range(len(self.tr.Electron_pt)):
            if self.eleSelector(pt=self.tr.Electron_pt[i], eta=self.tr.Electron_eta[i], deltaEtaSC=self.tr.Electron_deltaEtaSC[i], iso=self.tr.Electron_pfRelIso03_all[i], dxy=self.tr.Electron_dxy[i], dz=self.tr.Electron_dz[i], Id=self.tr.Electron_cutBased_Fall17_V1[i], idopt=IdOpt):
                idx.append(i)
        return idx
    
    def selectMuIdx(self, IdOpt):
        idx = []
        for i in range(len(self.tr.Muon_pt)):
            if self.muonSelector(pt=self.tr.Muon_pt[i], eta=self.tr.Muon_eta[i], iso=self.tr.Muon_pfRelIso03_all[i], dxy=self.tr.Muon_dxy[i], dz=self.tr.Muon_dz[i], Id = self.tr.Muon_tightId[i] if 'tight' in IdOpt else self.tr.Muon_looseId[i] if 'loose' in IdOpt else self.tr.Muon_mediumId[i]):
                idx.append(i)
        return idx


    def eleSelector(self, pt, eta, deltaEtaSC, iso, dxy, dz, Id, idopt):
        return pt > 5 \
            and abs(eta)       < 2.5 \
            and (abs(eta+deltaEtaSC)<1.4442 or abs(eta+deltaEtaSC)>1.566) \
            and (iso) < 0.2 \
            and abs(dxy)       < 0.02 \
            and abs(dz)        < 0.1 \
            and self.eleID(Id, idopt) #cutbased id: 0:fail, 1:veto, 2:loose, 3:medium, 4:tight    
    
    def muonSelector( self, pt, eta, iso, dxy, dz, Id):
        return pt > 3.5 \
            and abs(eta)       < 2.4 \
            and (iso) < 0.15 \
	    and abs(dxy)       < 0.02 \
            and abs(dz)        < 0.1 \
            and Id

    def eleID(self, idval, idtype):
        return idval >= idtype

    def EleIDconv(self, idopt):
        eid = 0
        if 'tight' in idopt : eid = 4
        if 'medium' in idopt : eid = 3
        if 'loose' in idopt : eid = 2
        if 'veto' in idopt : eid = 1
        return eid


    def ISRcut(self, thr=100):
        return len(self.selectjetIdx(thr)) > 0

    def METcut(self, thr=200):
        cut = False
        if self.tr.MET_pt > thr:
            cut = True
        return cut
        
    def HTcut(self, thr=300):
        cut = False
        HT = self.calHT()
        if HT > thr:
            cut = True
        return cut

    def calHT(self):
        HT = 0
        for i in self.selectjetIdx(30):
            HT = HT + self.tr.Jet_pt[i]
        return HT


    def selectjetIdx(self, thrsld):
        lepvar = sortedlist(self.getLepVar(self.selectMuIdx('tight'), self.selectEleIdx('tight')))
        idx = []
        d = {}
        for j in range(len(self.tr.Jet_pt)):
            clean = False
            if self.tr.Jet_pt[j] > thrsld and abs(self.tr.Jet_eta[j]) < 2.4 and self.tr.Jet_jetId[j] > 0:
                clean = True
                for l in range(len(lepvar)):
                    dR = DeltaR(lepvar[l]['eta'], lepvar[l]['phi'], self.tr.Jet_eta[j], self.tr.Jet_phi[j])
                    ptRatio = float(self.tr.Jet_pt[j])/float(lepvar[l]['pt'])
                    if dR < 0.4 and ptRatio < 2:
                        clean = False
                        break
                if clean:
                    d[self.tr.Jet_pt[j]] = j
        od = coll.OrderedDict(sorted(d.items(), reverse=True))
        for jetpt in od:
            idx.append(od[jetpt])
        return idx
