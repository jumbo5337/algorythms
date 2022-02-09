from sorting_algorythms.visualizator import animate_iterations
from sorting_algorythms.visualizator import generate_shuffled_arr


def selection_sort(arr):
    if not arr:
        return
    for i in range(0, len(arr)):
        min_idx = i
        min_elem = arr[min_idx]
        for j in range(i, len(arr)):
            if min_elem > arr[j]:
                min_idx = j
                min_elem = arr[j]
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def selection_sort_gen(arr):
    if not arr:
        return
    for i in range(0, len(arr)):
        min_idx = i
        min_elem = arr[min_idx]
        for j in range(i, len(arr)):
            if min_elem > arr[j]:
                min_idx = j
                min_elem = arr[j]
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        yield arr


if __name__ == '__main__':
    array_1 = generate_shuffled_arr(50)
    array_2 = array_1.copy()
    print("Initial array", array_1)
    selection_sort(array_1)
    print("Sorted array", array_1)
    animate_iterations(array_2, selection_sort_gen(array_2))
