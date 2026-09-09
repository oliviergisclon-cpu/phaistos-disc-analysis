# Proof Table — Phaistos Disc Structural Analysis

**Regenerated from `python3 phaistos_analysis.py` against `phaistos_disc.csv`.**
Where a value differs from the originally published figure, both are shown —
see "Reconciliation notes" below the table.

| # | Hypothesis | Test Method | Observed (this repo) | p-value (this repo) | Originally published | Bonferroni (n=14, α=0.0036) | Decision |
|---|-----------|-------------|---------|---------|---------|-----------|---------|
| T1 | S02 occupies position 1 in all groups | Exact binomial | 19/19 | 3.64 × 10⁻¹² | 4.62 × 10⁻¹² | ✓ PASS | **Certain** |
| T2 | S38 marks the 4 solar cardinals (±10d window) | Exact binomial | 4/4 | 5.20 × 10⁻³ | 1.92 × 10⁻⁶ | — | Strong |
| T3 | S12 follows S02 in face A | Exact binomial | 12/14 | 1.10 × 10⁻⁵ | 13/14, 1.40 × 10⁻¹⁴ | ✓ PASS | **Certain** |
| T4 | S27 correlates with new moon | — | **not implemented** | — | 0.022 | — | Requires external lunar ephemeris; not derivable from this dataset |
| T5 | S31 (Orion) exclusive to face A | Fisher exact | 5A / 0B | 2.86 × 10⁻² | 0.034 | — | Strong |
| T6 | S22 (Scorpion) exclusive to face B | Fisher exact | 0A / 5B | 2.40 × 10⁻² | 0.029 | — | Strong |
| T7 | S31 always precedes S26 | Binomial | 5/5 | 3.13 × 10⁻² | 0.031 | — | Strong |
| T8 | S13 (Spica) face coherence | Binomial | 3A / 3B | 0.656 | 5/6, 0.036 | — | **Not significant — contradicts original claim** |
| T9 | A14 = A20 identical (verification protocol) | Exact combinatorial | Identical | 2.20 × 10⁻⁷ | 4.46 × 10⁻⁴ | ✓ PASS | **Certain** |
| T10 | S33 (Leo) face coherence | Binomial | 2A / 4B (B-dominant) | 0.344 | 5A/1B, 0.036 | — | **Not significant, and direction reversed vs. original claim** |
| T11 | S29 (Sagittarius) dominant face B | Fisher exact | 2A / 8B | 3.54 × 10⁻² | 0.029 | — | Strong |
| T12 | S13→S01 invariant order | Binomial | 5/5 | 3.13 × 10⁻² | 5/6, 0.031 | — | Strong (but only 5 co-occurrences exist in this dataset, not 6) |
| T13 | S40 and S45 never co-present | Exact combinatorial | 0/6 co-occurrences | 0.522 | 0.554 | — | Qualitative |
| T14 | S18 perfect A=B balance | Exact binomial | 6A / 6B | 1.000 | 1.000 | — | Qualitative |

**Fisher combined (14 tests): χ² = 166.6, df = 28, p ≈ 10⁻²⁰·⁹**

> ⚠️ **This combined figure is illustrative, not a formal significance level.**
> Fisher's method requires the input p-values to be statistically independent.
> Several tests here share the same underlying signs or groups (S02 in T1 and
> T3; S13 in T8, T10 and T12; S31 in T5 and T7), so the independence
> assumption does not hold. The combined p should not be quoted as "the
> probability this arose by chance" until the tests are decorrelated or the
> combination method is revisited.

---

## Reconciliation notes (this repo's data vs. originally published numbers)

Running the reproducible script against `phaistos_disc.csv` as it exists in
this repository does **not** reproduce several of the originally published
figures:

- **T2**: the code's ±10-day window around each solar cardinal gives
  p = 5.2 × 10⁻³, not the published 1.92 × 10⁻⁶. Matching the published
  figure would need a much narrower window (roughly ±3–4 days) — that
  narrower window is not documented anywhere in this repo. Needs a decision:
  either the window used in the paper should be specified and coded, or the
  published figure should be corrected.
- **T3**: this dataset shows S12 following S02 in 12/14 face-A groups, not
  13/14. This changes the p-value by nine orders of magnitude.
- **T8** and **T10**: recomputed directly from this repo's CSV, these come
  out **not statistically significant** (p = 0.66 and p = 0.34), and T10's
  direction is reversed (S33 is more common on face B, not face A as
  claimed). These two rows should not be cited as supporting evidence in
  their current published form.
- **T12**: only 5 groups in this dataset contain both S13 and S01 (not 6);
  the order is correct in all 5.

**What this means:** either the published paper used a dataset or parameters
that differ from what's checked into this public repository, or some of the
published figures need correction. Either way, the discrepancy should be
resolved and documented before these numbers are cited further — that's the
point of publishing a "reproducible" pipeline.

---

## What remains open

| Item | Status | Why |
|------|--------|-----|
| Astronomical dating (Stellarium) | Pending | Requires VSOP87 software |
| Iconographic validation (S31, S33, S35) | Pending | Requires Minoan specialist |
| Sign S26 polysemy (Sirius *or* Scorpion, by season) | Unresolved | A single sign being read as two different objects depending on which result it's supporting is a circularity risk that needs an independent justification, not just a note in the data file |
| 9 hapax signs | Undetermined | Insufficient data |
| Linguistic layer | Possible but untested | No comparative corpus |
| Test independence for Fisher combination | Unresolved | Several tests reuse the same signs/groups; combined p above is illustrative only |
