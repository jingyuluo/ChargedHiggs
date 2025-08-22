
for i in NPV NJets NBJetsNoSF JetPt Jet1Pt Jet2Pt Jet3Pt Jet4Pt lepPt lepEta
    do python plotTemplates_Common_nosig.py  kinematics_INC_M500_2024_8_13_topPtRW_XGBreduced_NEW $i 500
     python plotTemplates_Common_nosig_UL18.py  kinematics_INC_M500_2024_8_13_topPtRW_XGBreduced_NEW_UL18 $i 500
     python plotTemplates_Common_nosig_UL16.py  kinematics_INC_M500_2024_8_13_topPtRW_XGBreduced_NEW_UL16 $i 500
     python plotTemplates_Common_nosig_UL16APV.py  kinematics_INC_M500_2024_8_13_topPtRW_XGBreduced_NEW_UL16APV $i 500
done
