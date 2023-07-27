def bubble_sort(L):
    """
    sort ascendingly: order n^2
    send the greatest element at the back of the list
    """
    for i in range(len(L)-1, 0, -1):
        for j in range(len(L)-i):
            if L[j]>L[j+1]:
                temp = L[j]
                L[j] = L[j+1]
                L[j+1] = temp
    return L


def quick_sort(L):
    """
    avg time ==> order nlog(n)
    better version will be selecting a random element or middle element, 
    swap it with first ele and then do the below algo
    """
    if len(L) == 0:
        return []
    return quick_sort([x for x in L[1:] if x < L[0]]) + L[0:1] + quick_sort([x for x in L[1:] if x >= L[0]])


def insertion_sort(L):
    """bring element to it's right position in sorted sublist"""
    for i in range(len(L)):
        for j in range(i, 0, -1):
            if L[j-1]>L[j]:
                temp = L[j-1]
                L[j-1] = L[j]
                L[j] = temp
            else:
                break
    return L


# def shell_sort(L):
#     return


def selection_sort(L):
    """ 
    find the minimum element from the unsorted part and bring it to the end of sorted part
    """
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[i] > L[j]:
                temp = L[j]
                L[j] = L[i]
                L[i] = temp
    return L


def heap_sort(L):
    return


def merge_sort(L):
    if len(L) <= 1:
        return L
    
    mid = int(len(L)/2)
    l1 = merge_sort(L[:mid])
    l2 = merge_sort(L[mid:])
    
    i, j, k = 0, 0, 0
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            L[k] = l1[i]
            i += 1
        else:
            L[k] = l2[j]
            j += 1
        k += 1
    
    while k<len(L):
        if i == len(l1):
            L[k] = l2[j]
            j += 1
        else:
            L[k] = l1[i]
            i += 1
        k += 1
                
    return L


# def radix_sort(L):
#     return


# def bucket_sort(L):
#     return


if __name__ == "__main__":
    a = [30, 10, 1, 23, 45]
    print(a)
    # c = quick_sort(a)
    # print(c)
    # c = bubble_sort(a)
    # print(c)
    # c = insertion_sort(a)
    # print(c)
    # c = shell_sort(a)
    # print(c)
    # c = selection_sort(a)
    # print(c)
    # c = heap_sort(a)
    # print(c)
    c = merge_sort(a)
    print(c)
    # c = radix_sort(a)
    # print(c)
    # c = bucket_sort(a)
    # print(c)
    