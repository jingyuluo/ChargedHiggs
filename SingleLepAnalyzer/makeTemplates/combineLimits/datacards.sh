for i in 200 220 250 300 350 400 500 600 700 800 1000 1250 1500 1750 2000 2500 3000
    do
        python3 dataCard_new.py M500_2025_10_9_QCDsup_NEWXGBREDTT_KINE_FINAL_100bin R17 XGB${i} ${i}
        python3 dataCard_new.py M500_2025_10_7_QCDsup_NEWXGBREDTT_KINE_FINAL_100bin_UL16 R16 XGB${i} ${i}
        python3 dataCard_new.py M500_2025_10_7_QCDsup_NEWXGBREDTT_KINE_FINAL_100bin_UL16APV R16APV XGB${i} ${i}
        python3 dataCard_new.py M500_2025_10_7_QCDsup_NEWXGBREDTT_KINE_FINAL_100bin_UL18 R18 XGB${i} ${i}
    done


