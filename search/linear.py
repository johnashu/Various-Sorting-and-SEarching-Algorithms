"""
Linear search is a very simple search algorithm. In this type of search, a sequential search is made over all items one by one. Every item is checked and if a match is found then that particular item is returned, otherwise the search continues till the end of the data collection.
"""

a = [1, 5, 6, 7, 8, 9, 0, 'john', 56, 74, 456, 3, 6, 42, 53]

def maf_linear(a, x):
    """
    Step 1: Set i to 1
    Step 2: if i > n then go to step 7
    Step 3: if A[i] = x then go to step 6
    Step 4: Set i to i + 1
    Step 5: Go to Step 2
    Step 6: Print Element x Found at index i and go to step 8
    Step 7: Print element not found
    Step 8: Exit
    """
    e = "Item Not Found"
    for i in a:
        if i == x:
            print('Item found at index:', a.index(i))
            return a.index(i)
        elif i != a:
            print(e)
    
v = 'john'

normal = maf_linear(a, v)
print("Results from for Loop", normal)


def maf_lin_com(a, x):
    """ comprehensive linear search"""
    
    e = "Item Not Found"

    rtn = [ a.index(i) for i in a if  i == x]
    return rtn


print("Results from List Comprehension:", maf_lin_com(a, v) )