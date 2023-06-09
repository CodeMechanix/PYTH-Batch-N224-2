# Recursion

"""
- Recursion is a programming technique in which a *function* calls itself one or more times to solve a problem.
- Two Parts: 1. Base Case and 2. Recursive case

- A loop is control structure that iteratively executes a block of code until a certain condition is met.
- Recursion, is a technique in which a function calls itself to solve a problem.

- Recursion can be less efficient than loop
-
"""


# Sum of natural numbers using recursion [1 - N]

def getSum(n):
    if n != 0:
        return n + getSum(n - 1)
    else:
        return n


num = int(input())  # 5
print(getSum(num))
