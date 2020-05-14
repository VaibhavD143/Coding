from collections import deque
lst = []

class FirstUnique:

    def __init__(self, nums):
        self.ha = {}
        self.bal=0
        self.que = deque([])
        self.createDq(nums)


    def showFirstUnique(self):
        while self.que and not self.que[0]:
            self.que.popleft()
            self.bal-=1
        if not self.que:
            return -1
        else:
            return self.que[0]
        

    def add(self, value):
        if value in self.ha:
            if self.ha[value] != None:
                self.que[self.ha[value]+self.bal] = None
                self.ha[value] = None
        else:
            self.que.append(value)
            self.ha[value] = len(self.que)-1
        
    def createDq(self,nums):
        for i in nums:
            if i in self.ha:
                if self.ha[i] != None:
                    self.que[self.ha[i]+self.bal] = None
                    self.ha[i] = None
            else:
                self.que.append(i)
                self.ha[i] = len(self.que)-1
    
obj = FirstUnique([])
while True:
    n = int(input())
    if n == 0:
        print(obj.que)
        print(obj.ha)
    elif n ==1:
        print(obj.showFirstUnique())
    else:
        obj.add(int(input()))
    