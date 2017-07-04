//euler6.cpp

/*
he sum of the squares of the first ten natural numbers is

1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is

(1 + 2 + 3 + ... + 10)^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers
and the square of the sum is 3025 - 285 = 2640.

Firnd the difference between the sum of the squares of the first hundred
natural numbers and the square of the sum.
*/

//COMPLETED

#include<iostream>
using namespace std;

int main() {
  int n(10);
  int range[n];
  for (int i=0; i<n; i++) {
    range[i] = i+1;
  }
  int sumofsquares(0);
  int squareofsum(0);
  for (int i=0; i<n; i++) {
    sumofsquares += range[i]*range[i];
    squareofsum += range[i];
  }
  squareofsum *= squareofsum;
  cout << "sum of squares " << sumofsquares << endl;
  cout << "square of sum " << squareofsum << endl;
  cout << endl;
  cout << "And the answer is -- " << squareofsum - sumofsquares << endl;
}
