class Queue:
    def __init__(self,k,n):
        self.length = n
        self.k = k
        self.arr = [None]*n
        self.front = [-1]*k
        self.rear = [-1]*k
        self.next = list(range(1,n+1))
        self.next[-1] = -1
        self.free = 0

    def isEmpty(self,i):
        return self.rear[i] == -1
    
    def isFull(self):
        return self.free == -1
    
    def enqueue(self,elem,i):
        if self.isFull():
            print("Overflow",elem,"id",i)
            return
        
        if self.isEmpty(i):
            self.front[i] = self.rear[i] = self.free
        else:
            self.next[self.front[i]] = self.free
            self.front[i] = self.free
        nextFree = self.next[self.free]
        self.next[self.free] = -1

        self.arr[self.free] = elem
        self.free = nextFree
        print("Added",elem,"at",self.front[i],"id",i)
    
    def dequeue(self,i):
        if self.isEmpty(i):
            print("Empty",i)
        
        ind = self.rear[i]
        elem = self.arr[ind]
        self.arr[ind] = None
        
        self.rear[i] = self.next[ind]
            
        self.next[ind] = self.free
        self.free = ind
        print("Popped",elem,"at",ind,"id",i)
        return elem

obj = Queue(3,5)
obj.enqueue(15, 2) 
obj.enqueue(45, 2) 
print(obj.arr)
print(obj.next)
print(obj.front)
print(obj.rear)
obj.enqueue(17, 1) 
obj.dequeue(2)
print(obj.arr)
print(obj.next)
print(obj.front)
print(obj.rear)

obj.enqueue(49, 1) 
obj.enqueue(39, 1) 
print(obj.arr)
print(obj.next)
print(obj.front)
print(obj.rear)

obj.enqueue(11, 0) 
obj.enqueue(9, 0) 
obj.dequeue(2)
obj.enqueue(20, 0) 
obj.enqueue(7, 0)
print(obj.arr)
print(obj.next)
print(obj.front)
print(obj.rear)
