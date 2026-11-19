"""Exact rational covering for a 21-point causal DOS relaxation.
Finite certificates complement, not replace, the analytic RIGOR.md proof.
"""
from argparse import ArgumentParser
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json

p = ArgumentParser(description=__doc__)
p.add_argument('--mutant', choices=('head-square', 'head-denominator', 'moment-sign', 'complement-factor', 'tail-budget', 'far-loss', 'coverage-gap', 'strict-budget', 'edge-factor'))
bad = p.parse_args().mutant

def require(ok, name):
    if not ok:
        raise SystemExit('REJECT: ' + name)
root = Path(__file__).resolve().parent
for name, expected in json.loads((root/'closure.json').read_text())['source_sha256'].items():
    require(sha256((root.parent/name).read_bytes()).hexdigest() == expected, 'inherited proof bytes '+name)

alpha = Q(343, 500)
goal = Q(247, 1000)
reported = Q(123, 500)
limit = goal / (1 - goal)
points = 20

# Universal polynomial identity after clearing the positive denominator.
for c in (Q(-3), Q(0), Q(2, 5)):
    for g in (Q(1, 7), Q(2)):
        for x, y in ((Q(1), Q(3)), (Q(-2), Q(1, 4))):
            lhs = g * (g*y*y - (1 if bad == 'head-square' else 2)*c*x*y) + c*c*(x*x+y*y)
            require(lhs == (g*y-c*x)**2+c*c*y*y, 'sharper head square completion')

# The rational expression is the Young/Schur head lower bound.
for r in (Q(1, 3), Q(7, 10), Q(1), Q(3)):
    for t in (Q(1, 100), Q(1, 5), limit):
        R = r + 1/r
        a = 2/R
        u = 1/(1+t)
        beta = 1/(2*t*(1+t))
        direct = 1-u*a-u*u*(1-a*a)/(beta*R+2*u*a)
        rational = 1-a*(1+t+t*a*a)/((1+t)*(1+(1 if bad == 'head-denominator' else 2)*t*a*a))
        require(direct == rational, 'sharper head rationalization')

for m in range(1, points+1):
    w = 2*m+1
    for r in (Q(1, 3), Q(7, 10), Q(3)):
        for t in (Q(0), Q(1, 10), limit):
            pp = Q(w)/((t+m*m)*(t+(m+1)**2))
            ss = 1/(t+m*m)+1/(t+(m+1)**2)
            direct = r*pp/2 - ss*ss/(4*w*(alpha+pp/(2*r*w)))
            stated = pp*(r*alpha/2+Q(1, w*w) if bad == 'moment-sign' else r*alpha/2-Q(1, w*w))/(alpha+pp/(2*r*w))
            require(direct == stated, 'all retained head-tail completion identities')

q = Q(1, 2) if bad == 'tail-budget' else Q(33, 500)
tail = sum((Q(1, (2*m+1)*(m+2)**2) for m in range(1, 17)), Q(0))+Q(1, 4*16**2)
require(tail < q and 1-q-alpha > goal, 'infinite tail and allocated reserve')
loss = Q(59, 96)/(alpha if bad == 'far-loss' else 4*alpha)
require(Q(9, 17)-loss > goal and Q(2, 5)-Q(1, 32) > goal, 'unbalanced allocation reserves')
require(alpha > Q(2, 3) and limit < Q(1, 2), 'positive completion and monotonicity domain')
require(goal > (goal if bad == 'strict-budget' else reported), 'strict reported onset reserve')
require((1 if bad == 'edge-factor' else 2)*(1-reported) == Q(377, 250), 'ordered edges and temperature units')


def lower(l, h, lo, hi):
    R = Q(2) if l <= 1 <= h else min(l+1/l, h+1/h)
    a = 2/R
    e = 1-a*(1+lo+lo*a*a)/((1+lo)*(1+2*lo*a*a))
    s_w = Q(0)
    s_m = Q(0)
    value = Q(1)
    for m in range(1, points+1):
        w = 2*m+1
        b = Q(2*m, w)
        value = min(value, 1-b+e*b+b*s_w-s_m)
        pp = Q(w)/((hi+m*m)*(hi+(m+1)**2))
        d = pp*(l*alpha/2-Q(1, w*w))/(alpha+pp/(2*l*w))
        require(d >= 0, 'outward retained completion positive')
        s_w += w*d
        s_m += (2*m if bad != 'complement-factor' else 2*m+1)*d
    return min(value, e+s_w-s_m)

start = Q(1, 2) if bad == 'coverage-gap' else Q(1, 3)
boxes = [(start, Q(1), Q(0), limit, 0), (Q(1), Q(3), Q(0), limit, 0)]
volume = Q(0)
leaves = nodes = depthmax = 0
smallest = Q(1)
while boxes:
    l, h, lo, hi, depth = boxes.pop()
    nodes += 1
    bound = lower(l, h, lo, hi)
    if bound >= goal:
        volume += (h-l)*(hi-lo)
        leaves += 1
        depthmax = max(depthmax, depth)
        smallest = min(smallest, bound)
        continue
    require(depth < 28, 'exhaustive residual multipoint covering closes')
    if (h-l)/Q(8, 3) >= (hi-lo)/limit:
        mid = (l+h)/2
        boxes.extend(((l, mid, lo, hi, depth+1), (mid, h, lo, hi, depth+1)))
    else:
        mid = (lo+hi)/2
        boxes.extend(((l, h, lo, mid, depth+1), (l, h, mid, hi, depth+1)))
require(volume == Q(8, 3)*limit, 'complete residual domain without gaps')
print('CERTIFIED 21-point covering:', leaves, 'leaves;', nodes, 'nodes; depth', depthmax)
print('Exact smallest leaf bound:', smallest)
print('Analytic import: allocated reserve >=247/1000; strict squared ceiling numerator=377/250')
