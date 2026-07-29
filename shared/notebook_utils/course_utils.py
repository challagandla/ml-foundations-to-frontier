"""Shared helpers imported by every module's notebook.

Usage from a module notebook (e.g. modules/01-linear-algebra/notebook.ipynb):

    import sys, pathlib
    sys.path.append(str(pathlib.Path("../../shared/notebook_utils").resolve()))
    from course_utils import set_style, load_dataset, DATA_DIR

Keeps plotting style and dataset loading consistent across all 42 modules
without copy-pasting boilerplate into each notebook.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

# Same categorical palette used by the HTML modules (dataviz-skill
# validated, colorblind-safe, fixed order -- see shared/css/theme.css).
PALETTE = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#4a3aa7", "#e34948"]


def set_style():
    """Apply the course's matplotlib style. Call once at the top of a notebook."""
    plt.rcParams.update({
        "figure.figsize": (7, 4.5),
        "figure.facecolor": "#fcfcfb",
        "axes.facecolor": "#fcfcfb",
        "axes.edgecolor": "#c3c2b7",
        "axes.grid": True,
        "grid.color": "#e1e0d9",
        "grid.linewidth": 0.8,
        "axes.axisbelow": True,
        "axes.prop_cycle": plt.cycler(color=PALETTE),
        "font.size": 11,
        "axes.titleweight": "bold",
        "axes.spines.top": False,
        "axes.spines.right": False,
    })


def load_dataset(name: str) -> pd.DataFrame:
    """Load a CSV from shared/data by name (without the .csv suffix)."""
    path = DATA_DIR / f"{name}.csv"
    if not path.exists():
        raise FileNotFoundError(
            f"No dataset '{name}' in {DATA_DIR}. "
            "This module may generate synthetic data instead -- check the notebook intro."
        )
    return pd.read_csv(path)


def rng(seed: int = 0) -> np.random.Generator:
    """A seeded NumPy random generator, for reproducible synthetic datasets."""
    return np.random.default_rng(seed)
