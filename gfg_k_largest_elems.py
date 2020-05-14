#https://practice.geeksforgeeks.org/problems/k-largest-elements/0

import math

class max_heap:

    def __init__(self):
        self.lst = []
        self.length = 0

    def bottom_up_heapify(self,child):
        # par = child
        par = math.ceil(child/2)-1
        while par >=0:
            if self.lst[par] >= self.lst[child]:
                return
            self.lst[par],self.lst[child] = self.lst[child],self.lst[par]
            child= par
            par = math.ceil(child/2)-1

    def add(self,elm):
        self.lst.append(elm)
        self.length += 1
        self.bottom_up_heapify(self.length-1)

    def top_down_heapify(self,ind):
        curr = ind
        rightc = 2*curr + 2
        leftc = 2*curr + 1
        while rightc < self.length:
            if self.lst[rightc] > self.lst[leftc] and self.lst[rightc] > self.lst[curr]:
                self.lst[rightc],self.lst[curr] = self.lst[curr],self.lst[rightc]
                curr = rightc
                rightc = 2*curr + 2
                leftc = 2*curr + 1
            elif self.lst[leftc] > self.lst[curr]:
                self.lst[leftc],self.lst[curr] = self.lst[curr],self.lst[leftc]
                curr = leftc
                rightc = 2*curr + 2
                leftc = 2*curr + 1
            else:
                break
        if leftc == self.length -1 and self.lst[leftc] > self.lst[curr]:
            self.lst[leftc],self.lst[curr] = self.lst[curr],self.lst[leftc]
    
    def delete_root(self):
        self.lst[0] = self.lst[-1]
        del self.lst[-1]
        self.length -=1
        self.top_down_heapify(0)

    def generate_heap(self,lst):
        self.lst = lst
        self.length = len(lst)
        l_lst = len(lst)
        for i in range((l_lst//2)-1,-1,-1):
            self.top_down_heapify(i)

    def __str__(self):
        print(self.lst,end="")
        return ''

heap = max_heap()
for _ in range(int(input())):
    n,k = map(int,input().split())
    lst = list(map(int,input().split()))
    heap.lst= []
    heap.length = 0
    heap.generate_heap(lst)
    
    lst.sort(reverse = True)
    print(*lst[:k])