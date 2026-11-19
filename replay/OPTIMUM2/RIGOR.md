# A multipoint improvement of the causal multichannel ceiling

## Verdict and scope

**PROVED, with computer-assisted finite rational inequalities:** on the reciprocal reduced Eliashberg model and causal normal branches described below,
\[
 \tau_{\rm lin}<C_{21}\sqrt\rho,
 \qquad C_{21}=\frac{\sqrt{377/250}}{2\pi}.
\]
Here \(\tau=k_BT\) and \(\rho\) is the norm of the total, DOS-height-weighted moment operator. **NUMERICAL:** the displayed coefficient is approximately 0.19544330695411738. It is calculated, not an interval enclosure. **OPEN:** the optimal coefficient remains between the prior sharp scalar constant \(C_\infty\) and \(C_{21}\). No causal counterexample above \(C_\infty\), and no proof that it is the coupled-channel answer, is asserted.

**CERTIFIED:** a rational covering proves an edge reserve of at least 247/1000. The theorem uses the smaller reserve 123/500, so its endpoint is strictly stable. The primary and independent replays are independent implementations, not different model families or measurements.

## 1. Hypotheses and normalization

**PROVED under these hypotheses.** Use the finite reciprocal channel model and height measure \(d\eta=N_{\max}(x)d\mu(x)\) of `../SHARP-Q2/RIGOR.md`, dropping zero-height channels. The reciprocal nonnegative moment measures \(d\mathfrak m_{xy}(E)\), supported at \(E>0\), define a self-adjoint moment matrix \(\mathcal M\) with norm \(0<\rho<\infty\). At every tested temperature the normal frequency rows, including zero transfer, are bounded. No temperature-independent row bound is assumed or needed. These conditions allow the stated normal equations, quadratic forms and finite-support exhaustion. The measures need not be PSD as matrices; nonnegative reciprocal entries suffice.

Put \(w_n=2n+1\), \(t=(E/(2\pi\tau))^2\), and
\[
 K_j(x,y)=\frac1{(2\pi\tau)^2}\int\frac{d\mathfrak m_{xy}(E)}{t+j^2}.
\]
The normal widths satisfy the matched imaginary equation
\[
 s_n(x)=w_n+\int d\eta(y)\sum_{m\ge0}
 [K_{|n-m|}(x,y)-K_{n+m+1}(x,y)]b_m(y).
\]
Normal scattering in this formula and the attractive pairing envelope are the same transfer. A smaller dominated pairing kernel, including a sign-changing symmetry sector preserved by the propagator and envelope, is permitted. An additional normal Lorentzian kernel with bounded rows and odd-folded dominance only adds a nonnegative diagonal cost. Static PSD pairing subtraction is also permitted. Neither permission justifies replacing the envelope moment by a smaller signed pairing-only moment.

For a shifted actual channel branch, assume a holomorphic self-map \(F_x\) of the upper half-plane with reflected Matsubara values \(F_x(i\pi\tau w_n)=-\chi_n(x)+i\pi\tau s_n(x)\). Alternatively, the centered even-profile class uses the established normal width cone: \(s_n/w_n\) is nonincreasing and \(w_ns_n\) is nondecreasing, as proved in the byte-pinned `../CENTERED-GAP/RIGOR.md`. This does not require a separate causal-continuation assumption for that centered class. Its Poisson DOS weights have height-normalized profile \(0\le f_x(\xi)\le1\):
\[
 b_n(x)=\int f_x(\xi)\frac{\pi\tau s_n(x)}{\pi[(\pi\tau s_n(x))^2+(\xi+\chi_n(x))^2]}d\xi.
\]
These are the same centered and channel-wise causal shifted classes as the reviewed predecessor. The conditions apply to actual branches, not independently selected widths. No self-consistent real equation is discarded and then used to certify an arbitrary shift as physical. These are linear instabilities, not exact many-body transition temperatures.

## 2. Causal constraints at twenty Matsubara points

**PROVED.** For a shifted causal branch, the imaginary part of the composed normalized DOS Cauchy transform is a harmonic function \(b(z)\) on the upper half-plane with \(0\le b\le1\). Both \(b\) and \(1-b\) obey Harnack's inequality. Comparing \(i\pi\tau\) with \(i\pi\tau w_m\) gives
\[
 b_m\ge b_0/w_m,
 \qquad b_m\ge w_m b_0-(w_m-1),
 \qquad b_m\le\min(w_m b_0,1-(1-b_0)/w_m).
\]
For centered branches, telescoping the width cone gives \(w_m^{-1}\le s_m/s_0\le w_m\). The centered positive-width Poisson densities then have pointwise ratios in \([w_m^{-1},w_m]\). Integrating both the DOS and its bounded complement proves the same inequalities. The first twenty complement inequalities, not twenty independent numerical normal solves, generate the improvement below. Constants 0 and 1 are handled without logarithms or by the harmonic maximum principle.

**PROVED:** if \(b_0=1\), the positive-width Poisson kernel and \(0\le f_x\le1\) force \(f_x=1\) almost everywhere, hence every \(b_m=1\). A full-head, suppressed-tail profile is therefore not an admissible DOS branch. If every active channel has full-head weight, the prior flat-DOS sharp angular theorem applies. This kills that proposed route to a counterexample, not the general open question.

## 3. An edge quadratic form and its sharper head bound

**PROVED.** At one reciprocal channel pair and one spectral energy set
\[
 p_{nm}=\frac1{t+(n-m)^2}-\frac1{t+(n+m+1)^2},
 \quad S_{nm}=\frac1{t+(n-m)^2}+\frac1{t+(n+m+1)^2}.
\]
For real tests \(X_n,Y_m\), with the two channel weights \(b_n,c_m\), write
\[
 I=\sum_{n,m}b_nc_m[p_{nm}(X_n^2+Y_m^2)-2S_{nm}X_nY_m],
 \quad B_r=\sum_nw_n(r^{-1}b_nX_n^2+r c_nY_n^2),\quad r>0.
\]
We prove \(B_r+I/2\ge(247/1000)B_r\). This is an edge allocation statement, not an assumed angular Perron eigenfunction.

For the full head \(b_0=c_0=1\), normalizing by \(B_r\) gives
\[
 H_0=\begin{pmatrix}1+\beta r&-(\beta+u)\\-(\beta+u)&1+\beta/r\end{pmatrix},
 \quad u=(1+t)^{-1},\quad\beta=[2t(1+t)]^{-1}.
\]
Put \(R=r+r^{-1}\), \(a=2/R\). In the null/eigenvector basis of the rank-one \(\beta\) part, this matrix has diagonals \(h=1-ua\) and \(h+G\), where \(G=\beta R+2ua>0\); the off-diagonal has squared magnitude \(c^2=u^2(1-a^2)\). The identity
\[
 G(Gy^2-2cxy)+c^2(x^2+y^2)=(Gy-cx)^2+c^2y^2
\]
proves the lower bound
\[
 e_2(r,t)=h-\frac{c^2}{G}
 =1-\frac{a(1+t+t a^2)}{(1+t)(1+2t a^2)}.
\]
Its continuous value at \(t=0\) is \(1-a\). This is a lower bound, not a claim to have evaluated the exact smaller head eigenvalue.

For general head weights, the unnormalized quadratic is affine in each of \(b_0,c_0\). Regard it as the expectation of four head masks. A one-head mask has reserve 1; the two-head mask has reserve \(e_2\). Thus the X-head reserve is \(1-c_0+e_2c_0\), and the Y-head reserve is \(1-b_0+e_2b_0\). The opposite head weight is important here.

On \(0\le t\le T=247/753<1/2\), \(e_2\) increases with \(t\) and decreases with \(a\). Direct differentiation gives
\[
 \partial_t e_2=\frac{a^3[1+4t+2(1+a^2)t^2]}{(1+t)^2(1+2ta^2)^2}\ge0,
\]
\[
 \partial_a e_2=-\frac{1+t+t(1-2t)a^2+2t^2a^4}{(1+t)(1+2ta^2)^2}\le0.
\]
For all \(t\ge0\), \(e_2\ge1-a\). The older head comparison \(e_0\ge t/(1+t)\) is used outside this finite rectangle.

## 4. Head-tail completion and infinite-tail allocation

**PROVED.** Allocate \(\alpha=343/500\) of each tail's bare mass to the corresponding opposite-head interaction. Let
\[
 p_m=\frac{2m+1}{(t+m^2)(t+(m+1)^2)},\quad
 S_m=\frac1{t+m^2}+\frac1{t+(m+1)^2}.
\]
Completing the square in \(Y_m\), retaining its positive normal mass from \(X_0\), and using \(b_0\le1\), leaves the normalized X-head contribution \(c_m D_m(r,t)\), where
\[
 D_m=\frac{r p_m}{2}-\frac{S_m^2}{4w_m(\alpha+p_m/(2r w_m))}
 =\frac{p_m(r\alpha/2-w_m^{-2})}{\alpha+p_m/(2r w_m)}.
\]
The identity \(S_m^2-p_m^2=4p_m/w_m\) proves the second expression. The other head uses \(r^{-1}\). For \(1/3\le r\le3\), all \(D_m\) are positive, increase with \(r\), and increase with \(p_m\), which decreases with \(t\). The unretained \(m>20\) contributions are nonnegative there.

Within the tail-tail sector, retain the nonnegative ordinary-transfer squares and bound only the reflected transfer. Normalizing by the two tail masses cancels the reciprocal factors \(r\). With Schur weight \(w_n^{-1/2}\), the reflected tail norm is at most
\[
 q_* =\sum_{m\ge1}\frac1{(2m+1)(m+2)^2}<33/500=:q.
\]
For the replay, retain sixteen exact terms and bound the remainder by \(1/(4\cdot16^2)\), using the decreasing majorant \(1/(2m^3)\). Consequently the unallocated tail reserve is
\[
 1-q-\alpha=31/125=0.248>247/1000.
\]
These bounds hold for every \(t>0\); no infinite-frequency tail is replaced by a finite numerical cutoff.

For \(r\le1/4\), \(e_2\ge9/17\), while all negative completions together cost at most
\[
 L\le\frac1{4\alpha}\sum_{m\ge1}\frac{(m^{-2}+(m+1)^{-2})^2}{2m+1}
 \le\frac{59}{384\alpha}.
\]
The last constant follows from the first term \(25/48\) and the decreasing-majorant estimate \(\sum_{m\ge2}2m^{-5}\le3/32\). Thus \(9/17-L>247/1000\). For \(1/4\le r\le1/3\), \(e_2\ge2/5\); only \(D_1\) can be negative. Since \(p_1\le3/4\), \(r\alpha/2-1/9\ge-1/36\), and the denominator is at least \(2/3\), \(D_1\ge-1/32\). Hence \(2/5-1/32>247/1000\). Reciprocity covers \(r\ge3\) as well.

## 5. Certified compact rectangle

**PROVED with the attached rational certificate.** For \(1/3\le r\le3\) all retained completions are positive. The twenty causal complement inequalities give each head, with opposite head weight \(b\), the reserve
\[
 F_{r,t}(b)=1-b+e_2(r,t)b+
 \sum_{m=1}^{20}D_m(r,t)\max\{w_m b-(w_m-1),0\}.
\]
This convex piecewise-affine function takes its minimum on \([0,1]\) at 0, 1, or \(2m/(2m+1)\), \(1\le m\le20\).

On a rational rectangle \([l,h]\times[x,y]\), use \(a_{\max}=2/\min_{r\in[l,h]}(r+r^{-1})\), with the exact minimum 2 if the rectangle includes 1. Evaluate the head lower bound at \(a_{\max},x\) and each completion at \(l,y\). The monotonicities established above make these outward lower bounds for every point of the rectangle. Evaluate all twenty-two breakpoints exactly. The primary binary covering of \([1/3,3]\times[0,247/753]\) accepts 537 leaves, all at least 247/1000. Exact rectangle areas add to the full domain. The independent four-way covering implements the head and completion formulas differently and uses no primary import.

For \(t\ge247/753\), the older head bound \(t/(1+t)\ge247/1000\), together with positive completions and the tail reserve, closes the domain. The far imbalance bounds in section 4 close the remaining r values. This proves the asserted uniform edge inequality.

## 6. Integrating edges and strictness

**PROVED.** For finite-support tests, the eliminated stability form is
\[
 Q(v)=B(v)+\frac1{2(2\pi\tau)^2}\int d\eta(x)d\eta(y)\,d\mathfrak m_{xy}(E)\,I(v_x,v_y),
 \quad B(v)=\sum_n\int w_n b_n(x)|v_n(x)|^2d\eta(x).
\]
As in `../SHARP-Q2/RIGOR.md`, take a strictly positive resolvent vector \(a_\varepsilon\) satisfying \(\mathcal M a_\varepsilon\le(\rho+\varepsilon)a_\varepsilon\). Set \(r=a_\varepsilon(x)/a_\varepsilon(y)\). Reciprocity then gives
\[
 \frac12\int d\eta(x)d\eta(y)d\mathfrak m_{xy}(E)B_r
 \le(\rho+\varepsilon)B(v).
\]
No Perron eigenvector is assumed. Integrating the edge lower bound and taking \(\varepsilon\downarrow0\) yields
\[
 Q(v)\ge\left[1-\frac{2(1-247/1000)\rho}{(2\pi\tau)^2}\right]B(v).
\]
At the stated endpoint \((2\pi\tau)^2=2(1-123/500)\rho=(377/250)\rho\), the bare bracket is \(1/754>0\). For strictness choose the smaller temperature threshold \((2\pi\tau)^2=(1507/1000)\rho\), which lies strictly between the certified numerator \(753/500\) and the reported \(377/250\). At every temperature above this smaller threshold, the bare-form gap is at least \(1/1507\). The usual width comparison carries it to a symmetrized gap at least \(1/[1507(1+R(\tau))]\), positive separately at each temperature with finite normal row bound \(R(\tau)\). Hence the entire higher-temperature interval is stable and its lower endpoint is strictly below the reported ceiling. No uniform-in-temperature row bound or continuity argument is required. Odd-folded normal dominance and PSD subtraction add only positive costs.

## 7. Lower-side search and honest negative

**NUMERICAL:** `search.py` solves finite centered two-channel normal equations at \(\tau=C_\infty\), \(\rho=1\), with one Einstein spectrum. The 160 parameter sets include flat DOS, one flat/one box, unequal boxes, shells and random reciprocal nonnegative moment matrices. Bands are expressed in units of the dimensionless normal width \(\pi\tau\); all eigenvalues are dimensionless gain values. Newton solves are in positive logarithmic widths, and refusals would be retained instead of assigned zero errors. All 160 solves converged under the stated finite residual criterion. Six-point Pick matrices are necessary tests only, not causal continuations.

The greatest coarse gain is 1.0000000139673306, from the equal-channel flat case. Its gains at normal/pair cutoffs (64,32), (96,48), (160,80) are respectively 1.0000000139673306, 0.9999999987746481 and 0.9999999909813821. The later change is about 7.8e-9. These are empirical cutoff differences, not rigorous errors. **KILLED as a counterexample:** this candidate belongs to the already proved sharp flat-DOS family; the tiny finite-cutoff excess cannot overturn that theorem. **OPEN:** no certified causal nonflat family above \(C_\infty\) was found. The finite search neither proves absence nor certifies an exact thermodynamic instability.

## 8. Evidence, literature and custody

**CERTIFIED scope:** `replay.py` and `independent.py` certify finite rational inequalities and finite form samples. `Finite.lean` checks polynomial identities and rational budgets using `Std`; it does not formalize Harnack, normal branch causality, infinite operators or the entire proof. `RESULT.md` records executed commands and exit codes, including deliberate rejected mutants and numerical refusals.

**[INFERENCE], no novelty or priority claim:** this slice reuses the prior verified dossier in `../OPTIMUM/RIGOR.md`, including GSI Theorems 7-10 and finite-band companion DOI 10.5281/zenodo.24364879. The earlier targeted metadata search covered 19 September through 19 November 2026, not the full literature. No new third-party full text was fetched or parsed. Harnack, positive-kernel resolvent allocation and square completion are classical. The finite multipoint improvement is an internal mathematical result, not an independently reviewed publication.

The continuation proof and numerical search remain in OPTIMUM2. Under Main's explicit integration assignment of 19 November 2026, the improved manuscript and a closure-complete replay distribution are assembled in `../OPTIMUM/release-bundle/`. The earlier reviewed OPTIMUM proof and note, and the original published/candidate release packages, remain historical inputs. No outward action or paid compute is authorized here.
