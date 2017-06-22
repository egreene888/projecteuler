/* The following iterative sequence is defined for the set of positive integers:

n --> n/2 (n is even)
n --> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 --> 40 --> 20 --> 10 --> 5 --> 40 --> 16 --> 8 --> 4 --> 2 --> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been definitively proved yet (Collatz problem) it is thought that all
starting numbers finish at 1.

Which number, under one million, produces the longest chain?

*/
#include<stdio.h>

int collatz(long n);

int collatz(long n) {
  int p = 1;
  while (n != 1) {
    if (n % 2 == 0) {
      n = n/2;
      p += 1;
    }
    else {
      n = 3*n + 1;
      p +=1;
    }
  }
  return p;
}

int main() {
  // set up some starting record

  int recordholder = 13;
  int record = 10;
  int c;
  long i;
  for (i=2; i < 1000000; i++) {
    c = collatz(i);
    if (c > record) {
      recordholder = i;
      record = c;
      printf("%d -- %d\n", recordholder, record);
    }
    // if (i % 1 == 0 && i > 113380) {
    //   printf("%d--------\n", i );
    // }

  }
  printf("answer = %d\n", recordholder);
  // printf("interesting -- %d\n", collatz(113383));
}
