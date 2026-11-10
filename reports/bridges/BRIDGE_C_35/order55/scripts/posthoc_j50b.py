# POST-HOC (not a verdict): compare observed constant with endpoint-convention variants and per-residue m_r.
exec(open('rg45c2p.py').read().split("if __name__")[0])
obs=complex(-0.015103500611264729,-0.0034472754549707664); x=Fr(1,11); al,be=pairs[50]
for b0 in (0,-0.5,0.5): print('b0',b0,pred(al,be,x,2,b0)[0])
Nt=period(al,be,x,(1,0)); P=period(al,be,x,(21,-1)); th=Fr(al[0])+21*Fr(al[1])
ms=[ph(al,be,x,np.array([r,0])[None,:]+np.arange(P)[:,None]*np.array([21,-1])).mean() for r in range(Nt)]
print('theta2',th,'|m_r|',np.round(np.abs(ms),4)); print('obs/sqrt(pi/Q)',obs/math.sqrt(math.pi/297.5))
