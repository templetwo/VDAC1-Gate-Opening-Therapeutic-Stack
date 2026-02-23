# Strategic Architecture Document

## VDAC1 Gate-Opening Therapeutic Stack for MSS Colorectal Cancer

### From Gate-Jamming Score to Gate-Opening Sequence

**Anthony J. Vasquez Sr.**
Delaware Valley University, Doylestown, PA
February 2026 &bull; Version 1.0

*Classification: PRIVATE WORKING DOCUMENT &mdash; NOT FOR PUBLICATION*

---

## Executive Summary

The three-phase therapeutic hypothesis (TSPO inhibition &rarr; immune activation &rarr; CBD apoptosis) was subjected to critical literature review across 2013&ndash;2026 publications. Three fatal contradictions were identified: (1) restoring mitophagy suppresses rather than promotes cytosolic mtDNA release; (2) CBD suppresses the T-cell function required for immunotherapy; (3) chronic cGAS-STING activation is immunosuppressive in CRC. **The original architecture is dead.**

What survived is stronger. The Huang et al. (2024) lovastatin finding provides a direct mechanism: statin &rarr; mitochondrial cholesterol depletion &rarr; VDAC1 oligomerization &rarr; mtDNA release &rarr; cGAS-STING activation, validated in CRC cells and xenografts. This collapses Phase 1 and Phase 2 into a single mechanistically coherent step, targeting the \[Chol\]/\[CL\] term in the Gate-Jamming Score equation.

This document maps the reformulated stack: **statin-mediated gate opening &rarr; botensilimab cavalry &rarr; CBD quarantine**. It identifies the exact falsification triggers for each component and specifies the four experiments that would validate or kill the framework.

---

## 1. The Collapsed Gate: Statin-Mediated VDAC1 Opening

### 1.1 The Cofactor Equation and Its Locks

The GJS cofactor equation describes the apoptotic threshold of a cancer cell as a function of three physical parameters on the VDAC1 channel:

$$
\text{Apoptotic Threshold} = \frac{K}{(1 - f_{\text{HKII}})(1 - f_{\text{BclxL}})} \times \frac{[\text{Chol}]}{[\text{CL}]}
$$

Each variable has a physical address on the protein:

| Variable | Physical Address |
|----------|-----------------|
| f_HKII | Hexokinase-II occupancy on the cytoplasmic barrel face (E73 docking site) |
| f_BclxL | Bcl-xL binding to extruded N-terminal helices (BH4 domain interaction) |
| \[Chol\]/\[CL\] | Cholesterol-to-cardiolipin ratio in the outer mitochondrial membrane lipid annulus |
| K | Honeycomb lattice exit energy |

Cancer simultaneously rewrites all three terms: HK-II jammed ON (Warburg effect), Bcl-xL overexpressed, cholesterol loaded into the OMM. The multiplicative structure means the gate is **triply locked**. Each lock requires a specific key.

**Table 1. Cancer type&ndash;specific rate-limiting locks and their keys.**

| Cancer Type | Rate-Limiting Lock | Key (Drug) | Mechanism |
|-------------|-------------------|------------|-----------|
| MSS Colorectal | \[Chol\]/\[CL\] | Lovastatin | Depletes OMM cholesterol &rarr; permits VDAC1 oligomerization |
| AML | f_BclxL | Venetoclax | Displaces Bcl-xL from VDAC1 &rarr; N-terminal helix exposure |
| GBM / HCC | f_HKII | 2-DG / Lonidamine | Displaces HK-II from E73 docking site |

> **Critical insight:** The venetoclax AML experiment and the lovastatin CRC stack are testing the same physical event &mdash; VDAC1 gate opening &mdash; through different locks. The AML experiment proves the physics. The CRC stack solves the clinical nightmare.

### 1.2 Lovastatin as the Primary Gate Opener

Huang et al. (*Pharmacological Research*, 2024) demonstrated that lovastatin induces mtDNA release and cGAS-STING activation in CRC cells, confirmed in vivo in xenograft models. The mechanism: statin-mediated cholesterol depletion from the outer mitochondrial membrane reduces the \[Chol\]/\[CL\] ratio, destabilizing the lipid annulus that prevents VDAC1 oligomerization. Once the lattice barrier falls, VDAC1 oligomers form, creating the ~4 nm pore through which 500&ndash;650 bp mtDNA fragments escape into the cytoplasm.

**Supporting evidence:**

- **Shen et al.** (*eLife*, 2024) &mdash; statins specifically reduce mitochondrial membrane cholesterol
- **Catherall et al.** (*MCP*, 2022) &mdash; cholesterol disruption potentiates CBD-induced apoptosis
- **Montero et al.** (*Cancer Research*, 2008) &mdash; elevated mitochondrial cholesterol confers chemotherapy resistance in HCC
- **Betaneli et al.** (*Biophysical Journal*, 2012) &mdash; cholesterol rigidifies the OMM and disfavors VDAC1 oligomeric transitions

### 1.3 Why Lovastatin Bypasses the TSPO Paradox

The original hypothesis required TSPO inhibition to restore mitophagy, which would then somehow produce mtDNA release. The literature showed this runs backward &mdash; mitophagy **cleans up** mtDNA rather than releasing it (Jim&eacute;nez-Loygorri et al., *Nature Communications*, 2024). Lovastatin bypasses this entirely by targeting the lipid environment, not the protein&ndash;protein interaction. The gate opens because the membrane can no longer hold it shut, not because a tether was removed.

---

## 2. The TSPO Pivot: From Mitophagy Regulator to Physical Tether

TSPO is not abandoned &mdash; it is reframed. The Gatliff et al. (2014) finding that TSPO physically binds VDAC1 and the TSPO:VDAC1 expression ratio modulates downstream signaling remains valid. What changes is the interpretation: TSPO's relevance to the GJS framework is not as a mitophagy brake, but as a **direct physical tether** that stabilizes VDAC1 in its monomeric (gate-jammed) state.

This reframing predicts that TSPO-VDAC1 binding may constitute a **fourth lock** on the gate &mdash; one that operates independently of the cholesterol, HK-II, and Bcl-xL mechanisms. If confirmed, the cofactor equation expands:

$$
\text{Threshold} = \frac{K}{(1 - f_{\text{HKII}})(1 - f_{\text{BclxL}})(1 - f_{\text{TSPO}})} \times \frac{[\text{Chol}]}{[\text{CL}]}
$$

However, **zero direct published evidence** supports TSPO-VDAC1 complex disruption promoting VDAC1 oligomerization-mediated mtDNA release. This is the single most important unknown in the reformulated architecture. Experiment 1 (Section 4) tests it directly.

**TSPO overexpression in CRC:**

- 28% of CRC cases strongly overexpress TSPO (Maaser et al., *Clinical Cancer Research*, 2002/2005)
- Stage III patients with high TSPO: mean survival 56.2 vs 86.8 months (p = 0.03)
- TSPO knockout mice are viable, fertile, with normal lifespan (Banati et al., *Nature Communications*, 2014)
- Zhang et al. (*Advanced Science*, 2023) &mdash; PK11195 + anti-PD-1 produced synergistic anti-tumor effects in HCC

The clinical safety and immunotherapy synergy data support TSPO as a legitimate therapeutic target, even as the mechanistic pathway has shifted.

---

## 3. The Sequence: Botensilimab Cavalry and CBD Quarantine

### 3.1 Botensilimab as the Immunotherapy Layer

Botensilimab (Fc-enhanced anti-CTLA-4) is the only checkpoint agent showing meaningful MSS CRC activity: **17&ndash;20% ORR** in combination with balstilimab (anti-PD-1). This is modest but nonzero &mdash; the first signal in a population where all prior ICI monotherapy failed. The gate-opening hypothesis predicts that statin pre-treatment could substantially increase this response rate by generating the mtDNA-cGAS-STING signal that gives botensilimab something to amplify.

**Therapeutic sequence:**

1. Lovastatin strips the cholesterol lock
2. VDAC1 oligomerizes, mtDNA leaks, cGAS-STING fires
3. Botensilimab + balstilimab amplifies the now-active innate alarm into adaptive anti-tumor immunity

The statin creates the signal. The checkpoint inhibitor amplifies it.

**Retrospective support:**

- **Liao et al.** (*JCO Oncology Practice*, 2025) &mdash; meta-analysis of 25 studies (n = 46,154) found concomitant statin + ICI associated with 20% reduction in mortality and disease progression
- **Stokes et al.** (*Journal for ImmunoTherapy of Cancer*, 2023) &mdash; all statins enhanced PD-1 blockade in HNSCC models via T-cell activation and M2&rarr;M1 macrophage repolarization

### 3.2 CBD Quarantine

CBD is formally gated out of the immune-activation window. Three lines of evidence mandate this:

1. **Direct T-cell suppression.** CBD suppresses IL-2, IFN-&gamma;, proliferation, and JAK/STAT signaling at concentrations overlapping VDAC1-mediated apoptotic doses (&ge;10 &mu;M). Using CBD for apoptosis while relying on T-cell immunity creates an internal pharmacological conflict.

2. **Clinical signal.** Bar-Sela et al. reported OS of 6.4 months in cannabis users on immunotherapy vs. 28.5 months in non-users. While the CCTG pooled analysis found no significant difference, the directional signal demands caution.

3. **Nonspecific mechanism concern.** Nelson et al. (*Journal of Medicinal Chemistry*, 2020) raised the possibility that CBD's in vitro effects reflect colloidal aggregation rather than targeted VDAC1 modulation.

CBD is not dead. It may have a role as a late-stage or palliative apoptotic trigger after the immune cycle completes, or in non-immunotherapy contexts. But within the gate-opening &rarr; immunotherapy stack, it is a contaminant. The quarantine holds until bench data proves otherwise.

---

## 4. Critical Experiments: Four Questions, Four Kill Conditions

**Table 2. Strategic experiment map &mdash; questions, falsification conditions, and tools.**

| # | Core Question | Falsification Condition | Cell Line / Reagents |
|---|---------------|------------------------|----------------------|
| 1 | Does TSPO-VDAC1 binding suppress mtDNA release? | **KILL IF:** TSPO-knockdown CRC cells show equal or less cytosolic mtDNA than wild-type. | HCT116 (MSS CRC, TP53-wt), TSPO shRNA / CRISPR-KO, PicoGreen mtDNA quantification |
| 2 | Does lovastatin open the VDAC1 gate in CRC cells? | **KILL IF:** Lovastatin fails to increase cytosolic mtDNA or cGAS-STING activation is absent in VDAC1-KO cells. | HCT116 &pm; VDAC1-KO, Lovastatin (1&ndash;10 &mu;M), qPCR cytosolic mtDNA, IFN-&beta; ELISA |
| 3 | Does CBD suppress T-cell function at VDAC1-active doses? | **KILL IF:** CBD &ge;10 &mu;M does not suppress IL-2 / IFN-&gamma; in co-culture. (Rescues CBD from quarantine.) | PBMCs + HCT116 co-culture, CBD 1&ndash;50 &mu;M, Flow cytometry (CD8+ IFN-&gamma;), IL-2 ELISA |
| 4 | Does statin pre-treatment enhance botensilimab response? | **KILL IF:** Lovastatin pre-treatment + anti-CTLA-4 shows no improvement over anti-CTLA-4 alone in MSS CRC mouse model. | CT26 syngeneic (MSS CRC mouse), Lovastatin &times;7d pre-treatment, Anti-CTLA-4 mAb, Tumor volume + survival |

**Experiment priority:** Experiment 2 is the linchpin. If lovastatin does not open the VDAC1 gate in CRC cells with measurable cGAS-STING activation, the entire statin-based architecture collapses. Experiment 1 (TSPO tether) is exploratory &mdash; it extends the framework but is not load-bearing. Experiment 3 determines CBD's future. Experiment 4 is the translational proof but requires animal models and longer timeline.

The AML venetoclax experiment (separate proposal, already designed) tests the universal physics of gate opening: does Bcl-xL displacement from VDAC1 produce mtDNA release and cGAS-STING activation before canonical apoptosis? A positive result validates the entire gate-opener class, making Experiments 2 and 4 higher-confidence bets.

---

## 5. Support Mechanisms: What the Literature Validated

The critical literature review validated several support interventions that strengthen the statin-immunotherapy core without introducing the contradictions that killed the original hypothesis.

**Table 3. Validated support mechanisms and their evidence grade.**

| Intervention | Mechanism | Key Evidence | Grade |
|-------------|-----------|--------------|-------|
| Vitamin D | Gut microbiome &rarr; *Bacteroides fragilis* &rarr; enhanced ICI response | Giampazolias et al., *Science*, 2024; HR 0.47 meta-analysis | **STRONG** |
| Circadian timing | BMAL1 integrates mitochondrial metabolism + macrophage activation | Alexander et al., *eLife*, 2020; O'Siorain et al., *FASEB*, 2024 | **MODERATE** |
| Glucose restriction | Metabolic stress on Warburg-dependent cells; HK-II displacement | Preclinical only; no Phase III RCT | **WEAK** |
| Exercise | Catecholamine-driven NK/CD8+ mobilization; metabolic fitness | Epidemiological + mechanistic; timing matters | **MODERATE** |

---

## Next Steps

1. Let the foundational preprint (*Context-Specific Innate Immune Evasion via VDAC1 Gate-Jamming in Microsatellite-Stable Colorectal Cancer*) clear bioRxiv screening. The field digests that first.
2. Run the AML venetoclax experiment to prove the universal gate-opening physics (Bcl-xL lock). This is the proof-of-concept for the entire drug class.
3. Design and submit Experiment 2 (lovastatin &rarr; VDAC1 gate opening in HCT116) as the CRC-specific validation. This can run concurrently with the AML work.
4. When bench data returns from Experiments 1&ndash;2, this SAD converts into a *Cancer Discovery* or *Cell Perspective* paper with empirical backing.

---

*The literature burned the old phase sequence, but it handed us a weaponized, clinically actionable stack.*

&mdash; Gemini 2.5 Pro, February 2026
