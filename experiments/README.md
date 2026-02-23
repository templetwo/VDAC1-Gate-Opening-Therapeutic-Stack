# Experiments

This directory will contain protocols, raw data, and analysis for the six critical experiments defined in the SAD v2.

## Experiment Index

| # | Name | Status | Priority |
|---|------|--------|----------|
| 1 | TSPO-VDAC1 tether test | Designed | Exploratory |
| 2a | Lovastatin gate opening (HCT116) | Designed | **LINCHPIN** |
| 2b | Cholesterol isolation control (MbCD/CoQ10) | Designed | Co-runs with 2a |
| 3 | CBD T-cell suppression co-culture | Designed | Independent |
| 4 | CT26 mouse lovastatin + botensilimab | Designed | Post-2a |
| 5 | PK11195 + lovastatin synergy | Designed | Contingent on Exp 1 |

## Directory Convention

Each experiment gets its own subdirectory when initiated:

```
experiments/
  exp1_tspo_tether/
    protocol.md
    raw/
    analysis/
    results.md
  exp2a_lovastatin_gate/
    ...
```
