# Local-derived. t4407 O-b resource estimate: dimensions of the direct level-39200 / 78400 weight-3/2 spaces for Xi (no mfinit; dimension formula only).
import cypari2; pari=cypari2.Pari(); pari.allocatemem(10**9); P=pari
for N in [39200,78400]:
    for D in [1,5,8,40,28,140,56,280,-20,-4,-7,-35]:
        try: print(f"N={N} D={D}: dim S_3/2 = {P(f'mfdim([{N},3/2,{D}],1)')}",flush=True)
        except cypari2.PariError as e: print(f"N={N} D={D}: err {e}",flush=True)
