// euler15.c
/*
Starting in the top left corner of a 2 x 2 grid, and being only able to move left and right,
there are exactly 6 routes to the bottom right corner.

rrdd,
rdrd, rddr,
drrd, drdr,
ddrr

How many such routes are there on a 20 x 20 grid

SOLVED
*/
/*
These are the number of coin flip sequences that produce n heads and n tails

1 Coin

H
T

2 coins
HH
HT TH
TT

3 coins
HHH
HHT HTH THH
HTT THT TTH
TTT

4 coins

HHHH
HHHT HHTH HTHH THHH
HHTT HTHT HTTH THHT THTH TTHH
HTTT THTT TTHT TTTH
TTTT

5 coins
HHHHH
HHHHT HHHTH HHTHH HTHHH THHHH
HHHTT HHTHT HHTTH HTHHT HTHTH HTTHH THHHT THHTH THTHH TTHHH
HHTTT HTHTT HTTHT HTTTH THHTT THTHT THTTH TTHHT TTHTH TTTHH
HTTTT THTTT TTHTT TTTHT TTTTH
TTTTT

It's clearly just Pascal's triangle. So the answer to our problem is C(n, k)

= n! / k! (n - k)!

where n is double the size of the grid and k is the size of the grid
*/
#include<stdio.h>

double f(int start, int stop); // factorial function

double f(int start, int stop) {
  int i;
  long out = 1;
  for (i=start; i > stop; i-=1) {
    out *= i;
    printf("%d\n", i);
  }

  printf("-\n%f\n", out);
  printf("--------\n");

  return out;
}

int main() {
  int k = 20;
  int n = 2*k;
  // int notanswer = f(5, 1);
  // int answer = f(n, 1) / (f(n-k, 1) * f(k, 1));
  double answer = f(n, k) / f(k, 1);
  printf("and the answer is -- %f\n", answer);
  // printf("and the answer is not -- %d\n", notanswer);
}
