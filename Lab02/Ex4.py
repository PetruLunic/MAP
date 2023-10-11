def getAllDivisors(num: int):
    result = []

    while(num > 2):
        for i in range(2, num + 1):
            if (num % i == 0 ):
                num /= i
                num = int(num)
                result.append(i)
                break

    return result

def getMapOfDublicates(array):
    result = {}

    for i in array:
        if str(i) in result:
            result[str(i)] += 1
        else:
            result[str(i)] = 1

    return result

def getBiggestCommonDivisor(x: int, y: int):
    if (not x or not y): 
        print("Valoare invalida")
        return
    
    xDivisors = getMapOfDublicates(getAllDivisors(x))
    yDivisors = getMapOfDublicates(getAllDivisors(y))

    commonDivisors = {}

    for i in xDivisors:
        if i in yDivisors:
            commonDivisors[i] = min(xDivisors[i], yDivisors[i])

    result = 1
    for i in commonDivisors:
        result *= pow(int(i), commonDivisors[i])

    return result


num1 = int(input("Introduceti primul numar"))
num2 = int(input("Introduceti al doilea numar"))
print("Cel mai mare divizor comun este: ", getBiggestCommonDivisor(num1, num2))