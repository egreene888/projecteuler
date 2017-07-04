# euler5.py
"""completed"""
# Problem Statement
"""
The sum of the squares of the first ten natural numbers is

1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is

(1 + 2 + 3 + ... + 10)^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers
and the square of the sum is 3025 - 385 = 2640.

Firnd the difference between the sum of the squares of the first hundred
natural numbers and the square of the sum.
"""
def main():
    n = 10
    # n = 100
    # Calculate the sum of the squares
    sumofsquares = sum ( [x**2 for x in range(1, n+1)] )

    # Calculate the square of the sum
    squareofsum = (sum(range(1, n+1)))**2

    answer = squareofsum - sumofsquares
    print answer

main()
