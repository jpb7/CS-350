# CS 350: Homework 6
# Due: Week of 5/16
# Name: Jacob Bentley

import math

def machine(data, code):
    i = 0
    value = 0
    for instruction in code:
        if i >= len(data):
            raise Exception("Ran out of numbers")
        if instruction == "ADD":
            value += data[i]
            i += 1
        elif instruction == "MUL":
            value += data[i] * data[i+1]
            i += 2
        else:
            raise Exception("Illegal Instruction: " + instruction)
    if i < len(data):
        raise Exception("has leftover numbers")
    return value

###########################################################################
# Problem 1:
#
# I've constructed a new data processing language that I call addmul.
#
# It is a very simple language. Programs in addmul consist of two instructions:
#
# ADD takes a value from the data stream and adds it to the current total;
# MUL takes the next two numbers from the current data stream, multiplies them
# together, and adds them to the total.
#
# That's it.
#
# Your job is to take the data stream (just a list of numbers), and determine
# the program that will produce the largest value.
#
# Example:
#
# largestProgram([2,3,5]) should return
#
# ["ADD","MUL"]
#
# because this will return 17, where ["MUL","ADD"] will return 11, and
# ["ADD","ADD","ADD"] will return 10.
#
# You can run your program by calling machine([2,3,4], ["ADD","MUL"]).
#
# You can use `machine(numbers, largestProgram(numbers))` to test your
# algorithm on any list of numbers.
#
# Running time: O(2**n)
###########################################################################

def largestProgram(data):
    """
    >>> largestProgram([2,3,5])
    ['ADD', 'MUL']
    >>> largestProgram([6,3,5])
    ['MUL', 'ADD']
    >>> largestProgram([3,3,3])
    ['MUL', 'ADD']
    >>> largestProgram([9,4,7,6])
    ['MUL', 'MUL']
    >>> largestProgram([9,4,7,6,5])
    ['MUL', 'MUL', 'ADD']
    >>> largestProgram([1,4,7,6,5])
    ['ADD', 'MUL', 'MUL']
    >>> largestProgram([1,4,0,6,5])
    ['ADD', 'ADD', 'ADD', 'MUL']
    >>> largestProgram([1,4,0,6,-5])
    ['ADD', 'ADD', 'ADD', 'ADD', 'ADD']
    """
    d = getLargest(data, len(data) - 1, {}, 0, [])
    return d[max(d.keys())]

def getLargest(data, i, d, total, codes):
    if i < 0:
        d[total] = codes
        return d

    if i > 0:
        d = getLargest(data[:i-1], i-2, d, \
                       total + data[i] * data[i-1], \
                       ['MUL'] + codes)

    return getLargest(data[:i], i-1, d, \
                      total + data[i], \
                      ['ADD'] + codes)

###########################################################################
# Problem 2
#
# Implement the Floyd-Warshall algorithm from class.
#
# For example, the adjacency matrix
#
#    [ [  0, inf,  -2, inf], 
#      [  4,   0,   3, inf], 
#      [inf, inf,   0,   2], 
#      [inf,  -1, inf,   0] ]
#
# should give the distance matrix
#
#    [ [  0,  -1,  -2,   0], 
#      [  4,   0,   2,   4], 
#      [  5,   1,   0,   2], 
#      [  3,  -1,   1,   0] ].
#
# Running Time: O(V**3)
###########################################################################

def floyd(g):
    """
    >>> floyd([[0, math.inf, -2, math.inf], [4, 0, 3, math.inf], \
        [math.inf, math.inf, 0, 2], [math.inf, -1, math.inf, 0]])
    [[0, -1, -2, 0], [4, 0, 2, 4], [5, 1, 0, 2], [3, -1, 1, 0]]
    """
    for i in range(len(g)):
        for j in range(len(g)):
            for k in range(len(g)):
                g[j][k] = min(g[j][k], g[j][i] + g[i][k])
    return g

###########################################################################
# Problem 3
#
# Congratulations! You now own a factory that cuts rods.
#
# Customers will pay a certain value for a length of rods. For example:
#
#   rod length:  3  4  5  6   7
#   price:       2  3  6  8  11
#
# You just received a rod of length d.
#
# Write a function to determine the most efficient way to cut the rod
# to maximize the profit.
#
# You should return the maximum profit you can make.
#
# Running Time: O(n)
###########################################################################

def rods(lengths, prices, d):
    """
    >>> rods([3,4,5,6,7], [2,3,6,8,11], 20)
    30
    >>> rods([3,4,5,6,7], [2,3,6,8,11], 8)
    11
    >>> rods([3,4,5,6,7], [2,3,6,8,11], 10)
    13
    """
    revenue = 0
    i = len(lengths) - 1
    while d and i >= 0:
        if d < lengths[i]:
            i -= 1
        else:
            d -= lengths[i]
            revenue += prices[i]
    return revenue

############################################################################
# Problem 4: Parenthesizing matrices.
#
# This is the same problem as homework 4, problem 3, but this time I want
# you to do it in polynomial time using dynamic programming.
# 
# If I multiply an m*l matrix A by an l*n matrix B, that will take O(n*l*m)
# time to compute.
#
# If I include a n*o matrix C in this product, then I have the m*o matrix
# A*B*C.
#
# This is perfectly well defined, but I have a choice:
#
# Do I multiply (A*B)*C, giving a running time of n*l*m + n*m*o,
# or do I multiply A*(B*C), giving a running time of l*m*o + n*l*o?
#
# Since matrix multiplication is associative, we will get the same answer.
#
# So, given a list of dimensions of matrices such as 
#
#   [(n,l), (l,m), (m,o)],
#
# compute the fastest running time in which we can do matrix multiplication.
#
# Example: [(3,5), (5,4), (4,7)] is 3*5*4 + 3*4*7 = 144.
# 
# Running time: O(n)
############################################################################

def matrixParens(sizes):
    """
    >>> matrixParens([(3,5), (5,4), (4,7)])
    144
    """
    if len(sizes) < 3:
        return None

    a, c = 0, 2
    b, d = len(sizes) - 3, len(sizes) - 1
    leftSum = rightSum = 0

    # A and C go left to right, B and D go right to left
    while c < len(sizes):
        A, C = sizes[a], sizes[c] 
        B, D = sizes[b], sizes[d] 
        leftSum += A[0]*A[1]*C[0] + A[0]*C[0]*C[1]
        rightSum += B[0]*B[1]*D[1] + B[1]*D[0]*D[1]
        a, b, c, d = a+1, b-1, c+1, d-1

    if leftSum < rightSum:
        return leftSum
    return rightSum


if __name__ == "__main__":
    import doctest
    doctest.testmod()

