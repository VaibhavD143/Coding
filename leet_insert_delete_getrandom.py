import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pos={}
        self.lst=[]

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.pos:
            self.lst.append(val)
            self.pos[val] = len(self.lst)-1
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.pos:
            ind = self.pos[val]
            self.lst[ind],self.lst[-1] = self.lst[-1],self.lst[ind]
            self.pos[self.lst[ind]] = ind
            del self.pos[self.lst.pop()]
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.lst[random.randint(0,len(self.lst)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()