#Function1

def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)


#Function2

def linear_search(lst, key, index=0):
    if index >= len(lst):
        return -1
    if lst[index] == key:
        return index
    return linear_search(lst, key, index + 1)


#Function3

def binary_search(lst, key, low=0, high=None):
    if high is None:
        high = len(lst) - 1
    
    if low > high:
        return -1

    mid = (low + high) // 2

    if lst[mid] == key:
        return mid
    elif key < lst[mid]:
        return binary_search(lst, key, low, mid - 1)
    else:
        return binary_search(lst, key, mid + 1, high)

