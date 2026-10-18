cd "$(dirname "$0")"
python3 deep_cparts.py 32 200000 3 2 > enum_deep_s32_p2.log 2>&1; mv deep_cparts_s32_p2.json deep_cparts_s32_p2_e3_B200000.json
python3 deep_cparts.py 40 200000 1 2 > enum_deep_s40_p2.log 2>&1; mv deep_cparts_s40_p2.json deep_cparts_s40_p2_e1_B200000.json
python3 deep_cparts.py 36 200000 4 3 > enum_deep_s36_p3.log 2>&1; mv deep_cparts_s36_p3.json deep_cparts_s36_p3_e4_B200000.json
echo DONE > deep_done.flag
