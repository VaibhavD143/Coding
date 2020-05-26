class Node:
    def __init__(self,val=0,prev=None,next=None):
        self.val = val
        self.next = next
        self.prev = prev
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        # self.key_node={}
        self.head = None
        self.tail = None
        self.data = {}

    def get(self, key: int) -> int:
        if key in self.data:
            self.data[key][1] = self.updatePriority(key)
            return self.data[key][0]
        else:
            return -1

    
    def updatePriority(self,key):
        head = self.data[key][1]
        # newNode = Node(head.val)
        # print(head.val)
        # print(head.prev.val)
        if head.next and head.prev:
            # print("came")
            head.next.prev,head.prev.next = head.prev,head.next
        elif head.next:
            self.head = head.next
        elif head.prev:
            head.prev.next = None
            self.tail=head.prev
        else:
            self.head = None
            self.tail = None
        val = head.val
        del head
        # print("inside update")
        # self.printList()
        return self.addNode(val)        
    
    def addNode(self,val):
        newNode = Node(val)
        if self.head:
            self.head.prev = newNode
        else:
            self.tail = newNode
        newNode.next = self.head
        self.head = newNode
        self.length+=1
        return self.head
    
    def deleteNode(self):
        
        head = self.tail
        if head.prev:
            head.prev.next = None
            self.tail = head.prev
        else:
            self.head = None
            self.tail = None
        val = head.val
        del self.data[val]
        del head
        self.length-=1
        
    
    def printList(self):
        head = self.head
        while head:
            print(head.val,end=",")
            head=head.next
        print
    
    def put(self, key: int, value: int) -> None:
        if key in self.data:
            self.data[key][0]=value
            self.data[key][1]=self.updatePriority(key)
        else:
            if len(self.data)==self.capacity:
                self.deleteNode()
            self.data[key] = [value,None]
            self.data[key][1] = self.addNode(key)        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)