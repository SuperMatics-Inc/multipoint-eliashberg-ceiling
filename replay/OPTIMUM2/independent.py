"""Independent four-way subdivision and actual-weight finite forms.
No import of the primary replay; all arithmetic is rational.
"""
from argparse import ArgumentParser
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json

parser=ArgumentParser(description=__doc__)
parser.add_argument('--mutant',choices=('volume-copy','completion-coefficient','matrix-gain','missing-normal-mass','flat-admissibility'))
bad=parser.parse_args().mutant

def demand(ok,why):
    if not ok: raise SystemExit('REJECT: '+why)
root=Path(__file__).resolve().parent
for name, expected in json.loads((root/'closure.json').read_text())['source_sha256'].items():
    demand(sha256((root.parent/name).read_bytes()).hexdigest()==expected,'inherited proof bytes '+name)

A=F(343,500);G=F(247,1000);T=F(247,753)

def enclosure(l,h,x,y):
    R=F(2) if l<=1<=h else min(l+1/l,h+1/h)
    a=2/R
    if x==0:
        e=1-a
    else:
        u=1/(1+x);beta=1/(2*x*(1+x))
        e=1-u*a-u*u*(1-a*a)/(beta*R+2*u*a)
    ds=[]
    for m in range(1,21):
        w=2*m+1;p=F(w)/((y+m*m)*(y+(m+1)**2))
        ds.append(l*p*(A*l*w*w-(1 if bad=='completion-coefficient' else 2))/(w*(2*A*l*w+p)))
    costs=[]
    for j in range(1,21):
        b=F(2*j,2*j+1)
        costs.append(1-b+e*b+sum(ds[m-1]*((2*m+1)*b-2*m) for m in range(1,j)))
    costs.append(e+sum(ds))
    return min(costs)

queue=[(F(1,3),F(1),F(0),T,0),(F(1),F(3),F(0),T,0)]
area=F(0);cells=depthmax=0
while queue:
    l,h,x,y,depth=queue.pop()
    if enclosure(l,h,x,y)>=G:
        area+=(h-l)*(y-x)/(2 if bad=='volume-copy' else 1)
        cells+=1;depthmax=max(depthmax,depth)
        continue
    demand(depth<16,'independent multipoint cover closes')
    r=(l+h)/2;t=(x+y)/2
    queue.extend(((l,r,x,t,depth+1),(r,h,x,t,depth+1),(l,r,t,y,depth+1),(r,h,t,y,depth+1)))
demand(area==F(8,3)*T,'independent complete rectangle area')

# Exact equivalence of this rationalization to the original completion.
for m in range(1,21):
    w=2*m+1;r=F(7,10);t=F(1,11);p=F(w)/((t+m*m)*(t+(m+1)**2))
    c=1 if bad=='completion-coefficient' else 2
    demand(r*p*(A*r*w*w-c)/(w*(2*A*r*w+p))==p*(r*A/2-F(1,w*w))/(A+p/(2*r*w)), 'independent completion identity')

# Retain 21 normal weights even though the trial has only three frequencies.
def psd(M):
    for k in range(len(M)):
        v=M[k][k]
        if v<0:return False
        if v==0:
            if any(M[k][j]!=0 for j in range(k+1,len(M))):return False
            continue
        for i in range(k+1,len(M)):
            for j in range(i,len(M)):
                M[i][j]-=M[i][k]*M[k][j]/v
                M[j][i]=M[i][j]
    return True

count=0
for r in (F(1,4),F(1,3),F(7,10),F(1),F(3),F(4)):
    for t in (F(1,1000),F(1,10),F(1)):
        for code in range(4):
            b=[]
            for side in range(2):
                head=F((code+side+5)%9,8)
                prof=[head]
                for m in range(1,21):
                    w=2*m+1
                    low=max(head/w,w*head-(w-1),F(0))
                    high=min(w*head,F(w-1+head,w),F(1))
                    prof.append(low if code%2==0 else (low+high)/2)
                b.append(prof)
            M=[[F(0) for _ in range(6)] for _ in range(6)]
            for side in range(2):
                scale=1/r if side==0 else r
                for n in range(3):
                    i=side*3+n
                    M[i][i]=(1-F(123,500))*scale*(2*n+1)*b[side][n]
                    for m in range(21):
                        if bad=='missing-normal-mass' and m>0:continue
                        p=1/(t+(n-m)**2)-1/(t+(n+m+1)**2)
                        M[i][i]+=p*b[side][n]*b[1-side][m]/2
            for n in range(3):
                for m in range(3):
                    S=1/(t+(n-m)**2)+1/(t+(n+m+1)**2)
                    gain=S*b[0][n]*b[1][m]/(1 if bad=='matrix-gain' else 2)
                    M[n][3+m]-=gain;M[3+m][n]-=gain
            demand(psd(M),'actual-weight finite form with retained normal mass')
            count+=1

# A normalized positive-width Poisson average equal to one forces full DOS.
head=F(1);second=F(1,2) if bad=='flat-admissibility' else F(1)
demand(second>=3*head-2,'near-tight full-head Poisson admissibility')
print('CERTIFIED independent multipoint cover:',cells,'leaves; depth',depthmax)
print('CERTIFIED supplementary finite forms:',count)
print('Analytic import: full-head Poisson equality forces flat DOS almost everywhere')
