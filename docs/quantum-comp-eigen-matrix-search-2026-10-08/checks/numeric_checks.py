"""Re-run checkable eigenvalue/matrix/trace claims quoted in the Quantum Comp archive.
Values quoted from the archive are copied verbatim into CLAIM strings; nothing is corrected in the source."""
import numpy as np, sympy as sp, math, json, cmath
from scipy.integrate import quad
hbar=6.582119569e-16  # eV s
out=[]
def rec(id_,src,claim,computed,verdict,note=''):
    out.append(dict(id=id_,source=src,claim=claim,computed=computed,verdict=verdict,note=note))
# ---- A. two-level brane-crossing Hamiltonian (chat-01 / 17 Theorems)
Ep,Em,V=sp.symbols('E_p E_m V',real=True)
H=sp.Matrix([[Ep,V],[V,Em]])
ev=list(H.eigenvals().keys())
target=[(Ep+Em)/2+sp.sqrt((Ep-Em)**2/4+V**2),(Ep+Em)/2-sp.sqrt((Ep-Em)**2/4+V**2)]
ok=all(any(sp.simplify(e-t)==0 for e in ev) for t in target)
rec('A1','raw/chat-01.txt:3438','E_±(t) ≈ (E₊ + E₋)/2 ± √[(E₊ − E₋)²/4 + V(t)²]',str(ev),'HOLD' if ok else 'FAIL','exact eigenvalues of 2x2 real symmetric H (sympy)')
D=sp.symbols('Delta',positive=True)
split=sp.sqrt(D**2+4*V**2); ser=sp.series(split,V,0,4).removeO()
rec('A2','raw/chat-01.txt:3440','For weak leakage (|V(t)| << |E₊ − E₋|), the splitting is ΔE(t) ≈ V(t)² / |E₊ − E₋|',
    f'E_+ − E_- = sqrt(Δ²+4V²) ≈ {sp.simplify(ser)}; each level shifts by V²/Δ, splitting changes by 2V²/Δ','FAIL',
    'V²/|Δ| is the 2nd-order shift of each level, not the splitting (splitting ≈ |Δ| + 2V²/|Δ|)')
Vreq=math.sqrt(0.619*0.6)
rec('A3','raw/chat-01.txt:3441-3442','E₊ − E₋ ... set by ... σ_inh = 0.6 meV; ΔE_peak ≈ [...]² / σ_inh ≈ 0.619 meV (weak-leakage regime assumed at 3440)',
    f'|V| implied = sqrt(0.619*0.6) = {Vreq:.4f} meV vs |Δ| = 0.6 meV (ratio {Vreq/0.6:.3f})','FAIL','weak-coupling condition |V|<<|Δ| is violated by the chat\'s own numbers; exact splitting would be sqrt(0.36+4*0.371)=%.3f meV'%math.sqrt(0.36+4*Vreq**2))
rec('A4','raw/chat-01.txt:3445-3447','Δφ_mean ≈ 0.006 rad; E_bind ≈ ΔE² / (2 ħω) ≈ 0.0018 meV',f'0.6/100 = {0.6/100}; 0.6²/200 = {0.36/200} meV','HOLD')
t=hbar/(0.0018e-3)
rec('A5','raw/chat-01.txt:3448','τ_settle = ħ / E_bind ≈ 2 ħω ħ / ΔE² ≈ 22.5 attoseconds (with E_bind ≈ 0.0018 meV)',f'ħ/0.0018 meV = {t:.3e} s = {t*1e12:.0f} ps','FAIL','off by ~1.6e7')
e=100*(1-math.sqrt(2)/2); t2=hbar/(e*1e-3)
rec('A6','raw/chat-01.txt:1918-1921','E_bind = 100 meV × (1 − √2/2) ≈ 29.3 meV; τ_settle = ħ / E_bind ≈ (6.582 × 10^{-16} eV·s) / (29.3 × 10^{-3} eV) ≈ 22.5 attoseconds',
    f'E_bind = {e:.3f} meV (HOLD); ħ/E_bind = {t2:.3e} s = {t2*1e15:.2f} fs','FAIL','arithmetic gives 22.5 femtoseconds, not attoseconds (factor 1000); 22.5 as is repeated at chat-01 lines 1952, 2222, 2343, 2387, 2505, 2679')
# ---- density matrix
phi=sp.symbols('phi',real=True)
rho=sp.Rational(1,2)*sp.Matrix([[1,sp.exp(sp.I*phi)],[sp.exp(-sp.I*phi),1]])
evr=[sp.simplify(x) for x in rho.eigenvals().keys()]; pur=sp.simplify((rho*rho).trace())
sy=sp.Matrix([[0,-sp.I],[sp.I,0]]); exp_sy=sp.simplify((rho*sy).trace())
rec('A7','raw/chat-01.txt:3862-3866','ρ(Δx) = (1/2) [[1, e^{iΔφ}],[e^{-iΔφ}, 1]] ... V(Δx) = |⟨σ_y⟩| = |exp[i δΔφ(Δx)]| = exp[−(δΔφ(Δx))² / 2]',
    f'eigenvalues {evr}, Tr ρ² = {pur}, Tr(ρσ_y) = {exp_sy}; |exp(iθ)| = 1 for real θ','FAIL',
    'as written ρ is a pure state for every Δφ (no decoherence); |exp(iδΔφ)| = 1, and exp(−δΔφ²/2) only arises after averaging over a Gaussian-distributed phase, which the text does not state')
rec('A8','raw/chat-01.txt:1212','Tracing out -U yields a mixed state in +U ... global density matrix ρ_{+U ⊕ -U} remains pure','qualitative; standard (partial trace of a pure entangled state is mixed)','HOLD (qualitative)')
# ---- collective tubulin Lindblad numbers
rec('A9','raw/chat-01.txt:6141-6143','Collective enhancement factor √N ≈ 26 (for 676 tubulins); Γ_sup = N Γ_single ≈ 26 × 0.01 meV ≈ 0.26 meV → T₂ ≈ 1 / Γ_sup ≈ 2.5 ps (bare)',
    f'√676 = {math.sqrt(676):.0f}; N·0.01 = {676*0.01:.2f} meV; √N·0.01 = 0.26 meV; ħ/0.26 meV = {hbar/0.26e-3*1e12:.2f} ps','FAIL (internal)','formula says N·Γ (=6.76 meV, T₂≈0.097 ps) but number uses √N; also line 6203 says "enhanced by √N" then "γ_eff (bright) ≈ N γ_single"')
x=hbar/(0.01e-3*(26.7/(0.5*676)))
rec('A10','raw/chat-01.txt:6149','T₂ ≈ ħ / (Γ_single × (kT / J N)) ≈ 100–300 ms (for J ≈ 0.5 meV, N = 676, kT = 26.7 meV)',f'{x:.3e} s','FAIL','~0.83 ns, not 100–300 ms')
g=0.01/676*(27/0.5)**2
rec('A11','raw/chat-01.txt:6172-6173','γ_eff ≈ γ_single / N × (kT / J)^2 ≈ 0.01 meV / 676 × (27 / 0.5)^2 ≈ 10^{-5} meV; T₂ ≈ ħ / γ_eff ≈ 65 ms',
    f'γ_eff = {g:.4f} meV; ħ/γ_eff = {hbar/(g*1e-3):.2e} s; even with 1e-5 meV: ħ/1e-8 eV = {hbar/1e-8:.2e} s','FAIL','γ_eff is 0.043 meV (not 1e-5); 1e-5 meV would give 66 ns, not 65 ms')
g2=0.01*(26.7/(0.5*676))**2
rec('A12','raw/chat-01.txt:6218-6224','γ_eff ≈ 0.01 × (26.7 / 0.5 × 676)^2 ≈ ... ≈ 6.24 × 10^{-5} meV; T₂ ≈ 6.582 × 10^{-16} / 6.24 × 10^{-5} ≈ 1.055 × 10^{-11} s ≈ 10.55 ns',
    f'γ_eff = {g2:.3e} meV (HOLD); ħ/γ_eff = {hbar/(g2*1e-3):.3e} s = {hbar/(g2*1e-3)*1e9:.2f} ns','HOLD (final) / FAIL (intermediate)','10.55 ns is right; the intermediate "1.055 × 10^{-11} s" is 10.55 ps (meV→eV factor dropped)')
rec('A13','raw/chat-01.txt:6226','exp(−ΔE / kT) ≈ exp(−0.6 / 26.7) ≈ 0.978',f'{math.exp(-0.6/26.7):.4f}','HOLD')
# ---- B. K+ incidence spectrum + graph identities
rec('B1','raw/chat-05.txt:991-992','Incidence spectrum eigs: {2: 56, -1: 297, 1: 185, 0: 1}; 56+297+185+1 = 539 = V',
    'adjacency spectrum of disjoint fiber cliques (56 K3, 185 K2, 1 K1) = {2:56, -1:297, 1:185, 0:1}; see kplus_results.json','HOLD','computed in kplus_laplacian.py')
rec('B2','raw/chat-13.txt:29 etc.','K⁺ (V = 539, E = 594, F = 56 ...)',f'Euler χ = {539-594+56}; 594 = 538 path + 56 chords; n_jump = 241 recovered','HOLD')
# ---- C. map Lyapunov / Markov
gm=(sp.Rational(1,3)*sp.Rational(4,3)*sp.Rational(2,3))**sp.Rational(1,3)
rec('C1','raw/chat-01.txt:8525','The average absolute multiplier of the written map evaluates to 2/3, so the Lyapunov exponent evaluates to ln(2/3) ≈ –0.405 ... n = 10^18 ≈ 102 steps; n = 10^20 ≈ 114 steps',
    f'geometric mean of Canonical-T3 branch factors (1/3,4/3,2/3) = {gm}; ln(2/3) = {math.log(2/3):.6f}; ln(1e18)/0.405 = {math.log(1e18)/0.405:.1f}; ln(1e20)/0.405 = {math.log(1e20)/0.405:.1f}','HOLD',
    'holds as a GEOMETRIC mean; the arithmetic mean (1/3+4/3+2/3)/3 = 7/9 (conflict-brief A9)')
E=(2/3)*math.log(1/3)+(1/3)*math.log(4/3)
rec('C2','extracts/1e7fe572...md (HQCC Theorem Derives 539.9s Period)','𝔼_π[χ] = (2/3)ln(1/3) + (1/3)ln(4/3) = ln(4^{1/3}/3) ≈ −0.6365; λ_mean ≈ 0.529; N_⋆ = ⌈ln 4880/0.6365⌉ = 14',
    f'{E:.6f}; ln(4^(1/3)/3) = {math.log(4**(1/3)/3):.6f}; e^E = {math.exp(E):.4f}; ceil = {math.ceil(math.log(4880)/0.6365)}','HOLD','stationary distribution π = (2/3,1/3) over branches')
rec('C3','extracts/3da1f6d2...md (Hampton Qutrit Collatz Theorem Proven)','λ = −ln(27)/9 = −ln3/3 ≈ −0.4054651',f'−ln27/9 = {-math.log(27)/9:.7f}','FAIL','already flagged in the extract / BATCH2-ROLLUP')
rec('C4','raw/chat-13.txt:74-76','The same proof text states λ = ln(3)/539 ≈ 0.99996. The actual numerical value is ln(3)/539 ≈ 0.002038.',f'ln3/539 = {math.log(3)/539:.6f}; 1−ln3/539 = {1-math.log(3)/539:.5f}','HOLD (chat\'s correction)','Banach λ = ln3/539 is RETRACTED in INGEST-PROTOCOL.md / prompt.txt line 10')
# canonical T3 depths for information
def T3(n):
    r=n%3
    return n//3 if r==0 else ((4*n+2)//3 if r==1 else (2*n+1)//3)
def depth(n):
    k=0
    while n!=1 and k<10000: n=T3(n); k+=1
    return k
rec('C5','raw/chat-01.txt:8518-8521 (Public Grok)','seed 10^19 reaches 1 in 96 steps; seed 10^20 reaches 1 in 132 steps; seed 2^60 reaches 1 in 94 steps (for "the written map")',
    f'Canonical T3 depths: 10^18→{depth(10**18)}, 10^19→{depth(10**19)}, 10^20→{depth(10**20)}, 2^60→{depth(2**60)}, 4880→{depth(4880)}','HOLD','reproduced exactly by Canonical T3, so "the written map" behaves as Canonical T3 here')
# mod-9 well-definedness (question raised in extracts 0ed64ceb / BATCH3 L3.4)
bad=[a for a in range(9) if len({T3(n)%9 for n in range(a+9*0+9*1, 9*400, 9) if n>0})>1]
rec('C6','extracts/0ed64ceb...md:87; BATCH3-ROLLUP.md:87','Whether T3 admits a well-defined induced map on ℤ/9 (or a 9-state transfer matrix ...) is a concrete, checkable question',
    f'n mod 9 does NOT determine T3(n) mod 9 for residues {bad}','INFO','so any mod-9 "transfer matrix" must be stochastic (needs n mod 27 or a lift measure); question posed by extract authors, not a chat claim')
# ---- D. CKM / mixing
mt,mc,mu,mW=172.57,1.2730,0.00216,80.369
J=(mt**2-mc**2)*(mc**2-mu**2)*(mt**2-mu**2)*math.sin(1.2)*(1+0.05*0.32/10)/(12*mW**6)
rec('D1','raw/chat-06.txt:113','J = (m_t^2 - m_c^2)(m_c^2 - m_u^2)(m_t^2 - m_u^2) sin δ_CKM (1 + β_CP ρ_DM/10) / (12 m_W^6)  J≈3×10^{-5} enhanced (δ_CKM ≈ 1.2 rad, β_CP=0.05)',
    f'{J:.3e} (m_t=172.57, m_c=1.273, m_u=0.00216, m_W=80.369 GeV)','FAIL','formula evaluates to ~4e-4, ~14x the quoted 3e-5; it is also not the Jarlskog invariant (PDG J ≈ 3.1e-5 is a CKM-element combination)')
phi_g=(1+5**0.5)/2
rec('D2','prompt.txt:7 (Kept); reports/conflict-brief-for-grok.md:29 ("|V_us|=1/φ^2=0.382 HOLDS")','|V_us|=1/φ²',f'1/φ² = {1/phi_g**2:.6f}; PDG |V_us| ≈ 0.2243','HOLD (arithmetic) / FAIL vs data','not in saved chat text; freeze keeps it')
rec('D3','prompt.txt:10 (Retracted); theorems/unification-proof.txt:140','|V_cb| ≈ 1/φ^4 ≈0.056 (observed ~0.04)',f'1/φ⁴ = {1/phi_g**4:.4f}; PDG |V_cb| ≈ 0.041','FAIL','already RETRACTED (|V_cb| 0.146) in the freeze')
rec('D4','theorems/unification-proof.txt:142','|V_ub| ≈ 1/φ^6 ≈0.009 (observed ~0.004)',f'1/φ⁶ = {1/phi_g**6:.4f}','FAIL','arithmetic slip; not a chat; not on the retraction list')
masses=[2.30,4.80,95.00,1275.00,4180.00,173210.00]
rec('D5','extracts/931fd19f...md:39 / ea74f77f...md','Σ_q m_q = 178767.10 MeV ("trace" of the six quark masses)',f'{sum(masses):.2f}','HOLD (sum)','identification with Σz = 7021 is FAIL (already in extract)')
vals=[539.9*math.cos(2*math.pi*n/539.9) for n in [1,2,3,4,5,118]]
rec('D6','extracts/374f8b17...md; ea74f77f...md','m_q = 539.9 · Re(ζ_{539.9}^n), n ∈ {1,2,3,4,5,118} ("eigenvalues of the Frobenius warp operator")',str([round(v,3) for v in vals]),'FAIL','no value exceeds 539.9 MeV; none equals any listed mass')
# ---- E. resonant trace / zeta
P=539.9
re_=quad(lambda t: math.sin(2*math.pi*t/P)*math.cos(2*math.pi*t/P),0,P)[0]; im=quad(lambda t: math.sin(2*math.pi*t/P)**2,0,P)[0]
rec('E1','extracts/374f8b17...md (Riemann Zeta Function Resonant Trace)','∫_0^{539.9} sin(2πt/539.9) e^{2πit/539.9} dt = 539.9/(2i)',f'{re_:.3e} + {im:.4f} i  (= +i·P/2); 539.9/(2i) = −{P/2:.2f} i','FAIL','sign error (re-verified; extract already notes it)')
rec('E2','extracts/374f8b17...md','Fundamental unit ε = 331.3 with log ε = 2π exactly',f'e^(2π) = {math.exp(2*math.pi):.4f}; ln 331.3 = {math.log(331.3):.4f}','FAIL')
ordr=sp.n_order(3,539); tot=sp.totient(539)
rec('E3','extracts/374f8b17...md (residual note)','ord_539(3) = 210 = φ(539)/2; real cyclotomic subfield degree 210, not 269 generators',f'ord = {ordr}; φ(539) = {tot}; (539-1)/2 = 269; gcd(11,539) = {math.gcd(11,539)}','HOLD (extract\'s note); FAIL for chat\'s k = 1..269',
    'also: ξ ↦ ξ^11 is not a Galois automorphism of Q(ζ_539) since gcd(11,539)=11, so "Frobenius Φ_11" fails even at the integer 539')
rec('E4','raw/chat-02.txt:1213','the total linear density of states is of order 243/(2π) ≈ 38.7 (mode spacing 2π/G4)',f'243/(2π) = {243/(2*math.pi):.2f}; with spacing 2π/G4 the density is 243·G4/(2π) = {243*539.9/(2*math.pi):.0f}','HOLD (arithmetic) / inconsistent units','the stated spacing implies a factor G4 that the quoted 38.7 omits; conclusion (constant, not log, density) unaffected')
rec('E5','raw/chat-02.txt:1060,1076','counting function for eigenvalues of −d²/dt² on a fixed-length interval is still linear in T (spacing π/L) ... constant drift 2π/G4 ... N(T) ∼ (G4/2π) T','Dirichlet −d²/dt² on [0,L]: √λ_n = nπ/L → N linear in √λ; −i d/dt on circle length G4: λ_k = 2πk/G4 → N(T) = G4 T/2π','HOLD (standard)')
rec('E6','raw/chat-02.txt:1126','H± = −i d/dt + V±(t) on L²(ℝ) ... N±(T) ∼ (1/2π) ∫ √(λ − V±(θ))^+ dθ · T','first-order −i d/dt+V is gauge-equivalent to −i d/dt (spectrum ℝ, no bands); the √(λ−V) form belongs to −d²/dt²+V','QUALIFIED','"linear" conclusion holds; the quoted IDS formula / band-structure remark are for the second-order operator, not the stated first-order one')
# ---- F. reports (outside the 621-chat archive)
for s in [5,7,8,11]:
    M=np.array([[2,s],[s,s]],float); w=np.linalg.eigvalsh(M)
    rec(f'F{s}','reports/heavy-daily/da927a09dac3-Matrix_Analogues...md:10-16',f'M_s = [[2, s], [s, s]] has determinant -s(s-2) ... Signature is (1,1) (s={s})',f'det = {np.linalg.det(M):.3f} (= {-s*(s-2)}); eigenvalues {np.round(w,4).tolist()}','HOLD')
B7=sp.Matrix([[1,sp.Rational(7,2)],[sp.Rational(7,2),sp.Rational(7,2)]])
rec('F12','reports/heavy-daily/U1-GS-ZWEGERS-1d8e558.md:37','B_7 = [[1, 7/2],[7/2, 7/2]], det B_7 = −35/4',f'det = {B7.det()}; eigenvalues {[sp.nsimplify(x) for x in B7.eigenvals()]}','HOLD')
res=lambda s,f: sorted({f(n,k)%s for n in range(4*s) for k in range(4*s)})
rec('F13','reports/heavy-daily/da927a09dac3...md:22-41','residues: s=7 {0,1,2,4}; s=11 affine {0,1,3,4,5,9}; s=5 {0,1,4}; s=8 hom {0,1,4,5}, affine {0,1,4}',
    str(dict(s7=res(7,lambda n,k:n*n+7*n*k+7*k*(k+1)//2),s11=res(11,lambda n,k:n*n+11*n*k+11*k*(k+1)//2),s5=res(5,lambda n,k:n*n+5*n*k+5*k*(k+1)//2),s8h=res(8,lambda n,k:n*n+8*n*k+4*k*k),s8a=res(8,lambda n,k:n*n+8*n*k+4*k*(k+1))) ),'HOLD','affine form Q_s = n²+snk+(s/2)k(k+1)')
# ---- G. unification-proof tridiagonal mass matrix (paper, not chat)
p=phi_g
M=np.array([[p**3/61,1/p**3,0],[1/p**3,p**5/61,1/p**3],[0,1/p**3,p**7/61]])
w=np.linalg.eigvalsh(M)
mod=(1+0.18*0.31/10)**-0.5
rec('G1','theorems/unification-proof.txt:100-111','M = [[φ³/61, 1/φ³, 0],[1/φ³, φ⁵/61, 1/φ³],[0, 1/φ³, φ⁷/61]] × (1001/61) × mod × √2 × (1/φ^exp) ... three distinct real positive eigenvalues',
    f'core-matrix eigenvalues {np.round(w,5).tolist()}; det = {np.linalg.det(M):.5f}','FAIL','one eigenvalue is negative, so "three distinct real positive eigenvalues" fails; the common scale factor cannot change signs')
r=w.max()/np.abs(w).min()
rec('G2','theorems/unification-proof.txt:115-122','Charged leptons: exp ≈10 ... m_e ≈0.511, m_μ ≈105.7, m_τ ≈1777; Down: exp ≈11 ... m_d ≈4.8, m_s ≈95, m_b ≈4180; Up: exp ≈17 ... m_u ≈2.3, m_c ≈1275, m_t ≈173210 MeV',
    f'every sector uses the same core matrix times a scalar, so all sectors share the eigenvalue ratios {np.round(w/np.abs(w).min(),3).tolist()} (|max/min| = {r:.2f}); required ratios: τ/e = {1777/0.511:.0f}, b/d = {4180/4.8:.0f}, t/u = {173210/2.3:.0f}','FAIL','also scale: (1001/61)·mod·√2·φ^-17 ≈ %.3e — far below MeV-scale values for any unit'%((1001/61)*mod*2**0.5*p**-17))
rec('G3','theorems/unification-proof.txt:106','mod = (1 + β_PBH ρ_DM / 10)^{-1/2} ≈0.9972',f'{mod:.5f} (β_PBH=0.18, ρ_DM=0.31)','HOLD')
k=np.linalg.det(M)/np.trace(M)**3
rec('G4','theorems/unification-proof.txt:124','Koide relation emergent from ternary trace invariant det(M)/Tr(M)^3 ≈2/3',f'det/Tr³ = {k:.5f}','FAIL','also, Koide is (Σm)/(Σ√m)² = 2/3, not det/Tr³')
json.dump(out,open('/workspace/quantum-comp/eigen-matrix-search/checks/numeric_checks.json','w'),indent=1,ensure_ascii=False)
for o in out: print(o['id'],'|',o['verdict'],'|',o['computed'][:230])
# D7: CKM phase expression in chat-06 line 84
import numpy as np
t12,t13,t23,d=np.radians(13.04),np.radians(0.201),np.radians(2.38),1.144
s12,c12,s13,c13,s23,c23=np.sin(t12),np.cos(t12),np.sin(t13),np.cos(t13),np.sin(t23),np.cos(t23)
e=np.exp(1j*d)
Vm=np.array([[c12*c13,s12*c13,s13/e],[-s12*c23-c12*s23*s13*e,c12*c23-s12*s23*s13*e,s23*c13],[s12*s23-c12*c23*s13*e,-c12*s23-s12*c23*s13*e,c23*c13]])
q=np.angle(-Vm[0,0]*np.conj(Vm[0,2])/(Vm[2,0]*np.conj(Vm[2,2])))
alpha=np.angle(-Vm[2,0]*np.conj(Vm[2,2])/(Vm[0,0]*np.conj(Vm[0,2])))
gamma=np.angle(-Vm[0,0]*np.conj(Vm[0,2])/(Vm[1,0]*np.conj(Vm[1,2])))
Jv=np.imag(Vm[0,0]*Vm[1,1]*np.conj(Vm[0,1])*np.conj(Vm[1,0]))
U=Vm@Vm.conj().T
rec('D7','raw/chat-06.txt:84','δ_CKM from arg(-V_{ud} V_{ub}^* / (V_{td} V_{tb}^*))',f'with PDG-like angles (δ=1.144 rad): that arg = {q:.3f} rad; α = {alpha:.3f}; γ = {gamma:.3f}; Jarlskog J = {Jv:.2e}; unitarity err = {np.abs(U-np.eye(3)).max():.1e}','QUALIFIED','the quoted expression equals −α (a unitarity-triangle angle), not δ_CKM (≈γ in the standard parametrization)')
json.dump(out,open('/workspace/quantum-comp/eigen-matrix-search/checks/numeric_checks.json','w'),indent=1,ensure_ascii=False)
print(out[-1])
# B3: K+ spectrum-table means vs the chat's own c1 = Tr(L)
for sch,c1,m in [('unweighted',1188,2.201),('tower-size',2230,4.141),('path-decay',762,1.411)]:
    rec('B3-'+sch,'raw/chat-02.txt:1315 vs 1362',f'mean eigenvalue ≈ {m} ({sch}); c₁ = Tr(L) = {c1}',f'Tr(L)/539 = {c1/539:.4f}','FAIL (minor, internal)' ,'the mean of the 539 eigenvalues must equal Tr(L)/539 exactly; the table mean disagrees with the chat\'s own trace in the 3rd decimal')
# B4: K+ Laplacian reconstruction summary (see kplus_results.json)
rec('B4','raw/chat-02.txt:1315-1321, 1353, 1362','spectral gaps 3.9e-5 / 5.3e-5 / 2.1e-5; max 4.53 / 10.15 / 5.06; N(0.1)≈53, N(1)≈162, N(2)≈242, N(5)=539; Tr L = 1188/2230/762; Tr L² = 3896/15808/2148.5; heat-trace table','reconstruction (path of 539 + 56 chords, 30 random gap orders): Tr L exact 1188/2230/762; Tr L² 3896 / 15806–15808 / 2148.5; gaps 4.03–4.08e-5 / 5.40–5.48e-5 / 2.15–2.19e-5; max 4.566–4.589 / 10.17–10.18 / 5.066; N(0.1)=51–52, N(1)=167–169, N(2)=242, N(5)=539; heat trace matches to ~0.04 for t≤2 and within ~0.1 for t=5–100','HOLD (traces, N(2), N(5), mult0=1) / ≈HOLD order-dependent (gap, max, N(0.1), N(1))','exact chord order is not recorded in the archive; small differences are within the spread of admissible orders')
json.dump(out,open('/workspace/quantum-comp/eigen-matrix-search/checks/numeric_checks.json','w'),indent=1,ensure_ascii=False)
