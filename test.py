# Python3 program to Correct the 
# Random Pointer in Doubly Linked List 

class Node: 
	
	def __init__(self, data): 
		self.data = data 
		self.prev = None
		self.next = None

# Function to correct the random pointer 
def correctPointer(head): 

	if head == None: 
		return

	temp = head 

	# if head.next's previous is not 
	# pointing to head itself, change it. 
	if (head.next != None and
		head.next.prev != head): 

		head.next.prev = head 
		return
	
	# If head's previous pointer is 
	# incorrect, change it. 
	if head.prev != None: 

		head.prev = None
		return
	
	# Else check for remaining nodes. 
	temp = temp.next
	while temp != None: 

		# If node.next's previous pointer 
		# is incorrect, change it. 
		if (temp.next != None and
			temp.next.prev != temp): 

			temp.next.prev = temp 
			return
		
		# Else If node.prev's next pointer 
		# is incorrect, change it. 
		elif (temp.prev != None and
			temp.prev.next != temp): 

			temp.prev.next = temp 
			return
		
		# Else iterate on remaining. 
		temp = temp.next
	
# Function to print the DLL 
def printList(head): 

	temp = head 

	while temp != None: 

		print(temp.data, "(", end = "") 

		# If prev pointer is null, print -1. 
		if temp.prev == None: 
			print(-1, end = ") ") 
		else: 
			print(temp.prev.data, end = ") ") 
		
		temp = temp.next
	
	print() 

# Driver Code 
if __name__ == "__main__": 

    # Creating a DLL 
    head = Node(1) 
    head.next = Node(2) 
    head.next.prev = head 
    head.next.next = Node(3) 
    head.next.next.prev = head.next 
    #head.next.next.next = Node(4) 
    node = Node(4)
    #head.next.next.next.prev = head.next.next
    node.prev = head.next.next
    print("Incorrect Linked List:", 
                    end = " ") 
    printList(head) 

    correctPointer(head) 

    print("\nCorrected Linked List:", 
                    end = " ") 
    printList(head) 

# This code is contributed 
# by Rituraj Jain 
