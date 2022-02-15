import random as rnd
from sorting_algorythms.visualizator import animate_iterations
from sorting_algorythms.visualizator import generate_shuffled_arr


def bogo_sort(array):
    while not is_sorted(array):
        rnd.shuffle(array)


def bogo_sort_gen(array):
    while not is_sorted(array):
        rnd.shuffle(array)
        yield array


def is_sorted(array):
    for i in range(0, len(array) - 1):
        if array[i] > array[i + 1]:
            return False
    return True


if __name__ == '__main__':
    array_1 = generate_shuffled_arr(5)
    array_2 = array_1.copy()
    print("Initial array", array_1)
    bogo_sort(array_1)
    print("Sorted array", array_1)
    animate_iterations(array_2, bogo_sort_gen(array_2))