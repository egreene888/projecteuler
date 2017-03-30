/*
euler5.c

2250 is the smallest number that can be divided by each of the numbers 1 to
10 without a remainder. What is the smallest number that can be divided by
each of the numbers 1 to 20 without a remainder?
*/

#include <stdio.h>
int main() {
  int n;
  // n = 10;
  n = 20;

  // counters for loops
  int i = n;
  int j;
  int breakflag;
  // an int for the answer
  int answer;
  // printf("%d\n", answer);
  while(1) {
    breakflag = 1;
    for (j = 1; j < n+1; j++){
      if (i % j == 0) {
        continue;
      }
      else {
        breakflag = 0;
        break;
      }
    }
    if (breakflag) {
      answer = i;
      break;
    }
    else {
      i++;
    }
  }
  printf("answer = %d\n", answer);
}
