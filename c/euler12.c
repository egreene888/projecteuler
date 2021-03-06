/* euler12.c

The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

1: 1
3: 1, 3
6: 1, 2, 3
10: 1, 2, 5, 10
15: 1, 3, 5, 15
21: 1, 3, 7, 21
28: 1, 2, 4, 7, 15, 28

As we can see, 28 is the first triangle number to have over 5 factors.

What is the first triangle number to have over 500 factors?
*/

#include <stdio.h>

int find_num_factors(int n);
// finds the number of factors for a number.

int main() {
  int numfactors = 2;
  int i = 2;
  int triangle = 3;
  while (numfactors < 50) {
    triangle += i;
    i++;
    numfactors = find_num_factors(triangle);
    printf("%d -- %d \n", triangle, numfactors);

  }
  printf("answer = %d \n", triangle);
}

int find_num_factors(int n) {
  int limit = n;
  int i = 1;
  int numfactors = 2;
  while (limit > i) {
    // printf("%i\n", i);
    if (limit % i == 0) {
      numfactors += 2;
      limit = n/i;
    }
    i++;
  }
  return numfactors;
}
