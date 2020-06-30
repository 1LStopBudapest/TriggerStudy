import os, sys
import ROOT

from TriggerList import *
sys.path.append('../')
from Helper.CosmeticCode import *

def get_parser():
    ''' Argument parser.                                                                                                                                                
    '''
    import argparse
    argParser = argparse.ArgumentParser(description = "Argument parser")
    argParser.add_argument('--infile',           action='store',                     type=str,            default='TrigHist_SingleElectron_Data.root',                    help="Which input root file?" )
    argParser.add_argument('--sample',           action='store',                     type=str,            default='SingleElectron_Data',                    help="Which sample?" )
    return argParser

options = get_parser().parse_args()

f = options.infile
sample = options.sample

lepOpt = 'Ele' if 'Ele' in sample else 'Mu'

numTrigHist = dict((key, 'hMET_'+key) for key in METTriggers)

if os.path.exists(f):
    hfile = ROOT.TFile.Open(f)
else:
    print 'Trigger histogram file does not exist'




hnum = hfile.Get('hMET_HLT_PFMET120_PFMHT120_IDTight_num_'+sample)
hden = hfile.Get('hMET_HLT_PFMET120_PFMHT120_IDTight_den_'+sample)
heff = ROOT.TGraphAsymmErrors()
heff.BayesDivide(hnum, hden)
c = ROOT.TCanvas('c', '', 600, 800)
heff.Draw("AP")
c.SaveAs("TriggerEff_"+lepOpt+".png")
c.Close()

'''
trigDict = {}
for trig, hist in numTrigHist.items():
    trigDict[trig] = [hfile.Get(hist+'_num_'+sample), hfile.Get(hist+'_den_'+sample)]
mg = ROOT.TMultiGraph()
mgleg = ROOT.TLegend(0.5, 0.75, 0.9, 0.9)

for trig, hist in trigDict.items():
    heff = ROOT.TGraphAsymmErrors()
    heff.BayesDivide(hist[0],hist[1])
    
    mg.Add(heff)
    mgleg.AddEntry(heff, trig ,"p")

    heff.GetYaxis().SetRangeUser(0.0 , 1.5)
    heff.GetYaxis().SetTitle("Efficiency")
    heff.GetXaxis().SetTitle("MET")                                                                                                                                  
    heff.GetYaxis().SetTitleSize(0.05)
    heff.GetYaxis().SetTitleOffset(0.7)
    heff.GetYaxis().SetLabelSize(0.03)
    heff.GetXaxis().SetTitleSize(0.04)
    heff.GetXaxis().SetTitleOffset(0.8)
    heff.GetXaxis().SetLabelSize(0.04)
    heff.SetLineColor(getTrigColor(trig))
    heff.SetLineWidth(2)
    heff.SetMarkerSize(0.8)
    if 'Inclusive' in trig:heff.SetMarkerStyle(24)
    else:heff.SetMarkerStyle(20)
    heff.SetMarkerColor(getTrigColor(trig))
    leg = ROOT.TLegend(0.5, 0.8, 0.9, 0.9)
    leg.AddEntry(heff, trig ,"p")
    
    c = ROOT.TCanvas('c', '', 600, 800)
    heff.Draw("AP")
    leg.Draw("same")
    ROOT.gPad.SetGrid()
    c.SaveAs("TriggerEff_"+trig+"_"+lepOpt+".png")
    c.Close()

mg.GetYaxis().SetRangeUser(0.0 , 1.5)
mg.GetYaxis().SetTitle("Efficiency")
mg.GetXaxis().SetTitle("MET")                                                                                                                                  
mg.GetYaxis().SetTitleSize(0.05)
mg.GetYaxis().SetTitleOffset(0.7)
mg.GetYaxis().SetLabelSize(0.03)
mg.GetXaxis().SetTitleSize(0.04)
mg.GetXaxis().SetTitleOffset(0.8)
mg.GetXaxis().SetLabelSize(0.04)
c = ROOT.TCanvas('c', '', 600, 800)
mg.Draw("AP")
mgleg.Draw("same")
ROOT.gPad.SetGrid()
c.SaveAs("TriggerEff_together_"+lepOpt+".png")
c.Close()
'''
