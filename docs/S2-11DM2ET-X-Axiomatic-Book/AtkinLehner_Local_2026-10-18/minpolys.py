# Exact algebraic data: minimal polynomials over Q of eps_P (convention A) for one representative per sigma/inf class; root-of-unity flags.
import cypari2, json
pari=cypari2.Pari(); pari.allocatemem(10**9); gp=lambda s: pari(s)
D=json.load(open('local_eps.json')); C=json.load(open('compare.json')); NZ=D['NZ']
gp(f'Phi=polcyclo({NZ},x)')
out={}
for r,row in zip(D['results'],C['per_char']):
    k,e,_=r['chi']
    rec={P:{'root_of_unity_840':r['local'][P]['A']['root_of_unity_840'],'is_pm1':row[P]['eps_psiP_is_pm1'],
            'eps_pi_is_pm1':row[P]['eps_pi_p_is_pm1']} for P in ('P2','P5','P7')}
    if k<12 and e==0:
        for P in ('P5','P7'):
            rec[P]['minpoly']=str(gp(f"minpoly(Mod({r['local'][P]['A']['exact']},Phi),t)"))
        rec['W_minpoly']=str(gp(f"minpoly(Mod({r['prod_A']['exact']},Phi),t)"))
    out[str(r['chi'])]=rec
    print(r['chi'],rec)
json.dump(out,open('minpolys.json','w'),indent=1)
