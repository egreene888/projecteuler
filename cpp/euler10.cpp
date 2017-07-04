//euler10.cpp

/*
The sum of primes below 10 is 2 + 3 + 5 + 7 = 17

Find the sum of all primes below two million.
*/
// SOLVED

#include<iostream>
using namespace std;
#include<tgmath.h>
int main() {
  // We're using a time-intensive approach
  long primeSum = 0;
  int potentialprime = 2;
  bool primeflag;
  while (potentialprime < 2000000) {
    primeflag = true;
    for (int i = 2; i<sqrt(potentialprime); i++) {
      if (potentialprime % i == 0) {
        primeflag = false;
        break;
      }
    }
    if (primeflag) {
      primeSum += potentialprime;
    }
    potentialprime++;
  }
  cout << primeSum << endl;
}
