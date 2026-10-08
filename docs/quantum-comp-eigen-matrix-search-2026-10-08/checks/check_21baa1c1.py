import math, numpy as np
from sympy import floor, exp, N, GoldenRatio as golden
e3=exp(3); n_flux=int(floor(e3*3**5)); phi7=golden**7
sf=n_flux/(N(e3)*1001)*0.68/0.18
print("n_flux",n_flux,"scale_factor(code1)",float(sf),"m_base code1",float((61/1001)*(phi7/539.9)*sf))
m2=(61/1001)*(phi7/539.9)*(n_flux/float(N(e3)))*0.68/0.18
print("code2 m_base",float(m2), "4880/e3",n_flux/float(N(e3)))
print("printed product",0.060939*0.053792*243*0.68*5.5556)
print("theta12",math.degrees(math.asin(math.sqrt(2/55))),"dm21",(float(golden)**2/55)*1e-5)
print("e3/55",float(N(e3))/55,"base*e3/55",float((61/1001)*(phi7/539.9))*float(N(e3))/55)
print("539.9/(e3*1001/61)",539.9/(float(N(e3))*1001/61),"*phi^3",539.9/(float(N(e3))*1001/61)*float(golden)**3)
t=np.linspace(0,539.9,200);print("code2 t samples",[ (round(t[i],1), round(float(m2)+0.000113*math.sin(2*math.pi*t[i]/539.9),5)) for i in range(0,100,20)])
print("v^2/1e14GeV eV",246**2/1e14*1e9, "v^2/1e15",246**2/1e15*1e9)
print("M_-U/(e3 phi^3)",1414/(float(N(e3))*float(golden)**3),18832/(float(N(e3))*float(golden)**3))
print("g_-U*61/55",0.0098*61/55, "539/9",539/9)
