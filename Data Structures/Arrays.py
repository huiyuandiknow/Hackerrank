## This is a collection of my solution for Hacker rank- Algorithms- Implementation section in Python 3
## Last updated: 09-15-2017

## "Arrays - DS"
## Print all N integers in A in reverse order as a single line of space-separated integers.
#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
while n != 0: 
    print((str(arr[-1]) + ' '), end='')
    arr = arr[:-1]
    n -= 1