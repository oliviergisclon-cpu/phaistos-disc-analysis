# Reproducing the Phaistos Disc Analysis
## Gisclon (2026) — In 15 minutes

This repository contains all data and code to reproduce the statistical results
from: *"The Phaistos Disc as a Lunisolar Information System: Architecture,
Grammar, and Statistical Demonstration"*

---

## Requirements

```bash
pip install scipy numpy pandas
```

Python 3.8+ required.

---

## Quick Start (5 minutes)

```bash
git clone https://github.com/oliviergisclon/phaistos-disc-analysis
cd phaistos-disc-analysis
pip install -r requirements.txt
python phaistos_analysis.py
```

**Actual output of this script, as it stands in this repo:**
```
Fisher combined (14 tests):
  χ² = 166.6, df = 28, log10(p) = -20.94  (p ≈ 10^-20.9)

CAUTION: several of these 14 tests share the same underlying
signs/groups ... not statistically independent ...

Conclusion: p ≈ 10^-20.9 for the 14 tests implemented here.
T4 (lunar correlation) is not included — see note above.
```

This does **not** match the "15 tests, p < 10⁻³⁸" figure quoted elsewhere.
See `PROOF_TABLE.md` → "Reconciliation notes" for exactly which numbers
differ and why, before citing either figure.

---

## What this reproduces

14 of the paper's 15 tests are implemented and computed directly from
`phaistos_disc.csv` (T4 needs an external lunar ephemeris this repo doesn't
have, and is intentionally left out rather than faked). Values below are
what the script in this repo actually outputs — several differ from the
originally published numbers; see `PROOF_TABLE.md` for the full comparison.

| Test | Hypothesis | p-value (this repo) |
|------|-----------|-----------------|
| T1 | S02 always in position 1 | 3.64 × 10⁻¹² |
| T2 | S38 at solar cardinals (±10d) | 5.20 × 10⁻³ |
| T3 | S12 follows S02 in face A | 1.10 × 10⁻⁵ |
| T8 | S13 face coherence | 0.656 (not significant) |
| T9 | A14 = A20 identical groups | 2.20 × 10⁻⁷ |
| T10 | S33 face coherence | 0.344 (not significant) |
| T11 | S29 dominant face B | 3.54 × 10⁻² |
| T12 | S13→S01 invariant order | 3.13 × 10⁻² |
| T13 | S40/S45 never co-present | 0.522 |
| T14 | S18 A=B balance | 1.000 |
| T15 | Obliques exclude S27/S25 | 5.11 × 10⁻³ |
| T5 | S31 exclusive face A | 2.86 × 10⁻² |
| T6 | S22 exclusive face B | 2.40 × 10⁻² |
| T7 | S31→S26 invariant order | 3.13 × 10⁻² |

---

## Dataset

`phaistos_disc.csv` — 61 groups, 241 signs
- Transcription: Godart (1994), validated against Ridderstad (2010)
- Columns: group, face, position_global, signs, oblique, day_approx, notes

`sign_identifications.csv` — 27 identified signs
- Columns: sign_id, identification_en, category, certainty, occurrences, key_evidence

**Dataset SHA256:**
```bash
sha256sum phaistos_disc.csv
```

---

## What the results mean

Several individual tests (T1, T3, T9) show extremely small p-values that
survive Bonferroni correction on their own — the disc's group structure
(S02 as a delimiter, S12 as a period marker, the repeated A14/A20 group) is
very unlikely to be pure chance. The combined figure across all 14
implemented tests (p ≈ 10⁻²⁰·⁹) should be read as a rough illustration of
"the pattern as a whole is not random," **not** as a rigorous joint
significance level — several of the tests reuse the same signs and are not
independent, and two of them (T8, T10) came out not significant when
recomputed from this dataset. See `PROOF_TABLE.md` for the full picture,
including which claims still need reconciliation.

The proposed **5-level lunisolar calendar** reading — built from these
structural signs, on top of celestial-object identifications that are
themselves still pending specialist review (see "What remains open" below)
— is:

1. **Structure** — S02 (group delimiter) + S38 (solar cardinals)
2. **Period** — S12 (sub-period identifier)
3. **Lunar month** — S27 + S25
4. **Lunar phase** — S07 (moon visible)
5. **Astronomical content** — 11 proposed objects (Orion, Sirius, Venus, Jupiter...)

**Proposed reading of group A09:**
`[S31, S26, S35]` → Orion visible. Sirius present. Venus on the horizon.
Day 61 ≈ December 5, before dawn, from Phaistos (35°N). This is one candidate
reading under the hypothesis above, not an independently verified
translation.

---

## Citation

```
Gisclon, O. (2026). The Phaistos Disc as a Lunisolar Information System:
Architecture, Grammar, and Statistical Demonstration.
HAL: hal-05652844. Zenodo: 10.5281/zenodo.20630895
```

---

## License

Data and code: CC BY 4.0 — Olivier Gisclon (2026)
