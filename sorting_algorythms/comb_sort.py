from sorting_algorythms.visualizator import animate_iterations
from sorting_algorythms.visualizator import generate_shuffled_arr


def comb_sort(arr):
    factor = 1.2473309
    step = len(arr)
    while step >= 1:
        i = 0
        while i + step < len(arr):
            if arr[i] > arr[i + step]:
                arr[i], arr[i + step] = arr[i + step], arr[i]
            i += 1
        step = int(step // factor)


def comb_sort_gen(arr):
    factor = 1.2473309
    step = len(arr)
    while step >= 1:
        i = 0
        while i + step < len(arr):
            if arr[i] > arr[i + step]:
                arr[i], arr[i + step] = arr[i + step], arr[i]
                yield arr
            i += 1
        step = int(step // factor)


if __name__ == '__main__':
    array_1 = generate_shuffled_arr(50)
    array_2 = array_1.copy()
    print("Initial array", array_1)
    comb_sort(array_1)
    print("Sorted array", array_1)
    animate_iterations(array_2, comb_sort_gen(array_2), interval=150)
