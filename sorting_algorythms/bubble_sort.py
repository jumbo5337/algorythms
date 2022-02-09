from sorting_algorythms.visualizator import animate_iterations
from sorting_algorythms.visualizator import generate_shuffled_arr


def bubble_sort_v1(arr):
    if len(arr) <= 1:
        return
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False


def bubble_sort_v1_gen(arr):
    if len(arr) <= 1:
        return
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False
            yield arr


def bubble_sort_v2(arr):
    if len(arr) <= 1:
        return
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def bubble_sort_v2(arr):
    if len(arr) <= 1:
        return
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def bubble_sort_v2_gen(arr):
    if len(arr) <= 1:
        return
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            yield arr


if __name__ == '__main__':
    array_1 = generate_shuffled_arr(50)
    array_2 = array_1.copy()
    print("Initial array", array_1)
    bubble_sort_v2(array_1)
    print("Sorted array", array_1)
    animate_iterations(array_2, bubble_sort_v2_gen(array_2), interval=150)
