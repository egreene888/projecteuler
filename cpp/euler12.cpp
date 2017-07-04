//euler12.cpp

/*
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
28: 1, 2, 4, 7, 14, 28

As we can see, 28 is the first triangle number to have over 5 factors.

What is the first triangle number to have over 500 factors?
*/
#include<iostream>
using namespace std;

int findNumberOfFactors(long n) {
  // a function to find the number of factors of n
  int numFactors(2); // every number has both 1 and itself as factors
  int potentialFactor(2);
  int limit(n/2);
  while (potentialFactor<limit) {
    if (n % potentialFactor == 0) {
      if (n / potentialFactor == n) {
        numFactors += 1;
        // cout << potentialFactor << n/potentialFactor << endl;
      } else {
        numFactors += 2;
        // cout << potentialFactor << endl << n/potentialFactor << endl;
      }
      limit = n/potentialFactor;
    }
    potentialFactor++;
  }
  // cout << endl;
  return numFactors;
}

int main() {
  int i = 1;
  long triangle(1);
  int numFactors(0);
  while(numFactors < 500) {
    i++;
    triangle += i;
    numFactors = findNumberOfFactors(triangle);
    cout << triangle << " -- " << numFactors << endl;
  }
}
