# -*- coding: utf-8 -*-
"""Generate schematic diagrams (PNG) for the MPT102T
"Advances in Drug Delivery System" notes using matplotlib."""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import (FancyBboxPatch, Circle, Rectangle, FancyArrowPatch,
                                Polygon, Ellipse, Wedge, Arc)

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figures")
os.makedirs(OUT, exist_ok=True)

BLUE = "#1f4e9c"
RED = "#c0392b"
GREEN = "#1f7a33"
MAROON = "#5B1A38"
AMBER = "#E0A800"
PURPLE = "#6A1B9A"
plt.rcParams.update({"font.size": 11, "font.family": "DejaVu Sans", "figure.dpi": 150})


def save(fig, name):
    fig.savefig(os.path.join(OUT, name), bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("  wrote", name)


# =====================================================================
#  UNIT I  -  SR / CR CONCEPTS
# =====================================================================
def plasma_profiles():
    fig, ax = plt.subplots(figsize=(6.6, 4.0))
    t = np.linspace(0, 24, 500)
    # conventional multiple dosing (peaks & troughs)
    conv = np.zeros_like(t)
    for dose_t in [0, 6, 12, 18]:
        conv += 3.2 * np.where(t >= dose_t, np.exp(-0.5 * (t - dose_t)) *
                               (1 - np.exp(-1.5 * (t - dose_t))), 0)
    # controlled release - flat
    cr = 2.3 * (1 - np.exp(-0.9 * t)) * np.exp(-0.01 * t)
    # sustained release - gentle rise & slow decline
    sr = 3.0 * (1 - np.exp(-0.8 * t)) * np.exp(-0.03 * t)
    ax.axhspan(1.2, 3.2, color="#d7f0d7", alpha=0.5)
    ax.axhline(3.2, color=RED, ls="--", lw=1)
    ax.axhline(1.2, color=BLUE, ls="--", lw=1)
    ax.text(24.2, 3.2, "MSC", color=RED, fontsize=9, va="center")
    ax.text(24.2, 1.2, "MEC", color=BLUE, fontsize=9, va="center")
    ax.text(0.3, 2.2, "Therapeutic window", color=GREEN, fontsize=9)
    ax.plot(t, conv, color="#888888", lw=1.8, label="Conventional (multiple dose)")
    ax.plot(t, sr, color=AMBER, lw=2.4, label="Sustained release")
    ax.plot(t, cr, color=MAROON, lw=2.4, label="Controlled release")
    ax.set_xlim(0, 24); ax.set_ylim(0, 4.2)
    ax.set_xlabel("Time (h)  \u2192", fontweight="bold")
    ax.set_ylabel("Plasma drug concentration  \u2192", fontweight="bold")
    ax.set_title("Plasma Profiles: Conventional vs SR vs CR", fontweight="bold", color=MAROON)
    ax.legend(fontsize=8.5, loc="upper right"); ax.grid(alpha=0.25)
    save(fig, "plasma_profiles.png")


def release_terminology():
    fig, ax = plt.subplots(figsize=(6.6, 3.9))
    t = np.linspace(0, 12, 400)
    immediate = 100 * (1 - np.exp(-2.5 * t))
    sustained = 100 * (1 - np.exp(-0.35 * t))
    delayed = np.where(t < 3, 0, 100 * (1 - np.exp(-2.2 * (t - 3))))
    # repeat action - two pulses
    repeat = 55 * (1 - np.exp(-3 * t)) + np.where(t > 5, 45 * (1 - np.exp(-3 * (t - 5))), 0)
    ax.plot(t, immediate, color=BLUE, lw=2, label="Immediate release")
    ax.plot(t, sustained, color=GREEN, lw=2, label="Sustained release")
    ax.plot(t, delayed, color=RED, lw=2, label="Delayed (enteric) release")
    ax.plot(t, np.clip(repeat, 0, 100), color=PURPLE, lw=2, label="Repeat action")
    ax.set_xlim(0, 12); ax.set_ylim(0, 105)
    ax.set_xlabel("Time (h)  \u2192", fontweight="bold")
    ax.set_ylabel("% Drug released  \u2192", fontweight="bold")
    ax.set_title("Modified-Release Terminology", fontweight="bold", color=MAROON)
    ax.legend(fontsize=8.5); ax.grid(alpha=0.25)
    save(fig, "release_terminology.png")


def cdds_classification():
    fig, ax = plt.subplots(figsize=(7.6, 4.6))
    ax.axis("off")
    ax.add_patch(FancyBboxPatch((2.8, 5.2), 2.4, 0.7, boxstyle="round,pad=0.05",
                                fc="#d7f0d7", ec=GREEN, lw=1.6))
    ax.text(4.0, 5.55, "Oral Controlled\nDDS", ha="center", va="center", fontweight="bold", fontsize=9)
    groups = ["Diffusion\ncontrolled", "Dissolution\ncontrolled", "Osmotically\ncontrolled",
              "Ion-exchange\nresin", "Bioerodible /\nerosion"]
    subs = ["Reservoir\n& Matrix", "Encapsulation\n& Matrix", "EOP / OROS\npush-pull",
            "Drug-resinate", "Surface /\nbulk erosion"]
    x = np.linspace(0.2, 6.6, len(groups))
    for xi, g, s in zip(x, groups, subs):
        ax.add_patch(FancyBboxPatch((xi, 3.0), 1.35, 0.95, boxstyle="round,pad=0.04",
                                    fc="#cfe0f7", ec=BLUE, lw=1.3))
        ax.text(xi + 0.67, 3.47, g, ha="center", va="center", fontsize=8)
        ax.annotate("", xy=(xi + 0.67, 3.95), xytext=(4.0, 5.2),
                    arrowprops=dict(arrowstyle="->", color=MAROON, lw=1.1))
        ax.add_patch(FancyBboxPatch((xi, 1.6), 1.35, 0.9, boxstyle="round,pad=0.04",
                                    fc="#fde2b3", ec=AMBER, lw=1.2))
        ax.text(xi + 0.67, 2.05, s, ha="center", va="center", fontsize=7.5)
        ax.annotate("", xy=(xi + 0.67, 2.5), xytext=(xi + 0.67, 3.0),
                    arrowprops=dict(arrowstyle="->", color="#555", lw=1))
    ax.set_xlim(0, 8.2); ax.set_ylim(1.3, 6.2)
    ax.set_title("Classification of Oral Controlled DDS", fontweight="bold", color=MAROON)
    save(fig, "cdds_classification.png")


# =====================================================================
#  UNIT II  -  ORAL SR MECHANISMS
# =====================================================================
def reservoir_matrix():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.6, 3.8))
    # reservoir
    a1.add_patch(Circle((0.5, 0.5), 0.42, transform=a1.transAxes, fc="#eef5ff", ec="k", lw=1.5))
    a1.add_patch(Circle((0.5, 0.5), 0.27, transform=a1.transAxes, fc="#fde2b3", ec=AMBER, lw=1.4))
    a1.text(0.5, 0.5, "Drug\ncore", ha="center", va="center", transform=a1.transAxes, fontsize=9)
    a1.text(0.5, 0.83, "Polymer membrane", ha="center", transform=a1.transAxes, fontsize=8.5, color=BLUE)
    a1.annotate("", xy=(0.9, 0.5), xytext=(0.62, 0.5), transform=a1.transAxes,
                arrowprops=dict(arrowstyle="->", color=RED, lw=1.6))
    a1.set_title("Reservoir (membrane)\nsystem", fontweight="bold", fontsize=10)
    # matrix
    a2.add_patch(Circle((0.5, 0.5), 0.42, transform=a2.transAxes, fc="#cfe0f7", ec="k", lw=1.5))
    rng = np.random.RandomState(4)
    for _ in range(30):
        ang = rng.uniform(0, 2 * np.pi); rr = rng.uniform(0, 0.38)
        a2.add_patch(Circle((0.5 + rr * np.cos(ang), 0.5 + rr * np.sin(ang)), 0.02,
                            transform=a2.transAxes, fc=AMBER, ec=AMBER))
    a2.text(0.5, 0.83, "Drug dispersed in matrix", ha="center", transform=a2.transAxes,
            fontsize=8.5, color=BLUE)
    a2.set_title("Matrix (monolithic)\nsystem", fontweight="bold", fontsize=10)
    for a in (a1, a2):
        a.axis("off")
    fig.suptitle("Diffusion-Controlled Systems", fontweight="bold", color=MAROON, y=1.03)
    save(fig, "reservoir_matrix.png")


def dissolution_controlled():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.6, 3.6))
    # encapsulation - beads with different coat thickness
    rng = np.random.RandomState(7)
    for i, cx in enumerate(np.linspace(0.2, 0.8, 4)):
        th = 0.02 + i * 0.012
        a1.add_patch(Circle((cx, 0.5), 0.09, transform=a1.transAxes, fc="#cfe0f7", ec=BLUE, lw=1 + i))
        a1.add_patch(Circle((cx, 0.5), 0.09 - th, transform=a1.transAxes, fc="#fde2b3", ec=AMBER))
    a1.set_title("Encapsulation / coated\nbeads (varying coat)", fontweight="bold", fontsize=9.5)
    # matrix dissolution
    a2.add_patch(Circle((0.5, 0.5), 0.4, transform=a2.transAxes, fc="#e7d9ef", ec=PURPLE, lw=1.5))
    for _ in range(26):
        ang = rng.uniform(0, 2 * np.pi); rr = rng.uniform(0, 0.36)
        a2.add_patch(Circle((0.5 + rr * np.cos(ang), 0.5 + rr * np.sin(ang)), 0.018,
                            transform=a2.transAxes, fc=RED))
    a2.text(0.5, 0.86, "Slowly dissolving matrix", ha="center", transform=a2.transAxes,
            fontsize=8.5, color=PURPLE)
    a2.set_title("Matrix dissolution\nsystem", fontweight="bold", fontsize=9.5)
    for a in (a1, a2):
        a.axis("off")
    fig.suptitle("Dissolution-Controlled Systems", fontweight="bold", color=MAROON, y=1.03)
    save(fig, "dissolution_controlled.png")


def osmotic_pump():
    fig, ax = plt.subplots(figsize=(5.4, 4.2))
    ax.add_patch(Circle((0.5, 0.5), 0.4, transform=ax.transAxes, fc="none", ec="k", lw=2))
    ax.add_patch(Wedge((0.5, 0.5), 0.4, 0, 360, width=0.05, transform=ax.transAxes,
                       fc="#cfe0f7", ec=BLUE))
    ax.text(0.5, 0.9, "Semipermeable membrane", ha="center", transform=ax.transAxes,
            fontsize=8.5, color=BLUE)
    ax.add_patch(Circle((0.5, 0.5), 0.35, transform=ax.transAxes, fc="#fde2b3", ec=AMBER))
    ax.text(0.5, 0.5, "Osmotic core\n(drug + osmogen)", ha="center", va="center",
            transform=ax.transAxes, fontsize=9)
    # laser drilled orifice
    ax.add_patch(Circle((0.5, 0.1), 0.02, transform=ax.transAxes, fc="white", ec="k"))
    ax.annotate("Drug solution out\n(laser-drilled orifice)", xy=(0.5, 0.1), xytext=(0.5, -0.08),
                transform=ax.transAxes, ha="center", fontsize=8, color=RED,
                arrowprops=dict(arrowstyle="->", color=RED))
    ax.annotate("Water in", xy=(0.12, 0.5), xytext=(-0.05, 0.5), transform=ax.transAxes,
                fontsize=8, color=GREEN, arrowprops=dict(arrowstyle="->", color=GREEN))
    ax.axis("off")
    ax.set_title("Elementary Osmotic Pump (EOP)", fontweight="bold", color=MAROON)
    save(fig, "osmotic_pump.png")


def ion_exchange():
    fig, ax = plt.subplots(figsize=(6.6, 3.4))
    ax.text(0.02, 0.6, "Resin\u207b\u2013Drug\u207a", fontsize=12, fontweight="bold", color=MAROON)
    ax.text(0.30, 0.6, "+  X\u207a", fontsize=12, color=BLUE)
    ax.annotate("", xy=(0.55, 0.6), xytext=(0.45, 0.6),
                arrowprops=dict(arrowstyle="->", lw=2, color="k"))
    ax.text(0.58, 0.6, "Resin\u207b\u2013X\u207a", fontsize=12, fontweight="bold", color=GREEN)
    ax.text(0.86, 0.6, "+  Drug\u207a", fontsize=12, color=RED)
    ax.text(0.5, 0.25, "Exchange with counter-ions in GIT releases the free drug",
            ha="center", fontsize=9, style="italic", color="#555")
    ax.axis("off")
    ax.set_title("Ion-Exchange Resin Mechanism (cationic drug)", fontweight="bold", color=MAROON)
    save(fig, "ion_exchange.png")


def bioerosion():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.4, 3.6))
    rng = np.random.RandomState(2)
    # bulk erosion - shrinking + internal porosity
    for a, title, mode in [(a1, "Bulk erosion", "bulk"), (a2, "Surface erosion", "surface")]:
        for i, r in enumerate([0.4, 0.3, 0.2]):
            alpha = 1 - i * 0.28
            a.add_patch(Circle((0.5, 0.5), r, transform=a.transAxes,
                               fc="#cfe0f7", ec=BLUE, alpha=alpha, lw=1.4))
        if mode == "bulk":
            for _ in range(24):
                ang = rng.uniform(0, 2 * np.pi); rr = rng.uniform(0, 0.36)
                a.add_patch(Circle((0.5 + rr * np.cos(ang), 0.5 + rr * np.sin(ang)), 0.012,
                                   transform=a.transAxes, fc="white", ec="none"))
        a.set_title(title, fontweight="bold", fontsize=10)
        a.axis("off")
    a1.text(0.5, 0.04, "erodes throughout", ha="center", transform=a1.transAxes, fontsize=8)
    a2.text(0.5, 0.04, "erodes layer by layer", ha="center", transform=a2.transAxes, fontsize=8)
    fig.suptitle("Bioerodible / Erosion Systems", fontweight="bold", color=MAROON, y=1.03)
    save(fig, "bioerosion.png")


def mucoadhesion():
    fig, ax = plt.subplots(figsize=(6.8, 3.6))
    ax.add_patch(Rectangle((0, 0), 10, 1.1, fc="#f5c6cb", ec="k"))
    ax.text(5, 0.55, "Mucus / epithelial surface", ha="center", va="center", fontsize=9)
    stages = [("1. Contact\n(wetting)", 1.6), ("2. Swelling", 4.0),
              ("3. Interpenetration\nof chains", 6.4), ("4. Entanglement\n& bonding", 8.8)]
    for txt, x in stages:
        ax.add_patch(FancyBboxPatch((x - 0.9, 1.7), 1.8, 1.0, boxstyle="round,pad=0.05",
                                    fc="#d7f0d7", ec=GREEN, lw=1.3))
        ax.text(x, 2.2, txt, ha="center", va="center", fontsize=8)
        ax.annotate("", xy=(x, 1.15), xytext=(x, 1.7),
                    arrowprops=dict(arrowstyle="->", color=MAROON, lw=1.2))
    for x in [2.8, 5.2, 7.6]:
        ax.annotate("", xy=(x + 0.6, 2.2), xytext=(x, 2.2),
                    arrowprops=dict(arrowstyle="->", color="#555", lw=1.3))
    ax.set_xlim(0, 10); ax.set_ylim(-0.2, 3.0); ax.axis("off")
    ax.set_title("Stages / Theory of Mucoadhesion", fontweight="bold", color=MAROON)
    save(fig, "mucoadhesion.png")


# =====================================================================
#  UNIT III  -  MICROENCAPSULATION
# =====================================================================
def microcapsule_types():
    fig, (a1, a2, a3) = plt.subplots(1, 3, figsize=(7.8, 2.8))
    # mononuclear
    a1.add_patch(Circle((0.5, 0.5), 0.4, transform=a1.transAxes, fc="#eef5ff", ec="k", lw=1.4))
    a1.add_patch(Circle((0.5, 0.5), 0.24, transform=a1.transAxes, fc="#fde2b3", ec=AMBER))
    a1.set_title("Mononuclear\n(core-shell)", fontweight="bold", fontsize=9)
    # polynuclear
    a2.add_patch(Circle((0.5, 0.5), 0.4, transform=a2.transAxes, fc="#eef5ff", ec="k", lw=1.4))
    rng = np.random.RandomState(5)
    for _ in range(6):
        x, y = 0.5 + rng.uniform(-0.22, 0.22), 0.5 + rng.uniform(-0.22, 0.22)
        a2.add_patch(Circle((x, y), 0.07, transform=a2.transAxes, fc=AMBER, ec="#a86f00"))
    a2.set_title("Polynuclear\n(multi-core)", fontweight="bold", fontsize=9)
    # matrix
    a3.add_patch(Circle((0.5, 0.5), 0.4, transform=a3.transAxes, fc="#cfe0f7", ec="k", lw=1.4))
    for _ in range(30):
        x, y = 0.5 + rng.uniform(-0.34, 0.34), 0.5 + rng.uniform(-0.34, 0.34)
        if (x - 0.5) ** 2 + (y - 0.5) ** 2 < 0.36 ** 2:
            a3.add_patch(Circle((x, y), 0.02, transform=a3.transAxes, fc=RED))
    a3.set_title("Matrix\n(microsphere)", fontweight="bold", fontsize=9)
    for a in (a1, a2, a3):
        a.axis("off")
    fig.suptitle("Types of Microcapsules / Microspheres", fontweight="bold", color=MAROON, y=1.05)
    save(fig, "microcapsule_types.png")


def coacervation():
    fig, ax = plt.subplots(figsize=(7.6, 2.9))
    xs = [1.2, 3.6, 6.0, 8.4]
    titles = ["Core dispersed\nin polymer soln.", "Phase separation\n(coacervate droplets)",
              "Coating deposits\naround core", "Rigidised / cross-linked\nmicrocapsule"]
    for x, t in zip(xs, titles):
        ax.add_patch(Circle((x, 1.7), 0.55, fc="#eef5ff", ec="k", lw=1.2))
        ax.text(x, 0.7, t, ha="center", va="top", fontsize=7.8)
    # stage details
    ax.add_patch(Circle((xs[0], 1.7), 0.22, fc=AMBER, ec="#a86f00"))
    ax.add_patch(Circle((xs[1], 1.7), 0.22, fc=AMBER, ec="#a86f00"))
    for ang in np.linspace(0, 2 * np.pi, 8, endpoint=False):
        ax.add_patch(Circle((xs[1] + 0.4 * np.cos(ang), 1.7 + 0.4 * np.sin(ang)), 0.06,
                            fc="#cfe0f7", ec=BLUE))
    ax.add_patch(Circle((xs[2], 1.7), 0.34, fc="#cfe0f7", ec=BLUE))
    ax.add_patch(Circle((xs[2], 1.7), 0.2, fc=AMBER, ec="#a86f00"))
    ax.add_patch(Circle((xs[3], 1.7), 0.34, fc="#cfe0f7", ec=BLUE, lw=2))
    ax.add_patch(Circle((xs[3], 1.7), 0.2, fc=AMBER, ec="#a86f00"))
    for x in xs[:-1]:
        ax.annotate("", xy=(x + 1.0, 1.7), xytext=(x + 0.6, 1.7),
                    arrowprops=dict(arrowstyle="->", color=MAROON, lw=1.4))
    ax.set_xlim(0, 9.6); ax.set_ylim(-0.4, 2.6); ax.axis("off")
    ax.set_title("Coacervation \u2013 Phase Separation", fontweight="bold", color=MAROON)
    save(fig, "coacervation.png")


def spray_drying():
    fig, ax = plt.subplots(figsize=(4.8, 4.4))
    ax.add_patch(Polygon([(2, 8), (6, 8), (6, 4), (4, 2), (2, 4)], closed=True,
                         fc="#eef5ff", ec="k", lw=1.5))
    ax.add_patch(Rectangle((3.5, 8), 1, 0.8, fc="#cfe0f7", ec=BLUE))
    ax.text(4, 9.2, "Feed +\natomiser", ha="center", fontsize=8, color=BLUE)
    ax.annotate("Hot air in", xy=(2.2, 7.4), xytext=(0.2, 7.6),
                fontsize=8, color=RED, arrowprops=dict(arrowstyle="->", color=RED))
    for _ in range(30):
        x = np.random.uniform(2.4, 5.6); y = np.random.uniform(4, 7.6)
        ax.add_patch(Circle((x, y), 0.06, fc=AMBER, ec="none"))
    ax.annotate("Dry microcapsules\n(cyclone)", xy=(4, 2), xytext=(5.4, 1.0),
                fontsize=8, color=GREEN, arrowprops=dict(arrowstyle="->", color=GREEN))
    ax.set_xlim(0, 8); ax.set_ylim(0, 10); ax.axis("off")
    ax.set_title("Spray Drying", fontweight="bold", color=MAROON)
    save(fig, "spray_drying.png")


def pan_coating():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.6, 3.6))
    # pan coating
    a1.add_patch(Ellipse((0.5, 0.45), 0.7, 0.5, transform=a1.transAxes, fc="#eef5ff", ec="k", lw=1.6))
    rng = np.random.RandomState(9)
    for _ in range(12):
        x, y = 0.5 + rng.uniform(-0.22, 0.22), 0.4 + rng.uniform(-0.1, 0.06)
        a1.add_patch(Circle((x, y), 0.035, transform=a1.transAxes, fc=AMBER, ec="#a86f00"))
    a1.annotate("spray", xy=(0.5, 0.5), xytext=(0.5, 0.85), transform=a1.transAxes,
                ha="center", fontsize=8, color=RED, arrowprops=dict(arrowstyle="->", color=RED))
    a1.set_title("Pan Coating", fontweight="bold", fontsize=10)
    # wurster / air suspension
    a2.add_patch(Rectangle((0.3, 0.15), 0.4, 0.7, transform=a2.transAxes, fc="#eef5ff", ec="k", lw=1.5))
    a2.add_patch(Rectangle((0.42, 0.15), 0.16, 0.55, transform=a2.transAxes, fc="#e7f0ff", ec=BLUE, ls="--"))
    for _ in range(14):
        x, y = 0.5 + rng.uniform(-0.06, 0.06), rng.uniform(0.2, 0.75)
        a2.add_patch(Circle((x, y), 0.02, transform=a2.transAxes, fc=AMBER))
    a2.annotate("air", xy=(0.5, 0.15), xytext=(0.5, 0.02), transform=a2.transAxes,
                ha="center", fontsize=8, color=GREEN, arrowprops=dict(arrowstyle="->", color=GREEN))
    a2.set_title("Air Suspension\n(Wurster)", fontweight="bold", fontsize=10)
    for a in (a1, a2):
        a.axis("off")
    fig.suptitle("Microencapsulation \u2013 Coating Methods", fontweight="bold", color=MAROON, y=1.03)
    save(fig, "pan_coating.png")


def release_kinetics():
    fig, ax = plt.subplots(figsize=(6.2, 3.8))
    t = np.linspace(0, 10, 100)
    ax.plot(t, 10 * t, color=BLUE, lw=2, label="Zero order")
    ax.plot(t, 100 * (1 - np.exp(-0.4 * t)), color=RED, lw=2, label="First order")
    ax.plot(t, 32 * np.sqrt(t), color=GREEN, lw=2, label="Higuchi (\u221at)")
    ax.plot(t, 24 * t ** 0.7, color=PURPLE, lw=2, ls="--", label="Korsmeyer\u2013Peppas")
    ax.set_ylim(0, 105)
    ax.set_xlabel("Time \u2192", fontweight="bold"); ax.set_ylabel("% Drug released \u2192", fontweight="bold")
    ax.set_title("Drug-Release Kinetic Models", fontweight="bold", color=MAROON)
    ax.legend(fontsize=8.5); ax.grid(alpha=0.25)
    save(fig, "release_kinetics.png")


# =====================================================================
#  UNIT IV  -  IMPLANTS & INSERTS
# =====================================================================
def implant_sites():
    fig, ax = plt.subplots(figsize=(4.6, 5.6))
    # simple body outline
    ax.add_patch(Circle((0.5, 0.86), 0.09, transform=ax.transAxes, fc="#f2d5b8", ec="k"))
    ax.add_patch(FancyBboxPatch((0.36, 0.4), 0.28, 0.4, boxstyle="round,pad=0.02",
                                transform=ax.transAxes, fc="#f2d5b8", ec="k"))
    ax.add_patch(FancyBboxPatch((0.4, 0.1), 0.08, 0.32, transform=ax.transAxes, fc="#f2d5b8", ec="k"))
    ax.add_patch(FancyBboxPatch((0.52, 0.1), 0.08, 0.32, transform=ax.transAxes, fc="#f2d5b8", ec="k"))
    labels = [(0.62, 0.88, "Intra-ocular\n(Ocusert)", RED),
              (0.7, 0.66, "Subcutaneous\n(arm implant)", BLUE),
              (0.72, 0.52, "Intra-muscular", GREEN),
              (0.66, 0.34, "Intra-uterine\n(IUD)", PURPLE),
              (0.7, 0.2, "Intra-vaginal\n(ring)", MAROON)]
    pts = [(0.55, 0.87), (0.4, 0.66), (0.42, 0.52), (0.5, 0.45), (0.46, 0.28)]
    for (lx, ly, t, c), (px, py) in zip(labels, pts):
        ax.annotate(t, xy=(px, py), xytext=(lx, ly), transform=ax.transAxes, fontsize=7.6,
                    color=c, arrowprops=dict(arrowstyle="->", color=c, lw=1.1))
    ax.axis("off")
    ax.set_title("Implant & Insert Sites", fontweight="bold", color=MAROON)
    save(fig, "implant_sites.png")


def ocular_insert():
    fig, ax = plt.subplots(figsize=(5.6, 3.2))
    ax.add_patch(Ellipse((0.5, 0.5), 0.6, 0.34, transform=ax.transAxes, fc="#eef5ff", ec="k", lw=1.6))
    ax.add_patch(Ellipse((0.5, 0.5), 0.5, 0.24, transform=ax.transAxes, fc="#fde2b3", ec=AMBER))
    ax.add_patch(Ellipse((0.5, 0.5), 0.6, 0.34, transform=ax.transAxes, fc="none", ec=BLUE, lw=3))
    ax.text(0.5, 0.5, "Drug\nreservoir", ha="center", va="center", transform=ax.transAxes, fontsize=8.5)
    ax.text(0.5, 0.86, "Rate-controlling membrane (EVA)", ha="center", transform=ax.transAxes,
            fontsize=8, color=BLUE)
    ax.text(0.5, 0.08, "White retaining ring", ha="center", transform=ax.transAxes, fontsize=8, color=AMBER)
    ax.axis("off")
    ax.set_title("Ocular Insert (Ocusert\u00ae) \u2013 cross-section", fontweight="bold", color=MAROON)
    save(fig, "ocular_insert.png")


def iud_device():
    fig, ax = plt.subplots(figsize=(3.8, 4.4))
    # T-shaped device
    ax.add_patch(Rectangle((0.46, 0.2), 0.08, 0.6, transform=ax.transAxes, fc="#cfe0f7", ec=BLUE, lw=1.5))
    ax.add_patch(Rectangle((0.25, 0.72), 0.5, 0.08, transform=ax.transAxes, fc="#cfe0f7", ec=BLUE, lw=1.5))
    # progesterone reservoir on stem
    ax.add_patch(Rectangle((0.44, 0.34), 0.12, 0.28, transform=ax.transAxes, fc="#fde2b3", ec=AMBER))
    ax.annotate("Progesterone\nreservoir", xy=(0.56, 0.48), xytext=(0.72, 0.5),
                transform=ax.transAxes, fontsize=8, color=AMBER,
                arrowprops=dict(arrowstyle="->", color=AMBER))
    ax.plot([0.5, 0.5], [0.2, 0.05], transform=ax.transAxes, color="k", lw=1.2)
    ax.text(0.5, 0.02, "thread", ha="center", transform=ax.transAxes, fontsize=7.5)
    ax.axis("off")
    ax.set_title("Intra-uterine Device\n(Progestasert\u00ae)", fontweight="bold", color=MAROON)
    save(fig, "iud_device.png")


def implant_release():
    fig, ax = plt.subplots(figsize=(6.0, 3.4))
    t = np.linspace(0, 12, 100)
    ax.plot(t, 8 * t, color=MAROON, lw=2.4, label="Ideal implant (zero order)")
    ax.plot(t, 100 * (1 - np.exp(-0.35 * t)), color="#999", lw=1.8, ls="--",
            label="Conventional (first order)")
    ax.set_xlim(0, 12); ax.set_ylim(0, 105)
    ax.set_xlabel("Time (weeks) \u2192", fontweight="bold")
    ax.set_ylabel("Cumulative release \u2192", fontweight="bold")
    ax.set_title("Zero-Order Release from Implants", fontweight="bold", color=MAROON)
    ax.legend(fontsize=8.5); ax.grid(alpha=0.25)
    save(fig, "implant_release.png")


def host_reaction():
    fig, ax = plt.subplots(figsize=(7.2, 2.9))
    stages = ["Injury\n(implantation)", "Acute\ninflammation", "Chronic\ninflammation",
              "Granulation\ntissue", "Foreign-body\ngiant cells", "Fibrous\nencapsulation"]
    x = np.linspace(0.7, 9.3, len(stages))
    for xi, s in zip(x, stages):
        ax.add_patch(FancyBboxPatch((xi - 0.62, 1.0), 1.24, 1.0, boxstyle="round,pad=0.04",
                                    fc="#f5c6cb", ec=RED, lw=1.2))
        ax.text(xi, 1.5, s, ha="center", va="center", fontsize=7.6)
    for xi in x[:-1]:
        ax.annotate("", xy=(xi + 1.1, 1.5), xytext=(xi + 0.65, 1.5),
                    arrowprops=dict(arrowstyle="->", color=MAROON, lw=1.3))
    ax.set_xlim(0, 10); ax.set_ylim(0.6, 2.4); ax.axis("off")
    ax.set_title("Host Response to an Implant (foreign-body reaction)", fontweight="bold", color=MAROON)
    save(fig, "host_reaction.png")


# =====================================================================
#  UNIT V  -  TRANSDERMAL DDS
# =====================================================================
def skin_structure():
    fig, ax = plt.subplots(figsize=(6.6, 4.2))
    layers = [("Stratum corneum", 3.4, 0.5, "#e8d9c5"),
              ("Viable epidermis", 2.6, 0.8, "#f2d5b8"),
              ("Dermis (capillaries)", 0.9, 1.7, "#f5c6cb"),
              ("Subcutaneous tissue", 0.1, 0.8, "#fff0c2")]
    for name, y, h, c in layers:
        ax.add_patch(Rectangle((0, y), 10, h, fc=c, ec="k", lw=0.8))
        ax.text(0.2, y + h / 2, name, va="center", fontsize=9, fontweight="bold")
    # capillary
    ax.plot([6, 9], [1.4, 1.4], color=RED, lw=2.5)
    ax.text(7.5, 1.55, "blood capillary", color=RED, fontsize=8)
    # patch on top
    ax.add_patch(Rectangle((2, 3.9), 5, 0.5, fc="#cfe0f7", ec=BLUE, lw=1.4))
    ax.text(4.5, 4.15, "Transdermal patch", ha="center", fontsize=8.5, color=BLUE)
    ax.annotate("", xy=(4.5, 1.4), xytext=(4.5, 3.9),
                arrowprops=dict(arrowstyle="->", color=GREEN, lw=2))
    ax.text(4.7, 2.6, "drug permeation", color=GREEN, fontsize=8, rotation=90, va="center")
    ax.set_xlim(0, 10); ax.set_ylim(0, 4.6); ax.axis("off")
    ax.set_title("Skin Structure & Transdermal Permeation", fontweight="bold", color=MAROON)
    save(fig, "skin_structure.png")


def permeation_routes():
    fig, ax = plt.subplots(figsize=(6.6, 3.6))
    # brick-and-mortar stratum corneum
    for row in range(4):
        for col in range(9):
            off = 0.5 if row % 2 else 0
            ax.add_patch(Rectangle((col + off, row), 0.95, 0.9, fc="#f2d5b8", ec="#a86f00", lw=0.8))
    # transcellular (straight through)
    ax.annotate("", xy=(2.5, 0), xytext=(2.5, 4),
                arrowprops=dict(arrowstyle="->", color=BLUE, lw=2))
    ax.text(1.4, 4.2, "Transcellular", color=BLUE, fontsize=8.5)
    # intercellular (zig-zag)
    xs = [5, 5.5, 5, 5.5, 5]; ys = [4, 3, 2, 1, 0]
    ax.plot(xs, ys, color=GREEN, lw=2)
    ax.annotate("", xy=(5, 0), xytext=(5, 0.4), arrowprops=dict(arrowstyle="->", color=GREEN, lw=2))
    ax.text(5.6, 4.2, "Intercellular", color=GREEN, fontsize=8.5)
    # appendageal
    ax.annotate("", xy=(8, 0), xytext=(8, 4),
                arrowprops=dict(arrowstyle="->", color=RED, lw=2, ls="--"))
    ax.text(7.4, 4.2, "Appendageal", color=RED, fontsize=8.5)
    ax.set_xlim(0, 10); ax.set_ylim(-0.4, 4.8); ax.axis("off")
    ax.set_title("Routes of Drug Permeation across Skin", fontweight="bold", color=MAROON)
    save(fig, "permeation_routes.png")


def tdds_types():
    fig, axes = plt.subplots(1, 3, figsize=(8.0, 3.0))
    titles = ["Reservoir", "Drug-in-adhesive\n(matrix)", "Matrix-dispersion"]
    for ax, t in zip(axes, titles):
        ax.add_patch(Rectangle((0.1, 0.75), 0.8, 0.12, transform=ax.transAxes, fc="#888", ec="k"))  # backing
        ax.text(0.5, 0.93, "backing", ha="center", transform=ax.transAxes, fontsize=7)
        ax.axis("off")
        ax.set_title(t, fontweight="bold", fontsize=9)
    # reservoir
    axes[0].add_patch(Rectangle((0.1, 0.4), 0.8, 0.35, transform=axes[0].transAxes, fc="#fde2b3", ec=AMBER))
    axes[0].add_patch(Rectangle((0.1, 0.32), 0.8, 0.08, transform=axes[0].transAxes, fc="#cfe0f7", ec=BLUE))
    axes[0].add_patch(Rectangle((0.1, 0.22), 0.8, 0.1, transform=axes[0].transAxes, fc="#d7f0d7", ec=GREEN))
    axes[0].text(0.5, 0.57, "drug soln.", ha="center", transform=axes[0].transAxes, fontsize=7)
    axes[0].text(0.5, 0.36, "membrane", ha="center", transform=axes[0].transAxes, fontsize=6.5)
    # drug-in-adhesive
    axes[1].add_patch(Rectangle((0.1, 0.25), 0.8, 0.5, transform=axes[1].transAxes, fc="#fde2b3", ec=AMBER))
    rng = np.random.RandomState(11)
    for _ in range(20):
        axes[1].add_patch(Circle((0.1 + rng.uniform(0.03, 0.77), 0.25 + rng.uniform(0.03, 0.47)),
                                 0.012, transform=axes[1].transAxes, fc=RED))
    axes[1].text(0.5, 0.13, "drug + adhesive", ha="center", transform=axes[1].transAxes, fontsize=7)
    # matrix dispersion
    axes[2].add_patch(Rectangle((0.1, 0.35), 0.8, 0.4, transform=axes[2].transAxes, fc="#e7d9ef", ec=PURPLE))
    axes[2].add_patch(Rectangle((0.1, 0.25), 0.8, 0.1, transform=axes[2].transAxes, fc="#fde2b3", ec=AMBER))
    for _ in range(16):
        axes[2].add_patch(Circle((0.1 + rng.uniform(0.03, 0.77), 0.35 + rng.uniform(0.03, 0.37)),
                                 0.012, transform=axes[2].transAxes, fc=PURPLE))
    axes[2].text(0.5, 0.13, "polymer matrix", ha="center", transform=axes[2].transAxes, fontsize=7)
    fig.suptitle("Types of Transdermal Patches", fontweight="bold", color=MAROON, y=1.04)
    save(fig, "tdds_types.png")


def iontophoresis():
    fig, ax = plt.subplots(figsize=(6.4, 3.4))
    ax.add_patch(Rectangle((0, 0), 10, 1.2, fc="#f2d5b8", ec="k"))
    ax.text(5, 0.6, "SKIN", ha="center", va="center", fontsize=9)
    ax.add_patch(Rectangle((1.5, 1.2), 2, 0.7, fc="#f5c6cb", ec=RED, lw=1.4))
    ax.text(2.5, 1.55, "Anode (+)\ndrug\u207a", ha="center", va="center", fontsize=8)
    ax.add_patch(Rectangle((6.5, 1.2), 2, 0.7, fc="#cfe0f7", ec=BLUE, lw=1.4))
    ax.text(7.5, 1.55, "Cathode (\u2212)", ha="center", va="center", fontsize=8)
    ax.plot([2.5, 2.5, 7.5, 7.5], [1.9, 2.5, 2.5, 1.9], color="k", lw=1.4)
    ax.add_patch(Circle((5, 2.5), 0.25, fc="white", ec="k"))
    ax.text(5, 2.5, "V", ha="center", va="center", fontweight="bold")
    ax.annotate("drug driven in", xy=(2.5, 1.2), xytext=(2.5, 0.15),
                fontsize=7.5, color=RED, ha="center", arrowprops=dict(arrowstyle="->", color=RED))
    ax.set_xlim(0, 10); ax.set_ylim(-0.2, 2.9); ax.axis("off")
    ax.set_title("Iontophoresis", fontweight="bold", color=MAROON)
    save(fig, "iontophoresis.png")


def sonophoresis():
    fig, ax = plt.subplots(figsize=(6.0, 3.4))
    ax.add_patch(Rectangle((0, 0), 10, 1.4, fc="#f2d5b8", ec="k"))
    ax.text(5, 0.7, "SKIN", ha="center", va="center", fontsize=9)
    ax.add_patch(Rectangle((3.5, 2.3), 3, 0.6, fc="#cfe0f7", ec=BLUE, lw=1.4))
    ax.text(5, 2.6, "Ultrasound transducer", ha="center", va="center", fontsize=8)
    for i, y in enumerate([2.25, 2.05, 1.85, 1.65]):
        ax.add_patch(Arc((5, y + 0.4), 2 + i * 0.4, 0.5 + i * 0.2, theta1=200, theta2=340,
                         color=GREEN, lw=1.4))
    ax.text(6.7, 1.9, "acoustic\nwaves", color=GREEN, fontsize=8)
    ax.annotate("cavitation \u2192 permeation", xy=(5, 1.4), xytext=(5, 0.15),
                fontsize=7.5, color=RED, ha="center", arrowprops=dict(arrowstyle="->", color=RED))
    ax.set_xlim(0, 10); ax.set_ylim(-0.2, 3.1); ax.axis("off")
    ax.set_title("Sonophoresis (Phonophoresis)", fontweight="bold", color=MAROON)
    save(fig, "sonophoresis.png")


def permeation_kinetics():
    fig, ax = plt.subplots(figsize=(6.0, 3.6))
    t = np.linspace(0, 12, 200)
    lag = 2.0
    q = np.where(t > lag, 8 * (t - lag), 0)
    ax.plot(t, q, color=MAROON, lw=2.4)
    ax.plot([lag, 12], [0, 0], color="k", lw=0.6)
    # extrapolated steady-state line to x-axis => lag time
    ax.plot([0, lag], [-16, 0], color=BLUE, ls="--", lw=1.4)
    ax.axvline(lag, color=GREEN, ls=":")
    ax.text(lag + 0.1, 5, "lag time (t$_L$)", color=GREEN, fontsize=8.5)
    ax.text(7, 30, "steady-state flux (Jss = slope)", color=MAROON, fontsize=8.5)
    ax.set_xlim(0, 12); ax.set_ylim(-20, 90)
    ax.set_xlabel("Time (h) \u2192", fontweight="bold")
    ax.set_ylabel("Cumulative amount permeated / area \u2192", fontweight="bold")
    ax.set_title("Permeation Profile: Flux & Lag Time", fontweight="bold", color=MAROON)
    ax.grid(alpha=0.25)
    save(fig, "permeation_kinetics.png")


# =====================================================================
#  UNIT VI  -  PERSONALIZED MEDICINE
# =====================================================================
def personalized_workflow():
    fig, ax = plt.subplots(figsize=(7.6, 3.0))
    steps = ["Patient\nsample", "Genotyping /\nbiomarker test", "Data analysis\n(bioinformatics)",
             "Drug & dose\nselection", "Optimised\ntherapy"]
    x = np.linspace(0.8, 9.2, len(steps))
    cols = ["#cfe0f7", "#d7f0d7", "#fde2b3", "#e7d9ef", "#f5c6cb"]
    for xi, s, c in zip(x, steps, cols):
        ax.add_patch(FancyBboxPatch((xi - 0.72, 1.0), 1.44, 1.1, boxstyle="round,pad=0.05",
                                    fc=c, ec=MAROON, lw=1.3))
        ax.text(xi, 1.55, s, ha="center", va="center", fontsize=8)
    for xi in x[:-1]:
        ax.annotate("", xy=(xi + 1.15, 1.55), xytext=(xi + 0.75, 1.55),
                    arrowprops=dict(arrowstyle="->", color=MAROON, lw=1.5))
    ax.set_xlim(0, 10); ax.set_ylim(0.6, 2.4); ax.axis("off")
    ax.set_title("Personalized Medicine Work-flow", fontweight="bold", color=MAROON)
    save(fig, "personalized_workflow.png")


def metabolizer_types():
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    types = ["Poor\n(PM)", "Intermediate\n(IM)", "Extensive\n(EM)", "Ultra-rapid\n(UM)"]
    activity = [1, 2.5, 5, 8]
    cols = [RED, AMBER, GREEN, BLUE]
    ax.bar(types, activity, color=cols, edgecolor="k")
    ax.set_ylabel("Enzyme activity / metabolism rate", fontweight="bold")
    ax.set_title("Pharmacogenetic Metabolizer Phenotypes (e.g., CYP2D6)",
                 fontweight="bold", color=MAROON, fontsize=10.5)
    ax.text(0, 1.2, "\u2191 drug\nlevels", ha="center", fontsize=7.5, color=RED)
    ax.text(3, 8.2, "\u2193 drug\nlevels", ha="center", fontsize=7.5, color=BLUE)
    ax.grid(axis="y", alpha=0.25)
    save(fig, "metabolizer_types.png")


def printing_3d():
    fig, ax = plt.subplots(figsize=(5.2, 4.0))
    ax.add_patch(Rectangle((3, 7.5), 2, 1.2, fc="#cfe0f7", ec=BLUE, lw=1.4))
    ax.text(4, 8.1, "Print head\n(nozzle)", ha="center", va="center", fontsize=8)
    # deposited layers
    for i, y in enumerate(np.linspace(2, 5.5, 6)):
        w = 3 - i * 0.15
        ax.add_patch(Rectangle((4 - w / 2, y), w, 0.5, fc="#fde2b3", ec=AMBER, lw=0.9))
    ax.annotate("", xy=(4, 5.9), xytext=(4, 7.4),
                arrowprops=dict(arrowstyle="->", color=RED, lw=1.6))
    ax.text(6.2, 3.6, "layer-by-layer\ndeposition\n(tablet)", fontsize=8, color=MAROON)
    ax.add_patch(Rectangle((1, 1.2), 6, 0.6, fc="#888", ec="k"))
    ax.text(4, 1.5, "build platform", ha="center", va="center", fontsize=8, color="white")
    ax.set_xlim(0, 8); ax.set_ylim(0.8, 9.2); ax.axis("off")
    ax.set_title("3D Printing of Pharmaceuticals (FDM)", fontweight="bold", color=MAROON)
    save(fig, "printing_3d.png")


def bioelectronic():
    fig, ax = plt.subplots(figsize=(6.2, 3.2))
    ax.add_patch(FancyBboxPatch((0.5, 1.2), 1.8, 1.0, boxstyle="round,pad=0.05",
                                fc="#cfe0f7", ec=BLUE, lw=1.4))
    ax.text(1.4, 1.7, "Implanted\ndevice", ha="center", va="center", fontsize=8.5)
    ax.plot([2.3, 5.5], [1.7, 1.7], color=AMBER, lw=3)
    ax.text(3.9, 1.9, "electrode on nerve", ha="center", fontsize=8, color=AMBER)
    ax.add_patch(Circle((6.2, 1.7), 0.5, fc="#f5c6cb", ec=RED, lw=1.4))
    ax.text(6.2, 1.7, "target\norgan", ha="center", va="center", fontsize=7.5)
    ax.annotate("electrical\nimpulses", xy=(5.5, 1.7), xytext=(3.9, 0.4),
                fontsize=8, color=GREEN, ha="center", arrowprops=dict(arrowstyle="->", color=GREEN))
    ax.set_xlim(0, 8); ax.set_ylim(0, 2.8); ax.axis("off")
    ax.set_title("Bioelectronic Medicine (neuromodulation)", fontweight="bold", color=MAROON)
    save(fig, "bioelectronic.png")


def telepharmacy():
    fig, ax = plt.subplots(figsize=(6.6, 3.0))
    ax.add_patch(FancyBboxPatch((0.3, 1.0), 1.8, 1.2, boxstyle="round,pad=0.05",
                                fc="#d7f0d7", ec=GREEN, lw=1.4))
    ax.text(1.2, 1.6, "Pharmacist\n(remote)", ha="center", va="center", fontsize=8.5)
    ax.add_patch(FancyBboxPatch((4.0, 1.7), 1.8, 1.0, boxstyle="round,pad=0.05",
                                fc="#cfe0f7", ec=BLUE, lw=1.4))
    ax.text(4.9, 2.2, "Tele-link /\ncloud", ha="center", va="center", fontsize=8.5)
    ax.add_patch(FancyBboxPatch((7.5, 1.0), 1.8, 1.2, boxstyle="round,pad=0.05",
                                fc="#fde2b3", ec=AMBER, lw=1.4))
    ax.text(8.4, 1.6, "Patient\n(rural site)", ha="center", va="center", fontsize=8.5)
    ax.annotate("", xy=(4.0, 2.1), xytext=(2.1, 1.7), arrowprops=dict(arrowstyle="<->", color=MAROON, lw=1.4))
    ax.annotate("", xy=(7.5, 1.7), xytext=(5.8, 2.1), arrowprops=dict(arrowstyle="<->", color=MAROON, lw=1.4))
    ax.text(4.9, 0.5, "counselling \u2022 verification \u2022 dispensing oversight",
            ha="center", fontsize=8, style="italic", color="#555")
    ax.set_xlim(0, 9.6); ax.set_ylim(0, 3.0); ax.axis("off")
    ax.set_title("Telepharmacy", fontweight="bold", color=MAROON)
    save(fig, "telepharmacy.png")


# =====================================================================
#  EVALUATION / GENERAL
# =====================================================================
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


def franz_cell():
    fig, ax = plt.subplots(figsize=(5.2, 4.2))
    # donor compartment
    ax.add_patch(Rectangle((3, 6.5), 2, 2, fc="#fde2b3", ec=AMBER, lw=1.4))
    ax.text(4, 7.5, "Donor\n(drug)", ha="center", va="center", fontsize=8.5)
    # membrane
    ax.add_patch(Rectangle((2.4, 6.3), 3.2, 0.25, fc="#f5c6cb", ec=RED, lw=1.2))
    ax.text(6.0, 6.4, "skin / membrane", fontsize=7.5, color=RED, va="center")
    # receptor
    ax.add_patch(Polygon([(2.4, 6.3), (5.6, 6.3), (5.2, 2.0), (2.8, 2.0)], closed=True,
                         fc="#cfe0f7", ec=BLUE, lw=1.4))
    ax.text(4, 4.0, "Receptor\nmedium", ha="center", va="center", fontsize=8.5)
    # sampling port
    ax.add_patch(Rectangle((5.2, 3.2), 1.4, 0.25, fc="#cfe0f7", ec=BLUE))
    ax.text(6.7, 3.3, "sampling\nport", fontsize=7.5, va="center")
    # stir bar
    ax.add_patch(Ellipse((4, 2.4), 0.8, 0.25, fc="#888", ec="k"))
    ax.text(4, 2.0, "magnetic stirrer", ha="center", fontsize=7.5)
    ax.set_xlim(1.5, 8); ax.set_ylim(1.5, 9); ax.axis("off")
    ax.set_title("Franz Diffusion Cell", fontweight="bold", color=MAROON)
    save(fig, "franz_cell.png")


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


def main():
    print("Generating figures ...")
    dissolution_apparatus(); franz_cell(); bcs()
    # Unit I
    plasma_profiles(); release_terminology(); cdds_classification()
    # Unit II
    reservoir_matrix(); dissolution_controlled(); osmotic_pump(); ion_exchange()
    bioerosion(); mucoadhesion()
    # Unit III
    microcapsule_types(); coacervation(); spray_drying(); pan_coating(); release_kinetics()
    # Unit IV
    implant_sites(); ocular_insert(); iud_device(); implant_release(); host_reaction()
    # Unit V
    skin_structure(); permeation_routes(); tdds_types(); iontophoresis()
    sonophoresis(); permeation_kinetics()
    # Unit VI
    personalized_workflow(); metabolizer_types(); printing_3d(); bioelectronic(); telepharmacy()
    print("Done. Figures in", OUT)


if __name__ == "__main__":
    main()
