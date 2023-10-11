def factorial(num):
    if (num < 1): return 1
    return factorial(num - 1) * num

print("Factorial lui 10: " , factorial(10))