#for i in 200 220 250 300 350 400 500 600 700 800 1000 1250 1500 1750 2000 2500 3000
for i in 600 700 800 1000 1250 1500 1750 2000 2500 3000
#for i in 1500 1750 2000 2500 3000
#for i in 3000
    do
        text2workspace.py XGBcomb_NEWXGBREDTT_KINE_FINAL_100bin_QCDsup_Full/M${i}_cmb.txt -o XGBcomb_NEWXGBREDTT_KINE_FINAL_100bin_QCDsup_Full/M${i}_cmb.root
	combine -M AsymptoticLimits XGBcomb_NEWXGBREDTT_KINE_FINAL_100bin_QCDsup_Full/M${i}_cmb.root  --cminDefaultMinimizerStrategy 0 -n CH_M${i}_withsig_XGBTT_100bin_FINAL &> asy_m${i}_fullRun2_QCDsup_XGBTT_FINAL_100bin_Full.txt --run blind
    done
