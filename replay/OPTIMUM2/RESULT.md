# PROVED / CERTIFIED: a smaller causal multichannel ceiling; sharpness OPEN

**PROVED, with a CERTIFIED rational inequality, under the finite-channel hypotheses in RIGOR.md:**

\[
 k_B T_{\rm lin}< C_{21}\sqrt{\rho},\qquad
 C_{21}=\frac{\sqrt{377/250}}{2\pi}.
\]

Here \(\rho\) is the operator norm of the reciprocal nonnegative total retarded moment matrix in the channel DOS-height measure. The normal and attractive pairing envelope use the same transfer. A dominated pairing kernel, an odd-folded nonnegative extra normal mass, or a PSD static pairing subtraction cannot increase the onset within these hypotheses. The statement covers centered branches and shifted branches with the specified channel-wise causal radial propagator. Normal frequency rows need only be bounded separately at each tested temperature. No uniform-in-temperature row bound is used.

**NUMERICAL evaluation of the exact expression:** \(C_{21}=0.19544330695411738\). The relative gap to \(C_\infty=0.18272624777232952\) is approximately 7.0%. **PROVED:** the squared numerator decreases from the reviewed first-frequency value \(413/250\) by exactly \(18/125\). **OPEN:** the optimal coupled coefficient lies between the sharp scalar coefficient and this upper bound. Neither the scalar lower family nor a finite DOS relaxation proves that \(C_\infty\) is sharp for the full covered class.

## Proof and finite certificates

**PROVED:** the strengthened two-head lower bound and twenty retained head-to-tail completions leave an edge reserve of at least \(d_*=247/1000\). This certified reserve is distinct from the weaker reported reserve \(d=123/500\). A threshold with squared numerator \(1507/1000\), strictly between the certified \(753/500\) and reported \(377/250\), gives stability at every higher temperature. Its width-normalized gap is positive separately at each temperature with a finite normal row bound. This establishes strictness without a uniform row assumption or a continuity argument.

**CERTIFIED:** the primary exact-rational binary covering accepts 537 leaves, visits 1072 nodes and reaches depth 21. The independent four-way covering accepts 437 leaves, reaches depth 10 and checks 72 supplementary actual-weight finite forms. Exact rectangle areas establish complete coverage. The supplementary matrices are samples, not the universal certificate. Neither implementation imports the other.

**CERTIFIED finite Lean:** integer polynomial identities for the sharper head square and its monotonicity numerators, and rational budget identities, use Lean 4.35.0 with narrow `Std` imports. Lean does not formalize Harnack, the infinite operator, normal-branch causality, or the rectangle-cover algorithm. RIGOR.md gives those analytic arguments and the imported hypotheses.

### Executed integration evidence

All commands below were exercised locally. `VERIFICATION.txt` retains the complete statuses.

| Command or guarded group | Observed exit |
|---|---:|
| `python -I -B verify.py` in this directory | 0 |
| `python -I -B replay.py` | 0 |
| Primary mutants: `head-square`, `head-denominator`, `moment-sign`, `complement-factor`, `tail-budget`, `far-loss`, `coverage-gap`, `strict-budget`, `edge-factor` | 1 each, guarded `REJECT:` |
| `python -I -B independent.py` | 0 |
| Independent mutants: `volume-copy`, `completion-coefficient`, `matrix-gain`, `missing-normal-mass`, `flat-admissibility` | 1 each, guarded `REJECT:` |
| `C:/Users/davis/.elan/bin/elan.exe run leanprover/lean4:v4.35.0 lean --threads=1 --memory=500 Finite.lean` | 0 |
| `D:/dev/tools/tectonic/tectonic.exe --only-cached main.tex` in the release bundle, initial attempt | 1: uncached `cmr17.pfb` |
| `D:/dev/tools/tectonic/tectonic.exe main.tex` after permitting retrieval of the missing TeX font | 0 |

**Observed paper evidence:** the successful build produced six pages. All six rendered pages were inspected, including the exact coefficient in the title and abstract, the byline and ORCID, predecessor citation, fourteen-mutant count and approximately 7.0% remaining gap. Bibliography underfull-box and Fontconfig warnings remain documented; the successful font-retrieving build exits 0. No paper PDF was fetched or parsed ad hoc.

## Lower-side result

**NUMERICAL, retained search evidence:** `search.py`, `SEARCH.json` and `SEARCH.txt` describe 160 finite centered two-channel normal solves at \(\tau=C_\infty\), \(\rho=1\), with a common Einstein spectrum. All 160 rows report convergence, with no unresolved row. The greatest reported normal log residual is \(1.2238\times10^{-11}\). Six-point Pick matrices have smallest observed eigenvalue \(8.20\times10^{-12}\); these are necessary finite tests, not certified causal continuations. The original search process is not rerun merely to confirm its retained observations.

**KILLED as a counterexample:** the largest coarse gain, 1.0000000139673306, belongs to the already proved equal-channel flat-DOS family. At normal/pair cutoffs (64,32), (96,48), (160,80), the gains are 1.0000000139673306, 0.9999999987746481 and 0.9999999909813821. The later change is about \(7.8\times10^{-9}\), an empirical cutoff difference rather than a rigorous error. The greatest coarse nonflat gain is 0.9999669402994175, also below one. **OPEN:** this finite search finds no certified causal nonflat counterexample and does not prove absence.

**PROVED inherited relaxed comparison, not a full onset comparison:** a causal two-frequency Poisson boundary can be realized by centered points and an even interval DOS. A full-head DOS average of one forces full height almost everywhere and hence every DOS average to one. The boundary transformation need not preserve the full self-consistent normal equations, integrability, or physical transfer. **OPEN:** full shifted-versus-centered comparison remains unresolved.

## Manuscript, custody and prior work

The integrated candidate is `../OPTIMUM/release-bundle/main.tex`, with `refs.bib` and its six-page PDF. Its title states the exact coefficient. The byline is Davis Rens, SuperMatics Inc., ORCID 0000-0001-5839-5197. The verified finite-band companion DOI is 10.5281/zenodo.24364879. The predecessor is explicitly cited; its staging DOI macro is empty rather than invented. The original reviewed `../OPTIMUM/RIGOR.md`, RESULT.md and note stay unchanged as history.

**[INFERENCE], no priority claim:** the prior verified dossier and its targeted 19 September to 19 November 2026 metadata search are reused. That is not exhaustive coverage of the literature. Harnack, positive-kernel resolvents and square completion are classical. The multipoint refinement requires the separately assigned delta review before outward use.

**Scope and skipped checks:** no broad test suite, lint, formatter, cloud/GPU job, new third-party full-text intake, new material calculation, publication, email, push, merge, or commit. Exact proof replays and the assigned TeX build are the exercised verification. Local spend is $0. The theorem is about linear Eliashberg normal-branch stability, not a measured material or a general exact many-body transition.
