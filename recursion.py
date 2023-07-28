# Recursion allows a function to call itself. Fixed steps of code get 
# executed again and again for new values. We also have to set criteria 
# for deciding when the recursive call ends. In the below example we 
# see a recursive approach to the binary search. We take a sorted list 
# and give its index range as input to the recursive function.

def binary_search_using_recursion(list_of_elements, idx0, idxn, val):
    if (idxn < idx0):
        return None
    else:
        midval = (idx0 + idxn) // 2
    # Compare the search item with middle most value
    if list_of_elements[midval] > val:
        return binary_search_using_recursion(list_of_elements, idx0, midval-1, val)
    elif list_of_elements[midval] < val:
        return binary_search_using_recursion(list_of_elements, midval+1, idxn, val)
    else:
        return midval

  
if __name__ == "__main__":
    list_of_elements = [8,11,24,56,88,131] # sorted list
    print(binary_search_using_recursion(list_of_elements, 0, 5, 24))
    print(binary_search_using_recursion(list_of_elements, 0, 5, 51))