# E1: RTA Lambda_C row (K2_0, j=0) at x<0, |x| vs signed law; b3x method (read-only import from order12)
import sys, json, numpy as np; sys.dont_write_bytecode=True
sys.argv=['x']; sys.path.insert(0,'/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order12/scripts')
src=open('/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order12/scripts/b3x.py').read().split('res={}')[0]
exec(src)
res={}
for xs in ('-1/5','-2/3','-3/4'):
    x=Fr(xs); gx=g(x); gs=g(-1/x); s35=np.sqrt(ld(35)); Mg=(M@gx)[0]
    a=abs(1/x); r=1/x
    ra=float(abs(gs[0]-ld(a.numerator)/ld(a.denominator)/s35*Mg)/max(abs(gs[0]),ld(1e-30)))
    rs=float(abs(gs[0]-ld(r.numerator)/ld(r.denominator)/s35*Mg)/max(abs(gs[0]),ld(1e-30)))
    res[xs]=dict(abs_law=ra,signed_law=rs,K2_0=float(abs(gs[0]))); print(xs,res[xs],flush=True)
json.dump(res,open('../data/e1.json','w'),indent=1)
