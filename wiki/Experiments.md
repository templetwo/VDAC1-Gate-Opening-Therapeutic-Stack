# Experiments

Six falsifiable experiments with explicit kill conditions. Each addresses a single binary question. A framework that cannot be killed cannot be trusted.

## Strategic Experiment Map (Table 2)

| Exp | Question | Kill Condition | Primary Readout | Priority |
|-----|----------|---------------|-----------------|----------|
| 1 | Does TSPO-VDAC1 binding suppress mtDNA release? | No change in mtDNA release upon TSPO knockdown | qPCR (cytosolic mtDNA) | Exploratory (4th lock) |
| 2a | Does lovastatin deplete OMM cholesterol in HCT116? | <30% cholesterol reduction at 1-20 uM | Filipin staining + Amplex Red | **CRITICAL (linchpin)** |
| 2b | Does cholesterol depletion trigger VDAC1 oligomerization? | No oligomer increase despite >=30% chol depletion | EGS cross-linking + Western blot | **CRITICAL (linchpin)** |
| 3 | Does VDAC1 opening release mtDNA -> cGAS-STING? | No cytosolic mtDNA or no IFN-B induction | ELISA (IFN-B, CXCL10) | High |
| 4 | Does statin pre-treatment enhance ICI response in vivo? | No tumor growth difference: statin+ICI vs ICI alone | Tumor volume + survival | High (translational) |
| 5 | Does dual-lock targeting show synergy? | CI > 1.2 (antagonistic) at all dose ratios | Chou-Talalay CI | Contingent on Exp 1 |
| 6 | Can CBD be rehabilitated? | CBD suppresses T cells at all VDAC1-active doses | Flow cytometry + viability | Low (quarantined) |

## Dependency Structure

```
Exp 2a/2b (LINCHPIN) ---> Exp 3 (mtDNA/cGAS-STING) ---> Exp 4 (CT26 in vivo)
                                                                  |
                                                                  v
                                                          Journal submission

Exp 1 (TSPO tether, parallel) ---> Exp 5 (lovastatin + PK11195 synergy)

Exp 6 (CBD disposition, parallel w/ Phase C) ---> CBD quarantine decision
```

## Priority Logic

**Experiment 2a/2b is the linchpin.** If lovastatin does not deplete OMM cholesterol and trigger VDAC1 oligomerization in HCT116 cells, the entire framework collapses. This experiment must succeed before any downstream work is justified. It is also the most affordable (<=3,000 in reagents) and fastest (4 weeks) to execute.

- Exp 3 depends on 2a/2b (no point measuring mtDNA release if the gate doesn't open)
- Exp 4 depends on Exp 3 (no point testing in vivo if the cascade doesn't fire in vitro)
- Exp 1 is independent and can run in parallel, but its results only matter if 2a/2b succeeds
- Exp 5 depends on Exp 1
- Exp 6 is lowest priority and only relevant if Exps 1-3 all succeed

## Complete Bench Protocol

See [[Bench Protocol]] for the full operational protocol for Experiments 2a and 2b.
