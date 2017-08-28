"""
Merge sort is a sorting technique based on divide and conquer technique. With worst-case time complexity being Ο(n log n), it is one of the most respected algorithms.
Merge sort start divides the a into equal halves and then combines them in a sorted manner.
"""

unsort_list = [456, 456, 4,  1, 1, 23, 23, 65, 1, 1, 999, 9999999, 1, 1, 89, 4956,
               53, 1, 1, 1, 12, 123, 345, 134, 23, 46, 37, 9999999, 9999999, 999999999, 999999999]


def maf_merge(a):
    """ 
    Sorts a list using an Merge Sort algorithm 
    Step 1 − if it is only one element in the list it is already sorted, return.
    Step 2 − divide the list recursively into two halves until it can no more be divided.
    Step 3 − merge the smaller lists into new list in sorted order.
    """
    # if it is only one element in the list it is already sorted, return.

    def merge(a, b):
        """ Function to merge two as """
        c = []
        while len(a) != 0 and len(b) != 0:
            if a[0] < b[0]:
                c.append(a[0])
                del (a[0])
            else:
                c.append(b[0])
                del (b[0])
        if len(a) == 0:
            c += b
        else:
            c += a
        return c

    # Code for merge sort

    def mergesort(x):
        """ Function to sort an a using merge sort algorithm """
        l = len(x)
        if l == 0 or l == 1:
            return x
        else:
            mid = l // 2
            a = mergesort(x[:mid])
            b = mergesort(x[mid:])
        return merge(a, b)

    return (mergesort(a))

sorted_list = maf_merge(unsort_list)
print(sorted_list)

