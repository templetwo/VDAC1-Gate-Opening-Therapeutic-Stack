# The Four Locks on VDAC1

The VDAC1 channel exists in two functionally distinct states:
- **Monomeric (closed)**: Permits metabolite exchange but retains mtDNA
- **Oligomeric (open)**: Forms ~4 nm pore allowing 500-650 bp mtDNA fragments to escape

Cancer cells engage multiple "locks" simultaneously to keep the gate jammed shut.

---

## Lock 1: Hexokinase-II (f_HKII)

**Physical address:** Cytoplasmic barrel face, E73 docking site

**What cancer does:** HK-II jammed ON via the Warburg effect. HK-II physically occupies the VDAC1 barrel face, preventing the conformational rearrangement needed for oligomerization.

**Pharmacological key:** 2-deoxyglucose (2-DG), Lonidamine, 3-bromopyruvate (3-BrPA)

**Rate-limiting in:** HCC (hepatocellular carcinoma), where HK-II expression is extremely high

**Status in MSS CRC:** Elevated but not maximally engaged. Not the rate-limiting lock.

---

## Lock 2: Bcl-xL (f_BclxL)

**Physical address:** Extruded N-terminal helices, BH4 domain interaction

**What cancer does:** Bcl-xL overexpressed. Binds VDAC1 N-terminal helices and stabilizes the closed (monomeric) conformation, preventing oligomerization.

**Pharmacological key:** Venetoclax (BH3 mimetic) -- displaces Bcl-xL/Bcl-2 from VDAC1

**Rate-limiting in:** AML (acute myeloid leukemia) -- venetoclax is FDA-approved and works precisely through this lock

**Status in MSS CRC:** Elevated but not maximally engaged. Not the rate-limiting lock.

**Critical validation:** The AML venetoclax experiment tests the same physics as the CRC lovastatin experiment -- VDAC1 gate opening through a different lock. A positive result validates the entire gate-opener drug class.

---

## Lock 3: Cholesterol/Cardiolipin Ratio ([Chol]/[CL])

**Physical address:** Outer mitochondrial membrane lipid annulus surrounding VDAC1

**What cancer does:** Cholesterol loaded into the OMM. High [Chol]/[CL] rigidifies the membrane, preventing the conformational flexibility required for VDAC1 oligomeric transitions.

**Pharmacological key:** Lovastatin (HMG-CoA reductase inhibitor)

**Rate-limiting in:** **MSS CRC** -- consistently high OMM cholesterol loading across patient samples

**Why this is the target:** Genomic and proteomic data indicate that in MSS CRC, HK-II and Bcl-xL are elevated but not maximally engaged, while OMM cholesterol loading is consistently high. The cholesterol lock is the bottleneck.

**Evidence:**
- Montero et al. (2008): Elevated mitochondrial cholesterol confers chemotherapy resistance
- Huang et al. (2024): Lovastatin induces mtDNA release + cGAS-STING in HCT116
- Shen et al. (2024): Statins specifically reduce mitochondrial membrane cholesterol
- Betaneli et al. (2012): Cholesterol rigidifies OMM, disfavors oligomeric transitions

---

## Lock 4: TSPO Tether (f_TSPO) -- EXPLORATORY

**Physical address:** Five-transmembrane-helix protein (18 kDa) on the OMM, direct physical interaction with VDAC1

**What cancer does:** TSPO overexpressed in 28% of CRC cases. May stabilize VDAC1 in monomeric (closed) state through direct binding.

**Pharmacological key:** PK11195 (TSPO ligand/antagonist)

**Status:** Exploratory. Zero direct published evidence supports TSPO-VDAC1 complex disruption promoting VDAC1 oligomerization-mediated mtDNA release. This is the single most important unknown.

**Cautions:**
- **Binding ambiguity**: Whether TSPO binding stabilizes or destabilizes closed conformation is unresolved
- **Overexpression paradox**: 28% CRC overexpression could be compensatory, not causal
- **PK11195 selectivity**: Off-target effects at >10 uM, persist even in TSPO-KO (Tu et al., 2015)

**Experiment 1** tests this directly. **Experiment 5** (contingent on Exp 1 positive) tests lovastatin + PK11195 synergy.

---

## Dual-Lock Synergy

The multiplicative structure of the GJS equation predicts supra-additive threshold collapse when multiple locks are targeted simultaneously:

| Condition | Threshold | Fold Drop |
|-----------|-----------|-----------|
| Cancer baseline | 250.0 | -- |
| Lovastatin alone | 83.3 | 3.0x |
| PK11195 alone | 93.8 | 2.7x |
| **Dual lock (both)** | **31.3** | **8.0x** |

The 8x benefit arises from multiplicative pharmacology, not pharmacological synergy. Chou-Talalay baseline prediction: CI = 1.0 (Loewe additivity). Experiment 5 tests whether allosteric coupling produces true synergy (CI < 0.8).
