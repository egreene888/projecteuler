/*
problem statement

the sum of the squares of the first ten natural numbers is

1^2 + 2^2 + ... + 10^2 = 385

The square of the sums of the first ten natural numbers is

(1 + 2 + 3 + ...+ 10)^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers
and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first hundred
natural numbers and the square of the sum */

#include <stdio.h>

int main(){
  int n;
  // n = 10;
  n = 100;
  int sumofsquares = 0;
  int squareofsum = 0;

  // find the sum of the squares
  int i;
  for (i = 1; i < n+1; i++) {
    sumofsquares += i*i;
  }
  for (i = 1; i < n+1; i++) {
    squareofsum += i;
  }
  squareofsum *= squareofsum;
  printf("The answer is %d\n", squareofsum - sumofsquares);
}
