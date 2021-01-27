

def binary_search(arr, item):
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low+high)//2
        guess = arr[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return -1

list = [1,3,5,7,9]

print(binary_search(list, 5))
print(binary_search(list, 1))
print(binary_search(list, 9))
print(binary_search(list, 10))

print('-----------------')
def recursive_bs_algo(arr, item, start,end):
    mid = start + (end-start)//2
    if start == end and arr[mid] != item:
        return -1
    elif arr[mid] == item:
        return mid
    elif arr[mid] < item:
        return recursive_bs_algo(arr, item, mid+1, end)
    else:
        return recursive_bs_algo(arr,item, start, mid-1)

def recursive_bs(arr, item):
    return recursive_bs_algo(arr, item, 0, len(arr)-1)

print(recursive_bs(list, 5))
print(recursive_bs(list, 1))
print(recursive_bs(list, 9))
print(recursive_bs(list, 10))