
def fact(x):
    if x == 1:
        return x
    else:
        return x * fact(x-1)

print(fact(5))

def sum(arr):
    if(len(arr) == 1):
        return arr[0]
    else:
        return arr[0] + sum(arr[1:])

print(sum([1,5,6]))

def count_elements(arr):
    if len(arr) == 1 :
        return 1
    else:
        return 1 + count_elements(arr[1:])

print(count_elements(arr=[1,5,6]))