import json,sys; sys.path.insert(0,'scripts'); from common import *
out={m:stats(joint(b'l3explore',300,mod2=m),m) for m in (8,64)}
print(json.dumps(out,indent=0,default=str))
