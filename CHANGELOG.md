# Changelog

All notable changes to the Strategic Architecture Document (SAD) and repository.

## [4.1] - 2026-02-26

### Added
- Preprint DOI badge and link: [10.21203/rs.3.rs-8935902/v1](https://doi.org/10.21203/rs.3.rs-8935902/v1)
- Transcriptomic GJS (tGJS) bridging section in README connecting biophysical GJS to TCGA proxy score
- Preprint citation block (BibTeX) alongside existing SAD citation
- Link to companion analysis repo ([templetwo/vdac-pharmacology-atlas](https://github.com/templetwo/vdac-pharmacology-atlas))
- ORCID (0009-0000-6440-1506) added to CITATION.cff
- `preferred-citation` field in CITATION.cff pointing to the preprint
- Keywords: tGJS, innate immunity added to CITATION.cff
- Pillow dependency added to requirements.txt (used by gjs_simulation.py)

### Changed
- Status checklist updated with preprint milestone (Feb 26, 2026)
- Citation section now distinguishes preprint (transcriptomic evidence) from SAD (experimental architecture)

## [4.0] - 2026-02-23

### Added
- Complete bench protocol for Experiment 2a/2b (Section 3.2, pp. 10-14)
  - Lovastatin prodrug activation protocol (NaOH hydrolysis)
  - Mitochondrial isolation via differential centrifugation
  - Amplex Red cholesterol quantification on purified mito fractions
  - Filipin III staining with MitoTracker Red CMXRos colocalization
  - EGS cross-linking + non-reducing Western blot for VDAC1 oligomerization
  - Full reagent list with catalog numbers (14 items)
  - Estimated budget: $3,010
  - 4-week execution timeline
  - Statistical analysis plan (ANOVA, t-test, EC50 curve fit)
- Breast cancer (TNBC) added to Table 1 as fourth cancer type (dual-lock: HK-II + [Chol])
- Table 3 restructured: mechanistic evidence chain with 7 validated mechanisms
- Abbreviations and Acronyms glossary (50+ terms, 2 pages)
- Closing Statement section
- Publication-ready formatting: TOC, running headers, page numbers, embedded figures

### Changed
- Table 2 expanded with Primary Readout and Priority columns
- Phase B now explicitly references the bench protocol budget and timeline
- MbCD positive control logic formalized (distinguishes mechanism failure from delivery failure)

## [3.0] - 2026-02-22

### Added
- Experiments expanded from 4 to 6 (added Exp 5: dual-lock synergy, Exp 6: CBD rehabilitation)
- Complete reagent and cell line specifications in Table 2
- Chou-Talalay Combination Index analysis for dual-lock targeting (Figure 2e)
- Q2-Q4 2026 operational roadmap with 5 phases (A-E)
- Validated support mechanisms table with evidence grades (Vitamin D, circadian timing, exercise, glucose restriction)
- Experiment dependency graph with explicit go/no-go gates
- GJS simulation scripts (`gjs_simulation.py`, `gjs_chou_talalay_calculator.py`)
- Figure 1: Gate-Opening Therapeutic Sequence (3-panel SVG)
- Figure 2: GJS Simulation 4-panel composite
- Figure 2e: Chou-Talalay CI Analysis (3-panel)

### Changed
- AML venetoclax reframed as universal gate-opener physics validation (not CRC-specific)

## [2.0] - 2026-02-22

### Added
- TSPO cautions section: binding ambiguity, overexpression paradox, PK11195 selectivity
- Expanded experiment and reference tables
- Multi-model synthesis approach (Claude Opus 4.6, Gemini 2.5 Pro, Grok, Claude Sonnet 4.5)

### Changed
- TSPO repositioned from primary target to exploratory fourth lock with explicit risk flags

## [1.0] - 2026-02-22

### Added
- Gate-Jamming Score (GJS) cofactor equation
- Three-lock model: HK-II (f_HKII), Bcl-xL (f_BclxL), Cholesterol ([Chol]/[CL])
- TSPO reframed from mitophagy regulator to physical tether (fourth lock candidate)
- Lovastatin identified as primary gate opener for MSS CRC
- Botensilimab cavalry concept (Fc-enhanced anti-CTLA-4 + balstilimab)
- CBD formally quarantined from immune window (3 independent evidence lines)
- Four original experiments with explicit kill conditions
- Falsification of original three-phase hypothesis documented (3 fatal contradictions)

### Killed
- Original Phase 1: TSPO inhibition to restore mitophagy (mitophagy clears mtDNA, doesn't release it)
- Original Phase 2: CBD-mediated immune activation (CBD suppresses T-cells at active doses)
- Original Phase 3: Chronic cGAS-STING as therapeutic (chronic activation is immunosuppressive)
