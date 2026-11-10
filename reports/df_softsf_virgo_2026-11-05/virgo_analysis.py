# Soft SF VIRGO period test. Averaged Hann-windowed periodogram over clean segments + per-segment LSQ sinusoid fits.
import numpy as np, json
from astropy.io import fits
from scipy.stats import chi2
D='/workspace/quantum-comp/datasets/soho-virgo/'
L=16384; dt=60.0   # 16384 min ~11.4 d segments
TARGETS={'P539_hypCatB':539.0,'P539.9_CatB':539.9,'P540_freeze':540.0,'C500':500.0,'C600':600.0,'C700':700.0}
rng=np.random.default_rng(53991)
out={}
def load(name,col):
    a=fits.open(D+name,memmap=True)[0].data
    return np.array(a[:,0]),np.array(a[:,col])
for label,(fn,col) in {'TSI_new':('VIRGO_TSI_Minute.fits',2),'SPM_GREEN':('VIRGO-SPM-GREEN-L2-MISSIONLONG.fits',1),'SPM_RED':('VIRGO-SPM-RED-L2-MISSIONLONG.fits',1),'SPM_BLUE':('VIRGO-SPM-BLUE-L2-MISSIONLONG.fits',1)}.items():
    t,y=load(fn,col)
    n=len(y); nseg=n//L; good=0; P=np.zeros(L//2+1); fitA={k:[] for k in TARGETS}
    dtt=np.diff(t); cad=float(np.median(dtt))
    w=np.hanning(L); tt=np.arange(L)*dt
    for i in range(nseg):
        s=y[i*L:(i+1)*L]; m=np.isfinite(s)
        if m.mean()<0.95: continue
        x=np.arange(L); s=np.interp(x,x[m],s[m])
        s=s-np.polyval(np.polyfit(x,s,2),x)
        # 6-h running-mean highpass to suppress solar-cycle/rotation leakage
        k=360; s=s-np.convolve(s,np.ones(k)/k,'same')
        P+=np.abs(np.fft.rfft(s*w))**2; good+=1
        for kk,p in TARGETS.items():
            X=np.c_[np.sin(2*np.pi*tt/p),np.cos(2*np.pi*tt/p),np.ones(L)]
            c,*_=np.linalg.lstsq(X[m],s[m],rcond=None); fitA[kk].append(np.hypot(c[0],c[1]))
    P/=good; f=np.fft.rfftfreq(L,dt)
    res={'n_rows':n,'cadence_s':cad,'nan_frac':float(np.isnan(y).mean()),'segments_used':good,'segments_total':nseg,'df_uHz':f[1]*1e6,'dof':2*good}
    def snr_at(f0):
        j=int(np.argmin(abs(f-f0)))
        band=(abs(f-f0)<60e-6)&(abs(f-f0)>5e-6)
        bg=np.median(P[band])/np.log(2)  # median->mean for chi2_2-like
        loc=j-1+int(np.argmax(P[j-1:j+2]))
        r=P[loc]/bg
        pv=chi2.sf(r*2*good,2*good)
        return dict(nearest_bin_uHz=f[j]*1e6,peak_bin_uHz=f[loc]*1e6,peak_period_s=1/f[loc],power_over_bg=float(r),p_single=float(pv))
    for kk,p in TARGETS.items():
        d=snr_at(1/p); a=np.array(fitA[kk]); d.update(target_period_s=p,lsq_amp_mean=float(a.mean()),lsq_amp_sd=float(a.std()),n_fit=len(a)); res[kk]=d
    # null: random periods 450-750s
    nr=[snr_at(1/rng.uniform(450,750))['power_over_bg'] for _ in range(500)]
    res['null_random_periods_power_over_bg']=dict(mean=float(np.mean(nr)),sd=float(np.std(nr)),p95=float(np.percentile(nr,95)),p99=float(np.percentile(nr,99)))
    # scrambled-time null on one segment set: max ratio across target bins under shuffle of spectrum is equivalent; use phase-scramble count
    np.savez(f'spectrum_{label}.npz',f=f,P=P)
    out[label]=res; print(label,json.dumps(res,indent=1))
json.dump(out,open('virgo_results.json','w'),indent=1)
