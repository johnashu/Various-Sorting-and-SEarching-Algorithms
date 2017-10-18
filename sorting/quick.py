"""
Quick sort is a highly efficient sorting algorithm and is based on partitioning of array of data into smaller arrays. A large array is partitioned into two arrays one of which holds values smaller than the specified value, say p, based on which the partition is made and another array holds values r than the p value.

Quick sort partitions an array and then calls itself recursively twice to sort the two resulting subarrays. This algorithm is quite efficient for large-sized data sets as its average and worst case complexity are of Ο(n2), where n is the number of items.

"""

unsort_list = [5, 6, 7, 9, 1, 8, 3, 4, 2, 5, 8,
               10, 11, 15, 85, 12, 6, 7, 15, 45, 49, 61]

txt_file = 'text.txt'


with open(txt_file, "rb") as tf:
    usl = tf.read()

def maf_quickSort_com(a):
    """
    QuickSort Algorithm..

    Step 1 − Make the right-most index value pivot
    Step 2 − partition the array using pivot value
    Step 3 − quicksort left partition recursively
    Step 4 − quicksort right partition recursively

    """

    l = []
    m = []
    r = []

    if len(a) > 1:
        p = a[-1]
        a = [l.append(x) if x < p else m.append(x) if x == p else r.append(x) for x in a]
        return maf_quickSort_com(l) + m + maf_quickSort_com(r)
    else:
        return a

print(maf_quickSort_com(usl))