"""
Bubble Sort Algorithm

This sorting algorithm is comparison-based algorithm in which each pair of adjacent elements is compared and the elements are swapped if they are not in order.<br><br> This algorithm is not suitable for large data sets as its average and worst case complexity are of Ο(n2) where n is the number of items.

"""

unsort_list = [3, 12, 5, 4, 8, 5, 1]

def maf_bubble(lst):
    """ Sorts a list using a bubblesort algorithm """
    for p in range(len(lst)-1, 0, -1):
        for i in range(p):
            if lst[i] > lst[i + 1]:
                t = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = t
    return lst

#print(maf_bubble(unsort_list))

