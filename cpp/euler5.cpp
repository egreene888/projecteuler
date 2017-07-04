//euler5.cpp

/*
2520 is the smallest number that can be divided evenly by each of the numbers
1 to 10 without any remainder.

What is the smallest positive number that can be is evenly divisible by all
the numbers 1 through 20?
*/
#include<iostream>
using namespace std;

int main() {
  int n = 10;
  int factors[n];
  int lcm(n);
  for (int i=0; i<n; i++) {
    factors[i] = i+1;
  }
  bool breakflag;
  while (1) {
    breakflag = true;
    for (int i = 0; i < n; i++) {
      if (lcm % factors[i] == 0) {
        breakflag = false;
        break;
      }
      lcm += n;
    }
    if (breakflag) {break;}
  }
  cout << lcm << endl;
}
