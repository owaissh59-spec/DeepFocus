# -*- coding: utf-8 -*-
"""Generate schematic diagrams (PNG) for the MPH204T notes using matplotlib."""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, FancyArrowPatch, Polygon

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figures")
os.makedirs(OUT, exist_ok=True)

BLUE = "#1f4e9c"
RED = "#c0392b"
GREEN = "#1f7a33"
MAROON = "#5B1A38"
AMBER = "#E0A800"
plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans", "figure.dpi": 150})


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("  wrote", name)


# ---------------------------------------------------------------- Unit I
def bcs():
    fig, ax = plt.subplots(figsize=(6, 4.2))
    ax.axhline(1, color="k", lw=1); ax.axvline(1, color="k", lw=1)
    data = [(0.5, 1.5, "Class I", "High Solubility\nHigh Permeability", "#d7f0d7"),
            (1.5, 1.5, "Class II", "Low Solubility\nHigh Permeability", "#fde2b3"),
            (0.5, 0.5, "Class III", "High Solubility\nLow Permeability", "#cfe0f7"),
            (1.5, 0.5, "Class IV", "Low Solubility\nLow Permeability", "#f5c6cb")]
    for x, y, t, s, c in data:
        ax.add_patch(Rectangle((x - 0.5, y - 0.5), 1, 1, color=c, ec="k"))
        ax.text(x, y + 0.22, t, ha="center", va="center", fontweight="bold", fontsize=12)
        ax.text(x, y - 0.15, s, ha="center", va="center", fontsize=9.5)
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_xlim(0, 2); ax.set_ylim(0, 2)
    ax.set_xlabel("Permeability  \u2192", fontweight="bold")
    ax.set_ylabel("Solubility  \u2192", fontweight="bold")
    ax.set_title("Biopharmaceutics Classification System (BCS)", fontweight="bold", color=MAROON)
    save(fig, "bcs.png")


def ph_solubility():
    fig, ax = plt.subplots(figsize=(6, 3.8))
    ph = np.linspace(1, 10, 200)
    acid = 0.05 * (1 + 10 ** (ph - 4.5))
    base = 0.05 * (1 + 10 ** (7.5 - ph))
    ax.plot(ph, np.log10(acid), color=RED, lw=2.2, label="Weak acid (pKa ~4.5)")
    ax.plot(ph, np.log10(base), color=BLUE, lw=2.2, label="Weak base (pKa ~7.5)")
    ax.set_xlabel("pH", fontweight="bold")
    ax.set_ylabel("log (Solubility)", fontweight="bold")
    ax.set_title("pH\u2013Solubility Profile", fontweight="bold", color=MAROON)
    ax.legend(fontsize=9); ax.grid(alpha=0.3)
    save(fig, "ph_solubility.png")


def crystal_habit():
    fig, axes = plt.subplots(1, 5, figsize=(8, 2.1))
    shapes = {
        "Tabular": [(0.2, 0.3), (0.8, 0.35), (0.75, 0.7), (0.15, 0.65)],
        "Prismatic": [(0.35, 0.15), (0.65, 0.15), (0.7, 0.85), (0.3, 0.85)],
        "Acicular": [(0.42, 0.1), (0.58, 0.1), (0.55, 0.9), (0.45, 0.9)],
        "Platy": [(0.15, 0.4), (0.85, 0.42), (0.83, 0.58), (0.17, 0.56)],
        "Bladed": [(0.3, 0.12), (0.5, 0.1), (0.62, 0.9), (0.42, 0.9)],
    }
    for ax, (name, pts) in zip(axes, shapes.items()):
        ax.add_patch(Polygon(pts, closed=True, facecolor="#cfe0f7", edgecolor=BLUE, lw=1.6))
        ax.set_title(name, fontsize=10, fontweight="bold")
        ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
    fig.suptitle("Common Crystal Habits", fontweight="bold", color=MAROON, y=1.05)
    save(fig, "crystal_habit.png")


def angle_repose():
    fig, ax = plt.subplots(figsize=(5.4, 3.2))
    ax.add_patch(Polygon([(0, 0), (4, 0), (2, 1.6)], closed=True,
                         facecolor="#fde2b3", edgecolor=AMBER, lw=1.8))
    ax.annotate("", xy=(2, 1.6), xytext=(2, 0), arrowprops=dict(arrowstyle="-", ls="--"))
    ax.text(2.1, 0.8, "h", fontsize=12)
    ax.annotate("", xy=(4, 0), xytext=(2, 0), arrowprops=dict(arrowstyle="<->"))
    ax.text(3, -0.18, "r", fontsize=12, ha="center")
    ax.text(0.55, 0.12, r"$\theta$", fontsize=15, color=RED)
    ax.text(2, -0.6, r"tan $\theta$ = h / r", ha="center", fontsize=12, fontweight="bold")
    ax.set_xlim(-0.4, 4.4); ax.set_ylim(-0.9, 2)
    ax.axis("off")
    ax.set_title("Angle of Repose", fontweight="bold", color=MAROON)
    save(fig, "angle_repose.png")


def dsc():
    fig, ax = plt.subplots(figsize=(6, 3.4))
    x = np.linspace(0, 10, 500)
    y = np.zeros_like(x)
    y -= 1.2 * np.exp(-((x - 4) ** 2) / 0.25)   # endotherm (melting)
    y += 0.9 * np.exp(-((x - 7) ** 2) / 0.3)    # exotherm (crystallisation)
    ax.plot(x, y, color=BLUE, lw=2)
    ax.axhline(0, color="k", lw=0.6)
    ax.annotate("Endotherm\n(melting)", xy=(4, -1.1), xytext=(1.5, -1.0),
                fontsize=9, color=RED, arrowprops=dict(arrowstyle="->", color=RED))
    ax.annotate("Exotherm\n(recrystallisation)", xy=(7, 0.85), xytext=(7.6, 0.5),
                fontsize=9, color=GREEN, arrowprops=dict(arrowstyle="->", color=GREEN))
    ax.set_xlabel("Temperature (\u00b0C)  \u2192", fontweight="bold")
    ax.set_ylabel("Heat flow", fontweight="bold")
    ax.set_yticks([]); ax.set_title("DSC Thermogram (schematic)", fontweight="bold", color=MAROON)
    save(fig, "dsc.png")


def preform_flow():
    fig, ax = plt.subplots(figsize=(5.0, 5.2))
    steps = ["Bulk characterisation\n(organoleptic, purity, particle size)",
             "Solubility studies\n(pKa, log P, pH-solubility)",
             "Crystal / solid-state\n(polymorphism, habit)",
             "Powder properties\n(flow, density, compressibility)",
             "Stability screening\n(solution & solid state)",
             "Drug\u2013excipient\ncompatibility",
             "Dosage form design"]
    y = np.linspace(9, 0, len(steps))
    for i, (s, yy) in enumerate(zip(steps, y)):
        col = "#cfe0f7" if i < len(steps) - 1 else "#d7f0d7"
        ax.add_patch(FancyBboxPatch((0.1, yy), 3.6, 0.95, boxstyle="round,pad=0.05",
                                    fc=col, ec=BLUE, lw=1.4))
        ax.text(1.9, yy + 0.47, s, ha="center", va="center", fontsize=9)
        if i < len(steps) - 1:
            ax.annotate("", xy=(1.9, yy - 0.05), xytext=(1.9, yy - 0.35 + 0.35),
                        arrowprops=dict(arrowstyle="->", color=MAROON, lw=1.6))
    ax.set_xlim(0, 3.8); ax.set_ylim(-0.5, 10.3); ax.axis("off")
    ax.set_title("Preformulation Work-flow", fontweight="bold", color=MAROON)
    save(fig, "preform_flow.png")


# ---------------------------------------------------------------- Unit II
def factorial_cube():
    fig = plt.figure(figsize=(5.2, 4.6))
    ax = fig.add_subplot(111, projection="3d")
    r = [0, 1]
    import itertools
    pts = list(itertools.product(r, r, r))
    for s in pts:
        ax.scatter(*s, color=RED, s=55)
    edges = [(0, 1), (0, 2), (0, 4), (1, 3), (1, 5), (2, 3),
             (2, 6), (3, 7), (4, 5), (4, 6), (5, 7), (6, 7)]
    for a, b in edges:
        xs = [pts[a][0], pts[b][0]]; ys = [pts[a][1], pts[b][1]]; zs = [pts[a][2], pts[b][2]]
        ax.plot(xs, ys, zs, color=BLUE, lw=1.3)
    ax.set_xlabel("Factor A"); ax.set_ylabel("Factor B"); ax.set_zlabel("Factor C")
    ax.set_xticks([0, 1]); ax.set_yticks([0, 1]); ax.set_zticks([0, 1])
    ax.set_xticklabels(["\u2212", "+"]); ax.set_yticklabels(["\u2212", "+"]); ax.set_zticklabels(["\u2212", "+"])
    ax.set_title("2$^3$ Full Factorial Design (8 runs)", fontweight="bold", color=MAROON)
    save(fig, "factorial_cube.png")


def response_surface():
    fig, ax = plt.subplots(figsize=(5.4, 4.0))
    x = np.linspace(-2, 2, 100); y = np.linspace(-2, 2, 100)
    X, Y = np.meshgrid(x, y)
    Z = -(X ** 2 + Y ** 2) + 0.5 * X * Y + 6
    cs = ax.contourf(X, Y, Z, levels=12, cmap="YlOrRd")
    ax.contour(X, Y, Z, levels=12, colors="k", linewidths=0.4)
    ax.plot(0.15, 0.15, "b*", ms=16)
    ax.text(0.3, 0.3, "Optimum", color=BLUE, fontweight="bold")
    fig.colorbar(cs, label="Response")
    ax.set_xlabel("Factor X$_1$", fontweight="bold"); ax.set_ylabel("Factor X$_2$", fontweight="bold")
    ax.set_title("Response Surface / Contour Plot", fontweight="bold", color=MAROON)
    save(fig, "response_surface.png")


def ofat_vs_factorial():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.6, 3.4))
    a1.scatter([0, 1, 0], [0, 0, 1], color=RED, s=70)
    a1.set_title("OFAT (3 runs)", fontweight="bold")
    a2.scatter([0, 1, 0, 1], [0, 0, 1, 1], color=GREEN, s=70)
    a2.set_title("Factorial (4 runs)", fontweight="bold")
    for a in (a1, a2):
        a.set_xlim(-0.4, 1.4); a.set_ylim(-0.4, 1.4)
        a.set_xlabel("Factor A"); a.set_ylabel("Factor B")
        a.set_xticks([0, 1]); a.set_yticks([0, 1])
        a.set_xticklabels(["\u2212", "+"]); a.set_yticklabels(["\u2212", "+"])
        a.grid(alpha=0.3)
    fig.suptitle("OFAT vs Factorial Design", fontweight="bold", color=MAROON)
    save(fig, "ofat_vs_factorial.png")


# ---------------------------------------------------------------- Unit III
def diffusion_layer():
    fig, ax = plt.subplots(figsize=(6.2, 3.6))
    ax.add_patch(Rectangle((0, 0), 1.4, 3, color="#b0b0b0", ec="k"))
    ax.text(0.7, 1.5, "Solid\ndrug", ha="center", va="center", fontweight="bold")
    ax.add_patch(Rectangle((1.4, 0), 1.2, 3, color="#cfe0f7", alpha=0.7, ec="k", ls="--"))
    ax.text(2.0, 2.7, "Diffusion\nlayer (h)", ha="center", fontsize=9)
    ax.add_patch(Rectangle((2.6, 0), 3.0, 3, color="#eef5ff", ec="k"))
    ax.text(4.1, 1.5, "Bulk solution\n(Ct)", ha="center", va="center")
    ax.annotate("", xy=(4.4, 1.5), xytext=(1.5, 1.5),
                arrowprops=dict(arrowstyle="->", color=RED, lw=2))
    ax.text(1.45, 2.2, "Cs", color=RED, fontweight="bold")
    ax.set_xlim(0, 5.7); ax.set_ylim(0, 3.4); ax.axis("off")
    ax.set_title("Diffusion-Layer Model (Noyes\u2013Whitney)", fontweight="bold", color=MAROON)
    save(fig, "diffusion_layer.png")


def phase_solubility():
    fig, ax = plt.subplots(figsize=(6, 4.0))
    L = np.linspace(0, 10, 100)
    ax.plot(L, 2 + 0.5 * L, color=BLUE, lw=2, label="A$_L$ (linear)")
    ax.plot(L, 2 + 0.3 * L + 0.03 * L ** 2, color=GREEN, lw=2, label="A$_P$ (positive)")
    ax.plot(L, 2 + 0.55 * L - 0.02 * L ** 2, color=RED, lw=2, label="A$_N$ (negative)")
    bs = np.where(L < 5, 2 + 0.5 * L, 4.5)
    ax.plot(L, bs, color="purple", lw=2, ls="--", label="B$_S$ (limited sol.)")
    ax.set_xlabel("Ligand concentration \u2192", fontweight="bold")
    ax.set_ylabel("Drug solubility \u2192", fontweight="bold")
    ax.set_title("Phase-Solubility Diagrams", fontweight="bold", color=MAROON)
    ax.legend(fontsize=9); ax.grid(alpha=0.3)
    save(fig, "phase_solubility.png")


def dissolution_apparatus():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.2, 4.2))
    for a in (a1, a2):
        a.add_patch(Rectangle((0.2, 0.2), 2.6, 3.2, fc="#eef5ff", ec="k"))
        a.set_xlim(0, 3); a.set_ylim(0, 4); a.axis("off")
    a1.add_patch(Rectangle((1.3, 2.4), 0.06, 1.4, color="k"))
    a1.add_patch(Rectangle((1.05, 1.9), 0.55, 0.55, fc="#b0b0b0", ec="k"))
    a1.text(1.5, 3.9, "shaft", fontsize=8, ha="center")
    a1.set_title("USP I \u2013 Basket", fontweight="bold", color=MAROON)
    a2.add_patch(Rectangle((1.47, 1.5), 0.06, 2.3, color="k"))
    a2.add_patch(Polygon([(1.1, 1.5), (1.9, 1.5), (1.75, 1.2), (1.25, 1.2)], closed=True,
                         fc="#b0b0b0", ec="k"))
    a2.set_title("USP II \u2013 Paddle", fontweight="bold", color=MAROON)
    fig.suptitle("Dissolution Test Apparatus", fontweight="bold", color=MAROON, y=1.02)
    save(fig, "dissolution_apparatus.png")


def release_profiles():
    fig, ax = plt.subplots(figsize=(6, 3.8))
    t = np.linspace(0, 10, 100)
    ax.plot(t, 10 * t, color=BLUE, lw=2, label="Zero order")
    ax.plot(t, 100 * (1 - np.exp(-0.4 * t)), color=RED, lw=2, label="First order")
    ax.plot(t, 32 * np.sqrt(t), color=GREEN, lw=2, label="Higuchi (\u221at)")
    ax.set_ylim(0, 105)
    ax.set_xlabel("Time \u2192", fontweight="bold"); ax.set_ylabel("% Drug released \u2192", fontweight="bold")
    ax.set_title("Drug Release Kinetic Profiles", fontweight="bold", color=MAROON)
    ax.legend(fontsize=9); ax.grid(alpha=0.3)
    save(fig, "release_profiles.png")


def ivivc():
    fig, ax = plt.subplots(figsize=(5.4, 3.8))
    x = np.linspace(0, 100, 50)
    ax.plot(x, 0.95 * x + 2, color=MAROON, lw=2)
    ax.scatter(np.linspace(5, 95, 8), 0.95 * np.linspace(5, 95, 8) + 2 + np.random.RandomState(1).randn(8) * 2,
               color=RED, zorder=3)
    ax.set_xlabel("% Dissolved in-vitro", fontweight="bold")
    ax.set_ylabel("% Absorbed in-vivo", fontweight="bold")
    ax.set_title("Level A IVIVC (point-to-point)", fontweight="bold", color=MAROON)
    ax.grid(alpha=0.3)
    save(fig, "ivivc.png")


# ---------------------------------------------------------------- Unit IV
def order_kinetics():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.6, 3.4))
    t = np.linspace(0, 10, 50)
    a1.plot(t, 100 - 6 * t, color=BLUE, lw=2, label="Zero order")
    a1.plot(t, 100 * np.exp(-0.2 * t), color=RED, lw=2, label="First order")
    a1.set_title("Concentration vs Time", fontweight="bold")
    a1.set_xlabel("Time"); a1.set_ylabel("Conc. (C)"); a1.legend(fontsize=9); a1.grid(alpha=0.3)
    a2.plot(t, np.log10(100 - 6 * t + 1e-9), color=BLUE, lw=2, label="Zero (log C)")
    a2.plot(t, np.log10(100 * np.exp(-0.2 * t)), color=RED, lw=2, label="First (log C)")
    a2.set_title("log C vs Time", fontweight="bold")
    a2.set_xlabel("Time"); a2.set_ylabel("log C"); a2.legend(fontsize=9); a2.grid(alpha=0.3)
    fig.suptitle("Zero vs First Order Degradation", fontweight="bold", color=MAROON, y=1.03)
    save(fig, "order_kinetics.png")


def arrhenius():
    fig, ax = plt.subplots(figsize=(5.6, 3.6))
    inv_t = np.linspace(3.0, 3.5, 20)
    logk = -2.2 * inv_t + 6.5
    ax.plot(inv_t, logk, color=MAROON, lw=2)
    ax.scatter(inv_t[::4], logk[::4], color=RED, zorder=3)
    ax.annotate("slope = \u2212Ea / 2.303R", xy=(3.25, -0.6), fontsize=10, color=BLUE)
    ax.set_xlabel("1 / T  (\u00d710$^{-3}$ K$^{-1}$)", fontweight="bold")
    ax.set_ylabel("log k", fontweight="bold")
    ax.set_title("Arrhenius Plot", fontweight="bold", color=MAROON)
    ax.grid(alpha=0.3)
    save(fig, "arrhenius.png")


def ph_rate():
    fig, ax = plt.subplots(figsize=(5.8, 3.6))
    ph = np.linspace(1, 10, 200)
    logk = np.log10(10 ** (-ph) + 10 ** (ph - 12) + 1e-7)
    ax.plot(ph, logk, color=RED, lw=2.2)
    ax.axvline(6, color=GREEN, ls="--")
    ax.text(6.1, logk.min() + 0.4, "pH of maximum\nstability", color=GREEN, fontsize=9)
    ax.set_xlabel("pH", fontweight="bold"); ax.set_ylabel("log k$_{obs}$", fontweight="bold")
    ax.set_title("pH\u2013Rate Profile", fontweight="bold", color=MAROON)
    ax.grid(alpha=0.3)
    save(fig, "ph_rate.png")


# ---------------------------------------------------------------- Unit V
def emulsion_types():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.2, 3.6))
    rng = np.random.RandomState(3)
    a1.add_patch(Rectangle((0, 0), 4, 4, fc="#eef5ff", ec="k"))
    for _ in range(14):
        x, y = rng.uniform(0.4, 3.6, 2)
        a1.add_patch(Circle((x, y), 0.32, fc="#fde2b3", ec=AMBER))
    a1.set_title("Oil-in-Water (o/w)\n(vanishing cream)", fontweight="bold", fontsize=10)
    a2.add_patch(Rectangle((0, 0), 4, 4, fc="#fde2b3", ec="k"))
    for _ in range(14):
        x, y = rng.uniform(0.4, 3.6, 2)
        a2.add_patch(Circle((x, y), 0.32, fc="#cfe0f7", ec=BLUE))
    a2.set_title("Water-in-Oil (w/o)\n(cold cream)", fontweight="bold", fontsize=10)
    for a in (a1, a2):
        a.set_xlim(-0.2, 4.2); a.set_ylim(-0.2, 4.2); a.axis("off")
    fig.suptitle("Emulsion Types", fontweight="bold", color=MAROON, y=1.02)
    save(fig, "emulsion_types.png")


def hlb_scale():
    fig, ax = plt.subplots(figsize=(7.6, 2.4))
    ax.imshow([np.linspace(0, 1, 256)], aspect="auto", extent=[0, 20, 0, 1], cmap="RdYlBu")
    for x in [3, 6, 8, 13, 15, 18]:
        ax.axvline(x, color="k", lw=0.6)
    labels = [(1.5, "W/O\nemulsifier"), (4.5, "Wetting"), (7, "W/O"),
              (10.5, "O/W\nemulsifier"), (14, "Detergent"), (16.5, "Solubiliser")]
    for x, t in labels:
        ax.text(x, 1.15, t, ha="center", fontsize=8)
    ax.set_yticks([]); ax.set_xticks(range(0, 21, 2))
    ax.set_xlabel("HLB value", fontweight="bold")
    ax.set_title("HLB Scale & Surfactant Applications", fontweight="bold", color=MAROON)
    save(fig, "hlb_scale.png")


def main():
    print("Generating figures ...")
    bcs(); ph_solubility(); crystal_habit(); angle_repose(); dsc(); preform_flow()
    factorial_cube(); response_surface(); ofat_vs_factorial()
    diffusion_layer(); phase_solubility(); dissolution_apparatus(); release_profiles(); ivivc()
    order_kinetics(); arrhenius(); ph_rate()
    emulsion_types(); hlb_scale()
    print("Done. Figures in", OUT)


if __name__ == "__main__":
    main()
