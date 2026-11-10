# POST-HOC diagnostic (not a verdict): does the order54 mismatch shrink as t->0 (asymptotic regime)?
exec(open('rg45c.py').read().split('TS=[')[0])
import json
d=json.load(open('../data/rg45c.json'))['rows']
for w in (1,2):
  r=max([r for r in d if r['w']==w],key=lambda r:r['relerr'])
  x=Fr(r['x']); al,be=pairs[r['j']]
  P=period(al,be,x,WALL[w]['u']); Nt=period(al,be,x,(1,0))
  p,_=pred(al,be,x,w)
  print('wall',w,'x',x,'j',r['j'],'lineP',P,'Nt',Nt,'pred',p)
  for t in ([1e-3,1e-4,1e-5] if w==1 else [1e-3,1e-4,2e-5]):
    v=math.sqrt(t)*direct(al,be,x,w,t); print('  t',t,'sqrt(t)R',v,'|diff|',abs(v-p),flush=True)
