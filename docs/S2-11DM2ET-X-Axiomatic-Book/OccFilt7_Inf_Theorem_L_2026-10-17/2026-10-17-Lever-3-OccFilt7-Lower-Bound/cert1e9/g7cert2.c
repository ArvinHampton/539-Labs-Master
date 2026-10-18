// g7cert2.c -- memory-split variant of ../cert1e8/g7cert.c (class mask). Rigorous (Cat A) nonvanishing certificate for g_7(d), 0<=d<=D.
// g_7(q)=sum_{n>=0} q^{n^2}/(-q^7;q^7)_n ;  g_7(d)=sum_{n: n^2<=d, 7|d-n^2} phi_n((d-n^2)/7),
// phi_n = coefficients of P_n(x)=prod_{j<=n} 1/(1+x^j), built in place: P_n[m] = P_{n-1}[m] - P_n[m-n] (m ascending).
// Same recurrence/sign convention as ../g7mod.c. Arithmetic is exact mod a prime p<2^62 (PR[] = ../g7mod.c PR[]).
// If g_7(d) mod p != 0 then g_7(d) != 0. Primes are run one at a time; a bitset records "nonzero seen";
// a further prime is run only if some allowed d > 247 (d mod 7 in {0,1,2,4}) is still unresolved.
// Storage: G is class-major, only for classes r in {0,1,2,4}: d = r + 7t -> G[c][t]; P truncated at (D-n^2)/7.
// Parallel: wavefront over n (thread j handles n0+j, block index lag 2j, blocks of B>=nmax+1 entries of m).
// Variant: only the classes selected by CMASK (bit c <-> r=(0,1,2,4)[c]) are stored, so memory is
//   8(D/7+1)(1+popcount(CMASK)) bytes; P is still built for every n, G is only accumulated for selected classes.
// usage: g7cert2 D out_prefix threads maxprimes dumpD CMASK
//   writes out_prefix.zeros (allowed d with g==0 mod every prime run), out_prefix.log;
//   if dumpD>0, out_prefix.dump with "d g mod p0" for d<=dumpD (first prime) for validation.
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>
#include <omp.h>
#include <sys/resource.h>
static const uint64_t PR[16]={4611686018427387847ULL,4611686018427387817ULL,4611686018427387787ULL,4611686018427387761ULL,4611686018427387751ULL,4611686018427387737ULL,4611686018427387733ULL,4611686018427387709ULL,4611686018427387701ULL,4611686018427387631ULL,4611686018427387617ULL,4611686018427387587ULL,4611686018427387461ULL,4611686018427387421ULL,4611686018427387409ULL,4611686018427387329ULL};
static const int CLS[7]={0,1,2,-1,3,-1,-1}; // class index for r=d mod 7
int main(int argc,char**argv){
  if(argc<7){fprintf(stderr,"usage: %s D prefix threads maxprimes dumpD CMASK\n",argv[0]);return 1;}
  long D=atol(argv[1]); const char*pre=argv[2];
  int T=argc>3?atoi(argv[3]):1; int KMAX=argc>4?atoi(argv[4]):16; long dumpD=atol(argv[5]); int CM=atoi(argv[6])&15;
  static const int RV[4]={0,1,2,4}; int SL[4]={-1,-1,-1,-1}, NC=0; for(int c=0;c<4;c++) if(CM>>c&1) SL[c]=NC++;
  if(NC==0){fprintf(stderr,"empty mask\n");return 1;}
  if(T<1)T=1; if(T>8)T=8; if(KMAX>16)KMAX=16;
  long nmax=(long)floor(sqrt((double)D)); while(nmax*nmax>D)nmax--; while((nmax+1)*(nmax+1)<=D)nmax++;
  long M=D/7;                         // P index range 0..M
  long L=D/7+1;                       // class array length (t=0..D/7)
  long B=65536; while(B<nmax+1)B*=2;  // block size; must satisfy B>=nmax+1 (dependency distance n and G-disjointness)
  uint64_t *P=malloc(sizeof(uint64_t)*(M+1));
  uint64_t *G=malloc(sizeof(uint64_t)*NC*L);
  uint64_t *NZ=calloc((NC*L+63)/64,8);  // nonzero-seen bitset over (class,t)
  if(!P||!G||!NZ){fprintf(stderr,"alloc failed\n");return 2;}
  char fn[512]; snprintf(fn,sizeof fn,"%s.log",pre); FILE*lg=fopen(fn,"w");
  fprintf(lg,"D=%ld nmax=%ld threads=%d B=%ld cmask=%d classes=",D,nmax,T,B,CM); for(int c=0;c<4;c++) if(SL[c]>=0) fprintf(lg,"%d ",RV[c]); fprintf(lg,"\n");
  double t0=omp_get_wtime(); int k; long unres=0;
  for(k=0;k<KMAX;k++){
    const uint64_t p=PR[k]; double tk=omp_get_wtime();
    memset(P,0,sizeof(uint64_t)*(M+1)); P[0]=1; memset(G,0,sizeof(uint64_t)*NC*L);
    #pragma omp parallel num_threads(T)
    {
      int j=omp_get_thread_num(), TT=omp_get_num_threads();
      for(long n0=0;n0<=nmax;n0+=TT){
        long n=n0+j; int act=(n<=nmax);
        long Mn= act? (D-n*n)/7 : -1;            // last m needed for this n
        long nb= act? Mn/B+1 : 0;
        long nb0=M/B+1;                           // upper bound on blocks for the group
        int sl= act? SL[CLS[(n*n)%7]] : -1;
        uint64_t *Gc= sl>=0? G+(long)sl*L : NULL;
        long off= act? (n*n)/7 : 0;               // d=n^2+7m = r+7(off+m)
        for(long s=0;s<nb0+2*(TT-1);s++){
          long b=s-2*j;
          if(act && b>=0 && b<nb){
            long lo=b*B, hi=lo+B-1; if(hi>Mn)hi=Mn;
            long m=lo;
            if(!Gc){ if(n>=1){ if(m<n)m=n; for(;m<=hi;m++){ uint64_t a=P[m],c=P[m-n]; P[m]= a>=c? a-c : a+p-c; } } }
            else { uint64_t *g=Gc+off;
            if(n>=1){ if(m<n){ for(;m<n && m<=hi;m++){ uint64_t v=g[m]+P[m]; if(v>=p)v-=p; g[m]=v; } }
              for(;m<=hi;m++){ uint64_t a=P[m],c=P[m-n]; uint64_t v= a>=c? a-c : a+p-c; P[m]=v;
                uint64_t w=g[m]+v; if(w>=p)w-=p; g[m]=w; } }
            else { for(;m<=hi;m++){ uint64_t v=g[m]+P[m]; if(v>=p)v-=p; g[m]=v; } } }
          }
          #pragma omp barrier
        }
      }
    }
    long newnz=0; unres=0; long maxun=-1;
    int SR[4]; for(int c=0;c<4;c++) if(SL[c]>=0) SR[SL[c]]=RV[c];
    for(long i=0;i<NC*L;i++){ int r=SR[i/L]; long d=r+7*(i%L); if(d>D) continue;
      if(!(NZ[i>>6]>>(i&63)&1)){ if(G[i]){ NZ[i>>6]|=1ULL<<(i&63); newnz++; } else { if(d>247){unres++; if(d>maxun)maxun=d;} } } }
    if(k==0 && dumpD>0){ snprintf(fn,sizeof fn,"%s.dump",pre); FILE*f=fopen(fn,"w");
      for(long d=0;d<=dumpD&&d<=D;d++){ int c=CLS[d%7]; if(c<0||SL[c]<0) continue; fprintf(f,"%ld %llu\n",d,(unsigned long long)G[(long)SL[c]*L+d/7]); } fclose(f); }
    fprintf(lg,"prime %d p=%llu time=%.2fs newly_nonzero=%ld unresolved_allowed_gt247=%ld max_unresolved=%ld\n",k,(unsigned long long)p,omp_get_wtime()-tk,newnz,unres,maxun); fflush(lg);
    if(unres==0){k++;break;}
  }
  snprintf(fn,sizeof fn,"%s.zeros",pre); FILE*f=fopen(fn,"w"); long nz=0;
  for(long d=0;d<=D;d++){ int c=CLS[d%7]; if(c<0||SL[c]<0)continue; long i=(long)SL[c]*L+d/7; if(!(NZ[i>>6]>>(i&63)&1)){fprintf(f,"%ld\n",d);nz++;} } fclose(f);
  struct rusage ru; getrusage(RUSAGE_SELF,&ru);
  fprintf(lg,"primes_used=%d allowed_zero_candidates=%ld unresolved_gt247=%ld total_time=%.2fs maxrss_kB=%ld\n",k,nz,unres,omp_get_wtime()-t0,ru.ru_maxrss);
  fclose(lg); return 0;
}
