from sorting_algorythms.visualizator import animate_iterations
from sorting_algorythms.visualizator import generate_shuffled_arr


def merge_sort(array):
    sort_alg(array, 0, len(array) - 1)


def sort_alg(array, start, end):
    if end - start <= 0:
        return
    mid = start + (end - start) // 2
    sort_alg(array, start, mid)
    sort_alg(array, mid + 1, end)
    merge_alg(array, start, mid, end)


def merge_alg(array, start, mid, end):
    current_mid = mid
    i = start
    j = mid + 1
    while i <= current_mid and j <= end:
        if array[i] < array[j]:
            i += 1
        else:
            el = array[j]
            shift_index = j
            # Shift elements of first arr to the right
            while shift_index > i:
                array[shift_index] = array[shift_index - 1]
                shift_index -= 1
            array[i] = el
            j += 1
            i += 1
            current_mid += 1


def merg_sort_gen(array):
    yield from sort_alg_gen(array, 0, len(array) - 1)


def sort_alg_gen(array, start, end):
    if end - start <= 0:
        return
    mid = start + (end - start) // 2
    yield from sort_alg_gen(array, start, mid)
    yield from sort_alg_gen(array, mid + 1, end)
    yield from merge_alg_gen(array, start, mid, end)


def merge_alg_gen(array, start, mid, end):
    current_mid = mid
    i = start
    j = mid + 1
    while i <= current_mid and j <= end:
        if array[i] < array[j]:
            i += 1
        else:
            el = array[j]
            shift_index = j
            while shift_index > i:
                array[shift_index] = array[shift_index - 1]
                shift_index -= 1
            array[i] = el
            j += 1
            i += 1
            current_mid += 1
        yield array


if __name__ == '__main__':
    array_1 = generate_shuffled_arr(50)
    array_2 = array_1.copy()
    print("Initial array", array_1)
    merge_sort(array_1)
    print("Sorted array", array_1)
    animate_iterations(array_2, merg_sort_gen(array_2))
