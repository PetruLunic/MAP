def getOddNumbersTill(num):
    result = []
    for i in range(num):
        if (i % 2 != 0):
            result.append(i)

    return result

print("Primele 20 de numere impare: ", getOddNumbersTill(20))