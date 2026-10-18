"""Extra random tests of the profile S-law off the 140-label family, keeping only cases with LHS != 0."""
import random
from fractions import Fraction as Fr
from profile_law_check import check_S, G
random.seed(7)
out=[]; worst=0; kept=0; tried=0
while kept < 60 and tried < 3000:
    tried += 1
    d1 = random.choice([1,2,3,5,7,10,14]); d2 = random.choice([1,2,3,5,7,10,14])
    al = (Fr(random.randrange(d1),d1), Fr(random.randrange(d2),d2))
    d3 = random.choice([1,2,5,7,10,35]); d4 = random.choice([1,2,5,7,35])
    be = (Fr(random.randrange(d3),d3), Fr(random.randrange(d4),d4))
    x = random.choice([Fr(1),Fr(-1),Fr(1,3),Fr(-1,3),Fr(3),Fr(-3),Fr(1,9),Fr(-9,1)])
    if abs(G(al,be,-1/x)) < 1e-9: continue
    l,r = check_S(al,be,x); kept += 1; worst = max(worst, abs(l-r))
    out.append(f"al={al} be={be} x={x}: LHS={l:.12f} |dev|={abs(l-r):.1e}")
out.append(f"SUMMARY: {kept} nonzero random tests (of {tried} drawn), max |LHS-RHS| = {worst:.2e}")
print(out[-1]); open("profile_law_random.txt","w").write("\n".join(out)+"\n")
