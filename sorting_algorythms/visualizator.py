import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

matplotlib.use("TkAgg")


def update_plot(array, rec, epochs, text):
    for rec, val in zip(rec, array):
        rec.set_height(val)
    epochs[0] += 1
    text.set_text("№ operations:{}".format(epochs[0]))


def animate_iterations(source_array, generator, interval=50):
    size = len(source_array)
    max = np.max(source_array)
    fig, ax = plt.subplots()
    bars = ax.bar(range(size), source_array, align='edge')
    ax.set_xlim(0, size)
    ax.set_ylim(0, int(max * 1.4))
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    epochs = [0]
    anima = FuncAnimation(fig,
                          func=update_plot,
                          fargs=(bars, epochs, text),
                          frames=generator,
                          interval=interval,
                          repeat=False)
    plt.show()


def generate_shuffled_arr(len=50):
    arr = [i for i in range(1, len + 1)]
    random.shuffle(arr)
    return arr
