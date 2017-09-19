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
	
## "Sparse Arrays"
## There is a collection of N strings ( There can be multiple occurences of a particular string ). 
## Each string's length is no more than 20 characters. There are also Q queries. For each query, 
## you are given a string, and you need to find out how many times this string occurs in the 
## given collection of N strings.

import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
while n != 0: 
    print((str(arr[-1]) + ' '), end='')
    arr = arr[:-1]
    n -= 1	
	