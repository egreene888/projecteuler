/* euler1.c
Solves problem 1 in project euler

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6, and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000. */
#include <stdio.h>

int main() {
  int i;
  int sumofmultiples = 0;
  for (i = 1; i < 1000; i++){
    if ((i % 3 == 0) | (i % 5 == 0)){
      sumofmultiples += i;
    }
  }
  printf("%d \n", sumofmultiples);
  return 0;
}
