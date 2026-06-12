# Phaistos Disc — Structural Analysis Pack

**The first formally demonstrated reading of the Phaistos Disc (1700 BCE)**

> *"Group A09 = [Orion, Sirius, Venus]: Orion visible. Sirius present. Venus on the horizon.
> Day 61 ≈ December 5, before dawn, from Phaistos (35°N), ~1700 BCE."*

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

- **5-level nested architecture** demonstrated across 61 groups, 241 signs
- **15 statistical tests** — Fisher combined: χ² = 223.4, **p < 10⁻³⁸**
- **4 tests survive Bonferroni** correction (n=15, α=0.0036)
- **94% of occurrences** decoded in nature and function
- **11 celestial objects** identified: Orion, Sirius, Scorpion, Sagittarius, Spica, Leo, Aquila, Pleiades, Venus, Jupiter, and more
- **8 zodiacal positions** correspond directly to MUL.APIN tablets in the same order
- **43 grammatical rules** formalized (position, order, regime, intensity, absence, formula)

---

## Reproduce in 5 minutes

```bash
git clone https://github.com/oliviergisclon/phaistos-disc-analysis
cd phaistos-disc-analysis
pip install scipy numpy pandas
python scripts/phaistos_analysis.py
```

See [REPRODUCE.md](REPRODUCE.md) for full instructions and expected outputs.

---

## Repository structure

```
phaistos-disc-analysis/
├── README.md              ← This file
├── REPRODUCE.md           ← Step-by-step reproduction guide
├── PROOF_TABLE.md         ← All 15 tests: hypothesis → method → result
├── data/
│   ├── phaistos_disc.csv          ← 61 groups, 241 signs (main dataset)
│   └── sign_identifications.csv   ← 27 identified signs with evidence
├── scripts/
│   └── phaistos_analysis.py       ← Reproducible Python analysis (all tests)
└── web/
    └── index.html                 ← Interactive disc visualization
```

---

## The 5-level architecture

| Level | Sign(s) | Function | p-value |
|-------|---------|----------|---------|
| 1 | S02, S38 | Group delimiter, solar cardinals | < 10⁻⁶ |
| 2 | S12 | Period identifier | 1.40 × 10⁻¹⁴ |
| 3 | S27, S25 | Lunar month + quarter | 0.022 |
| 4 | S07 | Lunar phase (moon visible) | 0.029 |
| 5 | Multiple | Astronomical content | varied |

---

## Dataset

`data/phaistos_disc.csv` — transcription following Godart (1994),
validated against Ridderstad (2010).

```
sha256sum data/phaistos_disc.csv
```

---

## What remains open

- **Astronomical dating**: 3 independent constraints identified, Stellarium calculation pending
- **Iconographic validation**: 4 sign identifications need Minoan specialist review
- **9 hapax signs**: uninterpretable without external comparative data
- **Linguistic layer**: possible but untestable without comparative corpus

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
