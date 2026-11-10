import hashlib,json
W=[0,1]*269+[0]
r={'PM1_sha':hashlib.sha256(bytes(W)).hexdigest()}
r['PM1']=r['PM1_sha']=='c2c26fdae7b1e1f677799f9a6a210c429ea9c1f4b23f48ae1bbc66aab54f8d87'
d={a+b:sum(1 for i in range(538) if (W[i],W[i+1])==(int(a),int(b))) for a in'01' for b in'01'}
per=min(p for p in range(1,540) if all(W[i]==W[i+p] for i in range(539-p)))
r['PM2']=dict(len=len(W),ones=sum(W),zeros=W.count(0),period=per,digrams=d,
 is_prime_269=all(269%k for k in range(2,17)),c_539=539==2*269+1==7*7*11,
 gcd_269_with={n:__import__('math').gcd(269,n) for n in (18,521,105,35,140,72,539)},
 gcd_270_with={n:__import__('math').gcd(270,n) for n in (18,521,105,35,140,72,539)})
json.dump(r,open('data/pursue.json','w'),indent=1);print(json.dumps(r))
