# A √(377/250)/(2π) moment-norm ceiling for causal multichannel Eliashberg branches

`paper/main.tex` and `paper/refs.bib` are the source of the preprint. The paper is [10.5281/zenodo.24374032](https://doi.org/10.5281/zenodo.24374032), with [replay supplement 10.5281/zenodo.24374034](https://doi.org/10.5281/zenodo.24374034) and this [source repository](https://github.com/SuperMatics-Inc/multipoint-eliashberg-ceiling). It strengthens the published predecessor [10.5281/zenodo.24372930](https://doi.org/10.5281/zenodo.24372930) and relies on the sharp scalar result of the finite-band companion [preprint](https://doi.org/10.5281/zenodo.24364879) and its [supplement](https://doi.org/10.5281/zenodo.24364881). The preprint has not been peer reviewed.

## Result and its labels

For a reciprocal reduced Eliashberg model with finitely many positive-height channels, fixed bounded channel densities of states, and a centered normal branch or a shifted branch with a channel-wise causal radial-normal propagator, the linear pairing temperature obeys

`k_B T_lin < sqrt(377/250)/(2*pi) * sqrt(rho)`,

where `rho` is the norm of the reciprocal moment matrix. The bound concerns linearized pairing onset on those branches. It is not a bound on the exact thermodynamic transition of a many-body Hamiltonian, and it makes no material or measurement claim.

| Label | Statement | Evidence |
| --- | --- | --- |
| PROVED | The exact bound above under the stated hypotheses | Analytic arguments in the manuscript and `replay/OPTIMUM2/RIGOR.md`, with three byte-pinned inherited inputs in `replay/SHARP-Q2/`, `replay/CENTERED-GAP/` and `replay/GENERAL/` |
| CERTIFIED | The finite rational inequality with certified edge reserve `d_* = 247/1000`, which exceeds the reported reserve `d = 123/500` and gives strict onset | Two exact rational coverings: the primary `replay.py` with 537 leaves and the independent `independent.py` with 437 leaves plus 72 supplementary finite forms. The 72 forms are samples, not universal certificates |
| NUMERICAL | The decimal 0.19544330695411738, the relative gap of about 7.0% to the sharp scalar constant, and a 160-row finite two-channel normal search | Floating-point evaluation and finite solves. They are not interval-certified |
| OPEN | The full coupled sharp endpoint, the full shifted-versus-centered comparison, and any general many-body or material transition ceiling | Not claimed |

Normal frequency rows are bounded separately at each tested temperature, not uniformly in temperature. `Finite.lean` checks only finite polynomial identities and rational budgets; it does not formalize the infinite operator, the covering algorithm, the Harnack step, or the Poisson rearrangement.

## Layout

| Path | Contents |
| --- | --- |
| `paper/` | Released manuscript source `main.tex` and its bibliography `refs.bib` |
| `replay/` | The complete reviewed source bundle, byte for byte, with its pin manifests `PINS.json` and `SOURCE-PINS.json` |
| `replay/OPTIMUM2/` | `replay.py`, `independent.py`, `Finite.lean`, `RIGOR.md`, `closure.json`, the numerical search `search.py` with its `SEARCH.json` and `SEARCH.txt` |
| `replay/SHARP-Q2/`, `replay/CENTERED-GAP/`, `replay/GENERAL/`, `replay/OPTIMUM/` | Inherited analytic inputs and the earlier note that the replays read at these sibling paths |
| `lakefile.toml`, `lake-manifest.json`, `lean-toolchain` | An empty-dependency Lean package pinning Lean 4.35.0 |

`replay/main.tex`, `replay/refs.bib` and `replay/main.pdf` are the admitted pre-DOI source and its build (SHA-256 `17097afada28b456c70a07cecf6aa1ea6fc98b358ff8baa4bd9cb9a7459cce6e`, `c0031a8c9ec50d8c24b538d590fef28a0d21c8d38ad31264ad70c0a12342275e` and `393ab67e5b3918eae19b56553e8c1b8037f73e828c256bf52a047e260b488ca5`) and are kept byte for byte so that the admission pins stay valid. `paper/main.tex` differs from `replay/main.tex` by publication metadata (the predecessor DOI, three identifier macros for this release, and a short supporting-material section) and by one added introduction paragraph that cites Dolgov and Golubov, Physical Review B 77, 214526 (2008). `paper/refs.bib` differs from `replay/refs.bib` only by that added `dolgov` entry. No theorem, coefficient or hypothesis changed. The `replay/OPTIMUM2/verify.py` and `clean_copy.py` drivers are Windows-host tools with hard-coded local paths. They are kept unchanged; the commands below are their portable equivalent.

## Replay

The two Python replays use only the standard library. From a **clean checkout** with Python 3.12, Lean 4.35.0 and Tectonic on `PATH`, run the following from the repository root. Each base replay and the Lean file must exit 0. Each of the 14 named mutants (nine for `replay.py`, five for `independent.py`) must exit 1 with a named `REJECT:` guard. The Tectonic build must exit 0; independent builds can differ in PDF metadata.

```sh
set -eu
export PYTHONDONTWRITEBYTECODE=1
cd replay/OPTIMUM2

out=$(python -I -B replay.py)
printf '%s\n' "$out"
printf '%s\n' "$out" | grep -q '537 leaves'
printf 'PASS base replay.py (exit 0)\n'
out=$(python -I -B independent.py)
printf '%s\n' "$out"
printf '%s\n' "$out" | grep -q '437 leaves'
printf '%s\n' "$out" | grep -q 'supplementary finite forms: 72'
printf 'PASS base independent.py (exit 0)\n'

count=0
reject_all() {
    file=$1; shift
    for mutation in "$@"; do
        rc=0
        result=$(python -I -B "$file" --mutant "$mutation" 2>&1) || rc=$?
        if [ "$rc" -ne 1 ] || ! printf '%s\n' "$result" | grep -q '^REJECT: '; then
            printf 'Unexpected mutant result: %s %s (exit %s)\n%s\n' "$file" "$mutation" "$rc" "$result" >&2
            return 1
        fi
        printf 'PASS mutant %s %s (exit 1): %s\n' "$file" "$mutation" "$result"
        count=$((count + 1))
    done
}
reject_all replay.py head-square head-denominator moment-sign complement-factor tail-budget far-loss coverage-gap strict-budget edge-factor
reject_all independent.py volume-copy completion-coefficient matrix-gain missing-normal-mass flat-admissibility
[ "$count" -eq 14 ]
printf 'PASS all %s mutant rejections\n' "$count"

lean --version
lean --version | grep -q '4\.35\.0'
lean Finite.lean
printf 'PASS Lean Finite.lean (exit 0)\n'

cd ../../paper
tectonic --keep-logs main.tex
printf 'PASS Tectonic (exit 0)\n'
```

## Licenses and provenance

Replay code, the finite Lean file and proof documentation are licensed under Apache-2.0. The manuscript source, bibliography and PDF are licensed under CC-BY-4.0. The license exceptions are stated in `LICENSE`.

AI agents generated proofs, certificates, code, and manuscript drafts and edits under D. Rens' direction and review.
