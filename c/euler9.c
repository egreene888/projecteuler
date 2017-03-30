/*
A Pythagorean triple is a set of natural numbers, a < b < c, such that
a^2 + b^2 = c^2

for example, 3^2 + 4^2 = 5^2, 9 + 16 = 25.

There exists exactly one pythagorean triple for which a + b + c = 1000.
Find the product abc.
*/

#include <stdio.h>

int main(){
  int m, n, a, b, c, e, f, g;
  int answer = 0; // set up an answer
  int triple[] = {0, 0, 0};
  for (m = 1; m < 1000; m++) {
    for (n = 1; n < 1000; n++) {
      //pythagorean triples are generated according to the formula
      // a = m^2 - n^2; b = 2mn; c = m*2 + n^2
      // we loop through all possible combinations of m and n,
      a = m*m - n*n;
      b = 2 * m * n;
      c = m*m + n*n;
      // if our combo of m and n results in a negative a, no dice.
      if (a <= 0) {
        continue;
      }
      /* otherwise, we loop through the possible multiples e, g, f
      of a, b and c until the sum is over 1000. If we reach 1001 without
      finding what we're after, break the loop and go on. */
      else {
        e = a;
        f = b;
        g = c;
        while(e + f + g <= 1000) {
          if (e + f + g == 1000) {
            answer = e * f * g;
            triple[0] = e; triple[1] = f; triple[2] = g;
            // there's got to be a better way to do that.
            break;
          }
          else { if (e + f + g < 1000){
            e += a; f += b; g += c;
          }} // I'm going to c hell for those lines of code.

        }
      }
      // if we find the answer, break out of the loops.
      if (answer){
        break;
      }
    }
    if (answer){
      break;
    }
  }
  printf("triple = [%d, %d, %d]\n", triple[0], triple[1], triple[2]);
  printf("answer = %d\n", answer);
}
