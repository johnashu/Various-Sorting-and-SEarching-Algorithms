
unsort_list = [456, 456, 4, 89, 4956, 53, 12, 123, 345, 134, 23, 46, 37]

class mafsort(l):

    """
    bubble sort algorithm

    This sorting algorithm is comparison-based algorithm in which each pair of adjacent elements is compared and the elements are swapped if they are not in order. This algorithm is not suitable for large data sets as its average and worst case complexity are of Ο(n2) where n is the number of items.

    """



    def bubble(self, l):
        """ Sorts a list using a bubblesort algorithm """
        for p in range(len(l)-1,0,-1):
            for i in range(p):
                if l[i]>l[i+1]:
                    t = l[i]
                    l[i] = l[i+1]
                    l[i+1] = t


bubblesort = mafsort.bubble(unsort_list)

print(bubblesort)

