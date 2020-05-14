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
        temp = self.lst[0]
        self.lst[0] = self.lst[-1]
        del self.lst[-1]
        self.length -=1
        self.top_down_heapify(0)
        return temp

    def __str__(self):
        print(self.lst,end="")
        return ''


class min_heap:

    def __init__(self):
        self.lst = []
        self.length = 0

    def bottom_up_heapify(self,child):
        par = math.ceil(child/2)-1
        while par>=0:
            if self.lst[par] <= self.lst[child]:
                return
            self.lst[par],self.lst[child] =  self.lst[child],self.lst[par]
            child=par
            par = math.ceil(child/2)-1
        

    def add(self,elm):
        self.lst.append(elm)
        self.length += 1
        self.bottom_up_heapify(self.length-1)

    def delete_root(self):
        temp = self.lst[0]
        self.lst[0]= self.lst[-1]
        del self.lst[-1]
        self.length -=1
        self.top_down_heapify(0)
        return temp

    def top_down_heapify(self, ind):
        curr = ind
        leftc = curr*2+1
        rightc = curr*2+2
        while rightc < self.length:
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
        # print(leftc)
        if leftc == self.length-1 and self.lst[leftc] < self.lst[curr]:
            self.lst[leftc],self.lst[curr] = self.lst[curr],self.lst[leftc]

    def generate_heap(self,lst):
        self.lst = lst
        self.length = len(self.lst)
        for i in range(self.length//2,-1,-1):
            self.top_down_heapify(i)

    
    def __str__(self):
        print(self.lst,end="")
        return ''

def adjust(heap1,heap2):
    if heap1.length < heap2.length:
        heap1.add(heap2.delete_root())
    else:
        heap2.add(heap1.delete_root())
def insert(heap1,heap2,elem):
    if heap1.length == 0:
        heap1.add(elem)
        return
    if heap2.length == 0:
        heap2.add(elem)
        return
    if elem <= (heap1.lst[0]+heap2.lst[0])//2:
            heap1.add(elem)
    else:
        heap2.add(elem)
    if heap1.length != heap2.length and heap1.length-1 != heap2.length:
        adjust(heap1,heap2)

heap1 = max_heap()
heap2 = min_heap()

for _ in range(int(input())):
    elem = int(input())
    insert(heap1,heap2,elem)
    if heap1.length == heap2.length:
        print((heap1.lst[0]+heap2.lst[0])//2)
    else:
        print(heap1.lst[0])