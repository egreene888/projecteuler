"""
euler67.py

Problem Statement: By starting at the top of the triangle below and moving to
adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum sum from top to bottom in triangle.txt, a 15K text file
containing a triangle with 100 rows.
N.B. For some reason, triangle.txt is actually named p067_triangle.txt.
"""

def read_file():
    """ reads the file 'p067_triangle.txt' into a list of lists """
    f = open('p067_triangle.txt', 'r')
    line = f.readline()
    L = []
    while line != '':
        L.append(line)
        line = f.readline()

    for i in range(len(L)):
        L[i] = L[i].split()
        for j in range(len(L[i])):
            L[i][j] = int(L[i][j])

    return L

def recursive_approach(L, position = 0, nestlevel = 0):
    """ returns the maximum of the two paths stemming from the point given by
    [nestlevel][position] in the list. Uses recursion to find the maximum of
    the two paths stemming from the next level, and so on. When called on the
    first level of the triangle, should return the answer to the problem.

    Copied straight from problem 18"""
    if nestlevel == len(L) - 1:
        return L[nestlevel][position]
    else:
        if nestlevel < 10: print nestlevel
        firstanswer = recursive_approach(L, position, nestlevel + 1)
        secondanswer = recursive_approach(L, position + 1, nestlevel + 1)
        # print [firstanswer, secondanswer]

        return L[nestlevel][position] + max(firstanswer, secondanswer)

def iterative_approach(L):
    for i in range(len(L) - 1, 0, -1):
        for j in range(len(L[i])-1):
            L[i-1][j] += max(L[i][j], L[i][j+1])
        print i
    return L[0][0]

def main():
    listofnums = read_file()
    # answer = recursive_approach(listofnums)
    answer = iterative_approach(listofnums)
    print answer

    # answers may include
    # 7273


main()
