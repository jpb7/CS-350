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
    [1,2,3,4,6]
    >>> quicksort([5,4,3,2,1])
    [5,4,3,2,1]
    """
    pass

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
# Running time:
############################################################################

# def maxSublist(l):
#     """
#     >>> maxSublist([-2,1,-3,4,-1,2,1,-5,4])
#     [4,-1,2,1]
#     """
#     pass


############################################################################
# Problem 3: Parenthesizing matrices.
# 
# If I multiply and m*l matrix A by an l*n matrix B
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
# Running time:
############################################################################

#def matrixParens(sizes):
#    """
#    >>> matrixParens([(3,5), (5,4), (4,7)])
#    144
#    """
#    pass

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

# def convexHull
#     """
#     >>> convexHull([(1,1), (4,2), (4,5), (7,1)])
#     [(1, 1), (4, 5), (7, 1)]""
#     """
#     pass

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

