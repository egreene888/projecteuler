# euler22.py
"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a
name score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?
"""

def readfile():
    f = open('p022_names.txt', 'r')
    s = f.readline()
    s = s.strip('"')
    L = s.split('","')
    # print L[:5]
    # print len(L)
    return L

def sortlist(L):
    """ With a list this long, we can't use a recursive sorting algorithm.
    So we'll use bubble sort, even though it's awful by just about any measure
     """
    issorted = False
    while not issorted:
        issorted = True
        for i in range(len(L)-1):
            if L[i] > L[i + 1]:
                L[i], L[i+1] = L[i+1], L[i]
                issorted = False




def score(S):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    score = 0
    for ch in S:
        score += alpha.find(ch) + 1

    return score


def main():
    listofnames = readfile()
    # sortlist(listofnames)
    # wait a sec. Python has a built-in sort function.
    listofnames.sort()
    print 'Sorted List'

    answer = 0
    # calculate scores
    for i in range(len(listofnames)):
        answer += score(listofnames[i]) * (i + 1)

    print answer

main()
