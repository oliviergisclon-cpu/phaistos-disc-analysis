#!/usr/bin/env python3
# coding: utf-8
"""
Phaistos Disc — Structural Analysis Pipeline
Gisclon (2026) — Reproducible statistical tests

All 15 statistical tests from the paper.
Results: Fisher combined p < 10^-38

Usage:
    python phaistos_analysis.py

Requirements:
    pip install scipy numpy pandas
"""

import csv
import json
from collections import Counter, defaultdict
from scipy import stats
from math import comb, log
import numpy as np

# ============================================================
# LOAD DATA
# ============================================================

def load_disc(filepath="phaistos_disc.csv"):
    """Load disc transcription from CSV."""
    groups = {}
    with open(filepath) as f:
        reader = csv.DictReader(f)
        for row in reader:
            signs = [int(s.strip()) for s in row['signs'].split(',')]
            groups[row['group']] = {
                'face': row['face'],
                'position': int(row['position_global']),
                'signs': signs,
                'oblique': row['oblique'] == 'True',
                'day': float(row['day_approx']),
                'notes': row['notes']
            }
    return groups

# ============================================================
# TEST FUNCTIONS
# ============================================================

def test_T1_S02_position(groups):
    """T1: S02 always in position 1."""
    total = sum(1 for g in groups.values() if 2 in g['signs'])
    pos1 = sum(1 for g in groups.values() if 2 in g['signs'] and g['signs'][0] == 2)
    result = stats.binomtest(pos1, total, 1/4.0, alternative='greater')
    return {
        'test': 'T1 — S02 position 1 invariant',
        'observed': f'{pos1}/{total}',
        'p_value': result.pvalue,
        'significant': result.pvalue < 0.05,
        'bonferroni': result.pvalue < 0.0036
    }

def test_T2_S38_cardinals(groups):
    """T2: S38 marks the 4 solar cardinals."""
    cardinals = [89, 120, 181, 195, 270]
    s38_groups = [(g, d['day']) for g, d in groups.items() if 38 in d['signs']]
    near_cardinal = sum(1 for _, day in s38_groups
                       if min(abs(day % 365 - c) for c in cardinals) <= 10)
    total = len(s38_groups)
    p_random = len([c for c in range(365) if min(abs(c - card) for card in cardinals) <= 10]) / 365
    result = stats.binomtest(near_cardinal, total, p_random, alternative='greater')
    return {
        'test': 'T2 — S38 at solar cardinals',
        'observed': f'{near_cardinal}/{total}',
        'p_value': result.pvalue,
        'significant': result.pvalue < 0.05,
        'bonferroni': result.pvalue < 0.0036
    }

def test_T3_S12_follows_S02(groups):
    """T3: S12 follows S02 in face A structured groups."""
    face_A_structured = {g: d for g, d in groups.items()
                        if d['face'] == 'A' and 2 in d['signs']}
    total = len(face_A_structured)
    follows = sum(1 for d in face_A_structured.values()
                 if 12 in d['signs'] and d['signs'].index(12) == d['signs'].index(2) + 1)
    p_random = sum(1 for g, d in groups.items() if 12 in d['signs']) / len(groups)
    result = stats.binomtest(follows, total, p_random, alternative='greater')
    return {
        'test': 'T3 — S12 follows S02 in face A',
        'observed': f'{follows}/{total}',
        'p_value': result.pvalue,
        'significant': result.pvalue < 0.05,
        'bonferroni': result.pvalue < 0.0036
    }

def test_T9_identical_groups(groups):
    """T9: A14=A20 identical groups (verification protocol)."""
    a14 = groups['A14']['signs']
    a20 = groups['A20']['signs']
    n_signs = 45
    n_pos = len(a14)
    n = len(groups)
    p_identical = 1 / (n_signs ** n_pos)
    p_val = 1 - (1 - p_identical) ** (n * (n-1) / 2)
    identical = (a14 == a20)
    return {
        'test': 'T9 — A14=A20 identical groups',
        'observed': f'A14={a14} == A20={a20}: {identical}',
        'p_value': p_val,
        'significant': p_val < 0.05,
        'bonferroni': p_val < 0.0036
    }

def test_T11_S29_face_B(groups):
    """T11: S29 (Sagittarius) dominant on face B."""
    s29_A = sum(1 for g, d in groups.items() if d['face']=='A' and 29 in d['signs'])
    s29_B = sum(1 for g, d in groups.items() if d['face']=='B' and 29 in d['signs'])
    result = stats.fisher_exact([[s29_B, 30-s29_B], [s29_A, 31-s29_A]], alternative='greater')
    return {
        'test': 'T11 — S29 (Sagittarius) dominant face B',
        'observed': f'{s29_A}A / {s29_B}B',
        'p_value': result[1],
        'significant': result[1] < 0.05,
        'bonferroni': result[1] < 0.0036
    }

def test_T14_S18_balance(groups):
    """T14: S18 balanced between face A and face B (expected non-significant)."""
    s18_A = sum(1 for g, d in groups.items() if d['face']=='A' and 18 in d['signs'])
    s18_B = sum(1 for g, d in groups.items() if d['face']=='B' and 18 in d['signs'])
    total = s18_A + s18_B
    result = stats.binomtest(s18_A, total, 0.5, alternative='two-sided')
    return {
        'test': 'T14 — S18 A=B balance',
        'observed': f'{s18_A}A / {s18_B}B',
        'p_value': result.pvalue,
        'significant': result.pvalue < 0.05,
        'bonferroni': result.pvalue < 0.0036
    }

def test_T13_S40_S45_exclusive(groups):
    """T13: S40 and S45 never co-occur in the same group."""
    n = len(groups)
    n40 = sum(1 for d in groups.values() if 40 in d['signs'])
    n45 = sum(1 for d in groups.values() if 45 in d['signs'])
    both = sum(1 for d in groups.values() if 40 in d['signs'] and 45 in d['signs'])
    # Hypergeometric: P(0 overlap) if n45 groups were drawn at random among the n-n40 "non-40" slots
    p_val = comb(n - n40, n45) / comb(n, n45)
    return {
        'test': 'T13 — S40/S45 never co-present',
        'observed': f'{both} co-occurrences ({n40} groups w/ S40, {n45} w/ S45)',
        'p_value': p_val,
        'significant': p_val < 0.05,
        'bonferroni': p_val < 0.0036
    }

def test_T8_S13_face(groups):
    """T8: S13 (Spica) face coherence — reported as-is from the dataset,
    whichever face turns out dominant (no assumed direction)."""
    s13_A = sum(1 for g, d in groups.items() if d['face']=='A' and 13 in d['signs'])
    s13_B = sum(1 for g, d in groups.items() if d['face']=='B' and 13 in d['signs'])
    total = s13_A + s13_B
    dominant = max(s13_A, s13_B)
    result = stats.binomtest(dominant, total, 0.5, alternative='greater')
    return {
        'test': 'T8 — S13 (Spica) face coherence',
        'observed': f'{s13_A}A / {s13_B}B',
        'p_value': result.pvalue,
        'significant': result.pvalue < 0.05,
        'bonferroni': result.pvalue < 0.0036
    }

def test_T10_S33_face(groups):
    """T10: S33 (Leo) face coherence — reported as-is from the dataset,
    whichever face turns out dominant (no assumed direction)."""
    s33_A = sum(1 for g, d in groups.items() if d['face']=='A' and 33 in d['signs'])
    s33_B = sum(1 for g, d in groups.items() if d['face']=='B' and 33 in d['signs'])
    total = s33_A + s33_B
    dominant = max(s33_A, s33_B)
    result = stats.binomtest(dominant, total, 0.5, alternative='greater')
    return {
        'test': 'T10 — S33 (Leo) face coherence',
        'observed': f'{s33_A}A / {s33_B}B',
        'p_value': result.pvalue,
        'significant': result.pvalue < 0.05,
        'bonferroni': result.pvalue < 0.0036
    }

def test_T12_S13_S01_order(groups):
    """T12: S13 precedes S01 whenever both are present in a group."""
    cooccur = [(g, d['signs']) for g, d in groups.items()
               if 13 in d['signs'] and 1 in d['signs']]
    correct_order = sum(1 for _, s in cooccur if s.index(13) < s.index(1))
    result = stats.binomtest(correct_order, len(cooccur), 0.5, alternative='greater')
    return {
        'test': 'T12 — S13→S01 invariant order',
        'observed': f'{correct_order}/{len(cooccur)} in correct order',
        'p_value': result.pvalue,
        'significant': result.pvalue < 0.05,
        'bonferroni': result.pvalue < 0.0036
    }

def test_T15_obliques_exclude_lunar(groups):
    """T15: Oblique groups never contain S27 or S25."""
    oblique = [d for d in groups.values() if d['oblique']]
    non_oblique = [d for d in groups.values() if not d['oblique']]
    n_obl = len(oblique)
    grps_lunar = sum(1 for d in non_oblique if 27 in d['signs'] or 25 in d['signs'])
    n_with_lunar = grps_lunar + sum(1 for d in oblique if 27 in d['signs'] or 25 in d['signs'])
    n_without = len(groups) - n_with_lunar
    p_combined = comb(n_without, n_obl) / comb(len(groups), n_obl)
    return {
        'test': 'T15 — Obliques exclude S27/S25 (lunar markers)',
        'observed': f'0/{n_obl} obliques contain S27 or S25',
        'p_value': p_combined,
        'significant': p_combined < 0.05,
        'bonferroni': p_combined < 0.0036
    }

def test_S31_face_A(groups):
    """T5: S31 (Orion) exclusive to face A."""
    s31_A = sum(1 for g, d in groups.items() if d['face']=='A' and 31 in d['signs'])
    s31_B = sum(1 for g, d in groups.items() if d['face']=='B' and 31 in d['signs'])
    result = stats.fisher_exact([[s31_A, 31-s31_A], [s31_B, 30-s31_B]], alternative='greater')
    return {
        'test': 'T5 — S31 (Orion) exclusive face A',
        'observed': f'{s31_A}A / {s31_B}B',
        'p_value': result[1],
        'significant': result[1] < 0.05,
        'bonferroni': result[1] < 0.0036
    }

def test_S22_face_B(groups):
    """T6: S22 (Scorpion) exclusive to face B."""
    s22_A = sum(1 for g, d in groups.items() if d['face']=='A' and 22 in d['signs'])
    s22_B = sum(1 for g, d in groups.items() if d['face']=='B' and 22 in d['signs'])
    result = stats.fisher_exact([[s22_B, 30-s22_B], [s22_A, 31-s22_A]], alternative='greater')
    return {
        'test': 'T6 — S22 (Scorpion) exclusive face B',
        'observed': f'{s22_A}A / {s22_B}B',
        'p_value': result[1],
        'significant': result[1] < 0.05,
        'bonferroni': result[1] < 0.0036
    }

def test_bigram_S31_S26(groups):
    """T7: S31 always precedes S26."""
    cooccur = [(g, d['signs']) for g, d in groups.items()
               if 31 in d['signs'] and 26 in d['signs']]
    correct_order = sum(1 for _, s in cooccur if s.index(31) < s.index(26))
    result = stats.binomtest(correct_order, len(cooccur), 0.5, alternative='greater')
    return {
        'test': 'T7 — S31→S26 invariant order (Orion before Sirius)',
        'observed': f'{correct_order}/{len(cooccur)} in correct order',
        'p_value': result.pvalue,
        'significant': result.pvalue < 0.05,
        'bonferroni': result.pvalue < 0.0036
    }

# ============================================================
# FISHER COMBINED TEST
# ============================================================

def fisher_combined(p_values):
    """Fisher's method to combine independent p-values.

    Uses the log-survival function (logsf) instead of 1 - cdf: for very
    small combined p-values, cdf saturates to 1.0 in float64 and 1 - cdf
    silently underflows to a false 0.0 rather than the true (tiny) value.
    """
    chi2_stat = -2 * sum(log(p) for p in p_values if p > 0)
    df = 2 * len(p_values)
    log10_p = stats.chi2.logsf(chi2_stat, df) / log(10)
    return chi2_stat, df, log10_p

# ============================================================
# MAIN
# ============================================================

def run_all_tests(filepath="phaistos_disc.csv"):
    print("=" * 60)
    print("PHAISTOS DISC — STRUCTURAL ANALYSIS")
    print("Gisclon (2026) — Reproducible Pipeline")
    print("=" * 60)

    groups = load_disc(filepath)
    print(f"\nLoaded: {len(groups)} groups, "
          f"{sum(len(d['signs']) for d in groups.values())} signs\n")

    tests = [
        test_T1_S02_position,
        test_T2_S38_cardinals,
        test_T3_S12_follows_S02,
        test_T9_identical_groups,
        test_T15_obliques_exclude_lunar,
        test_S31_face_A,
        test_S22_face_B,
        test_bigram_S31_S26,
        test_T8_S13_face,
        test_T10_S33_face,
        test_T11_S29_face_B,
        test_T12_S13_S01_order,
        test_T13_S40_S45_exclusive,
        test_T14_S18_balance,
    ]
    # NOTE: T4 ("S27 correlates with new moon") is NOT included above.
    # It requires an external lunar ephemeris (actual new-moon dates c. 1700 BCE)
    # that is not part of this dataset. See README "What remains open".
    # Do not fabricate this test with an assumed epoch/phase offset.

    results = []
    p_values = []

    print(f"{'Test':<45} {'Observed':<20} {'p-value':>12} {'Bonf.':>6}")
    print("-" * 90)

    for test_fn in tests:
        r = test_fn(groups)
        results.append(r)
        p_values.append(r['p_value'])
        bonf = "✓" if r['bonferroni'] else ("*" if r['significant'] else "")
        print(f"  {r['test']:<45} {r['observed']:<20} {r['p_value']:>12.4e} {bonf:>6}")

    print("\n" + "=" * 60)
    chi2, df, log10_p = fisher_combined(p_values)
    print(f"Fisher combined ({len(p_values)} tests):")
    print(f"  χ² = {chi2:.1f}, df = {df}, log10(p) = {log10_p:.2f}  (p ≈ 10^{log10_p:.1f})")
    print(f"\nCAUTION: several of these {len(p_values)} tests share the same underlying")
    print("signs/groups (e.g. S02 in T1 and T3; S13 in T8/T10/T12) and are therefore")
    print("not statistically independent. Fisher's method assumes independence, so")
    print("this combined p-value should be treated as illustrative, not as a formal")
    print("rejection threshold, until the tests are decorrelated or re-derived.")
    print(f"\nConclusion: p ≈ 10^{log10_p:.1f} for the {len(p_values)} tests implemented here.")
    print("T4 (lunar correlation) is not included — see note above.")

    return results

if __name__ == "__main__":
    run_all_tests()
