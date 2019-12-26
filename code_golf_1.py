"""
@ Problem
https://codegolf.stackexchange.com/questions/197286/integer-interpretator
The Challenge

Given a finite list of integers, split it into the fewest partitions possible such that no partition contains a number more than once.
Rules

Input can be in any format and any order.

Output can be in any format, as long as it's clear that each group is separate.

This is code-golf, so lowest score wins!


Input: [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]
Output: [[1,2],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1]]

Input: [1,3,4,2,6,5,1,8,3,8]
Output: [[1,3,4,2,6,5,8],[1,3,8]]

Input: [5,9,12,5,2,71,23,4,7,2,6,8,2,4,8,9,0,65,4,5,3,2]
Output: [[5,9,12,2,71,23,4,7,6,8,0,65,3],[5,4,8,9,2],[4,5,2],[2]]


---
File: code_golf_1.py
@Author: Kasper Wikman
"""


"""
Function checks if a number (numb) appears in a list
False = is in list
True  = is not in list
"""
def isInList(list,numb):
    for i in list:
        if(i==numb):
            return False
    return True

"""
Function checks if a certain number is within a list that uses lists within lists.
"""
def numInList(list, numb):
    for j in range(0, len(list)):
        if(list[j][0]==numb):
            id = list[j][1]
            list[j][1] = list[j][1] + 1
            return id,list

"""
Sort the integer list into single appearing systems
"""
def sortOnlyOnceperlist(list):
    startList = [[]] # Used to track which numbers been seen
    freqsList = [] # Used to track frequency of startList

    for i in list:
        if(isInList(startList[0],i)):
            startList[0].append(i)
            freqsList.append([i,1])
        else:
            [id,freqsList] = numInList(freqsList,i)
            if(len(startList)-1<id):
                startList.append([])
            startList[id].append(i)

    return startList


# Test cases
print("Test case 1: ")
print("Input: [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]")
print("Output: ",sortOnlyOnceperlist([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]))
print("Expected output: [[1,2],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1]]")
print("Test case 2: \n")
print("Input: [1,3,4,2,6,5,1,8,3,8]")
print("Output: ", sortOnlyOnceperlist([1,3,4,2,6,5,1,8,3,8]))
print("Expected output: [[1,3,4,2,6,5,8],[1,3,8]]")
print("Test case 3: \n")
print("Input: [5,9,12,5,2,71,23,4,7,2,6,8,2,4,8,9,0,65,4,5,3,2]")
print("Output: ",sortOnlyOnceperlist([5,9,12,5,2,71,23,4,7,2,6,8,2,4,8,9,0,65,4,5,3,2]))
print("Expected output: [[5,9,12,2,71,23,4,7,6,8,0,65,3],[5,4,8,9,2],[4,5,2],[2]]")
