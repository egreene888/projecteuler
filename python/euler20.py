"""
euler20.py

Find the sum of the digits in the number 100!
"""

# use python to brute force it!

def f(n):
    """ factorial function"""
    factorial = n
    for i in range(1, n):
        factorial *= i
    return factorial

def main():
    answer = 0
    f_of_hundred = f(100)
    # print f_of_hundred
    for digit in str(f_of_hundred):
        answer += int(digit)

    print answer

main()
