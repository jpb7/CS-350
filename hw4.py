# CS 350: Homework 4
# Due: Week of 4/4
# Name: Jacob Bentley

############################################################################
# Problem 1: Quicksort
# 
# implement quicksort described in class.
#
# Recurrence worst case:
# Recurrence average case:
# Running time worst case:
# Running time average case:
# 
# When does the worst case happen?
############################################################################

def quicksort(l):

    """
    >>> quicksort([3,2,6,1,4])
    [1, 2, 3, 4, 6]
    >>> quicksort([5,4,3,2,1])
    [1, 2, 3, 4, 5]
    >>> quicksort([5,5,4,3,2,1])
    [1, 2, 3, 4, 5, 5]
    """

    if not l:
        return []

    pivot = l.pop()
    smaller = quicksort([n for n in l if n < pivot])
    larger = quicksort([n for n in l if n >= pivot])

    return smaller + [pivot] + larger

############################################################################
# Problem 2: maximum sublist sum
# 
# A sublist is a contiguous piece of a list
# [1,2,1] is a sublist of [4,1,2,1,3]
# but [1,2,3] isn't.
#
# the sum of a list is just adding all of the elements.
#
# compute the maximum sum of any sublist.
# For example:  [-2,1,-3,4,-1,2,1,-5,4]
# the maximum sublist is [4,-1,2,1] with a sum of 6
# 
# Running time: O(n**3)
############################################################################

def maxSublist(l):

    """
    >>> maxSublist([-2,1,-3,4,-1,2,1,-5,4])
    [4, -1, 2, 1]
    >>> maxSublist([-2,1,3,2,4,-3,-5])
    [1, 3, 2, 4]
    """

    d = {}
    for i in range(len(l)):
        for j in range(i, len(l)):
            d[sum(l[i:j])] = l[i:j]

    return d[max(d)]

############################################################################
# Problem 3: Parenthesizing matrices.
# 
# If I multiply an m*l matrix A by an l*n matrix B
# That will take O(n*l*m) time to compute.
#
# If I include a n*o matrix C in this product
# Then I have the m*o matrix A*B*C.
# This is perfectly well defined, but I have a choice.
# Do I multiply (A*B)*C (giving a running time of n*l*m + n*m*o)
# or do i multiply A*(B*C) (giving a running time of l*m*o + n*l*o)
#
# Since matrix multiplication is associative, We will get the same answer.
#
# So, given a list of dimensions of matrices
# (for example [(n,l), (l,m), (m,o)])
# compute the fastest running time that we can do matrix multiplication in. 
#
# example [(3,5), (5,4), (4,7)]
# is 3*5*4 + 3*4*7 = 144
# 
# Running time: O(n)
############################################################################

def matrixParens(sizes):

    """
    >>> matrixParens([(3,5), (5,4), (4,7)])
    144
    >>> matrixParens([(3,5), (5,4), (4,7), (7,8)])
    564
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

############################################################################
# Problem 4: Convex Hull again!
# 
# Use the Divide and Conquer algorithm described in class to compute
# the convex hull of a set of points.
#
# Recurrence worst case:
# Recurrence average case:
# Running time worst case:
# Running time average case:
# 
# When does the worst case happen?
############################################################################

#def convexHull(l):
#    """
#    >>> convexHull([(1,1), (4,2), (4,5), (7,1)])
#    [(1, 1), (4, 5), (7, 1)]
#    """
#    sortX = sorted(l, key=lambda point: point[0])
#    sortY = sorted(l, key=lambda point: point[1])
#    minX, minY = sortX[0], sortY[0]
#    maxX, maxY = sortX[-1], sortY[-1]
#    print(minX, maxX)
#    print(l[0], l[-1])
#
#def findExtrema(l):
#    sortX = sorted(l, key=lambda point: point[0])

############################################################################
# Problem 5: Recurrence relations
# 
# Give a closed form, and bit Theta for the following recurrence relations.
# If it's a divide and conquer relation, then you only need to give the Theta.
#
# a. Give the recurrence relation for Karatsuba's algorithm, and solve it.
# b. Give the recurrence relation for Strassen's algorithm, and solve it.
# c.
# T(1) = 1
# T(n) = T(n-1) + n
# d. 
# T(1) = 1
# T(n) = 2T(n-2) + 1
# 
############################################################################


if __name__ == "__main__":
    import doctest
    doctest.testmod()

