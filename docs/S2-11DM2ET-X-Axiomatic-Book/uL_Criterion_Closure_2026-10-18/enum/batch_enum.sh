# Enumerative completion of the coprime part at s = 34, 40, 32, 36: escalate B until every class of G is observable.
cd "$(dirname "$0")"
for s in 34 40 32 36; do
  for B in 200000 350000 500000; do
    python3 deep_cparts.py $s $B 0 2 > enum_s${s}_B${B}.log 2>&1
    mv deep_cparts_s${s}_p2.json deep_cparts_s${s}_coprime_B${B}.json 2>/dev/null
    if grep -q '"all_complete": true' enum_s${s}_B${B}.log; then break; fi
  done
done
echo DONE > batch_done.flag
