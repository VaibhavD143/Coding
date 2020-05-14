"""
https://practice.geeksforgeeks.org/problems/kth-largest-element-in-a-stream/0
"""
import math

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

    def change_key(self,elem):
        self.lst[0] = elem
        self.top_down_heapify(0)

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


for _ in range(int(input())):
    k,n = map(int,input().split())
    lst = list(map(int,input().split()))
    hp = min_heap()
    i=-1
    for i in range(k-1):
        hp.add(lst[i])
        print(-1,end=" ")
    hp.add(lst[i+1])
    print(hp.lst[0],end=" ")
    for j in range(k,n):
        if hp.lst[0] < lst[j]:
            hp.change_key(lst[j])
        print(hp.lst[0],end=" ")
    print()