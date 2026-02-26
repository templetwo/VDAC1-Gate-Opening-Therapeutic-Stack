# VDAC1 Gate-Opening Therapeutic Stack

**From Gate-Jamming Score to Gate-Opening Sequence for MSS Colorectal Cancer**

Anthony J. Vasquez Sr. | Delaware Valley University | February 2026 | v4.0

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)
[![Preprint](https://img.shields.io/badge/Preprint-10.21203%2Frs.3.rs--8935902%2Fv1-green)](https://doi.org/10.21203/rs.3.rs-8935902/v1)
[![DOI](https://img.shields.io/badge/DOI-10.17605%2FOSF.IO%2F4KNQR-blue)](https://doi.org/10.17605/OSF.IO/4KNQR)
[![OSF](https://img.shields.io/badge/OSF-yn3dw-lightblue)](https://osf.io/yn3dw)

**Preprint:** [Context-Specific Innate Immune Evasion via VDAC1 Gate-Jamming in Microsatellite-Stable Colorectal Cancer](https://doi.org/10.21203/rs.3.rs-8935902/v1) (Research Square, 2026) -- Transcriptomic validation across TCGA pan-cancer (n=10,071), COADREAD MSS/TP53-wt clean room (n=209), and IMvigor210 (n=348). Analysis code and data: [templetwo/vdac-pharmacology-atlas](https://github.com/templetwo/vdac-pharmacology-atlas)

**Companion work:** [CBD's Paradox at the Mitochondrial Gate](https://doi.org/10.17605/OSF.IO/NUXHV) (OSF Preprints, 2026) -- Multi-LLM convergence study of VDAC1 pharmacology (78 references)

---

## Overview

Microsatellite-stable (MSS) colorectal cancer is immune-invisible. Checkpoint inhibitors that work in MSI-H tumors fail completely here. This repository contains the **Strategic Architecture Document (SAD v4)** describing a reformulated therapeutic hypothesis targeting the VDAC1 channel on the outer mitochondrial membrane.

The original three-phase hypothesis (TSPO inhibition &rarr; immune activation &rarr; CBD apoptosis) was **killed by its own literature review**. Three fatal contradictions were identified. What survived is mechanistically cleaner and clinically actionable:

```
Lovastatin (cholesterol lock)
  → VDAC1 oligomerization → mtDNA release → cGAS-STING activation
    → Botensilimab amplifies innate → adaptive immune response
```

## The GJS Cofactor Equation

The apoptotic threshold of a cancer cell is governed by three physical locks on VDAC1:

$$
\text{Apoptotic Threshold} = \frac{K}{(1 - f_{\text{HKII}})(1 - f_{\text{BclxL}})} \times \frac{[\text{Chol}]}{[\text{CL}]}
$$

Cancer rewrites all three terms simultaneously. Each lock requires a specific key. In MSS CRC, the rate-limiting lock is the cholesterol-to-cardiolipin ratio in the OMM lipid annulus.

### Transcriptomic Proxy (tGJS)

The [preprint](https://doi.org/10.21203/rs.3.rs-8935902/v1) operationalizes the biophysical GJS as a transcriptomic score for TCGA analysis:

$$
\text{tGJS} = 0.40 \times \text{norm}(HK2) + 0.30 \times \text{norm}(BCL2L1) + 0.30 \times \text{norm}(TSPO)
$$

In the MSS/TP53-wildtype COADREAD clean room (n=209), high tGJS was inversely correlated with HAVCR2/TIM-3 ($\rho$ = &minus;0.349, p = 5 &times; 10<sup>&minus;6</sup>), CXCL10, and cGAS expression (all Bonferroni-significant). The key finding: high-tGJS MSS tumors suffer from **T cell absence, not T cell exhaustion** — the innate signal never fires.

## Key Findings

| Finding | Implication |
|---------|-------------|
| Lovastatin induces mtDNA release + cGAS-STING in HCT116 (Huang et al., 2024) | Collapses original Phase 1+2 into one mechanistic step |
| Statins deplete mitochondrial membrane cholesterol (Shen et al., 2024) | Lipid-annulus mechanism is defensible |
| CBD suppresses T-cells at VDAC1-active doses | CBD formally quarantined from immune window |
| TSPO physically tethers VDAC1 (Gatliff et al., 2014) | Reframed as explorable fourth lock, not load-bearing |
| Statin + ICI: 20% mortality reduction (Liao et al., 2025; n=46,154) | Retrospective support for combination |

## Repository Structure

```
docs/
  SAD_v4_VDAC1_Gate_Opening_Stack.pdf   # Current version (complete bench protocol)
  archive/
    SAD_v3_VDAC1_Gate_Opening_Stack.md  # v3: 6 experiments, reagent specs, timeline
    SAD_v3_VDAC1_Gate_Opening_Stack.docx
    SAD_v2_VDAC1_Gate_Opening_Stack.md  # v2: added TSPO cautions, expanded tables
    SAD_v2_VDAC1_Gate_Opening_Stack.docx
    SAD_v1_VDAC1_Gate_Opening_Stack.md  # v1: original 4-experiment architecture
    SAD_v1_VDAC1_Gate_Opening_Stack.docx
simulations/                             # GJS simulation & Chou-Talalay analysis
experiments/                             # Experiment protocols & results (future)
references/                              # Key citations & supplementary material
figures/                                 # Diagrams & visualizations
correspondence/                          # Faculty & collaboration letters
wiki/                                    # Documentation pages (11 topics)
```

## Critical Experiments

Six experiments with explicit kill conditions are specified in the SAD. The dependency structure:

```
Exp 2a (OMM cholesterol) ──→ Exp 2b (VDAC1 oligomerization)  ←── LINCHPIN
                                       ↓
                              Exp 3 (mtDNA → cGAS-STING)
                                       ↓
                              Exp 4 (CT26 mouse in vivo)

Exp 1 (TSPO tether) ──→ Exp 5 (lovastatin + PK11195 synergy)

Exp 6 (CBD disposition) ──→ CBD quarantine decision
```

**Experiment 2a/2b is the linchpin.** If lovastatin does not deplete OMM cholesterol and trigger VDAC1 oligomerization in HCT116 cells, the entire framework collapses. Four weeks. $3,010. Everything depends on this result.

## Execution Timeline (Q2&ndash;Q4 2026)

| Phase | Window | Goal | Deliverable |
|-------|--------|------|-------------|
| A | Feb&ndash;Mar 2026 | OSF registration + public GitHub release | DOI: 10.17605/OSF.IO/4KNQR |
| B | Apr&ndash;Jun 2026 | AML venetoclax temporal-decoupling (proves physics) | Gate-opener drug class validation |
| C | Jul&ndash;Sep 2026 | HCT116 lovastatin Exp 2a+2b (**LINCHPIN**) | Mechanistic confirmation |
| D | Oct&ndash;Dec 2026 | TSPO tether + synergy + CT26 mouse model | In vivo efficacy + journal submission |
| E | Parallel w/ C | CBD disposition (Exp 3 co-culture) | Quarantine decision |

9-month sprint. Standard reagents. Single-PI compatible.

## v4 Bench Protocol (Experiment 2a/2b)

SAD v4 includes a complete bench-ready protocol for the linchpin experiment:

- **Cell line:** HCT116 (MSS CRC, TP53-wt, ATCC CCL-247)
- **Lovastatin activation:** Prodrug conversion via NaOH hydrolysis, neutralization, filter sterilization
- **Readouts:** Amplex Red cholesterol quantification, filipin staining, DSS cross-linking + Western blot (VDAC1 oligomerization), qPCR cytosolic mtDNA, IFN-β ELISA
- **Controls:** VDAC1-KO, MβCD positive control, vehicle
- **Budget:** $3,010 | **Timeline:** 4 weeks
- **Statistical plan:** One-way ANOVA with Tukey post-hoc, α = 0.05, n ≥ 3

## Status

- [x] Literature review and falsification of original hypothesis
- [x] Reformulated therapeutic stack architecture (SAD v4)
- [x] Falsification triggers defined for each component
- [x] Six critical experiments designed with kill conditions
- [x] Complete experiment table with reagents and cell lines
- [x] Validated support mechanisms with evidence grades
- [x] Complete repository with indexes, wiki, 90-reference bibliography
- [x] OSF preregistration (DOI: 10.17605/OSF.IO/4KNQR)
- [x] Phase A: Public release (Feb 23, 2026)
- [x] Preprint posted to Research Square (Feb 26, 2026; DOI: 10.21203/rs.3.rs-8935902/v1)
- [ ] Phase B: AML venetoclax temporal-decoupling experiment
- [ ] Phase C: HCT116 lovastatin gate-opening experiments (2a + 2b)
- [ ] Phase D: TSPO exploration + CT26 mouse model
- [ ] Phase E: CBD disposition via co-culture experiment

## Citation

Cite the preprint:

```bibtex
@article{vasquez2026vdac1_preprint,
  title={Context-Specific Innate Immune Evasion via VDAC1 Gate-Jamming
         in Microsatellite-Stable Colorectal Cancer},
  author={Vasquez, Anthony J.},
  year={2026},
  doi={10.21203/rs.3.rs-8935902/v1},
  url={https://doi.org/10.21203/rs.3.rs-8935902/v1},
  journal={Research Square (Preprint)},
  institution={Delaware Valley University}
}
```

Cite this repository (experimental architecture):

```bibtex
@article{vasquez2026vdac1_sad,
  title={VDAC1 Gate-Opening Therapeutic Stack for MSS Colorectal Cancer:
         From Gate-Jamming Score to Gate-Opening Sequence},
  author={Vasquez, Anthony J., Sr.},
  year={2026},
  doi={10.17605/OSF.IO/4KNQR},
  url={https://osf.io/yn3dw},
  note={Strategic Architecture Document v4.0},
  institution={Delaware Valley University}
}
```

## License

This work is licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). You may share and adapt this material for non-commercial purposes with attribution.

---

*The literature burned the old phase sequence, but it handed us a weaponized, clinically actionable stack.*

*Silence has a measurable geometry. Now we know how to break it.*
