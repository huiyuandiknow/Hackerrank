## This is a collection of my solution for Hacker rank- Data Structures - Stacks in Python 3
## Last updated: 11-02-2017

## "Maximum element"
## For each type 3 query, print the maximum element in the stack on a new line.
class Stack:
    def __init__(self, head=None):
        self.storage = [head]
        self.max = None

    def push(self, new_element):
        self.storage.append(new_element) 
        if (self.max and new_element > self.max) or (not self.max): 
            self.max = new_element

    def pop(self):
        temp = self.storage[-1]
        self.storage = self.storage[0:-1]
        if temp == self.max: 
            self.max = self.recalculate()
    
    def recalculate(self):
       # print(self.storage)
        if not self.storage: 
            return None
        else: 
            if len(self.storage) == 1: 
                self.max = self.storage[0]
                return self.storage[0]
            else: 
                max = self.storage[0]
                for i in self.storage: 
                    if i > max: 
                        max = i
                self.max = max
                return max
    
    def maxx(self):
        if self.max: 
            return self.max
        else: 
            return self.recalculate()
    
import sys

n = int(input().strip())
first_time = True
while n!= 0:
    line = input().split(' ')
    command = int(line[0])
    if len(line) == 2: 
        num = int(line[1])
    if command == 1:
        if first_time: 
            s = Stack(num)
            first_time = False
        else: 
            s.push(num)
    elif command == 2: 
        s.pop()
    else: 
        print(s.maxx())
    n -= 1



# "balanced brackets"
#!/bin/python3

      
import sys

def isBalanced(s):
    lefts = '{[('
    rights = '}])'
    closes = { a:b for a,b in zip(rights,lefts)}
    
    stack = []
    for c in s:
        if c in lefts:
            stack.append(c)
        elif c in rights:
            if not stack or stack.pop() != closes[c]:
                return False
    return not stack  # stack must be empty at the end

                

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        s = input().strip()
        if isBalanced(s):
            print('YES')
        else:
            print('NO')
        
    
