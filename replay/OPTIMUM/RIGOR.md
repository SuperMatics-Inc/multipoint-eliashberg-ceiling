# OPTIMUM: an additive head reserve and a smaller causal multichannel ceiling

## Verdict and exact statement

**PROVED, computer-assisted finite inequality.** Under the hypotheses below, centered causal branches and causal shifted radial-normal branches obey
\[
 k_BT_{\rm lin}<C_{\rm new}\sqrt\rho,
 \qquad C_{\rm new}=\frac{\sqrt{413/250}}{2\pi}.
\]
The decimal 0.20456209043780693 is **NUMERICAL**, calculated from this exact expression, not an interval enclosure. The exact improvement over the preceding \(U\) follows from \(413/250<6466219/3576050\). The optimal coefficient is still **OPEN** in \([C_\infty,C_{\rm new}]\). No causal counterexample above \(C_\infty\), or actual shifted-versus-centered excess, is asserted.

**CERTIFIED.** Exact rational subdivisions cover a two-parameter residual rectangle and prove a stronger uniform allocated edge reserve \(d_*=349/2000\). An independent four-way subdivision verifies the same bound. These are exhaustive finite covering certificates, not samples. The finite edge matrices are supplementary samples only.

## 1. Hypotheses, normalization and scope

Retain the matched reciprocal reduced Eliashberg model from `../SHARP-Q2/RIGOR.md`, with finitely many positive-height angular channels, height measure \(d\eta\), energy-independent radial vertices, reciprocal nonnegative positive-energy moment measures \(d\mathfrak m_{xy}(E)\), and finite positive moment-operator norm \(\rho\). Transfers and folded normal rows are bounded, including zero transfer, uniformly on the temperature interval under discussion. Each channel DOS is a fixed measurable function of energy, between zero and its essential height. Integrable even DOS and the bounded flat limiting class are covered.

An actual positive normal branch must exist at every tested temperature, solve the matched imaginary normal equation, and have the reflection needed by the positive-frequency fold. For a centered branch it is sufficient to have the centered branch hypotheses and slope cone proved in CENTERED-GAP. For the causal class used here, each energy-independent effective frequency \(Z_x(z)=z-\Sigma_x(z)\) is a holomorphic upper-half-plane self-map. It represents the radial propagator \((Z_x(z)-\xi)^{-1}\). Glue passivity by itself does not establish this property for an arbitrary algebraic Matsubara solution. The width is \(\Im Z_x(i\pi\tau w_n)/(\pi\tau)>0\), \(w_n=2n+1\), and \(\tau=k_BT\) is an energy.

The pairing form can be the matched positive form or an eligible envelope whose odd-folded normal mass is dominated by the actual normal kernel. A bounded PSD pairing-only subtraction is harmless. Preservation of a claimed pairing symmetry sector must be separately assumed. A signed moment or an angular average is not \(\rho\).

Normalize the DOS height to one and write its Poisson weights as \(b_{n,x}\in[0,1]\). The only DOS information used by the new ceiling proof is
\[
 b_{1,x}\ge\max\{0,3b_{0,x}-2\}. \tag{1}
\]
For a causal branch, Schwarz-Pick at the first two Matsubara points gives pseudohyperbolic distance at most \(1/2\), or
\[
 |Z(i3\omega)-Z(i\omega)|^2\le\tfrac43\Im Z(i3\omega)\Im Z(i\omega).
\]
The pointwise Poisson-density ratio is between \(1/3\) and 3. Integrate it against the complementary DOS \(1-r\), using that the full Poisson integral is one, to obtain (1). GENERAL gives the determinant and limiting leading-coefficient proof of this comparison. For centered branches, the centered slope cone gives the same complementary inequality. Thus the new argument covers those branches without assuming arbitrary independent weights are realizable.

For a unit atom put \(t=(E/(2\pi\tau))^2>0\), \(k_j=(t+j^2)^{-1}\), \(p_{nm}=k_{|n-m|}-k_{n+m+1}\), and \(S_{nm}=k_{|n-m|}+k_{n+m+1}\). For a finite-support trial set \(g_{n,x}=\sqrt{w_nb_{n,x}}v_{n,x}\). With angular allocation \(r>0\), define
\[
 B_r=r^{-1}\|g_x\|^2+r\|g_y\|^2,
\]
\[
 I_{xy}=\sum_{n,m}b_{n,x}b_{m,y}\{p_{nm}(|v_{n,x}|^2+|v_{m,y}|^2)-2S_{nm}\Re(\bar v_{n,x}v_{m,y})\}.
\]
The stability form is
\[
 Q=\int\|g_x\|^2d\eta(x)+\frac1{2(2\pi\tau)^2}\iint\!\int I_{xy}\,d\mathfrak m_{xy}\,d\eta(x)d\eta(y). \tag{2}
\]
The ordered-edge factor one half is essential; the two endpoint bare allocations later produce a factor two.

## 2. Tail and head-tail costs, with a tighter tail enclosure

**PROVED.** The tail Hankel matrix \(H_{nm}=k_{n+m+1}/\sqrt{w_nw_m}\), \(n,m\ge1\), has norm smaller than \(q=33/500\). Use Schur weights \(1/\sqrt{w_n}\); the largest soft row is
\[
 \sum_{m\ge1}\frac1{(2m+1)(m+2)^2}
 \le \sum_{m=1}^{16}\frac1{(2m+1)(m+2)^2}+\frac1{4\cdot16^2}
 =\frac{46364886969645845897}{707706794762032665600}<\frac{33}{500}.
\]
The remainder follows from \(1/[(2m+1)(m+2)^2]\le1/(2m^3)\) and the integral from 16 to infinity. Dropping the PSD tail difference squares leaves at least \((1-q)\) of the two tail bare norms, independently of the angular allocation.

Use \(\alpha=759/1000\) of the tail bare norm for head-tail completion, leaving
\[
 1-q-\alpha=7/40>d_*:=349/2000. \tag{3}
\]
Reduce to independent Bernoulli endpoint masks, keeping \(v\) fixed. This is valid because the form is separately affine in the endpoint weights. Even on a loop, use two copies before identifying the actual profiles. For binary active coordinates set \(a_n=g_{n,x}/\sqrt r\), \(d_n=\sqrt r g_{n,y}\). Then \(B_r=\|a\|^2+\|d\|^2\).

For an active head and opposing frequency \(m\ge1\), the completion is
\[
 \frac{rp}{2}|a_0|^2+\left(\alpha+\frac p{2rw_m}\right)|d_m|^2-\frac S{\sqrt{w_m}}\Re(\bar a_0d_m),
\]
where \(p=k_m-k_{m+1}\), \(S=k_m+k_{m+1}\). Its residual head coefficient is \(rp/2-S^2/[4w_m(\alpha+p/(2rw_m))]\). Since
\[
 \frac{S^2-p^2}{w_mp}=\frac4{w_m^2},
\]
all completions are nonnegative in both directions when \(1/3\le r\le3\), because \(\alpha>2/3\).

Outside that allocation interval, the total loss of either head is at most
\[
 L=\frac{59/96}{4\alpha}.
\]
Indeed \(\sum_{m\ge1}S^2/w_m\le25/48+2\sum_{m\ge2}m^{-5}\le59/96\). Here \(S_1^2/3\le25/48\), and \(2\sum_{m\ge2}m^{-5}\le2(2^{-5}+\int_2^\infty x^{-5}dx)=3/32\). This loses a head coefficient, not a second copy of the tail allocation.

For frequency 1 specifically, retain rather than discard the positive head completion
\[
 D(r,t)=\frac{p(r\alpha/2-1/9)}{\alpha+p/(6r)},\qquad
 p=\frac3{(1+t)(4+t)}. \tag{4}
\]
The identity \(S^2-p^2=4p/3\) proves (4) exactly. Its numerator is positive for all balanced allocations. In that region D increases in p and r: writing \(a=r\alpha/2-1/9\), \(z=\alpha+p/(6r)\), its derivatives are \(a\alpha/z^2>0\) and \(p[(\alpha/2)z+ap/(6r^2)]/z^2>0\). Consequently D decreases with t. These monotonicities justify outward rectangle bounds; they are not inferred from a grid.

## 3. Add the two-head reserve to D instead of taking their minimum

**PROVED.** If both heads are present, their pre-completion matrix is
\[
 H_0=\begin{pmatrix}1+\beta r&-\beta-u\\-\beta-u&1+\beta/r\end{pmatrix},\qquad
 u=(1+t)^{-1},\quad \beta=1/[2t(1+t)].
\]
It is bounded below by \(e(r,t)I\), where
\[
 e(r,t)=\max\left\{\frac t{1+t},\ 1-\frac2{r+r^{-1}}\right\}. \tag{5}
\]
The first lower bound drops the PSD rank-one beta term. For the second put \(a=2/(r+r^{-1})\); the positive first diagonal and exact determinant identity
\[
 2(1-u)\det(H_0-(1-a)I)=2(1-u)a^2+u^2[a(r+r^{-1})-2]>0
\]
prove the claim. Here t is strictly positive; t=0 is used only in enclosures. If just one head is present, it retains its unit bare cost. Thus far allocations have head reserve at least
\[
 \frac25-L>d_*. \tag{6}
\]

In balanced allocations, the two-head matrix and the first head-tail completion are disjoint pieces of the form. Their reserves therefore add. Average the masks for the opposing endpoint. For the x-head, with \(b=b_{0,y}\) and \(b_1=b_{1,y}\), the coefficient left is at least
\[
 1-b+e b+D(r,t)b_1.
\]
Using (1) and minimizing the resulting piecewise affine function of b gives the exact bound
\[
 F(r,t)=\min\left\{e(r,t)+D(r,t),\frac{1+2e(r,t)}3\right\}. \tag{7}
\]
The only candidate b values are 0, 2/3 and 1. Their values are 1, \((1+2e)/3\), and \(e+D\); 1 cannot be the smallest since \(0\le e\le1\). This handles masks where the opposing head is absent and frequency 1 is present, without confusing those independent events. The x-head mask is independent of both opposing masks. Exchange endpoints and replace r by 1/r to obtain the same claim for the other head.

This additive use is the improvement over CENTERED-GAP: that proof retained the head imbalance reserve or D in separate parameter regions, rather than their sum.

## 4. CERTIFIED residual rectangle inequality

We prove \(F(r,t)\ge d_*\) for all \(1/3\le r\le3\), \(t\ge0\). For \(t\ge T=d_*/(1-d_*)=349/1651\), (5) already gives \(e\ge d_*\); head-mask averaging and nonnegative completions suffice, without (7).

It remains to cover \([1/3,3]\times[0,T]\). For a closed rational rectangle \([l,h]\times[a,b]\), set
\[
 e_L=\max\{\min_{r\in[l,h]}(r-1)^2/(r^2+1),\ a/(1+a)\},
\]
\[
 p_L=3/[(1+b)(4+b)],\qquad
 D_L=p_L(l\alpha/2-1/9)/(\alpha+p_L/(6l)).
\]
The imbalance minimum is zero if the interval contains 1 and otherwise is the smaller endpoint value. Monotonicity from section 2 gives \(D\ge D_L\); (5) gives \(e\ge e_L\). Hence
\[
 F(r,t)\ge\min\{e_L+D_L,(1+2e_L)/3\}. \tag{8}
\]

`replay.py` starts with the two rectangles separated at r=1. It accepts a rectangle only when (8) is at least \(349/2000\), otherwise bisects exactly along the longer normalized axis. Every child is contained in its parent, their interiors are disjoint, and their union is the parent. The exact sum of leaf areas must equal \((8/3)T\). Maximum depth is bounded; any unresolved box rejects the replay. Thus no zero-width gap, sampled interpolation or floating-point rounding enters the certificate. `independent.py` instead rationalizes D as \(rp(9r\alpha-2)/[3(6r\alpha+p)]\) and subdivides each unresolved rectangle in four. Its own exact leaf-volume assertion covers the same domain. Both bases must exit 0. Named mutants alter signs, denominators, area coverage, tail budgets and endpoint factors and must exit 1 at `REJECT:` guards.

The replay counts and command exit codes are recorded in RESULT.md. Exact finite LDL checks in the independent replay supplement but do not replace the universal rectangle proof.

## 5. From the allocated edge reserve to the onset ceiling

Sections 2-4 prove for every unit positive-energy atom, all r and every eligible actual weight profile,
\[
 B_r+I_{xy}(t)/2\ge d_* B_r. \tag{9}
\]
A finite trial need only include frequencies 0 and 1 with zero amplitudes when absent. Omitting other frequencies drops nonnegative normal diagonals. The tail estimates cover all remaining frequencies uniformly. Bernoulli averaging then gives (9) at actual weights, not only binary masks.

For any \(R'>\rho\), the nonnegative reciprocal moment matrix has a positive superharmonic vector h with \(\mathcal M h\le R'h\), for example the positive resolvent \((I-\mathcal M/R')^{-1}{\bf1}\). Allocate \(r=h_x/h_y\) edgewise. Insert (9) into (2), integrate the reciprocal measure, and retain both endpoints:
\[
 Q\ge\left[1-\frac{2(1-d_*)R'}{(2\pi\tau)^2}\right]\|g\|^2.
\]
Let \(R'\downarrow\rho\). Finite-support density and bounded normal rows carry the bare-form gap to the symmetrized pairing norm. Extra folded normal mass and PSD subtraction only add positive costs. Choose the deliberately smaller reported reserve \(d=87/500<d_*\). Since
\[
 2(1-d)=413/250,
\]
there is a common stable interval beginning strictly below \(\sqrt{413\rho/250}/(2\pi)\), and stability persists at larger temperatures under the stated normal-row hypotheses. This proves the strict onset statement, rather than only stability at a single temperature. \(\rho=0\) has no positive pairing envelope and is excluded only to define the ratio.

The lower endpoint \(C_\infty\) is imported from the existing sharp flat scalar soft family; the centered class includes it. The previous finite-band and broad-box results retain their own convergence hypotheses. No new assertion that a finite fixed box realizes the flat equality is needed.

## 6. PROVED geometric test of shifted-versus-centered excess, not a Tc counterexample

For any causal first pair, let d be the pseudohyperbolic distance of its two normal effective frequencies. Schwarz-Pick gives \(d\le1/2\). A real-boundary Möbius automorphism maps the pair to i and ih with \(1\le h=(1+d)/(1-d)\le3\). Poisson harmonic measure is invariant under this map. Composition carries every bounded normalized DOS into another function between zero and one, preserving the two Poisson averages. Even symmetrization of the transformed DOS preserves these averages because both canonical kernels are even. This is a statement about a two-point DOS relaxation, not about mapping a full normal solution.

**PROVED.** For a prescribed \(b_0\in[0,1]\), the smallest canonical second average is realized by an interval \([-W,W]\), with \(W=\tan(\pi b_0/2)\). Indeed \(q_i/q_{ih}\) decreases with absolute energy for h>1. Set c to the ratio \(q_{ih}(W)/q_i(W)\). For any competing DOS with the same first integral, subtract the interval indicator. Its product with \(q_{ih}-cq_i\) is nonnegative both inside and outside the interval. Integration proves the minimizing claim. Endpoint cases follow by limits. Therefore every causal first pair obeys
\[
 b_1\ge\frac2\pi\arctan\left[\frac13\tan\left(\frac{\pi b_0}2\right)\right]. \tag{10}
\]
Centered points i and 3i with even interval DOS attain the boundary of this two-frequency relaxation. In particular, the maximal difference between the two averages is at \(W=\sqrt h\). It increases with h, and at h=3 is
\[
 \max(b_0-b_1)=\frac4\pi\arctan\sqrt3-1=\frac13.
\]
Thus \(b_1\ge b_0-1/3\) is an additional exact necessary condition. The independent replay checks the canonical crossing identity \(q_i(a)-q_{3i}(a)=2(3-a^2)/[(a^2+1)(a^2+9)]\). The arctangent minimization and Möbius invariance are analytic arguments, not interval certificates.

**OPEN.** This produces no actual shifted advantage at the two-point Poisson level. It neither establishes nor excludes a shifted onset excess: the Möbius boundary change need not preserve the physical DOS integrability, the imaginary normal equation at all Matsubara frequencies, its relative real equation, or the glue transfer profile. Symmetrization and truncation may approximate two averages but are not a self-consistent branch construction. No numerical sampled Pick matrix is presented as an infinite causal continuation.

## 7. Scientific custody, prior work and trust boundary

**PROVED** concerns only the reduced normal-branch linear instability. No measured or exact many-body transition, confirmed material, or phonon-independent Hamiltonian theorem is claimed. The improvement uses the total eligible pairing-envelope moment in DOS-height measure, with signs and factors stated in (2).

The unchanged source proofs are SHA-256-pinned in `closure.json`. They are prior analytic inputs, not inferred from successful matrix samples. Lean checks finite polynomial identities and rational budgets only; the infinite form, Schwarz-Pick, DOS extremal argument and rectangle covering are not fully formalized in Lean.

**[INFERENCE] prior-work assessment.** This slice reuses the verified ceiling dossier and bibliography from the preceding work, including GSI Theorems 7-10 and finite-band companion DOI `10.5281/zenodo.24364879`. The earlier targeted metadata search covered 19 September through 19 November 2026 and is not exhaustive. Schwarz-Pick, Poisson extremal rearrangement and square completion are classical. No novelty or priority claim is made. Paper-reader spawning is unavailable, and no new third-party full text was fetched or parsed. The separate local note records an improvement to the existing bracket, not a resolved sharp constant.

The OPTIMUM proof and note remain separate and are not folded into any existing paper or release candidate. Under a separate explicit Main assignment, a packaging-only repair added two byte-exact receipts to `../note-shifted/GENERAL/`, corrected its RESULT provenance sentence and re-pinned those three package members in the producer manifest. No theorem, replay source, `main.tex` or `main.pdf` in that candidate changed. `../note/`, `../release-bundle/` and `../note-centered/` are untouched. No outward action or paid compute occurred.
