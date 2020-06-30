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

numTrigHist = dict((key, key+'_vs_MET') for key in MET120Triggers)

if os.path.exists('TrigHist_'+sample+'.root'):
    hfile = ROOT.TFile.Open('TrigHist_'+sample+'.root')
else:
    print 'Trigger histogram file does not exist'
trigDict = {}
for trig, hist in numTrigHist.items():
    trigDict[trig] = [hfile.Get('TriggerAnalyzer/'+hist+'_num'), hfile.Get('TriggerAnalyzer/'+hist+'_den')]


def PlotEff(hnum, hden, trig):
    heff = ROOT.TGraphAsymmErrors()
    heff.BayesDivide(hnum,hden)
    heff.GetYaxis().SetRangeUser(0.0 , 1.5)
    heff.GetYaxis().SetTitle("Efficiency")
    heff.GetXaxis().SetTitle("MET")                                                                                                                                  
    heff.GetYaxis().SetTitleSize(0.05)
    heff.GetYaxis().SetTitleOffset(0.7)
    heff.GetYaxis().SetLabelSize(0.03)
    heff.GetXaxis().SetTitleSize(0.04)
    heff.GetXaxis().SetTitleOffset(0.8)
    heff.GetXaxis().SetLabelSize(0.04)
    heff.SetLineWidth(2)
    heff.SetMarkerSize(0.8)
    heff.SetMarkerStyle(20)
    eff.GetYaxis().SetNdivisions(30)
    leg = ROOT.TLegend(0.3, 0.8, 0.9, 0.9)
    leg.AddEntry(heff, trig ,"p")

    c = ROOT.TCanvas('c', '', 600, 800)
    heff.Draw("AP")
    leg.Draw("same")
    ROOT.gPad.SetGrid()
    c.SaveAs("TriggerEff_MiniAOD_"+trig+".png")
    c.Close()



    
for trig, hist in trigDict.items():
    
    PlotEff(hist[0],hist[1], trig)    
   
    
