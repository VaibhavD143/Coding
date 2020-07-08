class Stack:
    def __init__(self,k,n):
        self.length = n
        self.k = k
        self.top = [-1]*k
        self.arr = [None]*n
        self.next = list(range(1,n+1))
        self.next[-1] = -1
        self.free = 0

    def isFull(self):
        return self.free == -1

    def isEmpty(self,i):
        return self.top[i] == -1

    def push(self,elem,i):
        if self.isFull():
            print("Overflow")
            return False

        ind = self.free
        self.free = self.next[self.free]
        self.next[ind] = self.top[i]
        self.top[i] = ind
        self.arr[ind] = elem
        print("Added",elem,"id",i)
    
    def pop(self,i):
        
        if self.isEmpty(i):
            print("Empty ",i)
            return

        val = self.arr[self.top[i]]
        curr = self.top[i]
        self.top[i] = self.next[curr]
        self.next[curr] = self.free
        self.free = curr

        print("Popped",val,"from",i)
        return val
obj = Stack(3,5)
obj.push(15, 2) 
obj.push(45, 2) 
print(obj.arr)
print(obj.next)
print(obj.top)
obj.push(17, 1) 
obj.pop(2)
print(obj.arr)
print(obj.next)
print(obj.top)

obj.push(49, 1) 
obj.push(39, 1) 
print(obj.arr)
print(obj.next)
print(obj.top)

obj.push(11, 0) 
obj.push(9, 0) 
obj.pop(2)
obj.push(20, 0) 
obj.push(7, 0)
print(obj.arr)
print(obj.next)
print(obj.top)