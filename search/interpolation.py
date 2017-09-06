"""
Interpolation search is an improved variant of binary search. This search algorithm works on the probing position of the required value. For this algorithm to work properly, the data collection should be in a sorted form and equally distributed.

Binary search has a huge advantage of time complexity over linear search. Linear search has worst-case complexity of Ο(n) whereas binary search has Ο(log n).

Step 1 − Start searching data from middle of the list.
Step 2 − If it is a match, return the index of the item, and exit.
Step 3 − If it is not a match, probe position.
Step 4 − Divide the list using probing formula and find the new midle.
Step 5 − If data is greater than middle, search in higher sub-list.
Step 6 − If data is smaller than middle, search in lower sub-list.
Step 7 − Repeat until match.

"""


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 42]

x = 77

def maf_interpolation(array, value):
    """
    In this algorithm, we want to find whether element x belongs to a set of numbers stored in an array numbers[]. Where l and r represent the left and right index of a sub-array in which searching operation should be performed.

    """
    err = "Not Found"

    lo = 0
    mid = -1
    hi = len(array) - 1
    while value != mid:

        if lo == hi or array[lo] == a[hi]:
            print("No Dice! Target NOT Found!")
            break 

        mid = lo + ((hi - lo) // (array[hi] - array[lo])) * (value - array[lo])

        if array[mid] == value:
            return print("Success, Found in Index: ", mid)
            break             
        
        elif array[mid] < value: 
            lo = mid + 1
        
        elif a[mid] > value:
            hi = mid - 1
        
          
print("Results from For Loop:", maf_interpolation(a, x))



