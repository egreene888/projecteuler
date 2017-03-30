/*
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
*/
#include <stdio.h>

int main(){
  long n;
  // n = 600851475143;
  // n = 13195;
  n = 51;
  int i = 3;
  int j;
  int lpf;
  int primeflag;
  while(1){
    if (n % i == 0) { // if it's a factor
      // check to see if the number is prime
      primeflag = 1;
      for(j = 2; j < i/2; j ++){
        if (i % j == 0){
          primeflag = 0;
          break;
        }
      }
      if (primeflag){
        lpf = i;
        n /= i;
      }
    }
    if (i > n){
      break;
    }
    i += 2;
  }
  printf("%d is the largest prime factor\n", lpf);
}
