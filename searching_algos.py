def linear_search(L, element):
    for i in range(len(L)):
        if L[i] == element:
            return i
    return -1


def quick_sort(L):
    if len(L) == 0:
        return []
    return quick_sort([x for x in L[1:] if x < L[0]]) + L[0:1] + quick_sort([x for x in L[1:] if x >= L[0]])


def binary_search(L, element):
    """
    solving using recurssion
    to solve using iterative method use while loop and update low & high
    avg time: log(n) when L is already sorted
    """
    low, high = 0, len(L)-1
    mid = int((low+high)/2)
    
    if high >= low:
        if L[mid]==element:
            return mid
        elif L[mid]>element:
            return binary_search(L[:mid], element)
        else:
            return binary_search(L[mid+1:], element)
    else:
        return


if __name__ == "__main__":
    a = [30, 10, 1, 23, 45]
    print(a)
    
    idx = linear_search(a, 1)
    print(idx)
    idx = linear_search(a, 25)
    print(idx)
    
    a = quick_sort(a)
    idx = binary_search(a, 1)
    print(idx)
    idx = binary_search(a, 25)
    print(idx)
    