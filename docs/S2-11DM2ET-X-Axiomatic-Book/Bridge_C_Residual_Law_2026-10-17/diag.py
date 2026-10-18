exec(open('identities.py').read().split('checks = {')[0].replace("int(sys.argv[1]) if len(sys.argv) > 1 else 3000","600"))
rhs = lin((Fr(3,2),one),(1,sq1),(1,tri1),(1,Ct))
bad = [(i,C[i],rhs[i]) for i in range(N+1) if C[i]!=rhs[i]]
print("first mismatches (deg, C, C_axis+C_third):", bad[:10])
d0 = bad[0][0]
# which lattice points contribute to C at d0
for n in range(-60,61):
    for k in range(-60,61):
        if Qs(n,k)==d0:
            w = Fr(sgn(5*n)-sgn(-n-21*k),2); orth = (n>=0 and k>=0)
            print((n,k), "w=",w, "orthant" if orth else "", "contrib to C:", (1 if orth else 0)-w)
