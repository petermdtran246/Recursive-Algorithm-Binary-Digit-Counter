# Recursive Algorithm: Binary Digit Counter

## Overview
This project contains a Python implementation of a recursive algorithm that calculates the number of digits in the binary representation of a positive integer n. The algorithm is designed to solve the problem using a simple recursive approach, counting the number of digits by continuously dividing n by 2.

## Contents
  -  binary_digit_counter.py: Python script implementing the recursive algorithm.
  -  README.md: Documentation for the project.
  -  Example usage in the main block for testing the algorithm with different values of n.

## Algorithm Description
### Problem Statement
The task is to calculate the number of digits in the binary expansion of a given positive integer n using a recursive algorithm.
### Recursive Logic
  -  Base Case:  If n=1, the binary representation has 1 digit.
  -  Recursive Case: If n>1, the number of digits is 1 more than the number of digits in the binary representation of floor(n/2).

The recursive function does not generate the binary representation but only counts the digits.

## Testing
### Example Outputs
Run the script using the provided main block to see the output for the problem instances:
  -  Input: n = 256
      -  Output: The number of binary digits in 256 is: 9
  -  Input: n = 750
      -  Output: The number of binary digits in 750 is: 10

## Asymptotic Analysis
### Recurrence Relation
The work performed by the algorithm in the worst case for a problem of size n is represented by the following recurrence relation:

                  T(n) = T(n-1) + 1, with the base case: T(1) = 1
### Asymptotic Complexity
Using the back-substitution method, we determine that:
                  T(n) = n
Thus, the time complexity of the algorithm is O(n).          
