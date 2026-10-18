import mpmath as mp
mp.mp.dps = 30
from em import res
I = mp.log(6+mp.sqrt(35))/(2*mp.sqrt(35)); sp_ = mp.sqrt(mp.pi)
out=[]
aP = res["P_s"][1]; cf = sp_*(49-2*mp.sqrt(14))/140
out.append(f"a_P = {aP}   closed form sqrt(pi)(49-2 sqrt14)/140 = {cf}   diff {aP-cf}")
aH = res["H_s"][1]
basis = [aH/sp_, mp.mpf(1), mp.sqrt(14), mp.sqrt(2)/mp.sqrt(595), mp.sqrt(2)/mp.sqrt(7)*0+mp.sqrt(1190)]
rel = mp.pslq([aH/sp_, 1, mp.sqrt(14), mp.sqrt(1190), mp.sqrt(85)], maxcoeff=10**6, maxsteps=10**6)
out.append(f"a_H/sqrt(pi) = {aH/sp_};  PSLQ on [a_H/sqrt pi, 1, sqrt14, sqrt1190, sqrt85]: {rel}")
for nm in ["P_s","C_third","R","E"]:
    b = res[nm][2]
    rel = mp.pslq([b, 1, I], maxcoeff=10**6, maxsteps=10**6)
    out.append(f"const({nm}) = {b};  PSLQ on [b, 1, I]: {rel}")
out.append(f"zeta(0,K) = const(E) + (7/10) I = {res['E'][2] + mp.mpf(7)/10*I}")
print("\n".join(out)); open("closed_forms.txt","w").write("\n".join(out)+"\n")
