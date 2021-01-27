

def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in  array[1:] if i <= pivot]
        more = [i for i in  array[1:] if i > pivot]
        yield quick_sort(less) + [pivot] + quick_sort(more)

arr = quick_sort([10, 5, 2, 3, 6])

for i in arr:
    print(i)

