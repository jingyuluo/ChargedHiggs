
for i in 200 220 250 300 350 400 500 600 700 800 1000 1250 1500 1750 2000 2500 3000
do combineCards.py R17=limits_Hptb${i}_M500_2025_10_9_QCDsup_NEWXGBREDTT_KINE_FINAL_100bin_XGB${i}_QCDsup_Full/cmb/combined.txt.cmb R18=limits_Hptb${i}_M500_2025_10_7_QCDsup_NEWXGBREDTT_KINE_FINAL_100bin_UL18_XGB${i}_QCDsup_Full/cmb/combined.txt.cmb R16=limits_Hptb${i}_M500_2025_10_7_QCDsup_NEWXGBREDTT_KINE_FINAL_100bin_UL16_XGB${i}_QCDsup_Full/cmb/combined.txt.cmb R16APV=limits_Hptb${i}_M500_2025_10_7_QCDsup_NEWXGBREDTT_KINE_FINAL_100bin_UL16APV_XGB${i}_QCDsup_Full/cmb/combined.txt.cmb &> XGBcomb_NEWXGBREDTT_KINE_FINAL_100bin_QCDsup_Full/M${i}_cmb.txt
    done
