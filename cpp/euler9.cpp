// euler9.cpp

/*
A Pythagorean triple is a set of natural numbers, a < b < c, such that
a^2 + b^2 = c^2

for example, 3^2 + 4^2 = 5^2, 9 + 16 = 25.

There exists exactly one pythagorean triple for which a + b + c = 1000.
Find the product abc.
*/
#include<iostream>
using namespace std;
int main() {
  // The way to generate Pythagorean triples-- for any m and n,
  // a = m^2 - n^2, b = 2mn, and c = m^2 + n^2 are a Pythagorean triple.
  // int triple[3];
  int answer = 0;
  for (int m = 1; m < 1000; m++) {
    for (int n = 1; n < m; n++) {
      // generate a Pythagorean triple
      int a = m*m -n*n;
      int b = 2*m*n;
      int c = m*m + n*n;
      // need to check all the multiples of a, b, c
      int e = a;
      int f = b;
      int g = c;
      while (1) {
        if (e + f + g > 1000) {
          break;
        } else if (e + f + g == 1000) {
          cout << "triple -- " << e << ", " << f << ", "<< g << endl;
          answer = e*f*g;
          break;
        } else {
          e += a; f += b; g += c;
        }
      }
      if (answer) {break;}
    }
    if (answer) {break;}
  }
  cout << "The answer is -- " << answer << endl;
}
