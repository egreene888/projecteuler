//euler14.cpp

/*
The following iterative sequence is defined for the set of positive integers:

n --> n/2 (n is even)
n --> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 --> 40 --> 20 --> 10 --> 5 --> 40 --> 16 --> 8 --> 4 --> 2 --> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been definitively proved yet (Collatz problem) it is thought that all
starting numbers finish at 1.

Which number, under one million, produces the longest chain.
*/

#include<iostream>
using namespace std;

int lengthOfChain(long n) {
  if (n < 1) {
    // prevent negative numbers from being passed.
    throw domain_error("Can't pass a negative number");
  }
  int length(1); // 1 is part of every chain.
  while (n!=1) {
    length += 1;
    // cout << n << "   ";
    if (n%2 == 0) {
      n = n/2;
    } else {
      n = 3*n + 1;
    }
  }
  // cout << endl;
  return length;
}

int main() {
  int longestChainNumber(0);
  int longestChainLength(0);
  int chainLength;
  for (long i=1; i<1000000; i++) {
    chainLength = lengthOfChain(i);
    if (chainLength > longestChainLength) {
      longestChainLength = chainLength;
      longestChainNumber = i;
    }
  }
  cout << "The number with the longest chain is " << longestChainNumber << endl;
  cout << "The length of the chain is " << longestChainLength << endl;
}
