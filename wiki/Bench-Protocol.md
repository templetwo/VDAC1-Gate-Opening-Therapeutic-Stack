# Bench Protocol: Experiment 2a/2b

Complete operational protocol for the linchpin experiment. Written at a level of detail sufficient for a trained technician to execute without additional guidance.

**Reference:** SAD v4.0, Section 3.2 (pp. 10-14)

---

## Overview

- **Experiment 2a**: Does lovastatin deplete OMM cholesterol in HCT116?
- **Experiment 2b**: Does cholesterol depletion trigger VDAC1 oligomerization?
- **Budget**: $3,010
- **Timeline**: 4 weeks
- **Cell line**: HCT116 (ATCC CCL-247), human MSS colorectal carcinoma, microsatellite-stable

## Cell Culture

- **Medium**: McCoy's 5A Modified Medium (ATCC 30-2007) + 10% FBS (heat-inactivated) + 100 U/mL penicillin + 100 ug/mL streptomycin
- **Conditions**: 37C, 5% CO2, humidified incubator
- **Passage**: Subculture at 70-80% confluency using 0.25% trypsin-EDTA. Do not exceed passage 25 from ATCC stock
- **Mycoplasma**: Verify mycoplasma-free status before experiments (MycoAlert Plus kit, Lonza LT07-710)

## Lovastatin Preparation

Lovastatin (Sigma-Aldrich M2147, powder) must be **activated** before use. The prodrug (lactone) form is biologically inactive; the open acid (hydroxy acid) form is the active HMG-CoA reductase inhibitor.

**Activation protocol:**
1. Dissolve 10 mg lovastatin in 250 uL ethanol
2. Add 375 uL of 0.1 N NaOH
3. Heat at 50C for 2 hours
4. Neutralize to pH 7.4 with HCl
5. Bring to 1 mL with sterile PBS
6. Filter-sterilize (0.22 um)
7. Stock concentration: ~25 mM
8. Aliquot and store at -20C. Stable for 3 months.

**Working concentrations:** 0, 1, 5, 10, 20 uM in complete medium (1-20 uM spans from below therapeutic plasma level to maximum tolerated in vitro)

## Experiment 2a: OMM Cholesterol Measurement

**Design:** HCT116 treated with lovastatin (0, 1, 5, 10, 20 uM) for 24 and 48 hours. Three biological replicates per condition. Two independent readouts.

### Readout 1: Amplex Red Cholesterol Assay (Quantitative)

**Mitochondrial isolation:**
1. Seed 2x10^6 cells per 10 cm dish (15 dishes per timepoint, 3 per concentration)
2. Treat with lovastatin at indicated concentrations for 24 or 48 hours
3. Harvest by trypsinization, wash 2x in ice-cold PBS
4. Isolate mitochondria using Mitochondria Isolation Kit for Cultured Cells (Thermo Fisher 89874) per manufacturer protocol
5. Confirm purity by Western blot: VDAC1 (mito marker), GAPDH (cytosolic, should be absent), Calnexin (ER, should be absent)

**Cholesterol quantification:**
1. Resuspend purified mitochondrial pellets in 200 uL of reaction buffer
2. Measure cholesterol using Amplex Red Cholesterol Assay Kit (Invitrogen A12216) per manufacturer protocol
3. Normalize to total mitochondrial protein (BCA assay, Pierce 23225)
4. Express as ug cholesterol per mg mitochondrial protein

### Readout 2: Filipin Staining (Confirmatory/Visual)

1. Seed cells on glass coverslips in 12-well plates
2. After lovastatin treatment, fix with 4% paraformaldehyde (15 min, RT)
3. Stain with filipin III (50 ug/mL in PBS, 2 hours, RT, protected from light)
4. Co-stain with MitoTracker Red CMXRos (100 nM, 30 min before fixation) for mitochondrial colocalization
5. Image on fluorescence microscope (UV excitation for filipin, 579/599 nm for MitoTracker)
6. Quantify colocalized fluorescence intensity using ImageJ/FIJI with Coloc2 plugin

**Success criterion (2a):** >=30% reduction in OMM cholesterol (normalized to mitochondrial protein) at >=1 lovastatin concentration vs vehicle control, p < 0.05 by one-way ANOVA with Dunnett's post-hoc test.

**Kill condition (2a):** <30% cholesterol reduction at all concentrations including 20 uM at both timepoints.

## Experiment 2b: VDAC1 Oligomerization

**Design:** Same lovastatin-treated cells. VDAC1 oligomeric state assessed by chemical cross-linking + SDS-PAGE + Western blot.

### Cross-linking Protocol

1. Following lovastatin treatment, wash cells 2x with ice-cold PBS
2. Incubate with 1 mM EGS (ethylene glycol bis-succinimidyl succinate, Thermo Fisher 21565) in PBS for 30 minutes on ice
3. Quench with 50 mM Tris-HCl pH 7.5 for 15 minutes
4. Lyse in RIPA buffer with protease inhibitors (Roche 04693159001)
5. Spin 14,000 x g, 15 min, 4C; collect supernatant
6. Determine protein concentration (BCA assay)

### Western Blot Protocol

1. Load 30 ug total protein per lane on 4-12% Bis-Tris gradient gel (NuPAGE, Invitrogen NP0322)
2. Run **non-reducing** (no B-mercaptoethanol) to preserve cross-links
3. Transfer to PVDF membrane (0.45 um, Immobilon-P)
4. Block 5% non-fat milk in TBS-T, 1 hour, RT
5. Primary antibody: anti-VDAC1 (Abcam ab15895, 1:1000, overnight at 4C)
6. Secondary antibody: HRP-conjugated anti-rabbit IgG (1:5000, 1 hour, RT)
7. Detect with ECL substrate (Pierce 32106)
8. Quantify bands by densitometry (ImageJ): calculate oligomer/monomer ratio

**Expected bands:** Monomers ~32 kDa; dimers ~64 kDa; tetramers/higher oligomers ~130 kDa and above

### Controls

- **Positive control:** MbCD (methyl-beta-cyclodextrin, 5 mM, 1 hour) as known cholesterol-depleting agent
  - If MbCD induces oligomerization but lovastatin does not: mechanism valid, drug delivery needs revision
  - If MbCD also fails: cholesterol depletion may not open the gate in this cell line
- **Negative control:** Vehicle (ethanol, <0.1% v/v) and untreated cells

**Success criterion (2b):** >=2-fold increase in VDAC1 oligomer/monomer ratio at >=1 lovastatin concentration where Exp 2a showed >=30% cholesterol depletion. Student's t-test, p < 0.05.

**Kill condition (2b):** No significant increase in oligomerization despite confirmed cholesterol depletion (>=30%).

## Reagent List and Budget

| Item | Catalog # | Qty | Est. Cost |
|------|-----------|-----|-----------|
| HCT116 cells | ATCC CCL-247 | 1 vial | $450 |
| Lovastatin | Sigma M2147 | 25 mg | $65 |
| McCoy's 5A + FBS + P/S | ATCC 30-2007 | 12 bottles | $350 |
| Mito Isolation Kit | Thermo 89874 | 1 kit | $285 |
| Amplex Red Cholesterol Kit | Invitrogen A12216 | 1 kit | $325 |
| Filipin III | Sigma F4767 | 5 mg | $75 |
| MitoTracker Red CMXRos | Invitrogen M7512 | 20 x 50 ug | $290 |
| EGS cross-linker | Thermo 21565 | 50 mg | $95 |
| Anti-VDAC1 antibody | Abcam ab15895 | 100 uL | $350 |
| NuPAGE gels + reagents | Invitrogen NP0322 | 10 gels | $350 |
| BCA assay kit | Pierce 23225 | 1 kit | $120 |
| MbCD (positive ctrl) | Sigma C4555 | 1 g | $55 |
| Consumables (tips, plates, etc.) | -- | -- | $200 |
| **TOTAL** | | | **$3,010** |

## Timeline

| Week | Activities |
|------|-----------|
| 1 | Cell culture setup, lovastatin activation, pilot filipin staining to verify method |
| 2 | Full Exp 2a: 24h and 48h lovastatin treatments, mitochondrial isolation, Amplex Red cholesterol assay |
| 3 | Full Exp 2b: cross-linking, Western blots, positive control (MbCD) |
| 4 | Replicate experiments (n=3 biological replicates), data analysis, statistical testing, figure preparation |

## Statistical Analysis Plan

- All data expressed as mean +/- SEM from n=3 independent biological replicates
- Cholesterol measurements: one-way ANOVA with Dunnett's post-hoc test (each concentration vs vehicle control)
- Oligomer/monomer ratios: Student's t-test (treated vs vehicle)
- Dose-response analysis: four-parameter logistic curve fit to determine EC50 for cholesterol depletion
- Significance threshold: p < 0.05 throughout
- All analysis in GraphPad Prism 10 or R (version 4.3+)
