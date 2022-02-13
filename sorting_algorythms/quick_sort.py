from sorting_algorythms.visualizator import animate_iterations
from sorting_algorythms.visualizator import generate_shuffled_arr


def quick_sort(array):
    quick_sort_alg(array, 0, len(array) - 1)


def quick_sort_alg(array, start, end):
    if end - start <= 0:
        return
    mid = start + (end - start) // 2
    base = mid
    i = start
    # smaller_partition
    while i < base:
        if array[i] <= array[base]:
            i += 1
        else:
            buffer = array[i]
            for k in range(i, mid):
                array[k] = array[k + 1]
            array[mid] = buffer
            base -= 1
    j = mid + 1
    # bigger_partition
    while j <= end:
        if array[j] > array[base]:
            j += 1
        else:
            buffer = array[j]
            for i in range(j, base, -1):
                array[i] = array[i - 1]
            array[base] = buffer
            base += 1
            j += 1
    quick_sort_alg(array, start, base - 1)
    quick_sort_alg(array, base + 1, end)


def quick_sort_gen(array):
    yield from quick_sort_alg_gen(array, 0, len(array) - 1)


def quick_sort_alg_gen(array, start, end):
    if end - start <= 0:
        return
    mid = start + (end - start) // 2
    base = mid
    i = start
    # smaller_partition
    while i < base:
        if array[i] <= array[base]:
            i += 1
        else:
            buffer = array[i]
            for k in range(i, mid):
                array[k] = array[k + 1]
            array[mid] = buffer
            base -= 1
        yield array
    j = mid + 1
    # bigger_partition
    while j <= end:
        if array[j] > array[base]:
            j += 1
        else:
            buffer = array[j]
            for i in range(j, base, -1):
                array[i] = array[i - 1]
            array[base] = buffer
            base += 1
            j += 1
        yield array
    yield from quick_sort_alg_gen(array, start, base - 1)
    yield from quick_sort_alg_gen(array, base + 1, end)


if __name__ == '__main__':
    array_1 = generate_shuffled_arr(50)
    array_2 = array_1.copy()
    print("Initial array", array_1)
    quick_sort(array_1)
    print("Sorted array", array_1)
    animate_iterations(array_2, quick_sort_gen(array_2))
