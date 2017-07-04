//euler15.cpp

/*
Starting in the top left corner of a 2 x 2 grid, and being only able to move left and right,
there are exactly 6 routes to the bottom right corner.

rrdd,
rdrd, rddr,
drrd, drdr,
ddrr

How many such routes are there on a 20 x 20 grid
*/

/*
We notice this problem is the same as the problem of "How many different
coin flip sequences produce n heads and n tails?"

The answer to this problem is C(n, k) = n! / k! (n-k)! where k is the size of the grid and
n = 2k.

See the header comment in euler15.py for more details
*/
#include<iostream>
using namespace std;

double factorial(int start, int stop = 1) {
  // returns f(start) / f(stop) where f is factorial fucntion.
  double answer = 1;
  for (int i=start; i > stop; i--) {
    answer *= i;
  }
  cout << answer << endl;
  return answer;
}

int main() {
  // int k = 2; // test case
  int k = 20;
  int n = 2*k;

  // Naive way of calculating. Will likely cause overflows.
  // long answer = factorial(n) / (factorial(k) * factorial(n-k));

  // better way of calculating. Why that factorial function has a stop.
  long answer = factorial(n, k) / factorial(n-k);
  cout << answer << endl;
}
