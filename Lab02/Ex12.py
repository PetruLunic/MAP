def getFibonacciInRange(num: int):
    result = [1, 1]

    for i in range(num-2):
        result.append(result[i+1] + result[i])

    return result

number = int(input("Introduceti un numar"))
print("Lista lui fibonaci cu ", number, " elemente: ", getFibonacciInRange(number))