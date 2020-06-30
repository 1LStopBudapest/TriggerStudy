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
    argParser.add_argument('--sample',           action='store',                     type=str,            default='MiniAOD_2016',                    help="Which sample?" )
    return argParser

options = get_parser().parse_args()

sample = options.sample

numTrigHist = dict((key, key+'_vs_MET') for key in METTriggers)

if os.path.exists('TrigHist_'+sample+'.root'):
    hfile = ROOT.TFile.Open('TrigHist_'+sample+'.root')
else:
    print 'Trigger histogram file does not exist'
trigDict = {}
for trig, hist in numTrigHist.items():
    trigDict[trig] = [hfile.Get('TriggerAnalyzer/'+hist+'_num'), hfile.Get('TriggerAnalyzer/'+hist+'_den')]

mg = []
mgleg = ROOT.TLegend(0.5, 0.75, 0.9, 0.9)

for trig, hist in trigDict.items():
    heff = ROOT.TGraphAsymmErrors()
    heff.BayesDivide(hist[0],hist[1])
    
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
    if trig=='HLT_MET_Inclusive':heff.SetMarkerStyle(24)
    else:heff.SetMarkerStyle(20)
    heff.SetMarkerColor(getTrigColor(trig))
    leg = ROOT.TLegend(0.5, 0.8, 0.9, 0.9)
    leg.AddEntry(heff, trig ,"p")

    mg.append(heff)
    mgleg.AddEntry(heff, trig ,"p")

    c = ROOT.TCanvas('c', '', 600, 800)
    heff.Draw("AP")
    leg.Draw("same")
    ROOT.gPad.SetGrid()
    c.SaveAs("TriggerEff_MiniAOD_"+trig+".png")
    c.Close()
'''
mg.GetYaxis().SetRangeUser(0.0 , 1.5)
mg.GetYaxis().SetTitle("Efficiency")
mg.GetXaxis().SetTitle("MET")                                                                                                                                  
mg.GetYaxis().SetTitleSize(0.05)
mg.GetYaxis().SetTitleOffset(0.7)
mg.GetYaxis().SetLabelSize(0.03)
mg.GetXaxis().SetTitleSize(0.04)
mg.GetXaxis().SetTitleOffset(0.8)
mg.GetXaxis().SetLabelSize(0.04)
'''
c = ROOT.TCanvas('c', '', 600, 800)
c.cd()
fr = c.DrawFrame(0., 0.0, 500, 1.2)
fr.GetYaxis().SetTitle("Efficiency")
fr.GetYaxis().SetTitleSize(0.05)
fr.GetYaxis().SetTitleOffset(0.7)
fr.GetYaxis().SetLabelSize(0.03)
fr.GetXaxis().SetTitle("MET")
fr.GetXaxis().SetTitleSize(0.04)
fr.GetXaxis().SetTitleOffset(0.8)
fr.GetXaxis().SetLabelSize(0.04)
for g in mg: 
    g.Draw("P")
mgleg.Draw("same")
ROOT.gPad.SetGrid()
c.SaveAs("TriggerEff_MiniAOD_together.png")
c.Close()
    
