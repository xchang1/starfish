import warnings
from typing import Optional

import matplotlib.axes
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import pearsonr

from starfish import IntensityTable
from starfish.types import Features, Indices
from .util import equalize_axes_extents


def intensities_by_target(intensities: IntensityTable, target: str):
    """

    Parameters
    ----------
    intensities : IntensityTable
        normalized and decoded intensities
    target : str
        name of target for which to visualize spots

    Returns
    -------

    """
    target_intensities = intensities.where(intensities[Features.TARGET] == target, drop=True)
    traces = target_intensities.stack(traces=(Indices.CH.value, Indices.ROUND.value))
    x_labs = traces.traces
    x_inds = np.repeat(np.arange(len(x_labs)), axis=1, repeats=traces.sizes[Features.AXIS])



# from notebook
# target_intensities = spot_intensities.where(spot_intensities[Features.TARGET] == 'ANKRD13A', drop=True)
#
# traces = target_intensities.stack(traces=(Indices.CH.value, Indices.ROUND.value))
#
# x_labs = [f'ch={c}, round={r}' for c, r in zip(traces[Indices.CH.value].values, traces[Indices.ROUND.value].values)]
# x_inds = np.repeat(np.arange(len(x_labs), dtype=np.float)[None, :], axis=0, repeats=traces.sizes[Features.AXIS])
# # add jitter
# x_inds += np.random.uniform(-0.4, 0.4, size=x_inds.shape)
#
# y_inds = np.ravel(traces)
# x_inds = np.ravel(x_inds)
#
# f, ax = plt.subplots(figsize=(5,5))
# plt.scatter(x_inds, y_inds, s=6)
# sns.despine(offset=2)
# ax.set_xticks(np.arange(len(x_labs)))
# ax.set_xticklabels(x_labs, rotation='vertical')
# ax.set_title('ANKRD13A Intensities\nper Round and Channel')
# ax.set_ylabel('normalized\nintensity')
# f.tight_layout()
# f.savefig('decoding_plot2.png', dpi=150, transparent=True)