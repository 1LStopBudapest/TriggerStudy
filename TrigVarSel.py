import ROOT
import math
import os, sys

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


    def passFakeRateJetTrig(self):
        return (self.tr.HLT_PFHT800 if hasattr(self.tr, 'HLT_PFHT800') else False) or (self.tr.HLT_PFJet450 if hasattr(self.tr, 'HLT_PFJet450') else False) or (self.tr.HLT_AK8PFJet450 if hasattr(self.tr, 'HLT_AK8PFJet450') else False)
                                                                                                                                                                
    def passFakeRateMuTrig(self):
        return self.tr.HLT_Mu50 if hasattr(self.tr, 'HLT_Mu50') else False
                                                                                                                                                                

    def Elecut(self, thr=30):
        return self.tr.Electron_pt[self.selectEleIdx()[0]]>thr if len(self.selectEleIdx()) else False
        
    def selectEleIdx(self):
        idx = []
        for i in range(len(self.tr.Electron_pt)):
            if self.tr.Electron_pt[i]>5 and abs(self.tr.Electron_eta[i])<2.5:
                idx.append(i)
        return idx

    def Mucut(self, thr=30):
        return self.tr.Muon_pt[self.selectMuIdx()[0]]>thr if len(self.selectMuIdx()) else False
    
    def selectMuIdx(self):
        idx = []
        for i in range(len(self.tr.Muon_pt)):
            if self.tr.Muon_pt[i]>3.5 and abs(self.tr.Muon_eta[i])<2.4 and self.tr.Muon_isPFcand[i] and (self.tr.Muon_isGlobal[i] or self.tr.Muon_isTracker[i]):
                idx.append(i)
        return idx
