def bubble_sort(arr):
    if (len(arr) == 1):
        return
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
               is_sorted = False
               arr[i], arr[i+1] = arr[i+1], arr[i]
            yield arr

def merge_sort(arr, start, end):
    if(end<=start):
        return
    elif(start < end):
        mid = (start + end) // 2
        yield from merge_sort(arr, start, mid)
        yield from merge_sort(arr, mid + 1, end)
        yield from merge(arr, start, mid, end)
        yield arr

def merge(arr, start, mid, end):
    new = []
    i = start
    j = mid+1
    while(i <= mid and j <= end):
        if(arr[i]<arr[j]):
            new.append(arr[i])
            i+=1
        else:
            new.append(arr[j])
            j+=1
    if(i>mid):
        while(j <= end):
            new.append(arr[j])
            j+=1
    else:
        while(i<=mid):
            new.append(arr[i])
            i+=1
    for i,val in enumerate(new):
        arr[start + i] = val
        yield arr

import random

def bogoSort(a):
    while (is_sorted(a) == False):
        random.shuffle(a)
        yield a

def is_sorted(a):
    n = len(a)
    for i in range(0, n - 1):
        if (a[i] > a[i + 1]):
            return False
    return True

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
matplotlib.use("TkAgg")

def update_plot(array, rec, epochs, text):
    for rec, val in zip(rec, array):
        rec.set_height(val)
    epochs[0]+=1
    text.set_text("№ operations:{}".format(epochs[0]))

def animate_iterations(source_array, generator):
    size = len(source_array)
    max = np.max(source_array)
    fig, ax = plt.subplots()
    bars = ax.bar(range(size), source_array , align='edge')
    ax.set_xlim(0, size)
    ax.set_ylim(0, int(max * 1.4))
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    epochs = [0]
    anima = FuncAnimation(fig,
                          func=update_plot,
                          fargs=(bars,epochs,text),
                          frames=generator,
                          interval=50,
                          repeat=False)
    plt.show()

arr = [i for i in range(1,50)]
random.shuffle(arr)
generator = merge_sort(arr, 0, len(arr)-1)
animate_iterations(arr, generator)


