for s in $(seq 5 44); do python3 coset.py $s 0 2>&1 | grep -v stack; done > coset_all_5_44.log
