import numpy as np
import heap


class sortList(list):

    "all methods sort in increasing order"

    "mergeSort methods"
    def __merge(self, low, middle, high):
        """
        low < middle < high are indices for the bounds of the two subarrays to be merged.
        method called by mergeSort to merge the lists If the subarrays self[low:middle] and self[middle:high+1] are sorted increasing order, 
        the merge sorts the sub array A[low:high+1] by merge the two subarrays
        """
        buffer1 = self[low:middle+1] 
        buffer2 = self[middle+1:high+1]
        for i in range(low,high+1):
            if len(buffer1)== 0:
                self[i:high+1] = buffer2
                break
            elif len(buffer2) == 0:
                self[i:high+1] = buffer1
                break
            else:
                if buffer1[0] <= buffer2[0]:
                    self[i] = buffer1[0]
                    buffer1 = buffer1[1:]
                else:
                    self[i] = buffer2[0]
                    buffer2 = buffer2[1:]

    def __mergeSortRange(self, low, high):
        """
        mergeSorts all elements between the indices low and high.  
        """
        if low < high:
            middle = (low + high)/2
            self.__mergeSortRange(low,middle)
            self.__mergeSortRange(middle+1,high)
            self.__merge(low,middle,high)
    def mergeSort(self):
        high = len(self) -1
        self.__mergeSortRange(0,high)


    "quickSort methods"
    def quickSort(self):
        high = len(self)-1
        self.__quickSortRange(0,high)


    def swap(self,i,j):
        """
        swaps the value of index i and index j in self
        """
        placeholder = self[i]
        self[i] = self[j]
        self[j] = placeholder

    def __partition(self,low,high):
        """
        low and high are the indices 
        returns the pivot index p.  And partitions the array so that all elements in indices low to pivot index -1 are less than or equal to the value at the pivot index and 
        all elements in indices pivot index + 1 to high are large than the index
        """
        p = high
        pivotValue = self[high]
        firstHigh = low
        for i in range(low, high):
            if (self[i] < pivotValue):
                self.swap(i,firstHigh)
                firstHigh = firstHigh +1
        self.swap(firstHigh,high)
        return firstHigh


    def __quickSortRange(self,low,high):
        "applies to the subarray in the idices [low,high]"
        if low < high:
            p = self.__partition(low,high)
            self.__quickSortRange(low,p-1)
            self.__quickSortRange(p+1,high)


    def heapSort(self):
        "implements heapsort on an array.  Returns a new array whose entries are the  entries of self are in increasing order"
        sortedList = [0]*len(self)
        H = heap.heap(self)
        for i in range(len(self)):
            sortedList[i] = H.extractMin()
        return sortList(sortedList)

    "binary search methods"

    def __binarySearchRange(self,low,high,val):
        if high < low:
            return -1
        middle = (low+high)/2
        middleValue = self[middle]
        if val == self[middle]:
            return middle
        elif val <self[middle]:
            "binary search in first half of array"
            return self.__binarySearchRange(low,middle-1,val)
        else:
            "binary search in second half of array"
            return self.__binarySearchRange(middle+1,high,val)

    def binarySearch(self,val):
        """
        Implements binary search on a sorted list.  Returns the index of the match if val is in the array and -1 if val is not in the array.
        """
        high = len(self) -1
        return self.__binarySearchRange(0,high,val)



