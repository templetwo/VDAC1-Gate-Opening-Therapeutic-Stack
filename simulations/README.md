# Simulations

Computational validation of the Gate-Jamming Score (GJS) cofactor equation and Chou-Talalay combination pharmacology.

## Scripts

| Script | Output | Description |
|--------|--------|-------------|
| `gjs_simulation.py` | Figure 2 (4-panel) | GJS equation simulation: 2D sensitivity curves, 3D surface, heatmap, synergy bar chart |
| `gjs_chou_talalay_calculator.py` | Figure 2e (3-panel) | Chou-Talalay CI analysis: isobologram, CI predictions, therapeutic advantage comparison |

## The GJS Equation

```
Apoptotic Threshold = K / [(1 - f_HKII)(1 - f_BclxL)(1 - f_TSPO)] x [Chol]/[CL]
```

### Parameters

| Parameter | Description | Cancer Baseline | After Treatment |
|-----------|-------------|----------------|-----------------|
| K | Lattice exit energy (scaling constant) | 1 | 1 |
| f_HKII | HK-II fractional occupancy on VDAC1 | 0.8 | 0.8 (not targeted) |
| f_BclxL | Bcl-xL fractional binding | 0.8 | 0.8 (not targeted in CRC) |
| f_TSPO | TSPO tether strength | 0.7 | 0.2 (if PK11195 works) |
| [Chol]/[CL] | Cholesterol-to-cardiolipin ratio | 3.0 | 1.0 (lovastatin target) |

### Numerical Predictions

| Condition | Threshold | Fold Change |
|-----------|-----------|-------------|
| Cancer baseline | 250.0 | -- |
| Lovastatin alone ([Chol]/[CL] -> 1.0) | 83.3 | 3.0x drop |
| PK11195 alone (f_TSPO -> 0.2) | 93.8 | 2.7x drop |
| Dual lock (both) | 31.3 | 8.0x drop |
| Additive prediction | 31.3 | -- |
| If cooperative (CI=0.8) | 18.8 | 13.3x drop |

### Dose-Reduction Index (DRI)

- DRI_lovastatin = 1.31x (modest dose reduction)
- DRI_PK11195 = 4.2x (significant dose reduction)

## Running

```bash
# Requires Python 3.8+
pip install numpy matplotlib scipy

# Generate Figure 2 panels
python gjs_simulation.py

# Generate Figure 2e panels
python gjs_chou_talalay_calculator.py
```

Output PNGs are saved to `../figures/`.
