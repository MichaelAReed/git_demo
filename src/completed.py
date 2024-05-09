"""Example script that generates a plot."""

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


# def setup_style():
#     STYLE = "seaborn-v0_8"
#     mpl.style.use(STYLE)


def gen_damped_data():
    x = np.linspace(0.0, 5.0)
    y = np.cos(2 * np.pi * x) * np.exp(-x)
    return x, y


# def gen_undamped_data():
#     x = np.linspace(0.0, 2.0)
#     y = np.cos(2 * np.pi * x)
#     return x, y


def setup_plot():
    fig, ax = plt.subplots()
    # fig.suptitle("Some desalination stuff.")
    # ax.set_xlabel("time (s)")
    # ax.set_ylabel("Voltage (mV)")
    return fig, ax


if __name__ == "__main__":
    # setup_style()

    # Create some fake data.
    x1, y1 = gen_damped_data()
    # x2, y2 = gen_undamped_data()

    fig, ax = setup_plot()

    ax.plot(x1, y1, "C0o-")
    # ax.plot(x2, y2, "Green.-")
    # ax.plot(x2, y2, "C1.-")

    plt.savefig("output_images/stack_voltage.png")

    plt.show()
