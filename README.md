# VDAC1 Gate-Opening Therapeutic Stack

**From Gate-Jamming Score to Gate-Opening Sequence for MSS Colorectal Cancer**

Anthony J. Vasquez Sr. | Delaware Valley University | February 2026

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

---

## Overview

Microsatellite-stable (MSS) colorectal cancer is immune-invisible. Checkpoint inhibitors that work in MSI-H tumors fail completely here. This repository contains the **Strategic Architecture Document (SAD v2)** describing a reformulated therapeutic hypothesis targeting the VDAC1 channel on the outer mitochondrial membrane.

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
  SAD_v2_VDAC1_Gate_Opening_Stack.md    # Full document (markdown)
  SAD_v2_VDAC1_Gate_Opening_Stack.docx  # Original document
experiments/                             # Experiment protocols & results (future)
references/                              # Key citations & supplementary material
figures/                                 # Diagrams & visualizations
```

## Critical Experiments

Six experiments with explicit kill conditions are specified in the SAD. The dependency structure:

```
AML Venetoclax ──→ Validates gate-opener physics
                         ↓
Exp 2a (Lovastatin) ◄────┘  ←── LINCHPIN
Exp 2b (MβCD/CoQ10) ───┤
                        ↓
Exp 4 (CT26 mouse) ◄───┘

Exp 1 (TSPO tether) ──→ Exp 5 (TSPO + lovastatin synergy)

Exp 3 (CBD quarantine) ──→ CBD disposition decision
```

**Experiment 2a is the linchpin.** If lovastatin does not open the VDAC1 gate in CRC cells with measurable cGAS-STING activation, the statin-based architecture collapses. Four weeks. Everything depends on this result.

## Status

- [x] Literature review and falsification of original hypothesis
- [x] Reformulated therapeutic stack architecture (SAD v2)
- [x] Falsification triggers defined for each component
- [x] Six critical experiments designed with kill conditions
- [ ] Phase A: Foundational preprint on bioRxiv
- [ ] Phase B: AML venetoclax temporal-decoupling experiment
- [ ] Phase C: HCT116 lovastatin gate-opening experiments (2a + 2b)
- [ ] Phase D: TSPO exploration + CT26 mouse model
- [ ] Phase E: CBD disposition via co-culture experiment

## Citation

```bibtex
@article{vasquez2026vdac1,
  title={VDAC1 Gate-Opening Therapeutic Stack for MSS Colorectal Cancer:
         From Gate-Jamming Score to Gate-Opening Sequence},
  author={Vasquez, Anthony J., Sr.},
  year={2026},
  note={Strategic Architecture Document v2.0},
  institution={Delaware Valley University}
}
```

## License

This work is licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). You may share and adapt this material for non-commercial purposes with attribution.

---

*The literature burned the old phase sequence, but it handed us a weaponized, clinically actionable stack.*

*Silence has a measurable geometry. Now we know how to break it.*
