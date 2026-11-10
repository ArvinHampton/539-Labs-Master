# HQH-539 per HQH539_Formal_Games_and_Hard_Problem_Pi.md:24-38: H=SHA3-512(bytes(T3^539(int(SHA3-512(m||s))))||s)
import hashlib,os,collections,math
def T3(n):
  r=n%3
  return n//3 if r==0 else ((4*n+2)//3 if r==1 else (2*n+1)//3)
def body(u):
  for _ in range(539): u=T3(u)
  return u
o=[]
bl=[]
for i in range(3000):
  u=int.from_bytes(hashlib.sha3_512(os.urandom(16)).digest(),'big'); bl.append(body(u).bit_length())
o.append(f"bit length of u_539 over 3000 random inputs: min {min(bl)} max {max(bl)} mean {sum(bl)/len(bl):.1f}")
o.append(f"=> intermediate state has at most ~{max(bl)} bits; generic birthday collision on the body ~2^{max(bl)/2:.0f} vs 2^256 for SHA3-512 alone (upper bound on entropy; true image entropy is lower still)")
# toy scaled demo: 40-bit inputs, L scaled proportionally (539/512*40 ~ 42)
L=42; c=collections.Counter()
for i in range(200000):
  u=int.from_bytes(os.urandom(5),'big')
  for _ in range(L): u=T3(u)
  c[u]+=1
o.append(f"toy (40-bit inputs, L=42): 200000 samples -> {len(c)} distinct body outputs; max multiplicity {max(c.values())}")
open('scripts/verify_HQH_entropy.out','w').write("\n".join(o)); print("\n".join(o))
