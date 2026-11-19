"""NUMERICAL centered branch search at T=C_inf with moment norm rho=1.
Finite Pick matrices are necessary tests, never a causal continuation proof.
No sampled instability is advertised without convergence or admissibility proof.
"""
import json, math
from pathlib import Path
import numpy as np
from scipy.linalg import eigvalsh, solve

CINF = 0.18272624777232952
SCALE = (2*math.pi*CINF)**2


def evaluate(t, P, bands, count, pair_count):
    n = np.arange(count)
    w = 2*n+1.0
    difference = t/(t+(n[:,None]-n[None,:])**2)
    reflection = t/(t+(n[:,None]+n[None,:]+1)**2)
    transfer = P/(SCALE*t)
    normal = np.kron(transfer, difference-reflection)
    W = np.tile(w, len(P))
    row = transfer.sum(axis=1)
    flat_row = 1+2*np.cumsum(t/(t+np.arange(count)**2))-2
    initial = np.concatenate([w+r*flat_row for r in row])

    def poisson(s):
        b = np.empty_like(s)
        db = np.empty_like(s)
        for x, band in enumerate(bands):
            v = s[x*count:(x+1)*count]
            if band is None:
                b[x*count:(x+1)*count]=1
                db[x*count:(x+1)*count]=0
            else:
                lo, hi = band
                b[x*count:(x+1)*count]=2/math.pi*(np.arctan(hi/v)-np.arctan(lo/v))
                db[x*count:(x+1)*count]=2/math.pi*(-hi/(v*v+hi*hi)+lo/(v*v+lo*lo))
        return b, db

    log_s = np.log(initial)
    residual = math.inf
    for iteration in range(60):
        s = np.exp(log_s)
        b, db = poisson(s)
        target = W+normal@b
        f = log_s-np.log(target)
        residual = float(np.max(np.abs(f)))
        if residual < 2e-11:
            break
        J = np.eye(len(s))-normal*(db*s)[None,:]/target[:,None]
        step = solve(J, f, assume_a='gen', check_finite=True)
        damping = 1.0
        accepted = False
        for attempt in range(20):
            candidate = log_s-damping*step
            if np.max(np.abs(candidate)) > 600:
                damping *= .5
                continue
            cb, _ = poisson(np.exp(candidate))
            cf = candidate-np.log(W+normal@cb)
            if np.max(np.abs(cf)) < residual:
                log_s=candidate
                accepted=True
                break
            damping *= .5
        if not accepted:
            raise RuntimeError('Newton line search unresolved; residual '+str(residual))
    else:
        raise RuntimeError('normal branch unresolved; residual '+str(residual))
    s = np.exp(log_s)
    b, _ = poisson(s)
    chosen = np.concatenate([np.arange(x*count,x*count+pair_count) for x in range(len(P))])
    kp = np.kron(transfer, (difference+reflection)[:pair_count,:pair_count])
    R = np.sqrt(b[chosen]/s[chosen])
    gain = R[:,None]*kp*R[None,:]
    top = float(eigvalsh(gain, subset_by_index=[len(gain)-1,len(gain)-1])[0])
    pick=[]
    for x in range(len(P)):
        z=s[x*count:x*count+6]
        source=w[:6]
        pick.append(float(eigvalsh((z[:,None]+z[None,:])/(source[:,None]+source[None,:]))[0]))
    return {'gain':top,'normal_log_residual':residual,'normal_iterations':iteration,
            'six_point_pick_minimum':pick,'width_first_three':s.reshape(len(P),count)[:,:3].tolist(),
            'poisson_first_three':b.reshape(len(P),count)[:,:3].tolist(),
            'normal_count':count,'pair_count':pair_count}

rng=np.random.default_rng(260119)
params=[]
# The near-tight upper relaxation has flat first weights, soft t, and imbalance.
for t in (1e-4,1e-3,.01,.1,1.0):
    for ratio in (.35,.7,1.0,2.0):
        v=np.array([1.0,ratio]);P=np.outer(v,v)/(v@v)
        for shape in ('flat','one-box','unequal-box','shell'):
            lam=1/(SCALE*t)
            bands={'flat':[None,None],'one-box':[None,(0,.5*lam)],
                   'unequal-box':[(0,.1*lam),(0,2*lam)],
                   'shell':[(.2*lam,2*lam),(0,lam)]}[shape]
            params.append((t,P,bands,shape))
for i in range(80):
    t=10**rng.uniform(-4,1)
    raw=rng.uniform(0,1,(2,2));raw=(raw+raw.T)/2
    P=raw/eigvalsh(raw)[-1]
    lam=1/(SCALE*t)
    bands=[]
    for x in range(2):
        hi=lam*10**rng.uniform(-2,2)
        lo=0.0 if rng.uniform()<.6 else hi*rng.uniform(.05,.9)
        bands.append((float(lo),float(hi)))
    params.append((float(t),P,bands,'random'))
rows=[]
for i,(t,P,bands,shape) in enumerate(params):
    row={'id':i,'t':t,'moment':P.tolist(),'bands':bands,'shape':shape}
    try:
        row.update(evaluate(t,P,bands,64,32))
        row['status']='solved finite normal equations'
    except (RuntimeError,ValueError,np.linalg.LinAlgError) as exc:
        row['status']='unresolved';row['reason']=str(exc)
    rows.append(row)
solved=[r for r in rows if 'gain' in r]
selected=sorted(solved,key=lambda r:r['gain'],reverse=True)[:8]
refinements=[]
for row in selected:
    t,P,bands,_=params[row['id']]
    sequence=[row]
    for count,pair_count in ((96,48),(160,80)):
        trial={'id':row['id']}
        try:
            trial.update(evaluate(t,P,bands,count,pair_count))
            trial['status']='solved finite normal equations'
        except (RuntimeError,ValueError,np.linalg.LinAlgError) as exc:
            trial['status']='unresolved';trial['reason']=str(exc)
        sequence.append(trial)
    refinements.append(sequence)
report={'label':'NUMERICAL','temperature':CINF,'rho':1,'seed':260119,'rows':rows,
        'refinements':refinements,'admissibility_boundary':'Finite Pick positivity is necessary only. No full causal continuation or infinite-frequency root is certified.',
        'cutoff_error_boundary':'Differences between cutoffs are empirical convergence indicators, not rigorous error bounds.'}
Path('SEARCH.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n',encoding='utf-8')
print('NUMERICAL attempted',len(rows),'solved',len(solved),'unresolved',len(rows)-len(solved))
print('NUMERICAL greatest coarse gain',max(r['gain'] for r in solved))
for seq in refinements:
    print('NUMERICAL refinement id',seq[0]['id'],[(s.get('normal_count'),s.get('pair_count'),s.get('gain'),s.get('six_point_pick_minimum')) for s in seq])
print('No finite Pick test is claimed to certify causality or a counterexample.')
