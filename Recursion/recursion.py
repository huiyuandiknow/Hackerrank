## This is a collection of my solution for Hacker rank- Algorithms- Warmup section in Python 3
## Last updated: 09-14-2017

## "Recursive Digit Sum"
## Output the super digit of P, where P is created as string N replicated k times.
import sys

inputs = input().split(' ')
n = inputs[0]; k = int(inputs[1])
#value = n * int(k)

def recursiveSum(n, k): 
    # base case
    if len(str(n)) == 1: 
        return n  
    else: 
        splitted =  list(n)
        return recursiveSum(str(k*sum(int(i) for i in splitted)), 1)
    
print(recursiveSum(n, k))