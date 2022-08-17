# Recursion

[Reference](https://www.geeksforgeeks.org/recursion/)

Problem 1: Write a program and recurrence relation to find the Fibonacci series of n where n>2.

Mathematical Equation:

    n if n == 0, n == 1;
    fib(n) = fib(n-1) + fib(n-2) otherwise;

Recurrence Relation:

    T(n) = T(n-1) + T(n-2) + O(1)

Recursive program:

    Input: n = 5
    Output:
    Fibonacci series of 5 numbers is : 0 1 1 2 3
