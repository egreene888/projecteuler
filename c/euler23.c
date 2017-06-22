// euler23.c

/*
Solves problem 23 in project euler.

Problem statement:
A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than
n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
the smallest number that can be written as the sum of two abundant numbers is
24. By mathematical analysis, it can be shown that all integers greater than
28123 can be written as the sum of two abundant numbers. However, this upper
limit cannot be reduced any further by analysis even though it is known that
the greatest number that cannot be expressed as the sum of two abundant numbers
is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.
*/

int is_abundant(int n);
int is_sum(int L, int n);

int is_abundant(int n) {
  int limit = n/2;
  int sum_of_factors = 1; // 1 is a factor of all numbers
  int i = 2;
  while (i < limit) {
    if (n % i == 0) {
      if (i == n/i) {
        sum_of_factors += i;
      }
      else {
        sum_of_factors += (i + n/i);
      }
      limit = n/i;
    }
    i++;
  }
  return sum_of_factors;
}

int is_sum(int L; int n) {
  
}
