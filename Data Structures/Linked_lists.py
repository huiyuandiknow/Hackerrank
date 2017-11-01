## This is a collection of my solution for Hacker rank- Data Strucutres- Linked lists in Python 3
## Last updated: 10-30-2017

## "Print the Elements of a Linked List"

"""
 Print elements of a linked list on console
 head input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
 
 
"""
def print_list(head):
    current = head
    while current != None: 
        print(current.data)
        current = current.next

#Get Node Value
"""
 Get Node data of the Nth Node from the end.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the node data of the linked list in the below method.
"""

def GetNode(head, position):
    values = []
    current = head
    while current != None: 
        values.append(current.data)
        current = current.next
    values.reverse()
    return values[position]


# Delete a node  
"""
 Delete Node at a given position in a linked list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""

def Delete(head, position):
    if position == 0: 
        return head.next
    
    current = head
    while position != 1: 
        
        # if the to-be-deleted is already None
        if current.next == None:
            return head
        
        current = current.next
        position -= 1
        
    current.next = current.next.next
    return head
  
# print in reverse
"""
 Print elements of a linked list in reverse order as standard output
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""

def ReversePrint(head):
    values = []
    current = head
    while current != None: 
        values.append(current.data)
        current = current.next
    values.reverse()
    for i in values:
        print(i)



# Compare two linked lists
"""
 Merge two linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def CompareLists(headA, headB):
    if headA.data != headB.data: 
        return 0
    else: 
        currentA = headA
        currentB = headB
        while currentA != None and currentB != None and currentA.data == currentB.data:
            currentA = currentA.next
            currentB = currentB.next
        if (currentA == None and currentB != None) or (currentA != None and currentB == None):
            return 0
        return 1
    
  
# reverse a linked list 
"""
 Reverse a linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def Reverse(head):
    values = []
    current = head
    while current != None: 
        values.append(current.data)
        current = current.next
    values.reverse()
    if len(values) == 0:
        return None
    
    else:
        head = Node(values[0])
        if len(values) == 1: 
            head.next = None        
        else:
            current = head
            for i in values[1:]:
                current.next = Node(i)
                current = current.next
        return head

# Insert a Node at the Tail of a Linked List 
"""
 Insert Node at the end of a linked list 
 head pointer input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
 
 return back the head of the linked list in the below method
"""

def Insert(head, data):
    current = head
    new = Node(data)
    if head == None: 
        head = new
        head.next = None
        return head
    
    else: 
        while current.next != None: 
            current = current.next 
    
        current.next = new
    return head


# Delete duplicate- value nodes from a sorted linked list
"""
 Delete duplicate nodes
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def RemoveDuplicates(head):
    current = head
    if head == None: 
        return head 
    
    while current.next != None:
        while current.data == current.next.data: 
            current.next = current.next.next
            if current.next == None: 
                return head
        current = current.next
    return head
 
# Insert a node at a specific position in a linked list  
  
"""
 Insert Node at a specific position in a linked list
 head input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""
#This is a "method-only" submission.
#You only need to complete this method.
def InsertNth(head, data, position):
    if head == None: 
        return Node(data)
    elif position == 0: 
        front = Node(data)
        front.next = head
        return front 
    else: 
        current = head
        while position != 1:
            if current.next == None: 
                return head
            current = current.next
            position -= 1
        temp = current.next
        current.next = Node(data)
        current.next.next = temp
        return head
  
  
  
  
  
  
  
  
  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

  
  
  

  
  
  
  
  
  

	
