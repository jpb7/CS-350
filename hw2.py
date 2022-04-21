
# CS 350: Homework 2
# Due: Week of 4/11
# Name: Jacob Bentley

import math as m

#########################################3
# Problem 1:
#
# Find a pair with a given sum.
#
# input: a list of integers l, an integer s
# return None if this sum doesn't exist in the array.
# output: a pair of numbers (a,b) where a,b are in l, and a + b == s
# findSum([1,3,5], 8) returns (3, 5)
# 
# What data structure did you use? hash map
# Running Time: O(n)
#########################################3

def findSum(l, s):
    """
    >>> findSum([1,3,5], 8)
    (3, 5)
    >>> findSum([1,2,5], 8)
    >>> findSum([1,5,4,3], 4)
    (1, 3)
    >>> findSum([1,1,3], 2)
    (1, 1)
    """
    d = {}
    for n in l:
        d[n] = s - n
        if d[n] in d:
            return (d[n], n)

#########################################3
# Problem 2:
#
# Find the mode of a list of numbers.
# The mode of a list is the most commonly occurring number in the list.
#
# input: a list of integers l
# output: the mode of l.
# mode([1,2,3,3,4,5]) returns 3
# 
# What data structure did you use? hash map
# Running Time: O(n)
#########################################3

def mode(l):
    """
    >>> mode([1,2,3,3,4,5])
    3
    >>> mode([-8,2,-3,-8,4,-8,5,1])
    -8
    >>> mode([5,4,7,4,3,4,-2,0])
    4
    """
    d = {}
    mode = l[0]
    for n in l:
        if n not in d:
            d[n] = 0
        d[n] += 1
        if d[n] > d[mode]:
            mode = n
    return mode

#########################################3
# Problem 3:
#
# We talked about a ring buffer in class
# A ring buffer has four methods
# pushFront(x)
# pushBack(x)
# popFront()
# popBack()
#
# Your job is to implement these four methods.
# We can't just use the list append method to resize the ring buffer.
# we might have front and back in the middle of the buffer,
# and append only adds new space at the end.
# for that reason, you're going to have to copy
# the array over to a bigger one manually.
#
# I've provided a malloc function to allocate a new array.
# You need to copy the old array into the new one
# but be sure to keep elements in the correct position
#
# For example if we have the buffer :
#
#     v back
# [3, 4, 1, 2]
#        ^ front
#
# and we were to resize it, then the new buffer should be
#     v back
# [3, 4, None, None, None, None, 1, 2]
#                                ^ front
#    
# pushFront Running Time: O(n) for resize
# pushBack Running Time: O(n) for resize
# popFront Running Time: O(n)
# popBack Running Time: O(n)
#########################################3

def malloc(size):
    return [None] * size

class RingBuffer():
    """
    >>> r = RingBuffer()
    >>> r.pushBack(3)
    >>> r.pushBack(4)
    >>> r.pushBack(5)
    >>> r.pushFront(2)
    >>> r.pushFront(1)
    >>> r.popFront()
    1
    >>> r.popFront()
    2
    >>> r.popFront()
    3
    >>> r.popFront()
    4
    >>> r.popFront()
    5
    >>> r.pushBack(7)
    >>> r.pushFront(6)
    >>> r.popFront()
    6
    >>> r.popBack()
    7
    """

    def __init__(self):
        self.size = 0
        self.body = [None] * 4
        self.front = -1
        self.back = 0

    # This method isn't mandatory,
    # but I suggest you implement it anyway.
    # It will help to test this method on its own.
    # Think carefully about what cases you can have with front and back.

    def frontEqualsBack(self):
        return self.front == self.back - len(self.body)

    def resize(self):
        if self.size == 0:
            self.body = [None] * 4
            self.front = -1
            self.back = 0
        else:
            first = self.body[:self.back+1]
            middle = malloc(len(self.body))
            last = self.body[self.front+1:]
            self.body = first + middle + last

    def pushFront(self, x):
        if self.body[self.front]:
            self.front -= 1
        if self.size == 0 or self.frontEqualsBack():
            self.resize()
        self.body[self.front] = x
        self.size += 1

    def pushBack(self, x):
        if self.body[self.back]:
            self.back += 1
        if self.size == 0 or self.frontEqualsBack():
            self.resize()
        self.body[self.back] = x
        self.size += 1

    def popFront(self):
        if self.size == 0:
            self.resize()
            return None
        while not self.body[self.front]:
            self.front += 1
        value = self.body[self.front]
        self.body[self.front] = None
        self.size -= 1
        return value

    def popBack(self):
        if self.size == 0:
            self.resize()
            return None
        while not self.body[self.back]:
            self.back -= 1
        value = self.body[self.back]
        self.body[self.back] = None
        self.size -= 1
        return value

#########################################3
# Problem 4:
#
# We talked about a heap in class
# A heap is a data structure that has a constructor,
# a push method, and a pop method.
# Your job is to implement these methods in Python.
# I've given you the skeleton for the class,
# you need to fill it in.
# 
# push Running Time: O(log n)
# pop Running Time: O(log n)
#########################################3

class Heap():

    """
    >>> h = Heap()
    >>> h.push(5)
    >>> h.push(4)
    >>> h.push(3)
    >>> h.push(2)
    >>> h.push(1)
    >>> h.push(0)
    >>> h.push(7)
    >>> h.pop()
    0
    >>> h.pop()
    1
    >>> h.pop()
    2
    >>> h.pop()
    3
    >>> h.pop()
    4
    >>> h.pop()
    5
    >>> h.pop()
    6
    >>> h.pop()
    7
    """

    def __init__(self):
        self.body = [None] * 5
        self.nodes = 0
        #self.height = 0

    def resize(self):
        self.body += [None] * len(self.body)
    
    def push(self, x):
        #print("pre-push:", self.body)
        if self.nodes == len(self.body):
            self.resize()

        self.body[self.nodes] = x
        c = self.nodes
        self.nodes += 1

        # Set parent based on parity of child.
        p = (c + ((c % 2) - 2)) // 2

        while p >= 0 and self.body[p] > self.body[c]:
            self.body[p], self.body[c] = self.body[c], self.body[p]
            c = p
            # shouldn't this be the same as line 250?
            p = (c - 1) // 2

        #print("post-push:", self.body)
    
    def pop(self):
        print("pre-pop:", self.body)
        if self.nodes == 0:
            return None

        # cases: one item only, two items only, three items only

        root = self.body[0]
        self.nodes -= 1
        self.body[0], self.body[self.nodes] = self.body[self.nodes], None

        if self.nodes > 1:
            height = m.ceil(m.log(self.nodes, 2))
        else:
            height = 1

        p, lc, rc, = 0, 1, 2
        i = 0

        while i < height:
            #c = rc if rc < lc else lc
            if self.body[p] > self.body[lc]:
                self.body[p], self.body[lc] = self.body[lc], self.body[p]
            if self.body[p] > self.body[rc]:
                self.body[p], self.body[rc] = self.body[rc], self.body[p]
            p = rc if rc < lc else lc
            if 2*p+2 >= self.nodes:
                p = 0
            lc, rc = 2*p+1, 2*p+2
            i += 1

        print("post-pop:", self.body)
        return root
    
#    """
#    >>> h = Heap()
#    >>> h.push(3)
#    >>> h.push(2)
#    >>> h.push(4)
#    >>> h.push(1)
#    >>> h.push(5)
#    >>> h.pop()
#    1
#    >>> h.pop()
#    2
#    >>> h.pop()
#    3
#    >>> h.pop()
#    4
#    >>> h.pop()
#    5
#    """
#
#    def __init__(self):
#        self.body = [None] * 7
#        self.nodes = 0
#        self.height = 0
#    
#    def resize(self):
#        self.body += [None] * len(self.body)
#
#    def partialSortUp(self, i, x):
#        offset = (i % 2) - 2
#        parent = (i + offset) // 2
#        y = self.body[parent]
#        while i >= 0 and x and y and x < y:
#            self.body[i], self.body[parent] = y, x
#            i = parent
#            parent = (i + offset) // 2
#            x, y = self.body[i], self.body[parent]
#        
#    def partialSortDown(self, p):
#        p, c1, c2 = 0, 1, 2
#        while c1 < self.nodes and c2 < self.nodes:
#            x, y, z = self.body[p], self.body[c1], self.body[c2]
#            if x and y and x > y:
#                self.body[p], self.body[c1] = y, x
#                p = c1
#                c1 = 2*p + 1
#            elif x and z and x > z:
#                self.body[p], self.body[c2] = z, x
#                p = c2
#                c2 = 2*p + 2
#            else:
#                break
#
#    def push(self, x):
#        print("pre-push:", self.body)
#        if self.nodes == len(self.body):
#            self.resize()
#        self.body[self.nodes] = x
#        self.partialSortUp(self.nodes, self.body[self.nodes])
#        self.nodes += 1
#        print("post-push:", self.body)
#
#    def pop(self):
#        print("pre-pop:", self.body)
#        root = self.body[0]
#        if root == None:
#            return None
#        self.nodes -= 1
#        self.body[0], self.body[self.nodes] = self.body[self.nodes], None
#        self.partialSortDown(0)
#        print("post-pop:", self.body)
#        return root

if __name__ == "__main__":
    import doctest
    doctest.testmod()
