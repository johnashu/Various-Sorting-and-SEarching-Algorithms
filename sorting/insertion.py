"""
This is an in-place comparison-based sorting algorithm. Here, a sub-list is maintained which is always sorted. For example, the lower part of an array is maintained to be sorted. An element which is to be 'insert'ed in this sorted sub-list, has to find its appropriate place and then it has to be inserted there. Hence the name, insertion sort.

The array is searched sequentially and unsorted items are moved and inserted into the sorted sub-list (in the same array). This algorithm is not suitable for large data sets as its average and worst case complexity are of Ο(n2), where n is the number of items.



"""

unsort_list = [456, 456, 4, 89, 4956, 53, 12, 123, 345, 134, 23, 46, 37]

def maf_insertion(l):
    """ 
    Sorts a list using an Insertion algorithm 
    Step 1 − If it is the first element, it is already sorted. return 1;
    Step 2 − Pick next element
    Step 3 − Compare with all elements in the sorted sub-list
    Step 4 − Shift all the elements in the sorted sub-list that is greater than the 
            value to be sorted
    Step 5 − Insert the value
    Step 6 − Repeat until list is sorted
    
    for p in range(len(l)-1,0,-1):
        for i in range(p):
            if l[i]>l[i+1]:
                t = l[i]
                l[i] = l[i+1]
                l[i+1] = t
    """
    #initialise  v and  h
    v = 0
    h = 0

    for i in range(1, len(l)):
        # select the value to be inserted
        v = l[i]
        h = i

        #locate the hole position for the element to be inserted into
        while h > 0 and l[h - 1] > v:
            l[h] = l[h - 1]
            h = h - 1

        #insert the number at the hole position
        l[h] = v

maf_insertion(unsort_list)
print(unsort_list)
