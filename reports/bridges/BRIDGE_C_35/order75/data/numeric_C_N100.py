import json,sys
from fractions import Fraction as F
s=7;N=100;c1=(-1,1);c2=(-4,1)
M=((2,s),(s,s))
def B(v,w): return sum(v[i]*M[i][j]*w[j] for i in range(2) for j in range(2))
sgn=lambda x:(x>0)-(x<0)  # sgn(0):=0
def Q(n,k): return F(n*n+s*n*k)+F(s,2)*k*(k+1)
def run(R):
    P={};H={};neg=[]
    for n in range(-R,R+1):
        for k in range(-R,R+1):
            q=Q(n,k)
            if n>=0 and k>=0 and q<=N: P[q]=P.get(q,0)+1
            w=F(sgn(B(c1,(n,k)))-sgn(B(c2,(n,k))),2)
            if w and q<=N:
                H[q]=H.get(q,0)+w
                if q<0: neg.append((n,k,str(q)))
    return P,H,neg
out={}
for R in (200,400,800):
    P,H,neg=run(R)
    keys=sorted(set(P)|set(H))
    out[R]={str(e):{"P":P.get(e,0),"H":str(H.get(e,0)),"C":str(P.get(e,0)-H.get(e,0))} for e in keys}
    out[f"neg{R}"]=len(neg); out[f"negsample{R}"]=neg[:10]
out["stable"]=out[200]==out[400]==out[800]
json.dump(out,open(sys.argv[1],"w"),indent=1)
print("stable",out["stable"],"neg",out["neg200"],out["neg400"],out["neg800"])
print("exp P H C"); [print(e,v["P"],v["H"],v["C"]) for e,v in out[200].items()]
allowed={F(0),F(1),F(3,2)}
out_l=[(e,v["C"]) for e,v in out[800].items() if F(v["C"]) not in allowed]
print("CLAIM", "PASS" if not out_l else "FAIL", "outliers", out_l)
