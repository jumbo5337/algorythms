def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    buff_arr = []
    for i in range (len(arr)):
        smallest = find_smallest(arr)
        buff_arr.append(arr.pop(smallest))
    return buff_arr

print(selection_sort([5,4,3,6,1,2]))