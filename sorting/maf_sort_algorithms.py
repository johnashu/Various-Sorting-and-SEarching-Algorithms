
unsorted = [456, 456, 4, 89, 4956, 53, 12, 123, 345, 134, 23, 46, 37]

class MafSort:

    def __init__(self, lst):
        self.lst1 = lst
        #self.list2 = list2

    
    """
    bubble sort algorithm

    This sorting algorithm is comparison-based algorithm in which each pair of adjacent elements is compared and the elements are swapped if they are not in order. This algorithm is not suitable for large data sets as its average and worst case complexity are of Ο(n2) where n is the number of items.

    """

    def bubble(self, lst):
        """ Sorts a list using a bubblesort algorithm """
        for p in range(len(lst)-1,0,-1):
            for i in range(p):
                if lst[i] > lst[i+1]:
                    t = lst[i]
                    lst[i] = lst[i+1]
                    lst[i+1] = t


bubblesort = MafSort.bubble(unsorted)

print(bubblesort)

