
# CS 350: Homework 3
# Due: Week of 4/18
# Name: Jacob Bentley

# for this homework, unless I'm asking you to sort a list,
# you are allowed to use the sorted function in Python.
# sorted takes a list, and returns a sorted copy of the list in Theta(n*log(n)) time.

############################################################################
#
# Problem 1
# Compute the largest gap between two numbers in a list.
#
# for example: gap([1,6,2,4,9]) == 3 because the gap between 6 and 9 is 3.
# The gap isn't 8 because even thought 9-1 is 8, there is a 4 in the middle
# of those numbers.
#
# Running Time: O(n*log(n))
############################################################################

def gap(l):

    """
    >>> gap([1,6,2,4,9])
    3
    >>> gap([-4, -5, 2, -6])
    6
    >>> gap([0, 5, 3, 1, 12, 7])
    5
    >>> gap([-12, -10, -2, 0])
    8
    >>> gap([])
    0
    """

    # O(n*log(n))
    l.sort()
    maxGap = 0

    # O(n)
    for i in range(len(l) - 1):
        currentGap = l[i+1] - l[i]
        if currentGap > maxGap:
            maxGap = currentGap

    return maxGap

############################################################################
#
# Problem 2
# We can concatenate two numbers together to get a new number.
# for example: 44 concatenated with 55 = 4455
# We can concatenate a list of numbers by concatenating all the numbers.
# concat([1,2,55,3]) = 12553
#
# If we rearrange the list, we can get a different number.
# concat([2,55,1,3]) = 25513
#
# Write a function to find the largest value we can get from concatenating a list.
#
# Running Time: O(n*log(n))
############################################################################

def concatenate(l):
    out = ""
    for x in l:
        out = out + str(x)
    return int(out)

def largestConcat(l):

    """
    >>> largestConcat([1,2,55,3])
    55321
    >>> largestConcat([55,9])
    955
    >>> largestConcat([55,67,6])
    67655
    >>> largestConcat([55,67,7])
    76755
    >>> largestConcat([5, 210, 43, 876])
    876543210
    """

    # O(n) + O(n*log(n)) + O(n)
    l = sorted((str(n) for n in l), reverse=True)
    return concatenate(l)

############################################################################
#
# Problem 3
# Write a function to return the number of unique elements in an array.
# for example the list [3,6,2,3,2,7,4] has 3 unique elements, 6, 7, and 4.
#
# Running Time: O(n)
############################################################################

def numberUnique(l):

    """
    >>> numberUnique([3,6,2,3,2,7,4])
    3
    >>> numberUnique([5,5,4,7,3,3,2,1])
    4
    >>> numberUnique([0,0,0,0,0])
    1
    >>> numberUnique([])
    0
    >>> numberUnique([0,0,0])
    1
    >>> numberUnique([0,0,0,1,2])
    2
    """

    if not l:
        return 0

    d = {}
    count = 0

    # O(n)
    for n in l:
        if n not in d:
            d[n] = 1
            count += 1
        else:
            d[n] += 1
        if d[n] == 2:
            count -= 1

    if not count:
        return 1
    return count
    
############################################################################
#
# Problem 4
# Implement insertion sort from class.
#
# Running Time: O(n**2)
############################################################################

def insertionSort(l):

    """
    >>> insertionSort([3,6,2,5,1])
    [1, 2, 3, 5, 6]
    >>> insertionSort([-3,-6,-2,-5,-1])
    [-6, -5, -3, -2, -1]
    >>> insertionSort([])
    []
    >>> insertionSort([3.2,6.1,3.1,3.0])
    [3.0, 3.1, 3.2, 6.1]
    >>> insertionSort(['b', 'c', 'a'])
    ['a', 'b', 'c']
    """

    for i in range(len(l)):
        inserted = False
        current = l[i]
        shift = 0
        for j in range(0, i+1):
            if inserted:
                l[j], shift = shift, l[j]
            elif current < l[j]:
                shift, l[j] = l[j], current
                inserted = True
    return l

############################################################################
#
# Problem 5
# Use the heap from last homework to sort an array.
#
# Running Time: O(n*log(n))
############################################################################

# Helper functions for Heap from HW2 solution:

def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

def up(i):
    return (i-1) // 2

# Heap from HW2 solution:

class Heap():
    def __init__(self):
        self.body = []

    def push(self, x):
        self.body.append(x)
        i = len(self.body) - 1

        while up(i) >= 0 and self.body[up(i)] > self.body[i]:
            self.body[i], self.body[up(i)] = self.body[up(i)], self.body[i]
            i = up(i)
    
    def pop(self):
        out = self.body[0]
        self.body[0] = self.body[-1]
        self.body.pop()
        i = 0

        while right(i) < len(self.body) and \
            self.body[i] > min(self.body[left(i)], self.body[right(i)]):

            if self.body[left(i)] < self.body[right(i)]:
                self.body[i], self.body[left(i)] = \
                    self.body[left(i)], self.body[i]
                i = left(i)
            else:
                self.body[i], self.body[right(i)] = \
                    self.body[right(i)], self.body[i]
                i = right(i)
        
        if left(i) < len(self.body) and self.body[i] > self.body[left(i)]:
            self.body[i], self.body[left(i)] = self.body[left(i)], self.body[i]
        
        return out
            
def heapSort(l):
    """
    >>> heapSort([3,6,2,5,1])
    [1, 2, 3, 5, 6]
    >>> heapSort([-1, 3, -6, 5, 4])
    [-6, -1, 3, 4, 5]
    >>> heapSort([])
    []
    >>> heapSort([1])
    [1]
    """
    h = Heap()
    # O(n)
    for n in l:
        # O(log(n))
        h.push(n)
    # O(n) * O(log(n))
    return [h.pop() for n in range(len(l))]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
