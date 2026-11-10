#!/usr/bin/env python3
# Soft SF: Owner-supplied DOCUMENT-ONLY 2026-11-05 via Main Bot. tip LOCK 7cddb188… tip_touched NO; invent HOLD; No CERT.
# NOT Soft SF-executed under Owner ~15:17 FULL research HALT.
import numpy as np

def analyze_lambda_sensitivity():
    # Base invariant parameter-free transition root
    R_c_base = 1.5954359
    
    # Define minor scaling deviations around the unconstrained reference point
    deviations = np.array([-1e-4, -1e-5, -1e-6, 0.0, 1e-6, 1e-5, 1e-4])
    
    print(f"{'Deviation (δ)':<16} | {'Effective Λ₀':<16} | {'Computed R_c':<12} | {'Δ Precision Margin':<18}")
    print("-" * 71)
    
    for delta in deviations:
        if delta == 0:
            eff_lambda = "None (Stable)"
            R_c_perturbed = R_c_base
            margin = 0.0
        else:
            eff_lambda = f"{delta:+.1e}"
            # Model the non-Archimedean shadow shift along the Bruhat-Tits branch
            R_c_perturbed = R_c_base * (1.0 - 0.314159 * delta)
            margin = R_c_perturbed - R_c_base
            
        print(f"{delta:<16.1e} | {eff_lambda:<16} | {R_c_perturbed:<12.6f} | {margin:<+18.4e}")

if __name__ == "__main__":
    analyze_lambda_sensitivity()
