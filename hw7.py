# CS 350: Homework 6
# Due: Week of 5/23
# Name: Jacob Bentley

################################################################
# Problem 1
# 
# We're going to take the job scheduling problem from class,
# but this time, I want to make sure every job is scheduled.
#
# If I have a set of n jobs where each job is represented
# by a tuple (s,f), give a greedy algorithm to schedule the
# jobs on the fewest number of processors total.
#
# Running Time: O(n*log(n))
################################################################

def schedule(jobs):
    """
    >>> schedule([(5,40), (30,35), (6,20), (19, 31), (23, 29), (28, 32)])
    [[(6, 20), (23, 29), (30, 35)], [(19, 31)], [(28, 32)], [(5, 40)]]
    """
    sched = []
    jobs.sort(key=lambda x: x[1])
    while jobs:
        sched = jobsToProcessor(jobs, sched)
    return sched

def jobsToProcessor(jobs, sched):
    thisProc = [jobs.pop(0)]
    for job in jobs:
        if job[0] > thisProc[-1][1]:
            thisProc.append(job)
            jobs.remove(job)
    sched.append(thisProc)
    return sched

################################################################
# Problem 2
# 
# Given a list of strings (strings), find a short string
# (bigstring) such that for every s in string, s is a substring of
# bigstring.
#
# Use the approximation algorithm we gave in class.
#
# Running Time: 
################################################################

def superstring(strings):
    """
    >>> superstring(["CADBC", "CDAABD", "BCDA", "DDCA", "ADBCADC"])
    'BCDAABDDCADBCADC'
    """
    # Approximation algorithm:
        # Look at all the strings and find which two overlap the most.
        # Combine those two strings.
        # Add that superstring to the set of strings.
        # Repeat until there's only one word.

################################################################
# Problem 3
# 
# Find the shortest path from a to b in a weighted graph g that
# is represented by an adjacency matrix.
#
# You can assume all edge weights are positive.
#
# Running time:
################################################################

# def dijkstra(g, a, b):
#     """
#     >>> g = [ [(1,3), (2,6)], \
#               [(0,3), (4,4)], \
#               [(0,6), (3,2), (5,7)], \
#               [(2,2), (4,4), (8,1)], \
#               [(1,4), (3,4), (6,9)], \
#               [(2,7), (6,2), (7,8)], \
#               [(4,9), (5,2), (9,4)], \
#               [(5,8), (8,3)], \
#               [(3,1), (7,3), (9,2)], \
#               [(6,4), (8,2)] ]
#     >>> dijkstra(g,0,9)
#     [0, 2, 3, 8, 9]
#     """
#     pass

#   Enable doctesting
if __name__ == "__main__":
    import doctest
    doctest.testmod()
