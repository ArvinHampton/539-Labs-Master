import json, sympy
out={}
for s in (9,25):
    r=json.load(open(f"irr_modl_{s}.json")); ell=r["ell"]; N=r["Kbig"]
    fN=sympy.factorint(N); order=N**3
    for p in fN: order=order*(p*p-1)//(p*p)
    order*=2
    fo=sympy.factorint(order)
    out[s]={"ell":ell,"N_used(multiple of level)":N,"N_factor":{str(k):v for k,v in fN.items()},
      "|Mp2(Z/N)|=2|SL2|":str(order),"order_factor":{str(k):v for k,v in fo.items()},
      "ell_divides":order%ell==0,"ell_gt_max_prime":ell>max(fo)}
    print(s,out[s])
json.dump(out,open("lift_check.json","w"),indent=1)
