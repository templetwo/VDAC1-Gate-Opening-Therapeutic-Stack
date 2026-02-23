# Experiments

Six critical experiments with explicit kill conditions. Each addresses a single binary question. A framework that cannot be killed cannot be trusted.

**Reference:** SAD v4.0, Section 3 (pp. 9-14)

## Experiment Index

| # | Question | Kill Condition | Primary Readout | Priority | Status |
|---|----------|---------------|-----------------|----------|--------|
| 1 | Does TSPO-VDAC1 binding suppress mtDNA release? | No change in mtDNA release upon TSPO knockdown | qPCR (cytosolic mtDNA) | Exploratory (4th lock) | Designed |
| 2a | Does lovastatin deplete OMM cholesterol in HCT116? | <30% cholesterol reduction at 1-20 uM | Filipin staining + Amplex Red | **CRITICAL (linchpin)** | Designed |
| 2b | Does cholesterol depletion trigger VDAC1 oligomerization? | No oligomer increase despite >=30% chol depletion | EGS cross-linking + Western blot | **CRITICAL (linchpin)** | Designed |
| 3 | Does VDAC1 opening release mtDNA and activate cGAS-STING? | No cytosolic mtDNA or no IFN-B induction | ELISA (IFN-B, CXCL10) | High | Designed |
| 4 | Does statin pre-treatment enhance ICI response in vivo? | No tumor growth difference: statin+ICI vs ICI alone | Tumor volume + survival | High (translational) | Designed |
| 5 | Does dual-lock targeting show synergy? | CI > 1.2 (antagonistic) at all dose ratios | Chou-Talalay CI | Contingent on Exp 1 | Designed |
| 6 | Can CBD be rehabilitated? | CBD suppresses T cells at all VDAC1-active doses | Flow cytometry + viability | Low (quarantined) | Designed |

## Dependency Graph

```
Exp 2a (cholesterol depletion) ──→ Exp 2b (oligomerization) ──→ Exp 3 (mtDNA/cGAS-STING)
                                                                         │
                                                                         ▼
                                                                  Exp 4 (CT26 in vivo)
                                                                         │
                                                                         ▼
                                                              Journal submission

Exp 1 (TSPO tether) ──→ Exp 5 (lovastatin + PK11195 synergy)
    [independent]           [contingent on Exp 1 positive]

Exp 6 (CBD disposition) ──→ CBD quarantine decision
    [parallel w/ Phase C]      [requires Exps 1-3 positive]
```

**Experiment 2a/2b is the linchpin.** Budget: $3,010. Timeline: 4 weeks. Complete bench protocol in SAD v4.0, Section 3.2.

## Bench Protocol Summary (Exp 2a/2b)

| Step | Method | Key Reagent | Catalog # |
|------|--------|-------------|-----------|
| Cell culture | HCT116 in McCoy's 5A + 10% FBS | ATCC CCL-247 | ATCC CCL-247 |
| Lovastatin activation | NaOH hydrolysis of prodrug (lactone to acid) | Lovastatin powder | Sigma M2147 |
| Mito isolation | Differential centrifugation | Mito Isolation Kit | Thermo 89874 |
| Cholesterol quantification | Amplex Red assay on mito fractions | Amplex Red Kit | Invitrogen A12216 |
| Filipin staining | Fluorescence microscopy + MitoTracker colocalization | Filipin III | Sigma F4767 |
| Cross-linking | EGS (1 mM, 30 min, ice) | EGS | Thermo 21565 |
| Western blot | Non-reducing SDS-PAGE, anti-VDAC1 | Anti-VDAC1 Ab | Abcam ab15895 |

**Working concentrations:** 0, 1, 5, 10, 20 uM lovastatin | **Timepoints:** 24h, 48h | **Replicates:** n >= 3

**Success criteria:**
- Exp 2a: >=30% OMM cholesterol reduction at >=1 lovastatin concentration (p < 0.05, one-way ANOVA with Dunnett's)
- Exp 2b: >=2-fold VDAC1 oligomer/monomer ratio increase (Student's t-test, p < 0.05)

**Controls:** MbCD (5 mM, 1h) as positive control, vehicle (ethanol <0.1% v/v) as negative control

## Directory Convention

Each experiment gets its own subdirectory when initiated:

```
experiments/
  exp1_tspo_tether/
    protocol.md
    raw/
    analysis/
    results.md
  exp2a_lovastatin_cholesterol/
    protocol.md
    raw/
    analysis/
    results.md
  exp2b_vdac1_oligomerization/
    ...
```

## Execution Timeline

| Phase | Window | Experiments | Go/No-Go Gate |
|-------|--------|-------------|---------------|
| B | Q2 2026 (Apr-Jun) | **2a + 2b** (linchpin) + 1 (parallel) | Chol >=30% AND oligomer >=2x |
| C | Q3 2026 (Jul-Sep) | 3 (mtDNA/cGAS-STING) | Cytosolic mtDNA + IFN-B induction |
| D | Q4 2026 (Oct-Dec) | 4 (CT26 mouse) + 5 (if Exp 1 positive) | Tumor volume reduction |
| E | Parallel w/ C | 6 (CBD disposition) | Therapeutic window exists below T-cell suppression |
