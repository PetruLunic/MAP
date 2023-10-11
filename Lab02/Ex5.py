def factorial(num):
    if (num < 1): return 1
    return factorial(num - 1) * num

number = int(input("Introduceti un numar: "))
print("Factorial lui", number, " este: " , factorial(number))