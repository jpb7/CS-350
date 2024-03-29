
# CS 350: Homework 1
# Due: Week of 4/4
# Name: Jacob Bentley

# This homework is largely review, and to make sure you have a working version of python.

import math as m

############################################################################
#
# Problem 1
# Find the largest two elements in a list.
# Return your answer in a tuple as (largest, secondLargest)
#
# Running Time: O(n)
############################################################################

def largest2(l):
    """
    >>> largest2([1, 2, 3, 4, 5, 6, 7])
    (7, 6)
    >>> largest2([7, 6, 5, 4, 3, 2, 1])
    (7, 6)
    >>> largest2([-3, -5, -2, -1, -4, 0, -6])
    (0, -1)
    >>> largest2([5, 6, 7, 3, 2, 4, 1])
    (7, 6)
    """
    max1, max2 = l[0], l[1]
    for n in l:
        if n > max1:
            max2 = max1
            max1 = n
        elif max1 > n > max2:
            max2 = n
    return max1, max2

############################################################################
#
# Problem 2
# Reverse a list in place,
# and returned the reversed list.
#
# Running Time: O(n)
############################################################################

def reverse(l):
    """
    >>> l = [1, 2, 3, 4, 5]
    >>> reverse(l)
    [5, 4, 3, 2, 1]
    >>> l
    [5, 4, 3, 2, 1]
    >>> l = [1, 2, 3, 4, 5, 6]
    >>> reverse(l)
    [6, 5, 4, 3, 2, 1]
    """
    i = 0
    j = len(l) - 1
    mid = len(l) // 2
    if not mid % 2:
        mid += 1
    # O(n/2), traverse from each end and meet in middle
    while i <= mid and j >= mid:
        l[i], l[j] = l[j], l[i]
        i += 1
        j -= 1
    return l

############################################################################
#
# Problem 3
# Compute the transpose of a matrix in place.
#
# What is the input size measuring? rows * columns
# Running Time: O(n^2)
############################################################################

#   Matrix must be square.
def transpose(m):
    """
    >>> m = [[1,2,3],[4,5,6],[7,8,9]]
    >>> transpose(m)
    [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    """
    # O(n^2)
    for i in range(len(m)):
        # O(n)
        for j in range(i+1, len(m[i])):
            m[i][j], m[j][i] = m[j][i], m[i][j]
    return m

############################################################################
#
# Problem 4
# Given a list of points, return the distance between the two closest points.
# The distance between two points (x1,y1) and (x2,y2) is:
# d = sqrt((x2-x1)^2 + (y2-y1)^2)
#
# Running Time: O(n^2)
############################################################################

def pointDist(points):
    """
    >>> pointDist([(1,1), (4,5), (13,6)])
    5.0
    >>> pointDist([(4,5), (13,6), (1,1)])
    5.0
    >>> pointDist([(5,7), (6,8), (10,11), (5, 6)])
    1.0
    """
    min_dist = m.inf
    # O(n^2)
    for i in range(len(points) - 1):
        x1, y1 = points[i][0], points[i][1]
        # O(n)
        for j in range(i+1, len(points)):
            x2, y2 = points[j][0], points[j][1]
            d = m.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            if d < min_dist:
                min_dist = d
    return min_dist

############################################################################
#
# Problem 5
# multiply two matrices A and B.
# For the running time A is an m*n matrix, and B is an n*l matrix.
#
# what is the size of the output? m*n
# Running Time: O(n^2)
############################################################################

def matMul(A, B):
    """
    >>> matMul([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]])
    [[58, 64], [139, 154]]
    """
    C = [[] for row in range(len(A))]
    i = 0
    # O(n^2)
    while i < len(A):
        j = k = prod = 0
        # O(n)
        while j < len(B) and k < len(A):
            prod += A[i][j] * B[j][k]
            if j == len(B) - 1:
                C[i] += [prod]
                j = prod = 0
                k += 1
            else:
                j += 1
        i += 1
    return C

############################################################################
#
# Problem 6
# Compute the number of 1s that would be in the binary representation of x
# for example: 30 = 11110 in base 2, and it has 4 1s.
#
# For full credit, you should assume that
# arithmetic operations are *not* constant time.
# bitwise operations are constant time though.
#
# What is the input size? n bits in x
# Running Time: O(n)
############################################################################

def popcount(x):
    """
    >>> popcount(7)
    3
    >>> popcount(30)
    4
    >>> popcount(256)
    1
    >>> popcount(0)
    0
    """
    count = 0
    # O(n)
    while x:
        if x & 1:
            count += 1
        x >>= 1
    return count

############################################################################
#
# Problem 7
# compute the integer square root of x.
# This is the largest number s such that s^2 <= x.
#
# You can assume that arithmetic operations are constant time for this algorithm.
#
# What is the input size? n bits in x
# Running Time: O(sqrt(n))
############################################################################

def isqrt(x):
    """
    >>> isqrt(6)
    2
    >>> isqrt(121)
    11
    >>> isqrt(64)
    8
    >>> isqrt(0)
    0
    >>> isqrt(1)
    1
    """
    i = 0
    # O(sqrt(n))
    while i**2 <= x:
        i += 1
    return i - 1

############################################################################
#
# Problem 8: Word Search
#
# determine if string s is any where in the word grid g.
#
# for example s = "bats"
# g = ["abrql",
#      "exayi",
#      "postn",
#      "cbkrs"]
#
# Then s is in the word grid
#     [" b   ",
#      "  a  ",
#      "   t ",
#      "    s"]
#
# what is your input size? len(grid) * len(grid[i])
# Running Time: O(n^2)
############################################################################

def wordSearch(word, grid):
    """
    >>> s = "bats"
    >>> g = ["abrql", "exayi", "postn", "cbkrs"]
    >>> wordSearch(s,g)
    True
    >>> s = "abrql"
    >>> wordSearch(s,g)
    True
    >>> s = "aep"
    >>> wordSearch(s,g)
    True
    >>> s = "bsyl"
    >>> wordSearch(s,g)
    True
    """
    # O(n^2)
    for i in range(len(grid)):
        # O(n)
        for j in range(len(grid[i])):
            # O(3)
            for dx in range(1, -2, -1):
                # O(3)
                for dy in range(1, -2, -1):
                    # O(1)
                    if not dx and not dy:
                        dy -= 1
                    k, row, col = 0, i, j
                    # O(n) worst, O(1) best
                    while (wordInGrid(k, row, col, grid, word)):
                        row += dx
                        col += dy
                        k += 1
                    # O(1)
                    if k == len(word):
                        return True
    return False

#   Return True if letter in grid matches letter in word.
def wordInGrid(k, row, col, grid, word):
    return (0 <= row < len(grid) and
            0 <= col < len(grid[row]) and
            k < len(word) and
            grid[row][col] == word[k])

############################################################################
#
# Problem 9: Convex Hull
#
# In class we learned about the convex hull problem.
# We also learned that for any line segment on the convex hull,
# every other point will we on the same side of that line.
#
# Use this fact to write an algorithm to find all of the points in the convex hull.
#
# for example: [(1,1), (4,2), (4,5), (7,1)] are the points shown below
#
#    *
#
#    *
# *     *
#
# The convex hull is [(1,1), (4,5), (7,1)]
#    *
#   / \
#  /   \
# *-----*
#
# Running Time: O(n^2)
############################################################################

#   Order of returned points may not match input.
def convexHull(points):
    """
    >>> convexHull([(1,1), (4,2), (4,5), (7,1)])
    [(1, 1), (4, 5), (7, 1)]
    >>> convexHull([(1,3), (2,3), (3,1), (6,6)])
    [(1, 3), (6, 6), (3, 1)]
    """
    hull = []
    # O(n^2)
    for p1 in points:
        # O(n)
        for p2 in points:
            if p1 == p2:
                continue
            a, b, c = makeLine(p1, p2)
            i = 0
            # O(1) at best, O(n) at worst
            while i < len(points) and a*points[i][0] + b*points[i][1] >= c:
                i += 1
            # O(1)
            if i == len(points):
                # O(n)
                if pointNotInHull(p1, hull):
                    hull += [p1]
                # O(n)
                if pointNotInHull(p2, hull):
                    hull += [p2]
    return hull

#   Return True if point is not already in hull.
def pointNotInHull(point, hull):
    i = 0
    # O(n)
    while i < len(hull) and hull[i] != point:
        i += 1
    if i == len(hull):
        return True
    return False

#   Take point1 and point2, return values such that ax + by = c.
def makeLine(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    a = y2 - y1
    b = x1 - x2
    c = x1*y2 - x2*y1
    return (a, b, c)

############################################################################
#
# Problem 10: Running time
#
# Find the Theta time complexity for the following functions.
# If the problem is a summation, give a closed form first.
#
# 1. f(n) = n^2 + 2n + 1
#    O(n^2)
# 2. f(n) = sum(i=0, n, sum(j=0, i, 1) )
#    O(n^2)
# 3. f(n) = (n+1)!
#    O(n!)
# 4. f(n) = sum(i=0, n, log(i))
#    O(n*log(n))
# 5. f(n) = log(n!)
#    O(log^n(n))
############################################################################

if __name__ == "__main__":
    import doctest
    doctest.testmod()
