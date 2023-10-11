def getMin(array):
    min = array[0]

    for i in array:
        if min > i:
            min = i

    return min

def getMax(array):
    max = array[0]

    for i in array:
        if max < i:
            max = i

    return max

length = int(input("Introduceti marimea array-ului"))
array = []
for i in range(length):
    number = int(input("Introduceti numar: "))
    array.append(number)

print("Numarul minim este: ", getMin(array))
print("Numarul maxim este: ", getMax(array))
