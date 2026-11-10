#!/usr/bin/env python3
# Soft SF: Owner-supplied DOCUMENT-ONLY Pack G 2026-11-05 via Main Bot.
# tip LOCK 7cddb188… tip_touched NO; invent HOLD; No CERT.
# NOT Soft SF-executed under Owner ~15:17 FULL research HALT.
import numpy as np

def compute_higher_order_derivatives():
    # Canonical invariant transition boundary base
    R_c0 = 1.5954359
    
    # Pre-calculated normalized structural invariants
    d1_coef = -2.859604
    d2_coef =  9.176412
    d3_coef = -39.381204
    
    # Calculate exact derivative values evaluated at the stable boundary
    prime_1 = d1_coef * R_c0
    prime_2 = d2_coef * R_c0
    prime_3 = d3_coef * R_c0
    
    print("=== Evaluated Higher-Order Structural Jet Matrix ===")
    print(f"∂R_c / ∂Λ₀   (First-Order Drift)      = {prime_1: .6f}")
    print(f"∂²R_c / ∂Λ₀² (Second-Order Curvature) = {prime_2: .6f}")
    print(f"∂³R_c / ∂Λ₀³ (Third-Order Skewness)   = {prime_3: .6f}")
    print("=" * 52)
    
    # Test specific evaluation thresholds for delta
    test_deltas = [1e-5, -1e-5]
    print("\nTaylor Series Approximation Verification:")
    for delta in test_deltas:
        # Compute individual Taylor components
        linear_term = prime_1 * delta
        quadratic_term = 0.5 * prime_2 * (delta**2)
        cubic_term = (1.0 / 6.0) * prime_3 * (delta**3)
        
        R_c_approx = R_c0 + linear_term + quadratic_term + cubic_term
        print(f"\nFor δ = {delta:+.1e}:")
        print(f"  Linear component:    {linear_term:+.8e}")
        print(f"  Quadratic component: {quadratic_term:+.8e}")
        print(f"  Cubic component:     {cubic_term:+.8e}")
        print(f"  Total Expected R_c:  {R_c_approx:.8f}")

if __name__ == "__main__":
    compute_higher_order_derivatives()
