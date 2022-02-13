from sorting_algorythms.visualizator import animate_iterations
from sorting_algorythms.visualizator import generate_shuffled_arr



def heap_sort(array):
    size = len(array)
    for i in range(size//2 -1, -1, -1):
        heapify(array, size, i)
    for j in range(size - 1, 0, -1):
        array[j], array[0] = array[0], array[j]
        heapify(array, j, 0)


def heapify(array, size, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < size and array[left] > array[largest]:
        largest = left
    if right < size and array[right] > array[largest]:
        largest = right
    if largest != i:
        array[largest], array[i] = array[i], array[largest]
        heapify(array, size, largest)


def heap_sort_gen(array):
    size = len(array)
    for i in range(size//2 -1, -1, -1):
        yield from heapify_gen(array, size, i)
    for j in range(size - 1, 0, -1):
        array[j], array[0] = array[0], array[j]
        yield array
        yield from heapify_gen(array, j, 0)


def heapify_gen(array, size, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < size and array[left] > array[largest]:
        largest = left
    if right < size and array[right] > array[largest]:
        largest = right
    if largest != i:
        array[largest], array[i] = array[i], array[largest]
        yield array
        yield from heapify_gen(array, size, largest)

if __name__ == '__main__':
    array_1 = generate_shuffled_arr(50)
    array_2 = array_1.copy()
    print("Initial array", array_1)
    heap_sort(array_1)
    print("Sorted array", array_1)
    animate_iterations(array_2, heap_sort_gen(array_2))