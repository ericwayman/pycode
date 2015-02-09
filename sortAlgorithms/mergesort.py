import numpy as np


class sortList(list):

    def merge(self, low, middle, high):
        """
        A is the array to be merged.  low < middle < high are indices for the bounds of the two subarrays to be merged.
        method called my mergeSort to merge the lists If the subarrays self[low:middle] and self[middle:high+1] are sorted increasing order, 
        the merge sorts the sub array A[low:high+1] by merge the two subarrays
        """
        counter = 0
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

    def mergeSort(self, low, high):
        if low < high:
            middle = (low + high)/2
            self.mergeSort(low,middle)
            self.mergeSort(middle+1,high)
            self.merge(low,middle,high)
