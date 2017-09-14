## This is a collection of my solution for Hacker rank- Algorithms- Warmup section in Python 3
## Last updated: 09-13-2017

## "Solve Me First"
## This function prints the sum calculated and returned by solveMeFirst is provided for you in the editor.
import sys

def solveMeFirst(a,b):
   return a+b
  

num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1,num2)
print(res)

## "Simple Array Sum"
## Print the sum of the array's elements as a single integer.

import sys

def simpleArraySum(n, ar):
    # Complete this function
    return sum(ar)

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = simpleArraySum(n, ar)
print(result)

## "Compare the Triplets"
## Print two space-separated integers denoting the respective comparison points earned by Alice and Bob.

def solve(a0, a1, a2, b0, b1, b2):
    # Complete this function
    tie = (a0 == b0 ) + (a1 == b1) + (a2 == b2)
    alice = (a0 > b0) + (a1 > b1) + (a2 > b2) 
    bob = 3 - tie - alice
    return [alice, bob]

a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print (" ".join(map(str, result)))

## "A very big sum"
## Print a single value equal to the sum of the elements in the array.

def aVeryBigSum(n, ar):
    # Complete this function
    return sum(ar)

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = aVeryBigSum(n, ar)
print(result)

## "Diagonal Difference"
## Print the absolute difference between the two sums of the matrix's diagonals as a single integer.

import sys, math

n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

dia1 = 0; dia2 = 0 
index = 0 
while n!=0: 
    dia1 += a[index][index]
    dia2 += a[index][n-1]
    index += 1
    n -= 1
print(abs(dia1 - dia2))

## "Plus Minus"
## You must print the following  lines:
## 
## A decimal representing of the fraction of positive numbers in the array compared to its size.
## A decimal representing of the fraction of negative numbers in the array compared to its size.
## A decimal representing of the fraction of zeroes in the array compared to its size.

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
pos = 0; neg = 0; zero = 0
index = 0
total = n 
while n!= 0: 
    if arr[index] > 0: 
        pos += 1
    elif arr[index] < 0: 
        neg += 1
    else: 
        zero += 1
    index += 1
    n -= 1
print(round(pos/total,6))
print(round(neg/total,6)) 
print(round(zero/total,6))

## "Staircase"
## Print a staircase of size  using # symbols and spaces.

import sys, math

n = int(input().strip())
index = 0
while n!= 0:
    print(" "*(n-1)+'#'*(1+index))
    n -= 1
    index += 1

## "Mini-Max Sum" 
## Print two space-separated long integers denoting the respective minimum and 
## maximum values that can be calculated by summing exactly four of the five integers. 
## (The output can be greater than 32 bit integer.)

arr = list(map(int, input().strip().split(' ')))
max = max(arr); min = min(arr); total = sum(arr)
print(total - max, total - min)

## "Birthday Cake Candles"
## Print the number of candles Colleen blows out on a new line.

def birthdayCakeCandles(n, ar):
    # Complete this function
    max = -1; index = 0; numberMax = 0
    while n!= 0: 
        current = ar[index]
        if max < current: 
            max = current
            numberMax = 1
        elif max == current: 
            numberMax += 1
        n -= 1
        index += 1
    return numberMax 

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)

## "Time Conversion"
## Convert and print the given time in 24-hour format, where 00 <= hh <= 23.

def timeConversion(s):
    # Complete this function
    timing = s[-2:].lower()
    hr = int(s[:2])
    if timing == "pm" and hr < 12: 
        return str(hr+12) + s[2:-2]
    elif timing == "am" and hr == 12: 
        return "00" + s[2:-2] 
    else: 
        return s[:-2]

s = input().strip()
result = timeConversion(s)
print(result)










