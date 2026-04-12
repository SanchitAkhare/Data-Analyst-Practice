"""
=====================================================
Problem: Factorial of a Number
=====================================================

Source: Practice
Level: Easy

Description:
Calculate the factorial of a given number using recursion.
Factorial of n (n!) = n * (n-1) * (n-2) * ... * 1

-----------------------------------------------------
Approach:
-----------------------------------------------------
1. Use recursion to solve the problem
2. Base case: factorial of 0 or 1 is 1
3. Recursive case: n * factorial(n-1)
4. Handle invalid input (negative numbers)

-----------------------------------------------------
"""

# Code

def calculate_factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n - 1)


# Example usage
num = 5
result = calculate_factorial(num)
print(f"Factorial of {num} is {result}")

"""
-----------------------------------------------------
Learning:
-----------------------------------------------------
- Understood recursion and base case importance
- Learned how function calls stack works
- Practiced handling edge cases (0 and negative numbers)

-----------------------------------------------------
Notes:
-----------------------------------------------------
- Recursive solution is simple but not optimal for large inputs
- Iterative approach can be more efficient
"""
