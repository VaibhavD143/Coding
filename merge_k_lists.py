"""
Merge in single sorted n number list from k sorted list with heap
"""

import math
import random

class min_heap:

    def __init__(self):
        #initialise heap
        self.lst = []
        self.length = 0

    def bottom_up_heapify(self,child):
        #heapify bottom up manner with index child
        par = math.ceil(child/2)-1
        while par>=0:
            if self.lst[par] <= self.lst[child]:
                #from here upper chain is heapified
                return
            self.lst[par],self.lst[child] =  self.lst[child],self.lst[par]
            child=par
            par = math.ceil(child/2)-1
        

    def add(self,elm):
        #add at the end of array and do bottom heapify
        self.lst.append(elm)
        self.length += 1
        self.bottom_up_heapify(self.length-1)

    def delete_root(self):
        #return minimum number and delete it from heap and heapify in top down manner
        temp = self.lst[0]
        self.lst[0]= self.lst[-1]
        del self.lst[-1]
        self.length -=1
        self.top_down_heapify(0)
        return temp

    def top_down_heapify(self, ind):
        #heapify in top down manner from index ind
        curr = ind
        leftc = curr*2+1    #left child
        rightc = curr*2+2   #right child
        while rightc < self.length:
            #check till both child of current node is present
            if self.lst[leftc] > self.lst[rightc] and self.lst[rightc] < self.lst[curr]:
                self.lst[rightc],self.lst[curr] = self.lst[curr],self.lst[rightc]
                curr = rightc
                leftc = curr*2+1
                rightc = curr*2+2
            elif self.lst[leftc] < self.lst[curr]:
                self.lst[leftc],self.lst[curr] = self.lst[curr],self.lst[leftc]
                curr = leftc
                leftc = curr*2+1
                rightc = curr*2+2
            else:
                break
        if leftc == self.length-1 and self.lst[leftc] < self.lst[curr]:
            #if only left child is present of current node
            self.lst[leftc],self.lst[curr] = self.lst[curr],self.lst[leftc]


    def generate_heap(self,lst):
        #assign list and call for top down heapify fron n//2 to 1 as leaves(n//2) elems doesn't violate heap
        self.lst = lst
        self.length = len(self.lst)
        for i in range(self.length//2,-1,-1):
            self.top_down_heapify(i)

    
    def __str__(self):
        print(self.lst,end="")
        return ''

def Rand(start, end, num): 
    res = [] 
    for j in range(num): 
        res.append(random.randint(start, end)) 
    return res 

def chunk_it(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]
chunks = []
heap = min_heap()
l_chunks = 10
for i in range(l_chunks):
    chunks.append(list(map(int,input().split(','))))
    heap.add([chunks[i].pop(0),i])

arr = []
while heap.length:
    elem,lind = heap.delete_root()
    arr.append(elem)
    if chunks[lind]:
        heap.add([chunks[lind].pop(0),lind])
print(arr)