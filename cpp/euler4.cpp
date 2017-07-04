//euler4.cpp

/*
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindromic number that is the product of two 3-digit numbers
*/
#include<iostream>
#include<sstream>
using namespace std;

bool isPalindrome(string in) {
  int stringLength = in.length();
  // cout << in << endl;
  // cout << stringLength << endl << endl;
  for (int i=0; i < stringLength  / 2 ; i++) {
    // cout << i << endl;
    // cout << in[i] << "  " << in[stringLength - i - 1] << endl;
    if (in[i] != in[stringLength - i - 1]) {
      return false;
    }
  }
  return true;
}

int main() {
  // test code for the palindrome function
  // bool blarf(isPalindrome("3483"));
  // cout << blarf << endl << endl;
  // blarf = isPalindrome("3443");
  // cout << blarf << endl;

  // test code for the stringstream
  // string blarf;
  // stringstream ss
  // ss << 3321;
  // ss >> blarf;
  // cout << blarf << endl;

  int product;
  string productString;
  int largestPalindrome(0);
  for (int i=1; i<1000; i++) {
    for (int j=1; j<1000; j++) {
      product = i*j;
      stringstream ss;
      ss << product;
      ss >> productString;
      // cout << productString;
      if (isPalindrome(productString)) {
        // cout << " is a palindrome ";
        if (product > largestPalindrome) {
          largestPalindrome = product;
          // cout << "and is the largest palindrome";
        }
      }
      // cout << endl;
    }
  }
  cout << largestPalindrome << endl;
}
