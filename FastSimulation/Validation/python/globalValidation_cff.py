import FWCore.ParameterSet.Config as cms

# Tracking particle module
#from FastSimulation.Validation.trackingParticlesFastSim_cfi import * # now deprecated


from Validation.RecoMET.METRelValForDQM_cff import *

from Validation.TrackingMCTruth.trackingTruthValidation_cfi import *
from Validation.RecoTrack.TrackValidation_fastsim_cff import *
from Validation.RecoJets.JetValidation_cff import *
from Validation.RecoMuon.muonValidationFastSim_cff import *
from Validation.MuonIsolation.MuIsoVal_cff import *
from Validation.MuonIdentification.muonIdVal_cff import *
muonIdVal.makeCosmicCompatibilityPlots = False

from Validation.RecoEgamma.egammaFastSimValidation_cff import *


from DQMOffline.RecoB.dqmAnalyzer_cff import *


#globalAssociation = cms.Sequence(trackingParticles + recoMuonAssociationFastSim + tracksValidationSelectors + prebTagSequence)
globalAssociation = cms.Sequence(recoMuonAssociationFastSim + tracksValidationSelectors + prebTagSequence)

globalValidation = cms.Sequence(trackingTruthValid
                                +tracksValidationFS
                                +METRelValSequence
                                +recoMuonValidationFastSim
                                +muIsoVal_seq
                                +muonIdValDQMSeq
                                +bTagPlotsMC
                                +egammaFastSimValidation
                                +electronValidationSequence
                                +JetValidation
                                )

globalValidation_preprod = cms.Sequence(trackingTruthValid
                                +tracksValidationFS
                                +METRelValSequence
                                +recoMuonValidationFastSim
                                +muIsoVal_seq
                                +muonIdValDQMSeq
                                )
