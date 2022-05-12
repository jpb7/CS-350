# CS 350: Homework 5
# Due: Week of 5/9
# Name: Jacob Bentley

# You should not assume anything about the data for these problems
# other than it's valid.
# Adjacency lists might not be in any particular order
# and graphs may not be connected.

############################################################################
#
# Problem 1
#
# write a function that returns the set of connected components 
# of an undirected graph g.
# g is represented as an adjacency list
# you should return a list of components, where each component is a list of vertices.
# Example g = [[1,2], [0,2], [0,1], [4], [3]]
# Should return a list of two components [[0,1,2],[3,4]]
#
# Running time: O(n*log(n))
#
############################################################################

from re import I


def components(g):
    """
    >>> components([[1,2], [0,2], [0,1], [4], [3]])
    [[0, 1, 2], [3, 4]]
    """
    d = {}
    isolated = []
    for edge in sorted(g):
        if len(edge) == 2:
            if edge[0] not in d:
                d[edge[0]] = edge[1]
            if edge[1] not in d:
                d[edge[1]] = edge[0]
        else:
            isolated.append(edge[0])
    return [[x for x in d.keys()]] + [isolated]
    
############################################################################
#
# Problem 2
#
# write a function the returns True if, and only if, graph g is bipartite
# g is represented as an adjacency list
#
# Running time: O(n**2)
#
############################################################################

def bipartite(g):
    """
    >>> bipartite([[3,4,7], [3,5,6], [4,5,7], [0,1], [0,2], [1,2], [1], [0,2]])
    True
    >>> bipartite([[1,2], [0,3], [0,3], [0,1,2]])
    False
    >>> bipartite([[3],[4],[5],[0],[1],[2]])
    False
    """
    A, B, C = set(g[0]), set(), set()
    for edges in g:
        added = False
        for edge in edges:
            if edge in A:
                A.update(edges)
                added = True
                break
            if edge in B:
                B.update(edges)
                added = True
                break
        if not added:
            if not B:
                B.update(edges)
            else:
                C.update(edges)
    return not C and A and B and not A & B

############################################################################
#
# Problem 3
#
# write a function the returns True if, and only if, graph g is a forrest
# g is represented by a adjacency list.
#
# Running time: O(n**2)
#
############################################################################

def isForrest(g):
    """
    >>> isForrest([[1,2], [3,4], [5,6], [], [], [], []])
    True
    >>> isForrest([[1,2], [3,4], [5,4], [], [], []])
    False
    """
    A = set()
    for edges in g:
        for edge in edges:
            if edge in A:
                return False
            A.add(edge)
    return True

############################################################################
#
# Problem 4
#
# write a function to topologically sort the vertices of a directed graph d
# Assume d is an adjacency list.
#
# Running time: O(n**2)
#
############################################################################

def topsort(d):
    """
    >>> topsort([[1, 2], [3], [3], []])
    [0, 1, 2, 3]
    >>> topsort([[3], [0], [1], [2]])
    [0, 3, 2, 1]
    """
    out = []
    visited = [False for i in range(len(d))]
    out = _topsort(d, 0, visited, out)
    out.reverse()
    return out

def _topsort(d, i, visited, out):
    visited[i] = True
    for v in d[i][::-1]:
        if not visited[v]:
            _topsort(d, v, visited, out)
    out.append(i)
    return out

############################################################################
#
# Problem 5
#
# write a function to determine the strongly connected components of digraph d.
# Just like the components example, you should return a list of strongly connected
# components.
#
# Running time?
#
############################################################################

#def scc(d):
#    """
#    >>> scc([[1], [2], [0,3], [1,2], [3,5,6], [4], [7], [8], [6]])
#    [[0, 1, 2, 3], [4, 5], [6, 7, 8]]
#    """
#    pass

############################################################################
#
# Problem 6
#
# a. What do we need to change about BFS/DFS if we use an adjacency matrix?
#
# b. What is the running time for BFS/DFS if we use an adjacency matrix?
#
# c. Give an example of a weighted graph where BFS doesn't return the shortest
#    path.
#
############################################################################

if __name__ == "__main__":
    import doctest
    doctest.testmod()
