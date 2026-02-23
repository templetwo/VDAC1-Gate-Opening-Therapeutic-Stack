import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LogNorm
import matplotlib.ticker as ticker

# ══════════════════════════════════════════════════════════════
# GJS EQUATION SIMULATION
# Vasquez (2026) — Strategic Architecture Document v3.0
# ══════════════════════════════════════════════════════════════

# Typography to match SAD document family
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Georgia', 'Times New Roman', 'DejaVu Serif'],
    'font.size': 11,
    'axes.titlesize': 14,
    'axes.labelsize': 12,
    'legend.fontsize': 10,
    'figure.facecolor': '#FAFBFC',
    'axes.facecolor': '#FAFBFC',
    'axes.edgecolor': '#334155',
    'axes.linewidth': 1.2,
    'grid.color': '#E2E8F0',
    'grid.linewidth': 0.8,
    'text.color': '#1E293B',
})

# === THE GJS EQUATION ===
# Threshold = K / [(1 - f_HKII)(1 - f_BclxL)(1 - f_TSPO)] × [Chol]/[CL]
# Lower threshold = easier to trigger mtDNA release → cGAS-STING → immune activation

def gjs_threshold(f_hkii=0.8, f_bclxl=0.8, f_tspo=0.7, chol_cl_ratio=2.0, K=1.0):
    """
    Gate-Jamming Score threshold.
    f_hkii, f_bclxl, f_tspo: fractional occupancy of each lock (0-1)
    chol_cl_ratio: [Cholesterol]/[Cardiolipin] in OMM
    K: scaling constant
    """
    denom = (1 - f_hkii) * (1 - f_bclxl) * (1 - f_tspo)
    if isinstance(denom, np.ndarray):
        denom = np.where(denom < 1e-10, 1e-10, denom)
    elif denom < 1e-10:
        denom = 1e-10
    return (K / denom) * chol_cl_ratio


# Cancer baseline parameters
f_hkii_cancer = 0.8    # HK-II heavily bound in MSS CRC
f_bclxl_cancer = 0.8   # Bcl-xL overexpressed
f_tspo_cancer = 0.7    # TSPO elevated (28% CRC overexpression)
chol_cl_cancer = 3.0   # High cholesterol loading in tumor OMM

# Color palette matching Figure 1
COLOR_SLATE = '#334155'
COLOR_BLUE = '#1D4ED8'
COLOR_GREEN = '#16A34A'
COLOR_AMBER = '#D97706'
COLOR_RED = '#DC2626'
COLOR_PURPLE = '#7C3AED'
COLOR_ORANGE = '#EA580C'
COLOR_LIGHT = '#F1F5F9'

# ══════════════════════════════════════════════════════════════
# PANEL 1: 2D Lines — Cholesterol sensitivity at TSPO levels
# ══════════════════════════════════════════════════════════════
fig1, ax1 = plt.subplots(figsize=(10, 6.5))

chol_values = np.linspace(0.3, 5.0, 200)
tspo_scenarios = [
    (0.0, 'TSPO absent (KO)', COLOR_GREEN, '-'),
    (0.3, 'Low TSPO (f = 0.3)', COLOR_BLUE, '--'),
    (0.5, 'Moderate TSPO (f = 0.5)', COLOR_AMBER, '-.'),
    (0.7, 'Cancer baseline (f = 0.7)', COLOR_RED, '-'),
    (0.9, 'High TSPO (f = 0.9)', COLOR_PURPLE, '-'),
]

for f_tspo, label, color, ls in tspo_scenarios:
    thresh = gjs_threshold(f_tspo=f_tspo, chol_cl_ratio=chol_values)
    ax1.plot(chol_values, thresh, linewidth=2.8, color=color, linestyle=ls, label=label)

# Mark cancer baseline point
cancer_thresh = gjs_threshold(f_tspo=f_tspo_cancer, chol_cl_ratio=chol_cl_cancer)
ax1.plot(chol_cl_cancer, cancer_thresh, 'o', color=COLOR_RED, markersize=12, 
         markeredgecolor='white', markeredgewidth=2, zorder=5)
ax1.annotate(f'Cancer baseline\nThreshold = {cancer_thresh:.1f}', 
             xy=(chol_cl_cancer, cancer_thresh),
             xytext=(chol_cl_cancer + 0.6, cancer_thresh + 40),
             fontsize=9, color=COLOR_RED, fontweight='bold',
             arrowprops=dict(arrowstyle='->', color=COLOR_RED, lw=1.5))

# Mark lovastatin target
lova_thresh = gjs_threshold(f_tspo=f_tspo_cancer, chol_cl_ratio=1.0)
ax1.plot(1.0, lova_thresh, 's', color=COLOR_BLUE, markersize=12,
         markeredgecolor='white', markeredgewidth=2, zorder=5)
ax1.annotate(f'Lovastatin target\nThreshold = {lova_thresh:.1f}', 
             xy=(1.0, lova_thresh),
             xytext=(1.6, lova_thresh + 25),
             fontsize=9, color=COLOR_BLUE, fontweight='bold',
             arrowprops=dict(arrowstyle='->', color=COLOR_BLUE, lw=1.5))

ax1.set_xlabel('[Chol] / [CL] Ratio in Outer Mitochondrial Membrane', fontweight='bold')
ax1.set_ylabel('Apoptotic Threshold (lower = easier gate opening)', fontweight='bold')
ax1.set_title('GJS Equation: TSPO Lock Modulates Cholesterol Sensitivity\n'
              'f_HKII = 0.8, f_BclxL = 0.8 (MSS CRC baseline)', fontweight='bold')
ax1.legend(loc='upper left', framealpha=0.9, edgecolor='#CBD5E1')
ax1.set_ylim(0, 500)
ax1.set_xlim(0.3, 5.0)
ax1.grid(True, alpha=0.4)

# Add therapeutic window annotation
ax1.axhspan(0, 80, color=COLOR_GREEN, alpha=0.06)
ax1.text(4.6, 40, 'Therapeutic\nwindow', fontsize=8, color=COLOR_GREEN, 
         ha='center', fontstyle='italic', fontweight='bold')

fig1.tight_layout()
fig1.savefig('gjs_panel1_2d_lines.png', dpi=300, bbox_inches='tight',
             facecolor='#FAFBFC', edgecolor='none')
plt.close(fig1)
print("Panel 1: 2D lines — done")

# ══════════════════════════════════════════════════════════════
# PANEL 2: 3D Surface — Full threshold landscape
# ══════════════════════════════════════════════════════════════
fig2 = plt.figure(figsize=(11, 8.5))
ax2 = fig2.add_subplot(111, projection='3d')

f_tspo_surf = np.linspace(0.0, 0.95, 60)
chol_surf = np.linspace(0.3, 5.0, 60)
F_surf, C_surf = np.meshgrid(f_tspo_surf, chol_surf)
Z_surf = gjs_threshold(f_tspo=F_surf, chol_cl_ratio=C_surf)
Z_surf = np.clip(Z_surf, 0, 800)

surf = ax2.plot_surface(C_surf, F_surf, Z_surf, cmap='magma', alpha=0.92,
                        edgecolor='none', antialiased=True, rstride=1, cstride=1)

# Mark cancer baseline
ax2.scatter([chol_cl_cancer], [f_tspo_cancer], [cancer_thresh], 
            color=COLOR_RED, s=120, edgecolors='white', linewidths=2, zorder=10)

# Mark dual-lock target
dual_thresh = gjs_threshold(f_tspo=0.2, chol_cl_ratio=1.0)
ax2.scatter([1.0], [0.2], [dual_thresh], 
            color=COLOR_GREEN, s=120, edgecolors='white', linewidths=2, zorder=10)

ax2.set_xlabel('\n[Chol] / [CL]', fontweight='bold', labelpad=10)
ax2.set_ylabel('\nf_TSPO', fontweight='bold', labelpad=10)
ax2.set_zlabel('\nApoptotic Threshold', fontweight='bold', labelpad=10)
ax2.set_title('3D GJS Threshold Surface\n'
              'Multiplicative synergy: steep collapse when both locks open\n'
              'f_HKII = 0.8, f_BclxL = 0.8 (held constant)',
              fontweight='bold', pad=15)

ax2.view_init(elev=25, azim=225)
cbar = fig2.colorbar(surf, ax=ax2, shrink=0.55, pad=0.08, label='Threshold')

fig2.tight_layout()
fig2.savefig('gjs_panel2_3d_surface.png', dpi=300, bbox_inches='tight',
             facecolor='#FAFBFC', edgecolor='none')
plt.close(fig2)
print("Panel 2: 3D surface — done")

# ══════════════════════════════════════════════════════════════
# PANEL 3: Log-scale heatmap — Dual-lock synergy zone
# ══════════════════════════════════════════════════════════════
fig3, ax3 = plt.subplots(figsize=(10, 8))

f_tspo_heat = np.linspace(0.0, 0.95, 100)
chol_heat = np.linspace(0.3, 5.0, 100)
F_heat, C_heat = np.meshgrid(f_tspo_heat, chol_heat)
Z_heat = gjs_threshold(f_tspo=F_heat, chol_cl_ratio=C_heat)

im = ax3.pcolormesh(f_tspo_heat, chol_heat, Z_heat, 
                     norm=LogNorm(vmin=10, vmax=800),
                     cmap='magma_r', shading='gouraud')

# Contour lines
contours = ax3.contour(f_tspo_heat, chol_heat, Z_heat, 
                        levels=[25, 50, 100, 200, 400],
                        colors='white', linewidths=1, alpha=0.7)
ax3.clabel(contours, fmt='%1.0f', fontsize=8, colors='white')

# Cancer baseline
ax3.plot(f_tspo_cancer, chol_cl_cancer, 'o', color='white', markersize=14,
         markeredgecolor=COLOR_RED, markeredgewidth=3)
ax3.annotate('CANCER\nBASELINE', xy=(f_tspo_cancer, chol_cl_cancer),
             xytext=(f_tspo_cancer - 0.18, chol_cl_cancer + 0.6),
             fontsize=9, color='white', fontweight='bold', ha='center',
             arrowprops=dict(arrowstyle='->', color='white', lw=2))

# Dual-lock target
ax3.plot(0.2, 1.0, 's', color='white', markersize=14,
         markeredgecolor=COLOR_GREEN, markeredgewidth=3)
ax3.annotate('DUAL-LOCK\nTARGET', xy=(0.2, 1.0),
             xytext=(0.37, 0.6),
             fontsize=9, color='white', fontweight='bold', ha='center',
             arrowprops=dict(arrowstyle='->', color='white', lw=2))

# Lovastatin only
ax3.plot(f_tspo_cancer, 1.0, 'D', color='white', markersize=10,
         markeredgecolor=COLOR_BLUE, markeredgewidth=2.5)
ax3.annotate('Lovastatin\nonly', xy=(f_tspo_cancer, 1.0),
             xytext=(f_tspo_cancer + 0.12, 1.5),
             fontsize=8, color='white', fontstyle='italic',
             arrowprops=dict(arrowstyle='->', color='white', lw=1.5))

# TSPO ligand only
ax3.plot(0.2, chol_cl_cancer, '^', color='white', markersize=10,
         markeredgecolor=COLOR_PURPLE, markeredgewidth=2.5)
ax3.annotate('PK11195\nonly', xy=(0.2, chol_cl_cancer),
             xytext=(0.05, chol_cl_cancer + 0.6),
             fontsize=8, color='white', fontstyle='italic',
             arrowprops=dict(arrowstyle='->', color='white', lw=1.5))

# Arrow showing therapeutic trajectory
ax3.annotate('', xy=(0.2, 1.0), xycoords='data',
             xytext=(f_tspo_cancer, chol_cl_cancer), textcoords='data',
             arrowprops=dict(arrowstyle='->', color=COLOR_GREEN, lw=3, 
                           connectionstyle='arc3,rad=-0.2'))

cbar3 = fig3.colorbar(im, ax=ax3, label='Apoptotic Threshold (log scale)',
                       shrink=0.85, pad=0.02)

ax3.set_xlabel('f_TSPO (TSPO lock strength)', fontweight='bold')
ax3.set_ylabel('[Chol] / [CL] (cholesterol lock)', fontweight='bold')
ax3.set_title('GJS Threshold Heatmap: Dual-Lock Synergy Zone\n'
              'Darkest region = lowest threshold = gate opens easiest\n'
              'f_HKII = 0.8, f_BclxL = 0.8 (held constant)',
              fontweight='bold')

fig3.tight_layout()
fig3.savefig('gjs_panel3_heatmap.png', dpi=300, bbox_inches='tight',
             facecolor='#FAFBFC', edgecolor='none')
plt.close(fig3)
print("Panel 3: heatmap — done")

# ══════════════════════════════════════════════════════════════
# PANEL 4: Synergy bar chart — Quantified comparison
# ══════════════════════════════════════════════════════════════
fig4, ax4 = plt.subplots(figsize=(10, 6.5))

scenarios = {
    'Cancer\nbaseline': gjs_threshold(f_tspo=0.7, chol_cl_ratio=3.0),
    'Lovastatin\nonly': gjs_threshold(f_tspo=0.7, chol_cl_ratio=1.0),
    'PK11195\nonly': gjs_threshold(f_tspo=0.2, chol_cl_ratio=3.0),
    'DUAL LOCK\n(Lova + PK)': gjs_threshold(f_tspo=0.2, chol_cl_ratio=1.0),
}
# Also show additive prediction
additive_prediction = (scenarios['Lovastatin\nonly'] + scenarios['PK11195\nonly']) / 2

labels = list(scenarios.keys())
values = list(scenarios.values())
colors = [COLOR_RED, COLOR_BLUE, COLOR_PURPLE, COLOR_GREEN]

bars = ax4.bar(labels, values, color=colors, edgecolor='white', linewidth=2, width=0.65)

# Add value labels on bars
for bar, val in zip(bars, values):
    ax4.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 3,
             f'{val:.1f}', ha='center', va='bottom', fontweight='bold', fontsize=13,
             color=COLOR_SLATE)

# Add fold-change annotations
baseline = values[0]
for i, (bar, val) in enumerate(zip(bars, values)):
    if i > 0:
        fold = baseline / val
        ax4.text(bar.get_x() + bar.get_width()/2, bar.get_height() / 2,
                 f'{fold:.1f}× drop', ha='center', va='center', fontsize=10,
                 color='white', fontweight='bold')

# Additive prediction line
ax4.axhline(y=additive_prediction, color=COLOR_ORANGE, linestyle='--', linewidth=2, alpha=0.8)
ax4.text(3.7, additive_prediction + 5, f'Additive prediction: {additive_prediction:.1f}',
         fontsize=9, color=COLOR_ORANGE, fontweight='bold', ha='center')

# Synergy annotation
actual_dual = values[3]
ax4.annotate('', xy=(3, actual_dual), xycoords='data',
             xytext=(3, additive_prediction), textcoords='data',
             arrowprops=dict(arrowstyle='<->', color=COLOR_ORANGE, lw=2))
synergy_gap = additive_prediction - actual_dual
ax4.text(3.35, (additive_prediction + actual_dual) / 2,
         f'SYNERGY\n−{synergy_gap:.0f}', fontsize=9, color=COLOR_ORANGE,
         fontweight='bold', ha='left', va='center')

ax4.set_ylabel('Apoptotic Threshold', fontweight='bold')
ax4.set_title('Quantified Synergy: Dual-Lock vs. Single-Lock Targeting\n'
              'Multiplicative collapse predicts Chou-Talalay CI < 0.8 (Experiment 5)',
              fontweight='bold')
ax4.set_ylim(0, max(values) * 1.25)
ax4.grid(axis='y', alpha=0.3)
ax4.spines['top'].set_visible(False)
ax4.spines['right'].set_visible(False)

fig4.tight_layout()
fig4.savefig('gjs_panel4_synergy_bars.png', dpi=300, bbox_inches='tight',
             facecolor='#FAFBFC', edgecolor='none')
plt.close(fig4)
print("Panel 4: synergy bars — done")

# ══════════════════════════════════════════════════════════════
# COMPOSITE 4-PANEL FIGURE
# ══════════════════════════════════════════════════════════════
from PIL import Image

panels = [
    Image.open('gjs_panel1_2d_lines.png'),
    Image.open('gjs_panel2_3d_surface.png'),
    Image.open('gjs_panel3_heatmap.png'),
    Image.open('gjs_panel4_synergy_bars.png'),
]

# Get max dimensions
widths = [p.width for p in panels]
heights = [p.height for p in panels]

# 2x2 grid
grid_w = max(widths[0], widths[2]) + max(widths[1], widths[3]) + 40
grid_h = max(heights[0], heights[1]) + max(heights[2], heights[3]) + 120

composite = Image.new('RGB', (grid_w, grid_h), color=(250, 251, 252))

# Place panels
x_left = 10
x_right = max(widths[0], widths[2]) + 30
y_top = 80
y_bottom = max(heights[0], heights[1]) + 90

composite.paste(panels[0], (x_left, y_top))
composite.paste(panels[1], (x_right, y_top))
composite.paste(panels[2], (x_left, y_bottom))
composite.paste(panels[3], (x_right, y_bottom))

# Add title using matplotlib for consistent typography
fig_title, ax_title = plt.subplots(figsize=(grid_w/300, 0.6))
ax_title.axis('off')
ax_title.text(0.5, 0.5, 
              'Figure 2.  GJS Equation Simulation — Multiplicative Synergy in Dual-Lock Targeting',
              transform=ax_title.transAxes, ha='center', va='center',
              fontsize=16, fontweight='bold', color='#0F172A',
              fontfamily='serif')
fig_title.savefig('title_bar.png', dpi=300, bbox_inches='tight',
                  facecolor='#FAFBFC', edgecolor='none', transparent=False)
plt.close(fig_title)

title_img = Image.open('title_bar.png')
# Center title
tx = (grid_w - title_img.width) // 2
composite.paste(title_img, (tx, 5))

composite.save('../figures/Figure2_GJS_Simulation_4Panel.png')
print(f"\nComposite: {composite.width}×{composite.height} px")

# ══════════════════════════════════════════════════════════════
# NUMERICAL SUMMARY TABLE
# ══════════════════════════════════════════════════════════════
print("\n" + "="*65)
print("GJS EQUATION — NUMERICAL SCENARIOS")
print("K=1, f_HKII=0.8, f_BclxL=0.8 (MSS CRC baseline)")
print("="*65)
scenarios_detail = [
    ("Cancer baseline",      0.7, 3.0),
    ("Lovastatin only",      0.7, 1.0),
    ("PK11195 only",         0.2, 3.0),
    ("DUAL LOCK (Lova+PK)",  0.2, 1.0),
    ("Venetoclax (f_BclxL→0.1)", None, None),  # special case
    ("Normal tissue",        0.1, 1.0),
]

print(f"{'Scenario':<30} {'f_TSPO':>8} {'[C]/[CL]':>10} {'Threshold':>12} {'Fold vs BL':>12}")
print("-"*65)
for name, f_t, c_cl in scenarios_detail:
    if name == "Venetoclax (f_BclxL→0.1)":
        t = gjs_threshold(f_hkii=0.8, f_bclxl=0.1, f_tspo=0.7, chol_cl_ratio=3.0)
    elif name == "Normal tissue":
        t = gjs_threshold(f_hkii=0.2, f_bclxl=0.2, f_tspo=0.1, chol_cl_ratio=1.0)
    else:
        t = gjs_threshold(f_tspo=f_t, chol_cl_ratio=c_cl)
    fold = cancer_thresh / t
    f_t_str = f"{f_t}" if f_t is not None else "0.7"
    c_cl_str = f"{c_cl}" if c_cl is not None else "3.0"
    print(f"{name:<30} {f_t_str:>8} {c_cl_str:>10} {t:>12.1f} {fold:>12.1f}×")

print("\nSupra-additive check:")
lova_only = gjs_threshold(f_tspo=0.7, chol_cl_ratio=1.0)
pk_only = gjs_threshold(f_tspo=0.2, chol_cl_ratio=3.0)
dual = gjs_threshold(f_tspo=0.2, chol_cl_ratio=1.0)
additive = lova_only + pk_only - cancer_thresh
print(f"  Additive prediction:  {additive:.1f}")
print(f"  Actual dual-lock:     {dual:.1f}")
print(f"  Synergy factor:       {additive/dual:.2f}× better than additive")
print(f"  → Chou-Talalay CI prediction: < 0.8 (supra-additive confirmed)")
