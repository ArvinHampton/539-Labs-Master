// g7mod.c: compute g_7(d) for 0<=d<=D modulo K primes and in long double.
// g_7(q)=sum_n q^{n^2}/(-q^7;q^7)_n ; P_n(x)=prod_{j<=n}1/(1+x^j) built incrementally:
// P_n[m] = P_{n-1}[m] - P_n[m-n]  (in-place, increasing m).
// usage: g7mod D K out_prefix -> out_prefix.zero (d with g==0 mod all K primes), out_prefix.bin (double pairs: g_7(d) float, sum_n |term|)
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
static const uint64_t PR[16]={4611686018427387847ULL,4611686018427387817ULL,4611686018427387787ULL,4611686018427387761ULL,4611686018427387751ULL,4611686018427387737ULL,4611686018427387733ULL,4611686018427387709ULL,4611686018427387701ULL,4611686018427387631ULL,4611686018427387617ULL,4611686018427387587ULL,4611686018427387461ULL,4611686018427387421ULL,4611686018427387409ULL,4611686018427387329ULL};
int main(int argc,char**argv){
  long D=atol(argv[1]); int K=atoi(argv[2]); const char*pre=argv[3];
  long M=D/7+1; long nmax=(long)floor(sqrtl((long double)D)); while((nmax+1)*(nmax+1)<=D) nmax++;
  uint64_t *P=malloc(sizeof(uint64_t)*(M+1)), *G=calloc((size_t)(D+1)*K,sizeof(uint64_t));
  long double *PL=malloc(sizeof(long double)*(M+1)), *GL=calloc(D+1,sizeof(long double)), *GA=calloc(D+1,sizeof(long double));
  for(int k=0;k<=K;k++){
    if(k<K){ uint64_t p=PR[k]; for(long m=0;m<=M;m++)P[m]=0; P[0]=1;
      for(long n=0;n<=nmax;n++){
        if(n>=1) for(long m=n;m<=M;m++){ uint64_t a=P[m],b=P[m-n]; P[m]= a>=b? a-b : a+p-b; }
        for(long m=0; n*n+7*m<=D; m++){ long d=n*n+7*m; uint64_t s=G[d*K+k]+P[m]; if(s>=p)s-=p; G[d*K+k]=s; }
      }
    } else { for(long m=0;m<=M;m++)PL[m]=0; PL[0]=1;
      for(long n=0;n<=nmax;n++){
        if(n>=1) for(long m=n;m<=M;m++) PL[m]-=PL[m-n];
        for(long m=0; n*n+7*m<=D; m++){ long d=n*n+7*m; GL[d]+=PL[m]; GA[d]+=fabsl(PL[m]); }
      }
    }
  }
  char fn[512]; sprintf(fn,"%s.zero",pre); FILE*f=fopen(fn,"w");
  // d whose residue is 0 mod ALL K primes (candidate exact zeros); everything else is certified nonzero
  for(long d=0;d<=D;d++){ int allz=1; for(int k=0;k<K;k++) if(G[d*K+k]) {allz=0;break;} if(allz) fprintf(f,"%ld\n",d);} fclose(f);
  sprintf(fn,"%s.bin",pre); f=fopen(fn,"wb");
  for(long d=0;d<=D;d++){ double a=(double)GL[d], b=(double)GA[d]; fwrite(&a,8,1,f); fwrite(&b,8,1,f);} fclose(f);
  return 0;
}
