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
    while current: 
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
    while current: 
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
        if not current.next:
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
    while current: 
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
        while currentA and currentB and currentA.data == currentB.data:
            currentA = currentA.next
            currentB = currentB.next
        if (not currentA and currentB) or (currentA and not currentB ):
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
    while current: 
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
    if not head: 
        head = new
        head.next = None
        return head
    
    else: 
        while current.next: 
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
    if not head: 
        return head 
    
    while current.next:
        while current.data == current.next.data: 
            current.next = current.next.next
            if not current.next: 
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
    if not head: 
        return Node(data)
    elif position == 0: 
        front = Node(data)
        front.next = head
        return front 
    else: 
        current = head
        while position != 1:
            if not current.next: 
                return head
            current = current.next
            position -= 1
        temp = current.next
        current.next = Node(data)
        current.next.next = temp
        return head
  
# Merge two sorted linked lists
"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def MergeLists(headA, headB):
    
    # special cases
    if not headA: 
        return headB
    elif not headB:
        return headA
    
    else: 
        currentA = headA
        currentB = headB
        # point to the head
        if headA.data < headB.data:
            head = headA
            currentA = currentA.next
        else: 
            head = headB
            currentB = currentB.next
        current = head
        while currentA and currentB: 
            if currentA.data > currentB.data:
                current.next = currentB
                currentB = currentB.next
            else:
                current.next = currentA           
                currentA = currentA.next
            current = current.next
        if currentA: 
            current.next = currentA
        elif currentB:
            current.next = currentB
        return head
            
# Inserting a node into a sorted doubly linked list
"""
 Insert a node into a sorted doubly linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list 
"""
def SortedInsert(head, data):
    if not head.next: 
        new = Node(data)
        head.next = new
        return head
    else: 
        new = Node(data)
        current = head.next
        
        #if new node is the smallest
        if current.data > data: 
            new.next = current
            new.prev = head
            head.next = new
            current.prev = new
            return head 
        
        else: 
        # scan through until we find a node with larger data
            while current.next and current.next.data < data:    
                current = current.next
            if current.next:
                current.next.prev = new
                new.next = current.next
            else: 
                new.next = None
            new.prev = current
            current.next = new
            
         # debugging code          

 #       current = head
  #      print(current.data)
  #      while current.next != None: 
   #         print(current.next.data)
  #          current = current.next
  #      while current.prev != None: 
   #         print(current.prev.data)
  #          current = current.prev
            return head
  
  
#cycle detection
"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    current = head
    # there's 0 or 1 node
    if not current or not current.next: 
        return 0
    
    # 2 or more nodes
    else: 
        values = []
        current = head.next
        while current and current.next: 
            values.append(current.data)
            if current.next.data in values: 
                return 1
        return 0
        
    

  
  
  
  
  
  

    
    
    
  
  
  
  
  
  
  
  
  

  
  
  
  
  
  
  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

  
  
  

  
  
  
  
  
  

	
