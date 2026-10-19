# Symbolic (general k) verification of the lattice identities used in Proposition K1 (report §1), plus
# brute-force Burnside counts on R/2sqrt(d)R for n=2..40.
import sympy as sp, json
k=sp.symbols('k',positive=True,integer=True); m=2*k**2-1
e1=sp.Matrix([1,0]); f=sp.Matrix([0,1/m]); A=sp.Matrix([[2,2*m**2],[2*m**2,2*m**2]])
g=sp.Matrix([[0,-m],[1/m,2*m]]); h=(g+sp.eye(2))/(2*k)
B=lambda x,y: sp.simplify((x.T*A*y)[0])
out={}
out['h^2=g']=sp.simplify(h*h-g)==sp.zeros(2)
out['h isometry']=sp.simplify(h.T*A*h-A)==sp.zeros(2)
out['g e1 = f']=sp.simplify(g*e1-f)==sp.zeros(2,1)
out['Gram(e1,f)']=str([B(e1,e1),B(e1,f),B(f,f)])
u=(e1+f)/(2*k)
out['h e1 = u']=sp.simplify(h*e1-u)==sp.zeros(2,1)
out['h u = f']=sp.simplify(h*u-f)==sp.zeros(2,1)
out['h f = -u + 2k f']=sp.simplify(h*f-(-u+2*k*f))==sp.zeros(2,1)
out['h^-1 f = u']=sp.simplify(h.inv()*f-u)==sp.zeros(2,1)
out['e1 = 2k u - f']=sp.simplify(e1-(2*k*u-f))==sp.zeros(2,1)
out['Gram(u,f)']=str([sp.factor(B(u,u)),sp.factor(B(u,f)),sp.factor(B(f,f))])
# Burnside on R_n/2sqrt(d)R_n, R_n=Z[sqrt d], d=n^2-1, eps=n+sqrt d acting by multiplication; elements a+b sqrt d,
# a mod 2d? R/2sqrt(d)R has Z-basis rep: 2sqrt d R = Z(2d)+Z(2 sqrt d): so a mod 2d, b mod 2.
def counts(n):
    d=n*n-1; els=[(a,b) for a in range(2*d) for b in range(2)]
    red=lambda a,b:(a%(2*d),b%2)
    mul=lambda a,b:red(n*a+d*b,a+n*b)
    lab={};no=0;no2=0;lab2={}
    for e in els:
        if e in lab: continue
        st=[e];lab[e]=no
        while st:
            x=st.pop()
            for y in (mul(*x),red(-x[0],-x[1])):
                if y not in lab: lab[y]=no; st.append(y)
        no+=1
    for e in els:
        if e in lab2: continue
        st=[e];lab2[e]=no2
        while st:
            x=st.pop()
            for y in (mul(*mul(*x)),red(-x[0],-x[1])):
                if y not in lab2: lab2[y]=no2; st.append(y)
        no2+=1
    return no,no2
bc={n:counts(n) for n in range(2,41)}
out['burnside_ok_all_n_2_40']=all(bc[n]==(n*(n+1),2*n*n) for n in bc)
out['sample']={n:bc[n] for n in (2,3,4,7,17,31)}
print(json.dumps(out,indent=1)); json.dump(out,open('proof_ingredients.json','w'),indent=1)
