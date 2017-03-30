/* euler2.py

Solves problem 2 for Project euler

Each new term in the Fibbonacci sequence is generated by summing the previous
two terms. Starting with 1 and 2, the first ten terms will be
1, 2, 3, 5, 8, 13, 21, 34, 55, 89.

By considering the terms in the Fibbonacci sequence whose values do not
exceed four million, find the sum of the even-valued terms. */

#include <stdio.h>

int main() {
  // set up first two terms, plus an accumulator
  int Fib1 = 1;
  int Fib2 = 2;
  int acc = 0;
  // We'll use this later
  int temp;
  while (Fib2 < 4000000) {
    // check to see if the last number in the sequence is even
    if (Fib2 % 2 == 0) {
      acc += Fib2;
    }
    temp = Fib2;
    Fib2 += Fib1;
    Fib1 = temp;
  }
  printf("%d \n", acc);
}