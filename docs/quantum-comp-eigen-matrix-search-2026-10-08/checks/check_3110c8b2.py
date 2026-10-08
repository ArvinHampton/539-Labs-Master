import math
phi=(1+5**.5)/2
print("m = 539.9*cos(2 pi n/539.9) MeV:")
for n in [1,2,3,4,5,118,6,7,8,9,10,119]: print(n, round(539.9*math.cos(2*math.pi*n/539.9),4))
f=lambda Q: sum(2*math.cos(2*math.pi*n/539.9)*(539.9-n) for n in Q)
print("7021 identity: quarks",f([1,2,3,4,5,118]),"leptons",f([6,7,8,9,10,119]))
print("alpha^-1 formula",2*math.pi*7021/(539.9*math.log(3)*phi**2))
