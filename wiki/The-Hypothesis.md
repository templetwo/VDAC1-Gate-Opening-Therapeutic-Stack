# The Hypothesis

## Central Thesis

Cancer cells simultaneously rewrite three physical parameters on the VDAC1 channel to jam the apoptotic gate shut and silence innate immune signaling. Each parameter is a "lock." Each lock requires a specific pharmacological "key." The rate-limiting lock varies by cancer type.

In MSS colorectal cancer, the rate-limiting lock is the **cholesterol-to-cardiolipin ratio** in the outer mitochondrial membrane lipid annulus.

## The Gate-Jamming Score (GJS) Equation

```
Apoptotic Threshold = K / [(1 - f_HKII)(1 - f_BclxL)] x [Chol]/[CL]
```

Expanded four-lock model (with TSPO, contingent on Experiment 1):

```
Threshold = K / [(1 - f_HKII)(1 - f_BclxL)(1 - f_TSPO)] x [Chol]/[CL]
```

### Variable Definitions

| Variable | Physical Address | What Cancer Does |
|----------|-----------------|-----------------|
| **f_HKII** | Hexokinase-II occupancy on VDAC1 cytoplasmic barrel face (E73 docking site) | Jammed ON (Warburg effect) |
| **f_BclxL** | Bcl-xL binding to extruded N-terminal helices (BH4 domain) | Overexpressed |
| **[Chol]/[CL]** | Cholesterol-to-cardiolipin molar ratio in OMM lipid annulus | Cholesterol loaded into OMM |
| **f_TSPO** | TSPO tether occupancy on VDAC1 (exploratory) | Overexpressed in 28% CRC |
| **K** | Honeycomb lattice exit energy (scaling constant) | -- |

### Key Property: Multiplicative Structure

The multiplicative denominator means a single highly-engaged lock can jam the gate even if others are partially open. This is why single-agent approaches fail -- and why targeting the rate-limiting lock produces disproportionate effect.

## Cancer Type-Specific Rate-Limiting Locks

| Cancer Type | Rate-Limiting Lock | Key (Drug) | Evidence Grade | Predicted Response |
|-------------|-------------------|------------|---------------|-------------------|
| **MSS CRC** | [Chol]/[CL] | Lovastatin (HMG-CoA inh.) | Strong (meta-analysis) | Gate opens -> mtDNA leak |
| **AML** | Bcl-xL / Bcl-2 | Venetoclax (BH3 mimetic) | Strong (FDA approved) | Lock 2 removed |
| **HCC** | HK-II | Lonidamine / 3-BrPA | Moderate (preclinical) | Lock 1 removed |
| **Breast (TNBC)** | Dual: HK-II + [Chol] | Statin + metabolic inh. | Emerging | Dual-key needed |

## What the Original Hypothesis Got Wrong

The original three-phase hypothesis (TSPO inhibition -> immune activation -> CBD apoptosis) was killed by three fatal contradictions:

1. **Mitophagy paradox**: Restoring mitophagy via TSPO inhibition **cleans up** mtDNA rather than releasing it (Jimenez-Loygorri et al., 2024)
2. **CBD immunosuppression**: CBD suppresses T-cell function at concentrations overlapping VDAC1-active doses, creating an internal pharmacological conflict
3. **Chronic cGAS-STING**: Chronic activation is immunosuppressive in CRC (Bakhoum et al., 2020)

Lovastatin bypasses all three by targeting the lipid environment directly, not protein-protein interactions.
