from fractions import Fraction as F
for m in range(0,6):
    for k,name,outer in ((2*m,'even',35*m*m+7*m),(2*m+1,'odd',F(35*m*m+42*m)+F(49,4))):
        e=F(-35,4)*k*k-F(7,2)*k
        print(f"k={k} sector={name} m={m} ledger_exp={e} -outer={-outer} match={e==-outer} char={F(7,2)*k}")
for k in range(-4,0): print(f"k={k} ledger_exp={F(-35,4)*k*k-F(7,2)*k} (k<0: not of -outer form; folding ABSENT)")
