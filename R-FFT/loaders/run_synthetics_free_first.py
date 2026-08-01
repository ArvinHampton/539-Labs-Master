"""
Example free-first runner for the staged synthetic suite.
Adapt the import of full_r_fft_analysis to the local scripts/r_fft_5399.py path.
"""

import sys
import os
import numpy as np
import json

# Adjust this path to the local R-FFT script
# sys.path.insert(0, r"C:\Users\bradl\S2-11DM2ET-X-Axiomatic-Book\scripts")
# from r_fft_5399 import full_r_fft_analysis, scrambled_g4_control

def load_npz(path):
    d = np.load(path)
    return d["t"], d["signal"], float(d["fs"])

def main():
    base = "/home/workdir/artifacts/RFFT_datasets/synthetic"
    results = {}
    for f in sorted(os.listdir(base)):
        if not f.endswith(".npz"):
            continue
        name = f.replace(".npz", "")
        t, sig, fs = load_npz(os.path.join(base, f))
        # Placeholder: replace with actual call once path is set
        # res_free = full_r_fft_analysis(t, sig, fs, precondition=False)
        # res_scr  = scrambled_g4_control(t, sig, fs)
        results[name] = {
            "N": len(sig),
            "fs": fs,
            "status": "loaded – call free_r_fft_analysis(precondition=False) + scrambled control on local machine"
        }
        print(name, results[name])
    with open("/home/workdir/artifacts/RFFT_datasets/registry/synthetic_run_status.json", "w") as fh:
        json.dump(results, fh, indent=2)
    print("Status written. Run the actual free-first analysis on the machine that has r_fft_5399.py.")

if __name__ == "__main__":
    main()
