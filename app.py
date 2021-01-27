import random

def bogoSort(a):
    while (is_sorted(a) == False):
        random.shuffle(a)
        yield a

def is_sorted(a):
    n = len(a)
    for i in range(0, n - 1):
        if (a[i] > a[i + 1]):
            return False
    return True

arr = [9,5,6,2]
iterations = bogoSort(arr)
for i in iterations:
    print(i)