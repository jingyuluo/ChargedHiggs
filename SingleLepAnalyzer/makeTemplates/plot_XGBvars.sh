for ivar in ST minMlb mass_minBBdr deltaR_lepBJet_maxpt MT_lepMet FW_momentum_2 HT theJetLeadPt MET mass_lepBJet0 mass_lepBJet_mindr sixthJetPt mass_maxBBmass M_allJet_W HT_bjets thirdcsvb_bb fourthcsvb_bb Sphericity Aplanarity BestTop_Discriminator NoTop_Jet1_CSV NoTop_Jet1_Pt NoTop_Jet2_CSV recLeptonicTopJetCSV LeptonicTB1_M LeptonicTB2_M HadronicTB2_M
    do python plotTemplates_Common_nosig.py  kinematics_CR_M500_2024_8_1_topPtRW_XGBreduced_NEW ${ivar} 500 
    python plotTemplates_Common_nosig_UL18.py  kinematics_CR_M500_2024_8_1_topPtRW_XGBreduced_NEW_UL18 ${ivar} 500
    python plotTemplates_Common_nosig_UL16.py  kinematics_CR_M500_2024_8_1_topPtRW_XGBreduced_NEW_UL16 ${ivar} 500
    python plotTemplates_Common_nosig_UL16APV.py  kinematics_CR_M500_2024_8_1_topPtRW_XGBreduced_NEW_UL16APV ${ivar} 500
done 
