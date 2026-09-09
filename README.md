# Phaistos Disc — Structural Analysis Pack

**A candidate structural reading of the Phaistos Disc (1700 BCE), open to review and refutation**

> *"Group A09 = [Orion, Sirius, Venus]: Orion visible. Sirius present. Venus on the horizon.
> Day 61 ≈ December 5, before dawn, from Phaistos (35°N), ~1700 BCE."*
> — one candidate reading under the hypothesis below, not a verified translation.

---

## What this is

This repository contains all data, code, and documentation to **reproduce and verify**
the statistical results from:

> Gisclon, O. (2026). *The Phaistos Disc as a Lunisolar Information System:
> Architecture, Grammar, and Statistical Demonstration.*
> HAL: [hal-05652844](https://hal.science/hal-05652844) ·
> Zenodo: [10.5281/zenodo.20630895](https://doi.org/10.5281/zenodo.20630895)

---

## Key results

- **5-level nested structural hypothesis** proposed across 61 groups, 241 signs
- **14 of 15 statistical tests are implemented and reproducible** from this
  repo's dataset (T4 needs an external lunar ephemeris not included here).
  Running them gives **p ≈ 10⁻²⁰·⁹** combined — see the important caveat
  below and in `PROOF_TABLE.md`
- **3 tests survive Bonferroni** correction (n=14, α=0.0036) on their own,
  independent of the combined figure: T1, T3, T9
- **2 of the 15 originally published tests (T8, T10) come out not
  statistically significant** when recomputed from this dataset — see
  `PROOF_TABLE.md` → "Reconciliation notes"
- **11 celestial objects proposed**: Orion, Sirius, Scorpion, Sagittarius, Spica, Leo, Aquila, Pleiades, Venus, Jupiter, and more — pending independent iconographic review (see "What remains open")
- Additional claims from the paper — **94% of occurrences decoded**, **8
  zodiacal positions matching MUL.APIN tablets**, **43 grammatical rules** —
  are not computed by anything in this repository, so they could not be
  checked as part of this reproducibility pass. They're listed here for
  completeness, not as verified.

> ⚠️ **Read before citing:** the combined p-value above treats all tests as
> statistically independent, which they are not — several reuse the same
> signs (e.g. S02 appears in both T1 and T3). It should be read as an
> illustration that the pattern is unlikely to be pure chance, not as a
> formal joint significance level. Full detail in `PROOF_TABLE.md`.

---

## Reproduce in 5 minutes

```bash
git clone https://github.com/oliviergisclon/phaistos-disc-analysis
cd phaistos-disc-analysis
pip install scipy numpy pandas
python phaistos_analysis.py
```

See [REPRODUCE.md](REPRODUCE.md) for full instructions and expected outputs.

---

## Repository structure

```
phaistos-disc-analysis/
├── README.md                  ← This file
├── REPRODUCE.md               ← Step-by-step reproduction guide
├── PROOF_TABLE.md             ← All tests: hypothesis → method → result → reconciliation notes
├── phaistos_disc.csv          ← 61 groups, 241 signs (main dataset)
├── sign_identifications.csv   ← 27 identified signs with evidence
├── phaistos_analysis.py       ← Reproducible Python analysis (14 of 15 tests)
└── index.html                 ← Interactive disc visualization
```

---

## The 5-level architecture

| Level | Sign(s) | Function | p-value (this repo) |
|-------|---------|----------|---------|
| 1 | S02, S38 | Group delimiter, solar cardinals | 3.64 × 10⁻¹² (T1) / 5.20 × 10⁻³ (T2) |
| 2 | S12 | Period identifier | 1.10 × 10⁻⁵ (T3) |
| 3 | S27, S25 | Lunar month + quarter | not independently tested in this repo (T4 needs external data) |
| 4 | S07 | Lunar phase (moon visible) | not independently tested in this repo |
| 5 | Multiple | Astronomical content, incl. S26's documented winter/summer polysemy | varied — see caveat on S26 below |

---

## Dataset

`phaistos_disc.csv` — transcription following Godart (1994),
validated against Ridderstad (2010).

```
sha256sum phaistos_disc.csv
```

---

## What remains open

- **Astronomical dating**: 3 independent constraints identified, Stellarium calculation pending
- **Iconographic validation**: 4 sign identifications need Minoan specialist review
- **Sign S26 polysemy**: `sign_identifications.csv` documents S26 as read
  as *either* Sirius or Scorpion depending on the season — a single glyph
  taking on whichever meaning fits the surrounding test is a circularity
  risk and needs an independent justification, not just a note in the data
- **9 hapax signs**: uninterpretable without external comparative data
- **Linguistic layer**: possible but untestable without comparative corpus
- **Reconciling T2, T3, T8, T10, T12** against the originally published
  figures — see `PROOF_TABLE.md` for the specifics

---

## Citation

```bibtex
@misc{gisclon2026phaistos,
  author = {Gisclon, Olivier},
  title = {The Phaistos Disc as a Lunisolar Information System:
           Architecture, Grammar, and Statistical Demonstration},
  year = {2026},
  note = {HAL: hal-05652844, Zenodo: 10.5281/zenodo.20630895}
}
```

---

## License

Data and code: **CC BY 4.0** — Olivier Gisclon (2026)

You are free to share and adapt this work with attribution.

---

*The disc has been waiting to be read since 1908.*
