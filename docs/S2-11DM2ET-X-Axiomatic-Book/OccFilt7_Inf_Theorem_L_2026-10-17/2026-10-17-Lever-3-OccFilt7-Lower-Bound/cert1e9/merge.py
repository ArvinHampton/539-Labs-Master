# merge per-pass zero lists and check allowed counts: python3 merge.py D prefixA prefixB out
import sys,re
D=int(sys.argv[1]); out=sys.argv[4]; Z=[]; cnt=0
for pre in sys.argv[2:4]:
    Z+= [int(x) for x in open(pre+'.zeros')]
    lg=open(pre+'.log').read()
    nz=sum(int(x) for x in re.findall(r'newly_nonzero=(\d+)',lg))
    cnt+=nz
Z.sort(); allowed=sum((D-r)//7+1 for r in (0,1,2,4))
open(out,'w').write(''.join(f'{z}\n' for z in Z))
print('D',D,'zeros',len(Z),'max',max(Z),'nonzero',cnt,'nonzero+zeros',cnt+len(Z),'allowed',allowed,'OK' if cnt+len(Z)==allowed else 'COUNT MISMATCH')
print(' '.join(map(str,Z)))
