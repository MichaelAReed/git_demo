"""Example script that generates a plot."""

import matplotlib.pyplot as plt
import numpy as np


def gen_damped_data():
    x = np.linspace(0.0, 5.0)
    y = np.cos(2 * np.pi * x) * np.exp(-x)
    return x, y


def setup_plot():
    fig, ax = plt.subplots()
    # fig.suptitle("Some desalination stuff.")
    # ax.set_xlabel("time (s)")
    # ax.set_ylabel("Voltage (mV)")
    return fig, ax


if __name__ == "__main__":
    # Create some fake data.

    x1, y1 = gen_damped_data()
    fig, ax = setup_plot()

    ax.plot(x1, y1, "C0o-")

    plt.show()
