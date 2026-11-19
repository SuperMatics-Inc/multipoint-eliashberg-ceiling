# Multipoint causal multichannel Eliashberg ceiling

PROVED, with a computer-assisted rational inequality: under the finite-channel centered or channel-wise causal shifted normal-branch hypotheses in `main.tex` and `OPTIMUM2/RIGOR.md`,

`k_B T_lin < sqrt(377/250)/(2*pi) * sqrt(rho)`.

The coefficient is calculated as 0.19544330695411738. The remaining relative gap to the sharp scalar coefficient is approximately 7.0%. The optimal coupled coefficient and full shifted-versus-centered comparison remain OPEN. This is a linear Eliashberg result, not an exact many-body ceiling or a material measurement.

The certified edge reserve `d_* = 247/1000` is distinct from the weaker reported reserve `d = 123/500`. Normal frequency rows need only be bounded separately at each tested temperature. No uniform-in-temperature row constant is assumed.

## Exact replay

From this directory on the stated Windows toolchain:

```sh
python -I -B OPTIMUM2/verify.py
```

The driver runs two independent exact rational coverings, fourteen expected guarded mutant failures, and finite Lean 4.35.0 lemmas. Each unmutated replay must exit 0. Each named mutant must exit 1 with a `REJECT:` guard. Python uses only the standard library for this proof replay. Lean is invoked through `C:/Users/davis/.elan/bin/elan.exe` with a 500 MB bound. Edit that executable location only when replaying on another machine with the same admitted Lean toolchain.

The primary accepts 537 binary-cover leaves; the independent implementation accepts 437 four-way-cover leaves and checks 72 supplementary actual-weight finite forms. The forms are samples, not the universal certificate. Lean verifies polynomial identities and rational budgets, not Harnack, the infinite operator or the covering algorithm.

Both replays verify `OPTIMUM2/closure.json` and consume exactly these sibling paths:

- `SHARP-Q2/RIGOR.md`
- `CENTERED-GAP/RIGOR.md`
- `GENERAL/RIGOR.md`

Do not flatten the distribution or change those bytes. `OPTIMUM/RIGOR.md` retains the reviewed first-frequency comparison as a historical analytic note, not as the improved theorem.

## Paper and provenance

`main.tex`, `refs.bib` and `main.pdf` are the integrated short paper. The byline is Davis Rens, SuperMatics Inc., ORCID 0000-0001-5839-5197. The predecessor note is cited explicitly. Its staging DOI macro `\PredecessorDOI` is intentionally empty; the manuscript makes no unsupported DOI claim.

Build locally with cached TeX resources:

```sh
D:/dev/tools/tectonic/tectonic.exe --only-cached main.tex
```

`SOURCE-PINS.json` records raw-byte SHA-256 hashes and sizes of all load-bearing sources and inherited proof inputs. `OPTIMUM2/clean_copy.py` requires its externally recorded digest, admits every member, preserves the sibling layout in an isolated copy, executes the complete replay, builds a fresh PDF and compares its page text with the admitted paper. It removes only its own temporary directory. This transport/build check also needs the installed PyMuPDF package; the exact proof replays themselves remain standard-library-only. Run after setting `ADMITTED_MANIFEST_SHA256` to the separately recorded `SOURCE-PINS.json` digest:

```sh
python -I -B OPTIMUM2/clean_copy.py --manifest-sha256 "$ADMITTED_MANIFEST_SHA256"
```

`CLEAN-COPY.txt` is the producer's observed clean-copy receipt. The final `PINS.json` includes that receipt and the unchanged admitted `SOURCE-PINS.json`; the receipt is not recursively included in its own source admission. No replay receipt is a new material experiment or a new scientific benchmark look.

No upload, email, commit, push, merge or publication is performed by either script. This local release candidate requires the separately assigned delta review before outward use.
