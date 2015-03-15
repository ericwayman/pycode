#help functions
def parentIndex(n):
    """For any index n in the heap returns the index of the corresponding parent node
    """
    if n == 0:
        return -1
    else:
        return (n+1)/2-1

def youngChildIndex(n):
    """For any index n in the heap returns the index of the younger child
    """
    return 2*n+1




class heap(list):
    #a class representing a min heap.  Keys of parents are less than or equal to keys of children


    def __init__(self,data):
        self.data = data
        for i in range(len(data)):
            self.insert(data[i])



    def swap(self,i,j):
        """
        swaps the entries at indices i and j.
        """
        placeHolder = self[i]
        self[i] = self[j]
        self[j] = placeHolder

    def bubbleUp(self,index):
        """
        Pushes the entry self[index] up through the heap until each parent is smaller than each child
        """
        if parentIndex(index) == -1:
            #at the root of heap, so no parent
            return
        if self[parentIndex(index)] > self[index]:
            self.swap(parentIndex(index),index)
            self.bubbleUp(parentIndex(index))


    def insert(self,x):
        """
        Inserts the entry x into the heap.  Initially inserts at the last entry of the heap, then using bubbleUp
        pushes the entry up the heap until each parent is smaller than each child.
        """
        self.append(x)
        self.bubbleUp(len(self)-1)



    def bubbleDown(self,index):
        """
        Pushes the entry self[index] down through the heap until each parent is smaller than each child.  
        Pushes the entry down the tree by swapping it with the smaller of the two children.
        """

        #minIndex is the index of the smallest entry of self[index] and its two children
        minIndex = index
        #check children of self[index] to see which is smallest
        for i in [0,1]:
            #check to see if either child is smaller than the parent (if the child exists)
            if youngChildIndex(index)+i < len(self): #len(self)-1 is the last index
                if self[youngChildIndex(index)+i] < self[minIndex]:
                    minIndex = youngChildIndex(index)+i
        if minIndex != index:
            self.swap(index,minIndex)
            self.bubbleDown(minIndex)


    def extractMin(self):
        """
        removes and returns the min element (the root) of the heap.  Creates a new root by placing the last entry of the heap
        as the new root and performing bubble down
        """
        minValue = -1
        if len(self) > 0:
            minValue = self[0]
            self[0] = self[len(self)-1]
            del self[-1]
            self.bubbleDown(0)
        return minValue



