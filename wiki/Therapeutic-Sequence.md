# The Therapeutic Sequence

## Three Phases, One Mechanistic Chain

### Phase 1: Lovastatin Opens the Gate

Lovastatin inhibits HMG-CoA reductase, producing two mechanistically distinct effects on VDAC1:

**Pathway A -- Cholesterol depletion:**
```
Mevalonate inhibition -> cholesterol biosynthesis drops -> OMM cholesterol drops
  -> [Chol]/[CL] ratio decreases -> membrane fluidity increases
    -> VDAC1 gains conformational freedom -> oligomeric pore forms (~4 nm)
      -> 500-650 bp mtDNA fragments escape into cytosol
```

**Pathway B -- CoQ10 depletion (amplifier):**
```
Mevalonate inhibition -> CoQ10 biosynthesis drops
  -> Complex III electron transfer impaired -> mitochondrial ROS increases
    -> cardiolipin oxidation -> further membrane destabilization
      -> amplifies Pathway A
```

This dual mechanism explains why statins show stronger anti-tumor effects than other cholesterol-lowering approaches.

### Phase 2: cGAS-STING Fires

Cytosolic mtDNA is detected by cyclic GMP-AMP synthase (cGAS), which produces cyclic GMP-AMP (cGAMP). cGAMP activates STING (stimulator of interferon genes), triggering:

- **IFN-B production** -- type I interferon signaling
- **CXCL10 secretion** -- chemokine attracting immune cells
- **TME transition** -- from immunologically cold to primed

### Phase 3: Botensilimab Cavalry Arrives

The combination of botensilimab (Fc-enhanced anti-CTLA-4) and balstilimab (anti-PD-1) amplifies the now-active innate signal:

1. **Innate amplification**: Enhanced Fc domain engages FcgRIIIa on macrophages and NK cells. Positive feedback loop: mtDNA -> cGAS-STING -> IFN-B -> macrophage activation -> tumor killing -> more mtDNA release

2. **Treg elimination**: Enhanced Fc mediates antibody-dependent cellular cytotoxicity (ADCC) against CTLA-4-high regulatory T cells in the TME, removing the immunosuppressive brake

3. **CD8+ T cell activation**: PD-1 blockade unleashes cytotoxic CD8+ T cells (IFN-gamma, Granzyme B, Perforin 1) against the now-visible tumor

**Current clinical signal:** Botensilimab + balstilimab achieves 17-20% ORR in MSS CRC (Vidal et al., Nature Medicine 2024) -- the best signal any immunotherapy has produced in this population.

**Prediction:** Statin pre-treatment will substantially increase this ORR by ensuring the TME is primed before checkpoint antibodies arrive.

## Retrospective Support

- **Liao et al.** (2025): Meta-analysis of 25 studies (n=46,154) -- statin + ICI = 20% mortality reduction
- **Stokes et al.** (2023): Statins enhance PD-1 blockade via T-cell activation + M2-to-M1 macrophage repolarization
