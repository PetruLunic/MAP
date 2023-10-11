def sortBubble(array):
    isSorted = False

    while(not isSorted):
        isSorted = True

        for i in range(len(array) - 1):
            if (array[i] > array[i+1]):
                [array[i], array[i+1]] = [array[i+1], array[i]]
                isSorted = False

length = int(input("Introduceti marimea array-ului"))
array = []
for i in range(length):
    number = int(input("Introduceti numar: "))
    array.append(number)

sortBubble(array)
print("Array-ul sortat: ", array)

