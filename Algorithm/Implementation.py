## This is a collection of my solution for Hacker rank- Algorithms- Implementation section in Python 3
## Last updated: 09-15-2017

## "Kangaroo"
## Print YES if they can land on the same location at the same time; otherwise, print NO.

import sys

def kangaroo(x1, v1, x2, v2):
    # Complete this function
    if x1 == x2: 
        return "YES"
    if x1 > x2: 
        toBeChased = x1; chaser= x2; s1 = v1; s2 = v2
    else: 
        toBeChased = x2; chaser= x1; s1 = v2; s2 = v1
    if s1 >= s2: 
        return "NO"
    
    while toBeChased > chaser: 
        toBeChased += s1
        chaser += s2
        if toBeChased == chaser: 
            return "YES"
    return "NO"   
            
x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)