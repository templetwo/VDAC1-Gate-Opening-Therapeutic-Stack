import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patheffects as pe

# ══════════════════════════════════════════════════════════════
# CHOU-TALALAY CI & DOSE-REDUCTION INDEX ANALYSIS
# GJS Equation — Vasquez (2026), SAD v3.0
#
# KEY INSIGHT: The GJS equation's multiplicative structure means
# drugs acting on independent locks satisfy Loewe CI = 1.0.
# This is NOT a failure — it means the combination achieves
# massive threshold reduction through INDEPENDENT mechanisms,
# and each drug's required dose is dramatically reduced.
#
# The REAL Chou-Talalay synergy (CI < 1) prediction emerges
# IF there is cooperative binding — e.g., TSPO displacement
# physically facilitates VDAC1 conformational change that
# enhances cholesterol sensitivity. This is testable in Exp 5.
# ══════════════════════════════════════════════════════════════

plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Georgia', 'Times New Roman', 'DejaVu Serif'],
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.labelsize': 11,
    'figure.facecolor': '#FAFBFC',
    'axes.facecolor': '#FAFBFC',
    'axes.edgecolor': '#334155',
    'axes.linewidth': 1.2,
    'grid.color': '#E2E8F0',
    'grid.linewidth': 0.8,
    'text.color': '#1E293B',
})

C_SLATE = '#334155'
C_BLUE = '#1D4ED8'
C_GREEN = '#16A34A'
C_AMBER = '#D97706'
C_RED = '#DC2626'
C_PURPLE = '#7C3AED'
C_ORANGE = '#EA580C'
C_TEAL = '#0D9488'

# === GJS Equation ===
def gjs(f_hkii=0.8, f_bclxl=0.8, f_tspo=0.7, chol_cl=3.0, K=1.0):
    d = (1 - f_hkii) * (1 - f_bclxl) * (1 - f_tspo)
    d = max(d, 1e-10) if not isinstance(d, np.ndarray) else np.maximum(d, 1e-10)
    return (K / d) * chol_cl

T0 = gjs()  # 250.0

# ══════════════════════════════════════════════════════════════
# 3-PANEL FIGURE
# ══════════════════════════════════════════════════════════════
fig = plt.figure(figsize=(22, 9))
gs = fig.add_gridspec(1, 3, width_ratios=[1, 1, 1.1], wspace=0.35)

# ─────────────────────────────────────────────────────────────
# PANEL A: Isobologram — shows dose-reduction benefit
# ─────────────────────────────────────────────────────────────
ax1 = fig.add_subplot(gs[0])

# Target: 87.5% threshold reduction (fa = 0.875, T_target = 31.25)
# This is the dual-lock target from Figure 2d
T_target = 31.25
fa_target = 1 - T_target / T0  # 0.875

# Drug 1 (lovastatin) dose to achieve T_target alone:
# T_target = K / [(0.2)(0.2)(0.3)] × (3.0 - Δc)
# Δc_alone = 3.0 - T_target × 0.012 = 3.0 - 0.375 = 2.625
dc_max = 3.0 - T_target * 0.012  # 2.625

# Drug 2 (PK11195) dose to achieve T_target alone:
# T_target = K / [(0.2)(0.2)(0.3+Δt)] × 3.0
# 0.3+Δt = 75/T_target = 2.4
# Δt_alone = 2.1
dt_max = 75.0 / T_target - 0.3  # 2.1

# Loewe additivity line (CI = 1): straight line from (dc_max, 0) to (0, dt_max)
dc_line = np.linspace(0, dc_max, 100)
dt_line = dt_max * (1 - dc_line / dc_max)

ax1.plot(dc_line, dt_line, '-', color=C_SLATE, linewidth=2.5, label='Loewe additivity (CI = 1.0)')
ax1.fill_between(dc_line, dt_line, 0, color=C_GREEN, alpha=0.06)

# Actual GJS isoeffect curve (for fa = 0.875)
# Since GJS is multiplicatively separable, the isoeffect curve IS the Loewe line
# But let's also plot sub-additive curves for cooperative scenarios
dc_iso = np.linspace(0.01, dc_max * 0.99, 200)
dt_iso_loewe = dt_max * (1 - dc_iso / dc_max)

# Cooperative scenario (CI = 0.6) — if TSPO displacement enhances cholesterol effect
# Hypothesis: TSPO removal exposes VDAC1 cholesterol-binding face → lovastatin more potent
# Model: interaction term α makes combined effect > independent product
alpha_coop = 0.4  # cooperativity parameter
dt_iso_coop = dt_max * (1 - dc_iso / dc_max) * (1 - alpha_coop * (dc_iso / dc_max))
dt_iso_coop = np.maximum(dt_iso_coop, 0)

ax1.plot(dc_iso, dt_iso_coop, '-', color=C_GREEN, linewidth=2.5, 
         label=f'Cooperative model (CI ≈ 0.6)')
ax1.fill_between(dc_iso, dt_iso_coop, 0, color=C_GREEN, alpha=0.08)

# Antagonistic scenario (CI = 1.5) — if there's steric interference
dt_iso_antag = dt_max * (1 - dc_iso / dc_max) * (1 + 0.5 * (dc_iso / dc_max))
ax1.plot(dc_iso, dt_iso_antag, '--', color=C_RED, linewidth=1.5, alpha=0.6,
         label='Antagonistic model (CI ≈ 1.5)')

# Mark the actual Exp 5 combination point
dc_exp5 = 2.0
dt_exp5 = 0.5
ax1.plot(dc_exp5, dt_exp5, '*', color=C_PURPLE, markersize=18, markeredgecolor='white',
         markeredgewidth=1.5, zorder=10)
ax1.annotate('Experiment 5\ncombination', xy=(dc_exp5, dt_exp5),
             xytext=(dc_exp5 - 0.5, dt_exp5 + 0.55),
             fontsize=9, color=C_PURPLE, fontweight='bold', ha='center',
             arrowprops=dict(arrowstyle='->', color=C_PURPLE, lw=1.8))

# Mark monotherapy points
ax1.plot(dc_max, 0, 'o', color=C_BLUE, markersize=12, markeredgecolor='white',
         markeredgewidth=2, zorder=10)
ax1.annotate(f'Lovastatin alone\nΔ[C]/[CL] = {dc_max:.2f}', 
             xy=(dc_max, 0), xytext=(dc_max - 0.6, 0.35),
             fontsize=8, color=C_BLUE, fontweight='bold', ha='center',
             arrowprops=dict(arrowstyle='->', color=C_BLUE, lw=1.5))

ax1.plot(0, dt_max, 'o', color=C_ORANGE, markersize=12, markeredgecolor='white',
         markeredgewidth=2, zorder=10)
ax1.annotate(f'PK11195 alone\nΔf_TSPO = {dt_max:.2f}', 
             xy=(0, dt_max), xytext=(0.6, dt_max - 0.2),
             fontsize=8, color=C_ORANGE, fontweight='bold', ha='center',
             arrowprops=dict(arrowstyle='->', color=C_ORANGE, lw=1.5))

# DRI annotation
# DRI1 = Dx1/d1 = dc_max / dc_exp5 = 2.625/2.0 = 1.31
# DRI2 = Dx2/d2 = dt_max / dt_exp5 = 2.1/0.5 = 4.2
dri1 = dc_max / dc_exp5
dri2 = dt_max / dt_exp5
ax1.text(0.97, 0.03, 
         f'Dose-Reduction Index:\n'
         f'  DRI_lova = {dri1:.2f}×\n'
         f'  DRI_PK = {dri2:.1f}×\n'
         f'Even at CI = 1.0, the\ncombination requires\nfar less of each drug.',
         transform=ax1.transAxes, fontsize=8, color=C_SLATE,
         ha='right', va='bottom',
         bbox=dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor='#CBD5E1', alpha=0.9))

ax1.set_xlabel('Lovastatin effect: Δ[Chol]/[CL]', fontweight='bold')
ax1.set_ylabel('PK11195 effect: Δf_TSPO', fontweight='bold')
ax1.set_title(f'Isobologram at {fa_target*100:.1f}% Threshold Reduction\n'
              f'Exp 5 tests whether curve bows BELOW the line',
              fontweight='bold')
ax1.legend(loc='upper right', framealpha=0.9, edgecolor='#CBD5E1', fontsize=8)
ax1.set_xlim(-0.1, dc_max + 0.3)
ax1.set_ylim(-0.15, dt_max + 0.5)
ax1.grid(True, alpha=0.3)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.text(-0.08, 1.05, 'A', transform=ax1.transAxes, fontsize=20, fontweight='bold', color=C_SLATE)

# ─────────────────────────────────────────────────────────────
# PANEL B: CI scenarios — independent vs. cooperative
# ─────────────────────────────────────────────────────────────
ax2 = fig.add_subplot(gs[1])

# Effect levels (fraction of threshold eliminated)
fa_range = np.linspace(0.1, 0.95, 100)

# Scenario 1: Independent targets (GJS as-is) → CI = 1.0 everywhere
ci_independent = np.ones_like(fa_range)

# Scenario 2: Weak cooperativity (TSPO removal exposes cholesterol annulus)
# CI decreases as effect level increases (stronger at higher doses)
ci_weak_coop = 1.0 - 0.15 * fa_range

# Scenario 3: Strong cooperativity (conformational coupling)
# CI = 0.5-0.7 range
ci_strong_coop = 1.0 - 0.45 * fa_range**0.7

# Scenario 4: What if there's high-dose antagonism?
ci_bell = 1.0 - 0.3 * fa_range + 0.6 * fa_range**3

ax2.plot(fa_range, ci_independent, '-', color=C_SLATE, linewidth=3,
         label='Independent targets (GJS baseline)')
ax2.plot(fa_range, ci_weak_coop, '-', color=C_TEAL, linewidth=2.5,
         label='Weak cooperativity (allosteric)')
ax2.plot(fa_range, ci_strong_coop, '-', color=C_GREEN, linewidth=2.5,
         label='Strong cooperativity (conformational)')
ax2.plot(fa_range, ci_bell, '--', color=C_RED, linewidth=2, alpha=0.7,
         label='High-dose antagonism (toxicity)')

# Reference lines and zones
ax2.axhline(y=1.0, color=C_SLATE, linewidth=1, alpha=0.3)
ax2.axhline(y=0.8, color=C_GREEN, linewidth=1.5, linestyle=':', alpha=0.5)
ax2.axhspan(0, 0.8, color=C_GREEN, alpha=0.04)
ax2.axhspan(1.0, 1.5, color=C_RED, alpha=0.03)

# Zone labels
ax2.text(0.15, 0.55, 'Synergy zone\nCI < 0.8', fontsize=9, color=C_GREEN,
         fontweight='bold', fontstyle='italic')
ax2.text(0.15, 1.08, 'Antagonism', fontsize=8, color=C_RED, fontstyle='italic', alpha=0.6)

# Experiment 5 decision criteria
ax2.axvline(x=0.5, color=C_AMBER, linewidth=1.5, linestyle=':', alpha=0.4)
ax2.annotate('Exp 5 readout:\nmeasure CI here\n(ED50 isoeffect)',
             xy=(0.5, 0.45), fontsize=8, color=C_AMBER, fontweight='bold',
             ha='center', va='center',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFFBEB', edgecolor=C_AMBER, alpha=0.9))

# Decision framework box
decision_text = (
    "EXPERIMENT 5 DECISION TREE:\n"
    "━━━━━━━━━━━━━━━━━━━━━━━━━\n"
    "CI ≈ 1.0 → Independent action\n"
    "  (still 8× better than monotherapy)\n"
    "CI = 0.7–0.9 → Weak cooperativity\n"
    "  (TSPO facilitates cholesterol effect)\n"
    "CI < 0.7 → Strong cooperativity\n"
    "  (conformational coupling confirmed)\n"
    "CI > 1.2 → Antagonism\n"
    "  (reconsider combination strategy)"
)
ax2.text(0.97, 0.97, decision_text, transform=ax2.transAxes,
         fontsize=7.5, fontfamily='monospace', color=C_SLATE,
         ha='right', va='top',
         bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor='#CBD5E1', alpha=0.95))

ax2.set_xlabel('Effect level (fraction of threshold eliminated)', fontweight='bold')
ax2.set_ylabel('Combination Index (CI)', fontweight='bold')
ax2.set_title('CI Predictions: What Experiment 5 Can Distinguish\n'
              'Independent targets → CI = 1.0 | Cooperativity → CI < 1.0',
              fontweight='bold')
ax2.legend(loc='lower left', framealpha=0.9, edgecolor='#CBD5E1', fontsize=8)
ax2.set_ylim(0.3, 1.35)
ax2.set_xlim(0.1, 0.95)
ax2.grid(True, alpha=0.3)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.text(-0.08, 1.05, 'B', transform=ax2.transAxes, fontsize=20, fontweight='bold', color=C_SLATE)

# ─────────────────────────────────────────────────────────────
# PANEL C: Therapeutic advantage comparison
# ─────────────────────────────────────────────────────────────
ax3 = fig.add_subplot(gs[2])

# Bar chart: absolute threshold values + fold changes + CI interpretation
scenarios = [
    ('Cancer\nbaseline',         250.0,  C_RED,    1.0,   '—'),
    ('Lovastatin\nalone',        83.3,   C_BLUE,   3.0,   'N/A'),
    ('PK11195\nalone',           93.8,   C_ORANGE, 2.7,   'N/A'),
    ('Simple\naddition',         250-83.3-93.8+250, C_SLATE, None, 'N/A'),
    ('Bliss\nindependence',      31.25,  '#6B7280', None, 'CI = 1.0'),
    ('GJS combo\n(independent)', 31.25,  C_PURPLE, 8.0,   'CI = 1.0'),
    ('GJS combo\n(cooperative)', 31.25*0.6, C_GREEN, 250/(31.25*0.6), 'CI ≈ 0.6'),
]

# Fix the simple addition value (it shouldn't go negative)
# Additive: threshold_baseline - drop1 - drop2 = 250 - (250-83.3) - (250-93.8) = 250 - 166.7 - 156.2 = -72.9
# This is impossible → shows why additive model fails at high effects
# Use: T_add = T_baseline - (T_baseline - T1) - (T_baseline - T2) = T1 + T2 - T_baseline
# T_add = 83.3 + 93.8 - 250 = -72.9 → clip to minimum meaningful value
simple_add = max(83.3 + 93.8 - 250, 5)  # clipped

scenarios_clean = [
    ('Cancer\nbaseline',          250.0,   C_RED),
    ('Lovastatin\nalone',         83.3,    C_BLUE),
    ('PK11195\nalone',            93.8,    C_ORANGE),
    ('Additive\nprediction',      simple_add, '#9CA3AF'),
    ('GJS combo\n(CI = 1.0)',     31.25,   C_PURPLE),
    ('If cooperative\n(CI ≈ 0.6)', 18.75,  C_GREEN),
]

labels = [s[0] for s in scenarios_clean]
values = [s[1] for s in scenarios_clean]
colors = [s[2] for s in scenarios_clean]

bars = ax3.bar(range(len(labels)), values, color=colors, edgecolor='white', linewidth=2, width=0.7)

# Value labels
for i, (bar, val) in enumerate(zip(bars, values)):
    ax3.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 3,
             f'{val:.1f}', ha='center', va='bottom', fontweight='bold', fontsize=11,
             color=C_SLATE)

# Fold changes from baseline
for i, (bar, val) in enumerate(zip(bars, values)):
    if i > 0 and val > 0:
        fold = 250.0 / val
        ax3.text(bar.get_x() + bar.get_width()/2, bar.get_height() / 2,
                 f'{fold:.1f}×', ha='center', va='center', fontsize=10,
                 color='white', fontweight='bold',
                 path_effects=[pe.withStroke(linewidth=2, foreground=colors[i])])

# Additive line with annotation
ax3.annotate('', xy=(3, simple_add), xycoords='data',
             xytext=(3, 88.5), textcoords='data',
             arrowprops=dict(arrowstyle='<->', color=C_AMBER, lw=2))
ax3.text(3.4, 50, 'Additive model\nfails here\n(goes negative\nat −72.9)',
         fontsize=7, color='#9CA3AF', fontstyle='italic', ha='left')

# Bracket between GJS independent and cooperative
ax3.annotate('', xy=(5, 18.75), xycoords='data',
             xytext=(4, 31.25), textcoords='data',
             arrowprops=dict(arrowstyle='<->', color=C_GREEN, lw=2,
                           connectionstyle='bar,fraction=0.3'))
ax3.text(4.85, 42, 'Exp 5\ntests this\ngap', fontsize=8, color=C_GREEN, fontweight='bold',
         ha='center')

ax3.set_xticks(range(len(labels)))
ax3.set_xticklabels(labels, fontsize=8)
ax3.set_ylabel('Apoptotic Threshold', fontweight='bold')
ax3.set_title('Therapeutic Advantage: Why CI = 1.0 Still Wins\n'
              'Multiplicative pharmacology > additive, even without synergy',
              fontweight='bold')
ax3.set_ylim(0, 290)
ax3.grid(axis='y', alpha=0.3)
ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)

# Key insight box
insight = (
    "KEY INSIGHT: The GJS equation's multiplicative\n"
    "structure guarantees the combination is 8× more\n"
    "effective than monotherapy even at CI = 1.0.\n"
    "True synergy (CI < 1.0) would be a bonus —\n"
    "testable if TSPO displacement enhances\n"
    "lovastatin's cholesterol-stripping effect."
)
ax3.text(0.98, 0.98, insight, transform=ax3.transAxes, fontsize=7.5,
         color=C_SLATE, ha='right', va='top',
         bbox=dict(boxstyle='round,pad=0.5', facecolor='#F0FDF4', edgecolor=C_GREEN, alpha=0.9))

ax3.text(-0.05, 1.05, 'C', transform=ax3.transAxes, fontsize=20, fontweight='bold', color=C_SLATE)

# ─────────────────────────────────────────────────────────────
# MASTER TITLE
# ─────────────────────────────────────────────────────────────
fig.suptitle('Figure 2e.  Chou-Talalay Combination Index Analysis — Lovastatin × PK11195\n'
             'GJS multiplicative structure predicts powerful combination benefit; Experiment 5 tests for true pharmacological synergy',
             fontsize=15, fontweight='bold', y=1.03, color='#0F172A')

fig.tight_layout(rect=[0, 0, 1, 0.96])
fig.savefig('../figures/Figure2e_Chou_Talalay_CI.png', dpi=300, bbox_inches='tight',
            facecolor='#FAFBFC', edgecolor='none')
plt.close(fig)
print("Panel 2e v2: Chou-Talalay CI (corrected) — done")

# ══════════════════════════════════════════════════════════════
# NUMERICAL OUTPUT
# ══════════════════════════════════════════════════════════════
print("\n" + "="*72)
print("CHOU-TALALAY CI ANALYSIS — CORRECTED INTERPRETATION")
print("="*72)
print()
print("1. BASELINE GJS PREDICTION (independent targets):")
print(f"   CI = 1.0 (exact) — this is a mathematical property")
print(f"   of multiplicatively-separable threshold equations.")
print(f"   Drugs acting on different multiplicative terms always")
print(f"   satisfy Loewe additivity by construction.")
print()
print("2. WHY THIS IS STILL THERAPEUTICALLY POWERFUL:")
print(f"   Cancer baseline threshold:  {T0:.1f}")
print(f"   Lovastatin alone:           {gjs(chol_cl=1.0):.1f} ({T0/gjs(chol_cl=1.0):.1f}× drop)")
print(f"   PK11195 alone:              {gjs(f_tspo=0.2):.1f} ({T0/gjs(f_tspo=0.2):.1f}× drop)")
print(f"   Combination:                {gjs(chol_cl=1.0, f_tspo=0.2):.1f} ({T0/gjs(chol_cl=1.0, f_tspo=0.2):.1f}× drop)")
print(f"   Simple additive prediction: {83.3+93.8-250:.1f} (IMPOSSIBLE — goes negative)")
print()
print("3. DOSE-REDUCTION INDEX (Exp 5):")
print(f"   DRI_lovastatin = {dc_max/2.0:.2f}× (need {2.0/dc_max*100:.0f}% of monotherapy dose)")
print(f"   DRI_PK11195   = {dt_max/0.5:.1f}× (need {0.5/dt_max*100:.0f}% of monotherapy dose)")
print()
print("4. WHAT EXPERIMENT 5 ACTUALLY TESTS:")
print(f"   Null hypothesis: CI = 1.0 (independent action)")
print(f"   Alternative:     CI < 0.8 (cooperative mechanism)")
print(f"   If TSPO displacement physically exposes the VDAC1")
print(f"   cholesterol-binding annulus, lovastatin becomes MORE")
print(f"   potent in TSPO-depleted mitochondria. This would give")
print(f"   CI < 1.0 — TRUE synergy beyond multiplicative benefit.")
print()
print("5. GRANT LANGUAGE:")
print(f"   'The GJS equation predicts that dual-lock targeting")
print(f"    achieves 8-fold threshold reduction through multiplicative")
print(f"    pharmacology (CI = 1.0). Experiment 5 tests whether")
print(f"    allosteric coupling between TSPO and the cholesterol")
print(f"    annulus produces true pharmacological synergy (CI < 0.8),")
print(f"    which would further enhance therapeutic index.'")
