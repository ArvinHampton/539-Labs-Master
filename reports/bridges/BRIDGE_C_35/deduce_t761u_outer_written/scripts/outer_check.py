# DEDUCED arithmetic only: outer_* from WRITTEN formula (e60cad9b L16-22) vs 1bab65c4 L15-18 listed values and |ledger_exp|.
from fractions import Fraction as F
oe=lambda m:35*m*m+7*m
oo=lambda m:35*m*m+42*m+F(49,4)
listed_e=[42,154,336,588,910,1302,1764,2296]           # 1bab65c4, m>=1
listed_o=[12.25,89.25,236.25,453.25,740.25,1097.25,1524.25]  # 1bab65c4, m>=0
ok=True
for i,v in enumerate(listed_e):
    m=i+1; r=oe(m)==v; ok&=r; print(f"even m={m} outer={oe(m)} listed={v} match={r}")
for m,v in enumerate(listed_o):
    r=float(oo(m))==v; ok&=r; print(f"odd m={m} outer={oo(m)} ({float(oo(m))}) listed={v} match={r}")
# |ledger_exp| from xi_written exponent_parity_check.log, k=0..11
led={0:0,1:F(49,4),2:42,3:F(357,4),4:154,5:F(945,4),6:336,7:F(1813,4),8:588,9:F(2961,4),10:910,11:F(4389,4)}
for k,a in led.items():
    o=oe(k//2) if k%2==0 else oo(k//2); r=o==a; ok&=r; print(f"k={k} |ledger_exp|={a} outer={o} match={r}")
print("note: 1bab65c4 even list starts m=1 (outer_even(0)=0 not listed) -> G-O1")
print("ALL_MATCH", ok)
