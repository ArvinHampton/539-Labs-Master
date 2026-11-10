# POST-HOC (not a verdict): order55 RG45c-2' wall-2 misses (j=50/85). Convergence in t and period check.
exec(open('rg45c2p.py').read().split("if __name__")[0])
for x,j in [(Fr(1,11),50)]:
    al,be=pairs[j]; P=period(al,be,x,(21,-1)); Nt=period(al,be,x,(1,0))
    # independent check: is the u2-line phase truly P-periodic for every base r<Nt?
    ok=all((phase_ints(al,be,x,np.array([[r,0]])+np.arange(4*P)[:,None]*np.array([21,-1]))[0].reshape(4,P)==phase_ints(al,be,x,np.array([[r,0]])+np.arange(P)[:,None]*np.array([21,-1]))[0]).all() for r in range(Nt))
    p,_=pred(al,be,x,2); T=math.pi**2/(40*297.5*max(P,Nt)**2)
    print('x',x,'j',j,'P',P,'Nt',Nt,'periodic_ok',ok,'al',al,'pred',p,flush=True)
    for c in (1,0.25,1/16):
        v=math.sqrt(c*T)*directc(al,be,x,2,c*T); print(' c',c,'sqrt(t)R',v,'|diff|',abs(v-p),flush=True)
