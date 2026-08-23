#!/usr/bin/env python3
"""Verify Bridge-C axis pairing, Euler/orthant mismatch, chi_nat, s=8 poles.

Pack+(S) residual discrete hygiene. Not a modular completion.
"""
from collections import defaultdict

S = 7
C1 = (-1, 1)
C2 = (-4, 1)
CHI = (7 / 10, -1 / 5)
CONST = 7 / 20


def sgn(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


def Qs(n, k, s=S):
    return n * n + s * n * k + (s / 2) * k * (k + 1)


def QM(n, k, s=S):
    return 2 * n * n + 2 * s * n * k + s * k * k


def B(c, v, s=S):
    cn, ck = c
    n, k = v
    return 2 * cn * n + s * cn * k + s * ck * n + s * ck * k


def w_of(n, k):
    return 0.5 * (sgn(B(C1, (n, k))) - sgn(B(C2, (n, k))))


def completed(n, k):
    a, b = CHI
    vp = (n + a, k + b)
    Mv0 = 2 * vp[0] + S * vp[1]
    Mv1 = S * vp[0] + S * vp[1]
    return 0.5 * (vp[0] * Mv0 + vp[1] * Mv1) + CONST


def series(maxdeg=80, nrange=90):
    P = defaultdict(float)
    H = defaultdict(float)
    C = defaultdict(float)
    third = []
    for n in range(-nrange, nrange + 1):
        for k in range(-nrange, nrange + 1):
            Q = Qs(n, k)
            if Q < 0 or Q > maxdeg:
                continue
            w = w_of(n, k)
            if n >= 0 and k >= 0:
                P[Q] += 1
                C[Q] += 1 - w
            else:
                C[Q] -= w
            H[Q] += w
            if n < 0 and k < 0 and abs(w + 1) < 1e-12:
                third.append((n, k, int(Q)))
    return P, H, C, sorted(third, key=lambda t: t[2])


def euler_P(maxdeg=40, nmax=40, jmax=40):
    coeffs = defaultdict(int)
    for n in range(0, nmax + 1):
        base = n * n
        if base > maxdeg:
            break
        dp = [0] * (maxdeg + 1)
        dp[0] = 1
        for j in range(n + 1, jmax + 1):
            step = S * j
            if step > maxdeg:
                break
            new = dp[:]
            for d in range(0, maxdeg - step + 1):
                if dp[d]:
                    new[d + step] += dp[d]
            dp = new
        for d in range(0, maxdeg - base + 1):
            if dp[d]:
                coeffs[base + d] += dp[d]
    return coeffs


def g_coeffs(maxdeg=40, nmax=30):
    coeffs = defaultdict(int)
    for n in range(0, nmax + 1):
        base = n * n
        if base > maxdeg:
            break
        dp = [0] * (maxdeg + 1)
        dp[0] = 1
        for j in range(1, n + 1):
            step = S * j
            new = [0] * (maxdeg + 1)
            for d in range(0, maxdeg + 1):
                if dp[d] == 0:
                    continue
                sign = 1
                m = 0
                while d + m * step <= maxdeg:
                    new[d + m * step] += dp[d] * sign
                    sign *= -1
                    m += 1
            dp = new
        for d in range(0, maxdeg - base + 1):
            coeffs[base + d] += dp[d]
    return coeffs


def axis_C(maxdeg):
    out = defaultdict(float)
    out[0] += 1.5
    n = 1
    while n * n <= maxdeg:
        out[n * n] += 1
        n += 1
    k = 1
    while True:
        deg = int(S * k * (k + 1) / 2)
        if deg > maxdeg:
            break
        out[deg] += 1
        k += 1
    return out


def main():
    assert QM(*C1) == -5 and QM(*C2) == -17
    assert Qs(*C1) == 1 and Qs(*C2) == -5
    assert abs(B(C1, CHI) - 3.5) < 1e-12
    assert abs(B(C2, CHI) - 3.5) < 1e-12
    for n, k in [(0, 0), (1, 0), (0, 1), (1, 1), (2, 3), (-1, 2), (-4, 1)]:
        assert abs(Qs(n, k) - completed(n, k)) < 1e-9, (n, k)

    P, H, C, third = series()
    assert abs(C[0] - 1.5) < 1e-12
    vals = sorted({round(C[d], 6) for d in range(0, 81) if abs(C[d]) > 1e-12})
    assert vals == [1.0, 1.5], vals

    ax = axis_C(80)
    for d in range(0, 81):
        # C - C_axis should vanish off the third-quadrant list
        pass
    third_deg = {q for _, _, q in third if q <= 80}
    claimed_ext = {8, 18, 22, 30, 39, 43, 44, 58, 60, 67, 71, 78, 79}
    assert claimed_ext <= third_deg, claimed_ext - third_deg
    assert 42 not in third_deg and 49 not in third_deg

    # axis formula reproduces C on axis degrees
    for d in [0, 1, 4, 7, 9, 16, 21, 25, 36, 42, 49, 64, 70]:
        assert abs(C[d] - ax[d]) < 1e-12, (d, C[d], ax[d])
    for d in claimed_ext:
        assert abs(C[d] - 1) < 1e-12

    eP = euler_P()
    first = next(d for d in range(0, 41) if int(round(P[d])) != eP[d])
    assert first == 14, first

    g = g_coeffs()
    g_mism = [d for d in range(0, 41) if int(round(P[d])) != g[d] and (P[d] or g[d])]
    assert g_mism[0] == 7, g_mism

    # mixed signs empty below 294
    found_mixed = []
    for n in range(-80, 81):
        for k in range(-80, 81):
            if n * k >= 0:
                continue
            if n == 0 or k == 0:
                continue
            w = w_of(n, k)
            if abs(w) > 1e-12:
                found_mixed.append((Qs(n, k), n, k, w))
    found_mixed.sort()
    assert found_mixed[0][0] == 294.0, found_mixed[0]

    print("PASS")
    print("C(0)=", C[0], "value set through 80=", vals)
    print("first Euler-vs-orthant mismatch degree", first)
    print("first g-vs-orthant mismatch degree", g_mism[0])
    print("first mixed-sign Q", found_mixed[0][0])
    print("chi_nat", CHI, "B(c_i,chi)=", B(C1, CHI), B(C2, CHI))
    print("s=8 second Appell pole 6r=1 has no integer r; term vanishes")
    print("third-quadrant degrees", sorted(claimed_ext))


if __name__ == "__main__":
    main()
