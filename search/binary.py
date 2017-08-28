"""
Binary search can be performed on a sorted array. In this approach, the index of an element x is determined if the element belongs to the list of elements. If the array is unsorted, linear search is used to determine the position.

In this algorithm, we want to find whether element x belongs to a set of numbers stored in an array numbers[]. Where l and r represent the left and right index of a sub-array in which searching operation should be performed.

"""


a = [1, 2, 3, 4, 5, 6, 7,  8, 9, 42]

l = a[0]
r = a[-1]



x = 4

def maf_binary(sorted_array, value):
    """
    In this algorithm, we want to find whether element x belongs to a set of numbers stored in an array numbers[]. Where l and r represent the left and right index of a sub-array in which searching operation should be performed.

    """
    err = "Not Found"

    min = 0
    max = len(sorted_array) - 1
    while min <= max: 
        mid = (min + max) // 2
        if sorted_array[mid] > value: max = mid - 1
        elif sorted_array[mid] < value: min = mid + 1
        else: return mid
    
print("Results fromFor Loop:", maf_binary(a, x))



def maf_bin_com(sorted_array, x, l, r):
    """ comprehensive binary search
    In this algorithm, we want to find whether element x belongs to a set of numbers stored in an array numbers[]. Where l and r represent the left and right index of a sub-array in which searching operation should be performed.
    """
    pass
    


print("Results from List Comprehension:", maf_bin_com(a, x, l, r))