//euler7.cpp
/*
Solves problem 7 on project euler

By listing the first six prime numbers, 2, 3, 5, 7, 11, 13, we can see that the
sixth prime number is 13.

What is the 10 001st prime number?
*/
#include<iostream>
#include<tgmath.h>
using namespace std;

void firstApproach() { // a memory-intensive approach.
  int n = 10001;
  long primes[n];
  primes[0] = 2;
  for (int i=1; i<n; i++) {
    primes[i] = 0;
  }


  bool primeflag;
  for (int i=0; i<n; i++) {
    // print the primes array
    // for (int j=0; j<n; j++) {cout << primes[j] << "  ";} cout << endl;

    int j = primes[i] + 1;
    // loop through all the numbers
    while (1) {
      // cout << j << endl;
      primeflag = true;
      for (int k=0; k<i; k++) {
        if (primes[k] == 0 || primes[k] > sqrt(j)) {break;}
        if (j%primes[k] == 0) {
          primeflag = false;
          break;
        }
      }
      if (primeflag) {
        primes[i+1] = j;
        break;
      }
      j++;
    }
  }
  // for (int i=0; i<n; i++){ cout << primes[i] << "  ";}
  // cout << endl;
  cout << primes[n-1] << endl;
}

void secondApproach() { // a time-intensive approach
  // cout << "Haven't written this yet" << endl;
  int n = 10001;
  int potentialprime = 2;
  int indexofprime = 1;

  while (indexofprime < n) {
    bool primeflag = true;
    potentialprime++;
    // cout << potentialprime << "  "  << sqrt(potentialprime) << endl;
    for (int i=2; i<=sqrt(potentialprime); i++) {
      if (potentialprime % i == 0) {
        primeflag = false;
        break;
      }
    }
    if (primeflag) {
      indexofprime++;
      // cout << potentialprime << endl;
    }
  }
  cout << potentialprime << endl;
}

int main() {
  firstApproach();
  secondApproach();
}
