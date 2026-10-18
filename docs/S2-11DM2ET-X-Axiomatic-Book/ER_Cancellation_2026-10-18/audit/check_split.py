# Audit check 1: Proposition 4 + 7 per character, 36-digit mpmath:  G_chi(-1/(20z)) - 2 R_chi(z) - T_chi(z) = 0, z in H.
# Includes points with Re z < 0 (Prop 4/7 are claimed on all of H) and a check of the R-tail stability (two cutoffs M).
import sys, math, mpmath as mp, common as C
from multiprocessing import Pool
mp.mp.dps = 36
ZS = [mp.mpc('0.6','0.45'), mp.mpc('1.0','0.9'), mp.mpc('0.25','0.3'), mp.mpc('-0.4','0.7'), mp.mpc('2.0','0.5')]
def run(i):
    mp.mp.dps = 36
    z = ZS[i]; CH = C.chars(); lines = []
    for key, c in CH.items():
        G = c.G(-1/(20*z)); R1 = c.R(z); T = c.Tser(z)
        M2 = 20*int(math.ceil(40*abs(complex(z)))); R2 = c.R(z, M=M2, K=50)
        lines.append(f"z={mp.nstr(z,3):14s} chi{key}: |G|={mp.nstr(abs(G),6):10s} |T|={mp.nstr(abs(T),6):10s} |G-2R-T|={mp.nstr(abs(G-2*R1-T),3):9s}  |R(M default)-R(M={M2})|={mp.nstr(abs(R1-R2),3)}")
    return lines
if __name__ == "__main__":
    with Pool(5) as p: res = p.map(run, range(len(ZS)))
    out = [l for r in res for l in r]
    print("\n".join(out)); open("check_split.txt", "w").write("\n".join(out)+"\n")
