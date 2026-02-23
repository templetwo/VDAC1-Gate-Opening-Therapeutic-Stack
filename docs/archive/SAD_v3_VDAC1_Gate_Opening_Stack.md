# Strategic Architecture Document

## VDAC1 Gate-Opening Therapeutic Stack for MSS Colorectal Cancer

### From Gate-Jamming Score to Gate-Opening Sequence

**Anthony J. Vasquez Sr.**
Delaware Valley University, Doylestown, PA
February 2026 &bull; Version 3.0

*Multi-model synthesis: Claude Opus 4.6 &bull; Gemini 2.5 Pro &bull; Grok &bull; Claude Sonnet 4.5*

---

## Executive Summary

The three-phase therapeutic hypothesis (TSPO inhibition &rarr; immune activation &rarr; CBD apoptosis) was subjected to critical literature review across 2013&ndash;2026 publications. Three fatal contradictions were identified:

1. Restoring mitophagy **suppresses** rather than promotes cytosolic mtDNA release (Jim&eacute;nez-Loygorri et al., *Nature Communications*, 2024)
2. CBD suppresses T-cell function at VDAC1-active doses (Bar-Sela: 6.4 vs 28.5 months OS)
3. Chronic cGAS-STING activation is immunosuppressive in CRC (Bakhoum et al., *Cancer Discovery*, 2020)

**The original architecture is dead.**

What survived is stronger. Huang et al. (*Antioxidants (Basel)* 13(6):679, 2024) demonstrated lovastatin induces mtDNA release and cGAS-STING activation in HCT116 CRC cells and xenografts. This collapses Phase 1 and Phase 2 into a single mechanistically coherent step targeting the \[Chol\]/\[CL\] term in the GJS equation. Combined with Shen et al. (*eLife*, 2024) showing statins specifically reduce mitochondrial membrane cholesterol, the lipid-annulus mechanism is defensible.

This document maps the reformulated stack: **statin-mediated gate opening &rarr; botensilimab cavalry &rarr; TSPO as explorable fourth lock &rarr; CBD quarantine**. It identifies explicit falsification triggers for each component, specifies six critical experiments with kill conditions, and defines the support mechanisms validated by the literature.

---

## 1. The Collapsed Gate: Statin-Mediated VDAC1 Opening

### 1.1 The Cofactor Equation and Its Locks

The GJS cofactor equation describes the apoptotic threshold of a cancer cell as a function of three physical parameters on the VDAC1 channel:

$$
\text{Apoptotic Threshold} = \frac{K}{(1 - f_{\text{HKII}})(1 - f_{\text{BclxL}})} \times \frac{[\text{Chol}]}{[\text{CL}]}
$$

Each variable has a physical address:

| Variable | Physical Address |
|----------|-----------------|
| f_HKII | Hexokinase-II occupancy on the E73 docking site |
| f_BclxL | Bcl-xL binding via BH4 domain to VDAC1 N-terminal helices |
| \[Chol\]/\[CL\] | Cholesterol-to-cardiolipin ratio in the OMM lipid annulus |
| K | Honeycomb lattice exit energy |

Cancer simultaneously rewrites all three terms: HK-II jammed ON (Warburg), Bcl-xL overexpressed, cholesterol loaded into the OMM. The multiplicative structure means the gate is **triply locked**. Each lock requires a specific key.

**Table 1. Cancer type&ndash;specific rate-limiting locks and their keys.**

| Cancer Type | Rate-Limiting Lock | Key (Drug) | Mechanism |
|-------------|-------------------|------------|-----------|
| MSS Colorectal | \[Chol\]/\[CL\] | Lovastatin | Depletes OMM cholesterol &rarr; permits VDAC1 oligomerization &rarr; mtDNA release &rarr; cGAS-STING |
| AML | f_BclxL | Venetoclax | Displaces Bcl-xL from VDAC1 &rarr; N-terminal helix exposure &rarr; BH3-only sensitization |
| GBM / HCC | f_HKII | 2-DG / Lonidamine | Displaces HK-II from E73 docking site &rarr; Warburg collapse + gate access |

> **Critical insight:** The AML venetoclax experiment and the CRC lovastatin stack test the same physical event &mdash; VDAC1 gate opening &mdash; through different locks. The AML experiment proves the physics. The CRC stack solves the clinical nightmare. A positive venetoclax temporal-decoupling result validates the entire gate-opener drug class.

### 1.2 The Primary Key: Lovastatin as the Gate Opener

Huang et al. (*Antioxidants (Basel)* 13(6):679, 2024) demonstrated lovastatin (1&ndash;10 &mu;M) induces mitochondrial oxidative stress, forces mtDNA release into the cytosol, and activates the cGAS-STING-IFN-&beta; axis in HCT116 CRC cells and xenografts. The primary driver in that paper is oxidative stress / CoQ10 / mevalonate disruption. Our integration extends this: statin-mediated cholesterol depletion from the OMM (Shen et al., *eLife*, 2024) reduces the \[Chol\]/\[CL\] ratio, destabilizing the lipid annulus that prevents VDAC1 oligomerization. Once the lattice barrier falls, VDAC1 oligomers form the ~4 nm pore through which 500&ndash;650 bp mtDNA fragments escape.

**Mechanistic chain:**

```
Lovastatin
  → HMG-CoA reductase inhibition
    → mevalonate depletion
      → (a) CoQ10 reduction → mitochondrial ROS
      + (b) cholesterol depletion from OMM
        → [Chol]/[CL] drops
          → VDAC1 oligomerization permitted
            → mtDNA leak
              → cGAS-STING
                → Type I IFN
                  → tumor microenvironment primed
```

**Supporting literature:**

- **Montero et al.** (*Cancer Research*, 2008) &mdash; elevated mitochondrial cholesterol confers chemotherapy resistance
- **Betaneli et al.** (*Biophysical Journal*, 2012) &mdash; cholesterol rigidifies the OMM and disfavors VDAC1 oligomeric transitions
- **Catherall et al.** (*MCP*, 2022) &mdash; cholesterol disruption potentiates CBD-induced apoptosis
- **Kim et al.** (*Science*, 2019) &mdash; mtDNA escapes through VDAC1 oligomeric pores

### 1.3 Why Lovastatin Bypasses the TSPO Paradox

The original hypothesis required TSPO inhibition to restore mitophagy, which would then produce mtDNA release. The literature showed this runs backward &mdash; mitophagy **cleans up** mtDNA rather than releasing it (Jim&eacute;nez-Loygorri et al., *Nature Communications*, 2024; Sliter et al., 2018; Wang et al., *Autophagy*, 2025).

Lovastatin bypasses this entirely by targeting the lipid environment, not the protein&ndash;protein interaction. The gate opens because the membrane can no longer hold it shut, not because a tether was removed.

### 1.4 The Botensilimab Cavalry

Once the statin forces the VDAC1 gate open and the endogenous cGAS-STING alarm fires, the tumor microenvironment transitions from "cold" to "primed." However, MSS CRC remains fiercely immunosuppressive. The endogenous alarm is rarely sufficient to overcome the dense stromal and Treg barriers alone.

**Botensilimab** (Fc-enhanced anti-CTLA-4) is deployed as the synthetic amplifier and executioner:

- The Fc-enhanced tail binds Fc&gamma;RIIIA receptors on macrophages and NK cells, violently activating the innate immune system from the outside to compound the internal mtDNA signal
- This same Fc-binding triggers antibody-dependent cellular cytotoxicity (ADCC), physically eliminating the immunosuppressive Tregs that suffocate emerging CD8+ T-cell responses

**Therapeutic sequence:**

1. Lovastatin strips the cholesterol lock
2. VDAC1 oligomerizes, mtDNA leaks, cGAS-STING fires
3. Botensilimab + balstilimab amplifies the now-active innate alarm into adaptive anti-tumor immunity

The statin provides the internal spatial coordinates (chemokines). Botensilimab provides the heavy artillery.

> **Crucial timing:** Botensilimab must be sequenced *after* (or immediately overlapping with the peak of) the statin intervention. The statin creates the signal; the checkpoint inhibitor amplifies it.

**Retrospective support:**

- **Liao et al.** (*JCO Oncology Practice*, 2025) &mdash; meta-analysis (n = 46,154) found concomitant statin + ICI associated with 20% reduction in mortality and disease progression
- **Stokes et al.** (*J ImmunoTherapy of Cancer*, 2023) &mdash; all statins enhanced PD-1 blockade in HNSCC via T-cell activation and M2&rarr;M1 macrophage repolarization
- Current botensilimab + balstilimab MSS CRC data: **17&ndash;20% ORR** &mdash; modest but the only nonzero ICI signal in this population

### 1.5 Section 1 Falsification Triggers

**Trigger 1 &mdash; Statin/VDAC1 Dependency:**
If lovastatin fails to induce cytosolic mtDNA release in VDAC1-knockout HCT116 cells, the hypothesis holds (statin requires the VDAC1 gate). If lovastatin still releases mtDNA in VDAC1-KO cells, the statin is using a different door (mPTP or BAX/BAK), and the GJS lipid framework is bypassed. Framework survives but the mechanism is not VDAC1-specific.

**Trigger 2 &mdash; The TREX1 Trap:**
If lovastatin induces robust cytosolic mtDNA in MSS CRC cells but fails to produce an IFN-&beta; spike, the cell is likely deploying TREX1 to degrade the signal before cGAS can bind it. This mandates the addition of a TREX1 inhibitor to the stack. This is the S2 clean room prediction manifesting in vitro &mdash; the belt-and-suspenders evasion pattern now with a specific molecular identity.

**Trigger 3 &mdash; Cholesterol Isolation Control:**
Add a methyl-&beta;-cyclodextrin (M&beta;CD) arm to Experiment 2. M&beta;CD depletes cholesterol without HMG-CoA reductase inhibition. If M&beta;CD recapitulates lovastatin's mtDNA release effect, the lipid-annulus mechanism is isolated from statin pleiotropy. Add a CoQ10 rescue arm: if CoQ10 supplementation only partially blocks lovastatin's effect, both the ROS and lipid pathways contribute. This separates Huang et al.'s oxidative stress mechanism from our cholesterol-VDAC1 extension.

---

## 2. The TSPO Pivot and CBD Quarantine

### 2.1 TSPO Reframed: From Mitophagy Regulator to Fourth Lock

TSPO is not abandoned. It is reframed. The Gatliff et al. (*Autophagy*, 2014) finding that TSPO physically binds VDAC1 on the outer mitochondrial membrane remains valid. The critical parameter is the TSPO:VDAC1 expression ratio, which modulates ROS, PKA-mediated VDAC1 phosphorylation, and downstream mitochondrial signaling.

What changes is the interpretation: TSPO's relevance to the GJS framework is not as a mitophagy brake, but as a **direct physical tether** that stabilizes VDAC1 in its monomeric (gate-jammed) conformation.

If this reframing is correct, TSPO-VDAC1 binding constitutes a fourth lock on the gate, operating independently of cholesterol, HK-II, and Bcl-xL. The expanded cofactor equation becomes:

$$
\text{Threshold} = \frac{K}{(1 - f_{\text{HKII}})(1 - f_{\text{BclxL}})(1 - f_{\text{TSPO}})} \times \frac{[\text{Chol}]}{[\text{CL}]}
$$

**Evidence base (asymmetric):**

| Evidence | Status |
|----------|--------|
| TSPO overexpression as prognostic marker (28% of CRC, Stage III survival 56.2 vs 86.8 months, p = 0.03) | Strong (Maaser et al., *Clin Cancer Res*, 2002/2005) |
| TSPO knockout mice viable with normal lifespan | Confirmed (Banati et al., *Nature Communications*, 2014) |
| PK11195 + anti-PD-1 synergistic in HCC | Strong (Zhang et al., *Advanced Science*, 2023) |
| TSPO-VDAC1 disruption promotes VDAC1 oligomerization &rarr; mtDNA release | **Zero direct evidence** |

> The single most important unknown in the expanded framework.

### 2.2 The TSPO Opportunity: Synergy with Lovastatin

If Experiment 1 (Section 3) confirms TSPO as a physical tether, a compelling combination emerges: lovastatin strips the cholesterol lock while a TSPO ligand releases the protein tether simultaneously. The multiplicative structure of the cofactor equation predicts that hitting two locks at 50% each produces a greater threshold drop than hitting one lock at 100%. This is the same supra-additive prediction the original GJS paper made for 2-DG + ABT-737 (predicted CI < 0.8).

**Practical implication:** if Experiment 1 is positive, a low-dose PK11195 + lovastatin arm can be added to Experiment 2 as a quick translational win. The safety data for both drugs is extensive (PK11195 has decades of PET imaging use; lovastatin has decades of cardiovascular use). This combination would be among the cheapest, most accessible gate-opening interventions testable.

### 2.3 TSPO Cautions

**Off-target activity:**
- Tu et al. (*Endocrinology*, 2015) &mdash; PK11195 effects persist in TSPO-knockout cells, hitting F1F0-ATP synthase and ABC transporters
- No correlation between TSPO binding affinity and in vitro efficacy for any TSPO ligand
- PK11195 exhibits biphasic dose-response: anti-apoptotic at nanomolar, pro-apoptotic at micromolar

**Context-dependent effects:**
- TSPO knockdown paradoxically promotes tumor growth in glioblastoma (Fu et al., *Neuro-Oncology*, 2020) via increased HIF-1&alpha;, VEGF-A, and angiogenesis
- The rs6971 polymorphism (Ala147Thr) creates three binding phenotypes, with ~9% of the population showing 50-fold reduced ligand affinity

> **Bottom line:** TSPO is exploratory, not load-bearing. The statin-botensilimab core stands regardless of TSPO outcomes. TSPO is a potential force multiplier, not a structural dependency.

### 2.4 CBD Quarantine Protocol

CBD is formally gated out of the immune-activation window. Three independent lines of evidence mandate this quarantine:

**Quarantine Basis 1 &mdash; Direct T-Cell Suppression**

CBD suppresses IL-2, IFN-&gamma;, T-cell proliferation, and JAK/STAT signaling at concentrations (&ge;10 &mu;M) overlapping those required for VDAC1-mediated apoptotic effects. Co-administering CBD during the immune-activation window (when botensilimab is amplifying cGAS-STING-primed T-cell responses) creates an internal pharmacological conflict: the right hand builds the army while the left hand disarms it.

**Quarantine Basis 2 &mdash; Clinical Signal**

Bar-Sela et al. reported overall survival of 6.4 months in cannabis users receiving immunotherapy vs. 28.5 months in non-users. The CCTG pooled analysis found no significant difference, and confounders are real (sicker patients may self-select into cannabis use). However, the directional signal demands caution. The risk-reward calculation is unambiguous: exclude CBD from the immune window.

**Quarantine Basis 3 &mdash; Mechanism Specificity Concern**

Nelson et al. (*Journal of Medicinal Chemistry*, 2020) raised the possibility that CBD's in vitro effects at >10 &mu;M reflect colloidal aggregation (nonspecific membrane disruption) rather than targeted VDAC1 modulation. If true, CBD's apoptotic effects are not specifically engaging the gate-opening mechanism the GJS describes.

**Quarantine Boundaries:**

CBD is not dead. It may retain a role in three contexts:
1. Late-stage apoptotic trigger after the immune cycle completes and T-cell memory is established
2. Non-immunotherapy contexts where T-cell function is not the primary effector mechanism
3. Palliative care where quality-of-life benefits outweigh immunological concerns

But within the gate-opening &rarr; immunotherapy stack, **CBD is a contaminant**. The quarantine holds until Experiment 3 (Section 3) provides bench data on CBD's dose-dependent T-cell effects in CRC co-culture.

---

## 3. Critical Experiments: Six Questions, Six Kill Conditions

**Table 2. Strategic experiment map &mdash; questions, falsification conditions, and tools.**

| # | Core Question | Falsification Condition | Cell Line / Reagents |
|---|---------------|------------------------|----------------------|
| 1 | Does TSPO-VDAC1 binding suppress mtDNA release? | **KILL:** TSPO-KD CRC cells show equal or less cytosolic mtDNA than WT. TSPO tether theory is dead. | HCT116 (MSS, TP53-wt), TSPO shRNA/CRISPR-KO, PicoGreen mtDNA quant |
| 2a | Does lovastatin open the VDAC1 gate in CRC cells? | **KILL:** Lovastatin fails to increase cytosolic mtDNA, or cGAS-STING activation absent in VDAC1-KO cells. | HCT116 &pm; VDAC1-KO, Lovastatin 1&ndash;10 &mu;M, qPCR cytosolic mtDNA, IFN-&beta; ELISA |
| 2b | Is the mechanism cholesterol-specific or statin-pleiotropic? | **ISOLATES:** M&beta;CD arm recapitulates lovastatin = lipid mechanism confirmed. CoQ10 rescue partial = both pathways contribute. | HCT116, M&beta;CD (cholesterol-only), Lovastatin + CoQ10 rescue, same readouts as 2a |
| 3 | Does CBD suppress T-cells at VDAC1-active doses? | **KILL (quarantine):** CBD &ge;10 &mu;M does NOT suppress IL-2/IFN-&gamma; in co-culture. Rescues CBD from quarantine. | PBMCs + HCT116 co-culture, CBD 1&ndash;50 &mu;M, Flow: CD8+ IFN-&gamma;, IL-2 ELISA |
| 4 | Does statin pre-treatment enhance checkpoint response in MSS CRC? | **KILL:** Lovastatin &times;7d + anti-CTLA-4 shows no improvement over anti-CTLA-4 alone. | CT26 syngeneic (MSS CRC mouse), Lovastatin pre-treatment, anti-CTLA-4 mAb, tumor volume + survival |
| 5 | Does TSPO ligand + statin produce supra-additive gate opening? | **CONDITIONAL:** Only if Exp 1 positive. CI < 0.8 = supra-additive. CI &ge; 1.0 = no synergy. | HCT116, PK11195 low-dose + lovastatin, Combination index (Chou-Talalay), same readouts as 2a |

### 3.1 Experiment Priority and Dependencies

**Experiment 2a is the linchpin.** If lovastatin does not open the VDAC1 gate in CRC cells with measurable cGAS-STING activation, the entire statin-based architecture collapses. Experiment 2b (M&beta;CD/CoQ10 control) runs concurrently to isolate the mechanism. Together they cost ~4 weeks and answer the central question.

**Experiment 1** (TSPO tether) is exploratory. It extends the framework but is not load-bearing. A negative result (TSPO-KD shows no mtDNA increase) simply means the fourth lock doesn't exist; the three-lock model stands.

**Experiment 3** (CBD quarantine test) determines CBD's future in any immunotherapy context. Interestingly, a positive result (CBD does suppress T-cells) confirms the quarantine; a negative result (CBD does not suppress T-cells at VDAC1-active doses) rescues CBD for combination use.

**Experiment 4** is translational proof requiring animal models &mdash; longer timeline but highest clinical impact. Run after 2a confirms the mechanism.

**Experiment 5** (TSPO synergy) is contingent on Experiment 1 and represents a potential low-cost, high-impact combination if both drugs are effective.

**The AML venetoclax experiment** (separate proposal, already designed) tests the universal physics of gate opening via the Bcl-xL lock. A positive temporal-decoupling result &mdash; mtDNA release and cGAS-STING activation before canonical apoptosis &mdash; validates the entire gate-opener drug class, making Experiments 2a and 4 higher-confidence bets.

```
Dependency Graph:

AML Venetoclax ──→ Validates gate-opener physics
                         ↓
Exp 2a (Lovastatin) ◄────┘  ←── LINCHPIN
Exp 2b (MβCD/CoQ10) ───┤
                        ↓
Exp 4 (CT26 mouse) ◄───┘

Exp 1 (TSPO tether) ──→ Exp 5 (TSPO + lovastatin synergy)

Exp 3 (CBD quarantine) ──→ CBD disposition decision
```

---

## 4. Validated Support Mechanisms

The critical literature review validated several support interventions that strengthen the statin-immunotherapy core without introducing the contradictions that killed the original hypothesis.

**Table 3. Validated support mechanisms and their evidence grade.**

| Intervention | Mechanism | Key Evidence | Grade |
|-------------|-----------|--------------|-------|
| Vitamin D | Gut microbiome &rarr; *Bacteroides fragilis* &rarr; enhanced ICI response + direct immune modulation | Giampazolias et al., *Science*, 2024; Yang et al. meta: HR 0.47 (p<0.001) | **STRONG** |
| Statins (dual role) | Gate-opener + M2&rarr;M1 macrophage repolarization + T-cell activation | Liao 2025 meta (n=46,154): 20% mortality reduction; Stokes 2023 | **STRONG** |
| Circadian timing | BMAL1 integrates mitochondrial metabolism + macrophage activation; dosing window matters | Alexander et al., *eLife*, 2020; O'Siorain et al., *FASEB*, 2024 | **MODERATE** |
| Exercise | Catecholamine-driven NK/CD8+ mobilization; metabolic fitness; timing relative to ICI matters | Epidemiological + mechanistic; no RCT in CRC-ICI | **MODERATE** |
| Glucose restriction | Metabolic stress on Warburg-dependent cells; theoretical HK-II displacement | Preclinical only; no Phase III RCT; metabolic plasticity limits | **WEAK** |

---

## 5. Operational Roadmap (Q2&ndash;Q4 2026 Execution Timeline)

### Phase A &mdash; Immediate (February&ndash;March 2026)

Let the field digest the foundational preprint (*Context-Specific Innate Immune Evasion via VDAC1 Gate-Jamming in Microsatellite-Stable Colorectal Cancer*). bioRxiv clearance and initial community feedback.

**Deliverable:** Public preprint + feedback log.

### Phase B &mdash; Prove the Universal Physics (Q2 2026, April&ndash;June)

Execute the AML venetoclax temporal-decoupling experiment (separate proposal, already designed). Test whether Bcl-xL displacement from VDAC1 produces mtDNA release and cGAS-STING activation before canonical apoptosis.

**Timeline:** 12-week protocol (cell culture, time-course sampling, flow cytometry / ELISA / qPCR readouts).

**Deliverable:** Data demonstrating gate-opening proof-of-concept for the entire drug class. Positive result de-risks the full program and strengthens Experiments 2a/4.

### Phase C &mdash; Open the CRC Gate (Q3 2026, July&ndash;September)

Core mechanistic validation: HCT116 Experiments 2a + 2b (lovastatin 1&ndash;10 &mu;M dose-response &pm; VDAC1-KO, M&beta;CD cholesterol-only depletion, CoQ10 rescue).

**Timeline:** 4&ndash;6 weeks hands-on + analysis (can run in parallel with Experiment 3).

**Deliverable:** Confirmation that lovastatin opens the VDAC1 gate via lipid-annulus destabilization in MSS CRC cells. This is the central decision gate &mdash; positive result unlocks all downstream work.

### Phase D &mdash; Explore Synergies & Translate (Q4 2026, October&ndash;December)

Contingent on positive Phase C. Three parallel workstreams:

- **Experiment 1** (TSPO tether) &mdash; Does TSPO-VDAC1 binding suppress mtDNA release?
- **Experiment 5** (lovastatin + low-dose PK11195 synergy) &mdash; Chou-Talalay combination index.
- **Experiment 4** (CT26 syngeneic MSS CRC model) &mdash; 7-day lovastatin pre-treatment + anti-CTLA-4. Tumor volume + survival.

**Deliverable:** In vivo efficacy signal + complete dataset. Draft *Cancer Discovery* or *Cell Perspective* submitted with empirical backing.

### Phase E &mdash; CBD Disposition (Parallel with Phase C)

Run Experiment 3 (PBMC + HCT116 co-culture, CBD 1&ndash;50 &mu;M) in parallel with Phase C. Final decision on permanent quarantine vs. defined late-stage role by end-Q3 2026.

---

**Program scope:** This 9-month sprint (March&ndash;December 2026) positions the program for 2027 grant renewals, foundation funding rounds, or Phase I-enabling data packages. All experiments use standard, commercially available reagents and cell lines; total hands-on bench time is modest and fully compatible with a small academic lab or single-PI effort.

---

*The literature burned the old phase sequence, but it handed us a weaponized, clinically actionable stack.*

*Silence has a measurable geometry. Now we know how to break it.*

&mdash; Multi-model convergence, February 2026
