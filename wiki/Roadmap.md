# Operational Roadmap (Q2-Q4 2026)

9-month sprint. Standard reagents. Single-PI compatible.

---

## Phase A -- Immediate (February-March 2026)

**Goal:** Finalize SAD v4.0 and establish priority

**Activities:**
- Finalize SAD v4.0 with computational validation and complete Experiment 2a/2b protocol
- Submit to faculty advisor for review
- Post preprint to bioRxiv or OSF Preprints
- Invite community feedback

**Deliverable:** Public preprint + feedback log

**Status:** In progress

---

## Phase B -- Prove the Universal Physics (Q2 2026, April-June)

**Goal:** Execute the linchpin experiment

**Activities:**
- Execute Experiment 2a/2b -- the 4-week bench campaign
- HCT116 cells with lovastatin at 1-20 uM
- Budget: $3,010
- Readouts: Amplex Red cholesterol assay + filipin/MitoTracker colocalization (2a), EGS cross-linking + Western blot (2b)
- In parallel: begin Experiment 1 (TSPO-VDAC1 binding) using siRNA knockdown in HCT116 cells

**Go/No-Go Gate:** Cholesterol drops >=30% AND oligomerization increases >=2-fold
- If both pass: proceed to Phase C
- If either fails: framework requires fundamental revision
- MbCD positive control distinguishes "cholesterol doesn't open the gate" (MbCD also fails) from "lovastatin doesn't reach the OMM" (MbCD succeeds, lovastatin fails)

**Deliverable:** Gate-opener drug class validation (or falsification)

---

## Phase C -- Open the CRC Gate (Q3 2026, July-September)

**Goal:** Close the mechanistic chain

**Activities:**
- Execute Experiment 3: measure cytosolic mtDNA by qPCR following lovastatin treatment at concentrations validated in Phase B
- Confirm cGAS-STING activation by ELISA (IFN-B, CXCL10, CCL5)
- This closes the chain: statin -> cholesterol drops -> VDAC1 opens -> mtDNA escapes -> innate immunity fires
- Begin Experiment 4 planning: CT26 syngeneic mouse model (BALB/c)
  - IACUC approval (submit in Q2)
  - Colony establishment and pilot dosing studies
  - Lovastatin dosing in mice: 10-30 mg/kg oral gavage

**Deliverable:** Mechanistic confirmation (or kill)

---

## Phase D -- Explore Synergies & Translate (Q4 2026, October-December)

**Goal:** In vivo validation + synergy testing

**Activities (contingent on positive Phase C):**
- **Experiment 4 execution** -- CT26 mouse model
  - Arms: vehicle, lovastatin alone, anti-PD-1 alone, lovastatin + anti-PD-1
  - Endpoints: tumor volume, survival, intratumoral CD8+ density
- **Experiment 5** (if Exp 1 positive) -- Lovastatin + PK11195 combination
  - Fixed-ratio dose escalation
  - Chou-Talalay CI determination
  - Tests whether CI < 0.8 (true synergy) or CI = 1.0 (multiplicative independence)
- **Translational output**: If Exps 2-4 positive, prepare Cancer Discovery Perspective manuscript

**Deliverable:** In vivo efficacy data + journal submission

---

## Phase E -- CBD Disposition (Parallel with Phase C)

**Goal:** Determine CBD's future in the stack

**Trigger:** Only if Experiments 1-3 all succeed

**Activities:**
- Execute Experiment 6: CBD dose-response for VDAC1 modulation (filipin + oligomerization) and T-cell function (proliferation assay, IFN-gamma ELISA)
- Determine if a therapeutic window exists below T-cell suppression threshold (<=1 uM)
- If window exists: rehabilitation possible
- If thresholds overlap: CBD permanently quarantined from this stack

**Deliverable:** Quarantine decision (rehabilitate or permanent exclusion)

---

## Summary Timeline

| Phase | Window | Experiments | Gate |
|-------|--------|-------------|------|
| A | Feb-Mar 2026 | -- | Preprint posted |
| **B** | **Apr-Jun 2026** | **2a + 2b (LINCHPIN)** + 1 | **Chol >=30% AND oligomer >=2x** |
| C | Jul-Sep 2026 | 3 | Cytosolic mtDNA + IFN-B |
| D | Oct-Dec 2026 | 4 + 5 (conditional) | Tumor volume reduction |
| E | Parallel w/ C | 6 | Therapeutic window |
