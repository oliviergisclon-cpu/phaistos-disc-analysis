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
python scripts/phaistos_analysis.py
```

**Expected output:**
```
Fisher combined (15 tests):
  χ² = 223.4, df = 30, p < 10^-38
Conclusion: null hypothesis definitively rejected
```

---

## What this reproduces

| Test | Hypothesis | Expected p-value |
|------|-----------|-----------------|
| T1 | S02 always in position 1 | 4.62 × 10⁻¹² |
| T2 | S38 at solar cardinals | 1.92 × 10⁻⁶ |
| T3 | S12 follows S02 in face A | 1.40 × 10⁻¹⁴ |
| T9 | A14 = A20 identical groups | 4.46 × 10⁻⁴ |
| T15 | Obliques exclude S27/S25 | 0.005 |
| T5 | S31 exclusive face A | 0.034 |
| T6 | S22 exclusive face B | 0.029 |
| T7 | S31→S26 invariant order | 0.031 |

---

## Dataset

`data/phaistos_disc.csv` — 61 groups, 241 signs
- Transcription: Godart (1994), validated against Ridderstad (2010)
- Columns: group, face, position_global, signs, oblique, day_approx, notes

`data/sign_identifications.csv` — 27 identified signs
- Columns: sign_id, identification_en, category, certainty, occurrences, key_evidence

**Dataset SHA256:**
```bash
sha256sum data/phaistos_disc.csv
```

---

## What the results mean

The disc is **not a random document** (p < 10⁻³⁸).
It encodes a **5-level lunisolar calendar**:

1. **Structure** — S02 (group delimiter) + S38 (solar cardinals)
2. **Period** — S12 (sub-period identifier)
3. **Lunar month** — S27 + S25
4. **Lunar phase** — S07 (moon visible)
5. **Astronomical content** — 11 identified objects (Orion, Sirius, Venus, Jupiter...)

**What group A09 says:**
`[S31, S26, S35]` = Orion visible. Sirius present. Venus on the horizon.
Day 61 ≈ December 5, before dawn, from Phaistos (35°N).

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
