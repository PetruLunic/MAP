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

def isPrime(num):
    if (len(getAllDivisors(num)) < 2): return True
    return False

print(isPrime(19))