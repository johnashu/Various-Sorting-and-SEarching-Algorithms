"""
Shell sort is a highly efficient sorting algorithm and is based on insertion sort algorithm. This algorithm avoids large shifts as in case of insertion sort, if the smaller value is to the far right and has to be moved to the far left.

This algorithm uses insertion sort on a widely spread elements, first to sort them and then sorts the less widely spaced elements. This spacing is termed as interval. This interval is calculated based on Knuth's formula as −
Knuth's Formula

h = h * 3 + 1

where −
   h is interval with initial value 1

This algorithm is quite efficient for medium-sized data sets as its average and worst case complexity are of Ο(n), where n is the number of items.
"""

    def maf_shell(a):
        """ 
        Step 1 − Initialize the value of h
        Step 2 − Divide the list into smaller sub-list of equal interval (h)
        Step 3 − Sort these sub-lists using insertion sort
        Step 3 − Repeat until complete list is sorted

        """
        interval = len(a) // 2
    
        while interval:
            for i, j in enumerate(a):
                while i >= interval and a[i - interval] > j:
                    a[i] = a[i - interval]
                    i -= interval
                a[i] = j
            interval = 1 if interval == 2 else int(interval * 5.0 / 11)                
        
    unsort_list = [4, 6, 3, 2, 1, 9, 7, 8, 5]  
    maf_shell(unsort_list)

    print(unsort_list)
