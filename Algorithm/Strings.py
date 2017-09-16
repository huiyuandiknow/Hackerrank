## This is a collection of my solution for Hacker rank- Algorithms- Strings section in Python 3
## Last updated: 09-15-2017

## "Super Reduced String"
## If the final string is empty, print Empty String; otherwise, print the final non-reducible string.
import sys

def checkTwo(s): 
    return s[0] == s[1]

def reduce(s): 
    index = 0
    while len(s) >= 2 and index != len(s)-1:
        if s[index]==s[index+1]:
            if index == 0:  
                s = s[index+2:]
            else: 
                s = s[:index] + s[index+2:]
            index = 0 
        else: 
            index += 1
    return s

def super_reduced_string(s):
    result = reduce(s)
    if result == '': 
        return 'Empty String'
    else: 
        return result
    

s = input().strip()
result = super_reduced_string(s)
print(result)

## "CamelCase"
## Print the number of words in string s.

import sys, re

s = input().strip()
# use regular expression to find the words starting with upper case letters, followed by any number of lower case letters
print( len(re.findall('[A-Z][^A-Z]*', s))+1)
