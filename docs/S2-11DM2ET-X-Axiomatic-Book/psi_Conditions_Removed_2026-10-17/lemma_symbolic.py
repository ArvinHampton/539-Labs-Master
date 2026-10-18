# Symbolic ingredients of the Green-form lemma (Section 1 of the report):
#  (i)  Delta_w R_z(w)^{1/2} = (1/4) R_z(w)^{1/2}   for complex z   (Delta = -y^2(d_x^2+d_y^2))
#  (ii) d_wbar R_z = i/(2 (wbar-z)^2)
#  (iii) the Green form [u,v] = u_w v dw + u v_wbar dwbar is closed when Delta u = Delta v = (1/4)(.)
#  (iv) along w = z + i s the integrand for T_n = sqrt(y)K0(2 pi n y)e(nx) is  -e(nx)*{ [aY(K0+K1)-K0/2]/(2 sqrt(s(2y+s))) + K0 sqrt(s)/(4(2y+s)^{3/2}) }
import sympy as sp
x,y,X,Y=sp.symbols('x y X Y',real=True)
z=X+sp.I*Y
w=x+sp.I*y; wb=x-sp.I*y
R=y/((w-z)*(wb-z))
v=sp.sqrt(R)
lap=-y**2*(sp.diff(v,x,2)+sp.diff(v,y,2))
chk1=sp.simplify(sp.expand((lap-v/4)/v))
dwb=lambda f: (sp.diff(f,x)+sp.I*sp.diff(f,y))/2
dw =lambda f: (sp.diff(f,x)-sp.I*sp.diff(f,y))/2
chk2=sp.simplify(dwb(R)-sp.I/(2*(wb-z)**2))
# closedness: d(u_w v dw + u v_wbar dwbar) = (d_wbar(u_w v) - d_w(u v_wbar)) dwbar^dw = (u_w v_wbar - u_w v_wbar + u_{w wbar}v - u v_{w wbar})...
u=sp.Function('u')(x,y); V=sp.Function('V')(x,y)
expr=sp.simplify(dwb(dw(u)*V)-dw(u*dwb(V)))
# with u_{w wbar} = -Delta u/(4y^2) = -(1/4)u/(4y^2): expr = u_{wwbar}V - u V_{wwbar}
out=[f"(i)  (Delta R^(1/2) - R^(1/2)/4)/R^(1/2) simplifies to: {chk1}",
     f"(ii) d_wbar R - i/(2(wbar-z)^2) = {chk2}",
     f"(iii) d_wbar(u_w V) - d_w(u V_wbar) = {sp.simplify(expr - (dw(dwb(u))*V-u*dw(dwb(V))))} + (u_wwbar V - u V_wwbar); vanishes for equal eigenvalues"]
print("\n".join(out)); open("lemma_symbolic.txt","w").write("\n".join(out)+"\n")
