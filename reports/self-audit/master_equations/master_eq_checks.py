# Recompute numerical claims attached to the S2-11DM2ET-X master equations (Zenodo 17685476, lines cited in REPORT.md)
# and rerun with controls for the 539.9 s period.
from mpmath import mp,mpf,sqrt,log,e,pi,cos,quad,exp
mp.dps=30
o=[]; P=lambda s:(o.append(s),print(s))
lPl=mpf('1.616255e-35'); hbar_eVs=mpf('6.582119569e-16')
P("== Constants table / corollary (17685476:138-148, 250-256)")
P(f"G4 = 539 steps x 1 s = {539*1} s  (paper: 539.90 +/- 0.05 s)")
P(f"Banach lambda = ln3/539 = {log(3)/539}  (paper: 'approx 0.99996 < 1')")
P(f"R11 = sqrt(e^3 lPl^2 6 pi^2) = {sqrt(e**3*lPl**2*6*pi**2)} m (paper: 85.000 um)")
P(f"Lambda = 3/(e^3 lPl^2) = {3/(e**3*lPl**2)} m^-2 ; in Planck units 3/e^3 = {3/e**3} (paper: ~1.52e-123)")
P(f"tau_gamma = 539 x 25 fs = {539*25e-15} s = {539*25e-3} ps -> {1/(539*25e-15):.4e} Hz (paper: 13.475 us -> 40.00 Hz); 1/13.475us = {1/13.475e-6:.1f} Hz")
P(f"LISA line 1/539.90 s = {1000/mpf('539.90')} mHz (paper 1.8527 +/- 0.0009); 1/1.8527 mHz = {1000/mpf('1.8527')} s")
P(f"(1-3^-539) = 1 - {mpf(3)**-539}  (identical to 1 at any physical precision)")
P("== 5.3 F_friction factor (1000/T) for controls")
for T in [500,530,539,'539.9',540,550,600]:
  T=mpf(T); P(f"  T={T}: 1000/T = {1000/T}")
P("== 5.2 E_cosmos Higgs-echo integral  I(T)=int_0^{tau_echo} cos(2 pi tau/T) exp[-(tau-tau_echo)^2/(2 sig^2)] dtau")
tau=mpf('3e-12'); sig=hbar_eVs/mpf('0.6e-3')   # sigma_inh=0.6 meV is an energy; converted via hbar (source gives no conversion)
base=None
for T in [500,530,539,'539.9',540,550,600]:
  T=mpf(T); I=quad(lambda x:cos(2*pi*x/T)*exp(-(x-tau)**2/(2*sig**2)),[0,tau])
  base=base or I; P(f"  T={T}: I = {mp.nstr(I,20)}  rel. change vs T=500: {mp.nstr((I-base)/base,3)}")
P("  sigma_inh is in meV but enters a Gaussian in seconds: dimensionally inconsistent as written (converted with hbar here).")
P("== 5.4 mu = 1.55 with the source's stated inputs (17685476:1254,1387-1403)")
k1,k2,d,th=mpf('1.1'),mpf('-1.0'),3,0
t_echo=mpf('0.8')*mpf('0.6')/mpf('0.6'); t_cos=cos((k1-k2)*d-th)
t_rho=mpf('0.181')*mpf('0.31')/mpf('1e-7')
P(f"  A_HQP*dDelta/sigma_inh = {t_echo}; cos((k1-k2)d-theta) = {mp.nstr(t_cos,8)} (divided by 1+sigma_11D: sigma_11D never given)")
P(f"  0.181*rho_DM/E0 = 0.181*0.31 GeV/cm^3 / 1e-7 GeV = {mp.nstr(t_rho,6)} cm^-3  (not dimensionless; [mu]=1 claimed at 17685476:1838)")
P(f"  1 + 0.8 alone = 1.8 > 1.55; f_energy, Omega_11D, sigma_11D, p are never assigned -> mu=1.55 not reproducible; mu contains no 539.9 at all")
P("  source tuning rule (17685476:1088): 'If mu < 1.0 at kappa_dark = 0.45, reduce f_energy by 0.05'")
P("== 5.5 S/N: values in the same record: 1.43 (line 103), 1.3196 (1454), 1.33 (1832); contains (1-3^-539) only, no 539.9; O_signal, sigma_background unassigned")
P("== 17703994 'master harmonic' re-check")
yr=mpf('31556925.19')
P(f"  (61^2*55)^(3/2)*3^(1/6) = {(61**2*55)**mpf(1.5)*mpf(3)**(mpf(1)/6)}")
for T in [500,530,539,'539.9',540,550,600]:
  T=mpf(T); n=yr/T; P(f"  T={T}: year/T = {mp.nstr(n,10)}; nearest int {int(mp.nint(n))}; residual {mp.nstr((n-mp.nint(n))*T,6)} s")
P(f"  58481*539.9 - year = {58481*mpf('539.9')-yr} s ; period giving exact 58481 = {yr/58481} s")
P("== 17810793 harmonics h_j = 10..650000: any period P is matched by some integer h within T/(2P) relative error, for ANY T")
for name,Pd in [("Schwabe 11 yr",11*yr),("~24000xT cycle (Rieger 154 d)",154*86400),("5-min p-mode 300 s x h? (h>=10 so no)",3000)]:
  for T in [500,'539.9',600]:
    T=mpf(T); h=mp.nint(Pd/T); P(f"  {name}: T={T}: h={int(h)} rel err {mp.nstr(abs(h*T-Pd)/Pd,3)}")
open('master_eq_checks.out','w').write("\n".join(o))
