def getSumOfArray(array):
    result = 0

    for i in array:
        result += i

    return result

def getAverage(array):
    result = getSumOfArray(array)

    return result/len(array)

print(getAverage([4,6,8,2]))