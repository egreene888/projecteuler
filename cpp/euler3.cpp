// euler3.cpp

/*
The prime factors of 13195 are 5, 7, 13, and 29.
What is the largest prime factor of 600851475143?

*/
#include<iostream>
using namespace std;

bool is_prime(int n) {
  int i;
  for (i = 1; i < n/2; i++) {
    if (n%i == 0) {
      return false;
    }
  }
  return true;
}

int main() {
  long n(600851475143);
  // long n = 13195;
  long largestprimefactor(2);
  long i = 3;

  while (1) {
    // if i is a factor
    if (n % i == 0) {
      //determine if it's prime
      if (is_prime(i))
        largestprimefactor = i;
        cout << i << endl;
      n = n/i;
    }
    if (i > n) break;
    i += 2;
  }

}
