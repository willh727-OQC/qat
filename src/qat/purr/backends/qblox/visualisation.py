from typing import List

import numpy as np
from matplotlib import pyplot as plt

from qat.purr.backends.qblox.codegen import QbloxPackage


def plot_packages(packages: List[QbloxPackage]):
    if not packages:
        return

    max_length = max([len(pkg.timeline) for pkg in packages])
    if max_length <= 0:
        return

    t = np.linspace(0, max_length, max_length)
    fig, axes = plt.subplots(nrows=len(packages), ncols=1, sharex=False, squeeze=False)
    for i, pkg in enumerate(packages):
        axes[i][0].plot(t, pkg.timeline.real, label="I")
        axes[i][0].plot(t, pkg.timeline.imag, label="Q")
        axes[i][0].set_ylim(-1, 1)
        axes[i][0].set_title(pkg.target)
        axes[i][0].set_xlabel("Time (ns)")
        axes[i][0].set_ylabel("Digital offset (ratio)")
        axes[i][0].legend()

    plt.tight_layout()
    plt.show()
