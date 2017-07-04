"""
euler12.py

Problem Statement: By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by
trying every route. However, Problem 67, is the same challenge with a triangle
containing one-hundred rows; it cannot be solved by brute force, and requires a
clever method! ;o)

SOLVED
Couldn't even figure out how to brute-force it though. Not that I tried hard.
"""


def read_list():
    """ returns the list we're dealing with for this problem """
    L = '75\n 95 64\n 17 47 82\n 18 35 87 10\n 20 04 82 47 65\n 19 01 23 75 03 34\n 88 02 77 73 07 63 67\n 99 65 04 28 06 16 70 92\n 41 41 26 56 83 40 80 70 33\n 41 48 72 33 47 32 37 16 94 29\n 53 71 44 65 25 43 91 52 97 51 14\n 70 11 33 28 77 73 17 78 39 68 17 57\n 91 71 52 38 17 14 91 43 58 50 27 29 48\n 63 66 04 68 89 53 67 30 73 16 69 87 40 31\n 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'
    L = L.split('\n')
    for i in range(len(L)):
        L[i] = L[i].split()
        for j in range(len(L[i])):
            L[i][j] = int(L[i][j])

    return L

def recursive_approach(L, position = 0, nestlevel = 0):
    """ returns the maximum of the two paths stemming from the point given by
    [nestlevel][position] in the list. Uses recursion to find the maximum of
    the two paths stemming from the next level, and so on. When called on the
    first level of the triangle, should return the answer to the problem. """
    if nestlevel == len(L) - 1:
        return L[nestlevel][position]
    else:
        firstanswer = recursive_approach(L, position, nestlevel + 1)
        secondanswer = recursive_approach(L, position + 1, nestlevel + 1)
        # print [firstanswer, secondanswer]

        print nestlevel, firstanswer, secondanswer

        return L[nestlevel][position] + max(firstanswer, secondanswer)

def iterative_approach(L):

    for i in range(len(L) - 1, 0, -1):
        for j in range(len(L[i])-1):
            L[i-1][j] += max(L[i][j], L[i][j+1])
        print L[i]
    return L[0][0]


def main():
    listofnums = read_list()
    easy_problem = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
    # print recursive_approach(easy_problem)
    # print iterative_approach(easy_problem)

    # answer = recursive_approach(listofnums)
    answer = iterative_approach(listofnums)
    print answer

main()
