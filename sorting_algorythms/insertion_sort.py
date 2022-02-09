from sorting_algorythms.visualizator import animate_iterations
from sorting_algorythms.visualizator import generate_shuffled_arr


def insertion_sort(arr):
    for i in range(0, len(arr)):
        j = i - 1
        key = arr[i]
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def insertion_sort_gen(arr):
    for i in range(0, len(arr)):
        j = i - 1
        key = arr[i]
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            yield arr
        arr[j + 1] = key


if __name__ == '__main__':
    array_1 = generate_shuffled_arr(50)
    array_2 = array_1.copy()
    print("Initial array", array_1)
    insertion_sort(array_1)
    print("Sorted array", array_1)
    animate_iterations(array_2, insertion_sort_gen(array_2))
