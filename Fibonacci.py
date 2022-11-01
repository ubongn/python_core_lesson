# def factorial(x):
#     if x == 1:
#         return 1
#     else: 
#         return x * factorial(x-1)

# print(factorial(5))

import unittest
num = int(input()) #parsing
def fibonacci(n):
    if n <= 1:
        return n
    else:
        #recurssion
        return fibonacci(n-1) + fibonacci(n-2)
for i in range(num):
    print(fibonacci(i))