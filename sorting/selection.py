"""
Selection sort is a simple sorting algorithm. This sorting algorithm is an in-place comparison-based algorithm in which the l is divided into two parts, the sorted part at the left end and the unsorted part at the right end. Initially, the sorted part is empty and the unsorted part is the entire l.

The smallest element is selected from the unsorted array and swapped with the leftmost element, and that element becomes a part of the sorted array. This process continues moving unsorted array boundary by one element to the right.

This algorithm is not suitable for large data sets as its average and worst case complexities are of Ο(n2), where n is the number of items.
"""

unsort_l = [456, 456, 4, 23, 23, 65,1, 1, 1, 1, 89, 4956, 53, 1, 1, 1, 1, 1, 12, 123, 345, 134, 23, 46, 37, 999, 9999999, 9999999, 9999999, 999999999, 999999999]

def maf_selection(l):
    """ 
    Sorts a l using an Selection Sort algorithm 

    Step 1 − Set min to location 0
    Step 2 − Search the minimum element in the l
    Step 3 − Swap with value at location min
    Step 4 − Increment min to point to next element
    Step 5 − Repeat until l is sorted
    
    """
    n = len(l)

    for i in range(n):
        # set current element as min
        min = i
        #check the element to be min
        for j in range(i + 1, n):
            if l[j] < l[min]:
                min = j 
        
        #swap the min element with the current element*
        l[i], l[min] = l[min], l[i]
        
maf_selection(unsort_l)
print(unsort_l)

