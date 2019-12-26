"""
@ Problem
https://codegolf.stackexchange.com/questions/120052/make-me-a-square
The Challenge
Task

Given one non-whitespace printable character, make a 3x3 square representation of that input. For example, if the input is #, then the output is:

###
# #
###

Rules

    The output format is strict, although a trailing newline is allowed. It means that the space in the middle is required, and also that the two newline characters separating the three lines are required.

Testcases

Input: #

Output:

###
# #
###

Input: A

Output:

AAA
A A
AAA

Input: 0

Output:

000
0 0
000


---
File: code_golf_2.py
@Author: Kasper Wikman
"""

"""
Simple print function to create a square
"""
def createSquare(letter):
    print letter*3,"\n",letter,letter,"\n",letter*3 # Yield same as below
    print "----"
    print 3*letter+letter.join('\n \n')+3*letter # Neat solution to the problem


createSquare('A')
