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
    # List of sublists: each sublist has jobs for a single processor.
    sched = []

    # Sort jobs in ascending order by finishing time.
    jobs.sort(key=lambda x: x[1])

    # Collect jobs with compatible start/finish times into sublists.
    while jobs:
        sched = jobsToProcessor(jobs, sched)

    return sched

#   Given list of jobs and an existing schedule (list of sublists),
#   put compatible jobs into sublist for single processor, add that
#   sublist to the overall schedule and return it.
#   Note that jobs must be sorted according to finish time.
#
def jobsToProcessor(jobs, sched):
    # Add job with earliest finish time to schedule for this processor.
    thisProc = [jobs.pop(0)]
    
    for job in jobs:
        # Start time is after finish time of last job scheduled.
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

    # Approximation algorithm:
        # Look at all the strings and find which two overlap the most.
        # Combine those two strings.
        # Add that superstring to the set of strings.
        # Repeat until there's only one string.

def superstring(strings):
    """
    >>> superstring(["CADBC", "CDAABD", "BCDA", "DDCA", "ADBCADC"])
    'BCDAABDDCADBCADC'
    """
    if len(strings) == 1:
        return strings[0]

    # `maxOne` and `maxTwo` have most overlap out of `strings`.
    maxOne = maxTwo = ""

    # Index 0: starting index of overlap for `maxOne`.
    # Index 1: starting index of overlap for `maxTwo`.
    # Index 2: number of overlapping characters.
    maxOverlap = (0, 0, 0)

    for string in strings:
        for other in strings:
            if string == other:
                continue
            overlap = compareStrings(string, other)
            if overlap and overlap[2] > maxOverlap[2]:
                maxOne, maxTwo = string, other
                maxOverlap = overlap

    # Remove maxOne and maxTwo from `strings`, then add their combination.
    strings = [s for s in strings if s != maxOne and s != maxTwo]
    combined = combineStrings(maxOne, maxTwo, maxOverlap)
    strings.append(combined)

    return superstring(strings)


#   Return tuple indicating overlap between front of `a` and rear of `b`,
#   between rear of `a` and front of `b`, or None if no overlap exists.
#
def compareStrings(a, b):
    """
    >>> compareStrings("ABC", "DEF")
    >>> compareStrings("ABC", "DBA")
    (0, 2, 1)
    >>> compareStrings("ABC", "CBA")
    (2, 0, 1)
    >>> compareStrings("ABC", "CAB")
    (0, 1, 2)
    >>> compareStrings("ABC", "BCA")
    (1, 0, 2)
    >>> compareStrings("ABCD", "EBCF")
    >>> compareStrings("ABCDEF", "CDEFGHIJK")
    (2, 0, 4)
    >>> compareStrings("ABC", "CDEFAB")
    (0, 4, 2)
    """
    overlapFront = compareFront(a, b)
    overlapBack = compareBack(a, b)

    return biggestOverlap(overlapFront, overlapBack)


#   Return whichever overlap is larger, or None if no overlap exists.
#
def biggestOverlap(front, back):
    if not front and not back:
        return None
    if front and not back:
        return front
    if back and not front:
        return back
    if front[2] > back[2]:
        return front
    return back


#   Return tuple indicating overlap of strings `a` and `b`.
#   If no overlap exists, return None.
#
def compareFront(a, b):
    # Indices for a and b, respectively.
    i = 0
    j = len(b) - 1

    # Scan b from rear for char that matches first char in a.
    while j >= 0 and b[j] != a[i]:
        j -= 1

    # No match found.
    if j == -1:
        return None
    
    overlap = 0
    
    # Loop and increment as long as chars match.
    while j < len(b) and i < len(a) and b[j] == a[i]:
        overlap += 1
        i += 1
        j += 1
    
    # Make sure we're getting overlap at edges, not internally.
    if i == len(a) or j == len(b):
        i -= overlap
        j -= overlap
    else:
        return None

    # Return starting indices of match for both a and b;
    #   also return number of matching chars.
    return (i, j, overlap)


#   Use `compareFront()` to get result, then swap values and return.
#
def compareBack(a, b):
    # Get overlap in form (b, a, overlap).
    overlap = compareFront(b, a)

    # Swap starting indices to preserve (a, b, overlap) ordering.
    if overlap:
        return (overlap[1], overlap[0], overlap[2])

    return None


#   Given two strings and their overlap tuple, return combined string.
#
def combineStrings(a, b, overlap):
    """
    >>> combineStrings("ABC", "DBA", (0, 2, 1))
    'DBABC'
    >>> combineStrings("ABC", "CBA", (2, 0, 1))
    'ABCBA'
    >>> combineStrings("ABC", "CAB", (0, 1, 2))
    'CABC'
    >>> combineStrings("ABC", "BCA", (1, 0, 2))
    'ABCA'
    >>> combineStrings("ABCDEF", "CDEFGHIJK", (2, 0, 4))
    'ABCDEFGHIJK'
    >>> combineStrings("ABC", "CDEFAB", (0, 4, 2))
    'CDEFABC'
    >>> combineStrings("BCDAABD", "DDCADBCADC", (6, 0, 1))
    'BCDAABDDCADBCADC'
    """
    startA, startB = overlap[0], overlap[1]

    # Back of a overlaps with front of b.
    if startA > startB:
        return a[:startA] + b

    # Front of a overlaps with back of b.
    if startA < startB:
        return b[:startB] + a

    # Match at equal indices: return longer string.
    if len(a) > len(b):
        return a

    return b


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
