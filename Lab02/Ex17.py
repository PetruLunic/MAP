def isTriangle(x, y, z):
    if x <= 0 or y <= 0 or z <= 0:
        raise Exception("Unghiul nu poate fi nul sau negativ")
    
    return x + y + z == 180


angle1 = int(input("Introduceti primul unghi: "))
angle2 = int(input("Introduceti al doilea unghi: "))
angle3 = int(input("Introduceti al treilea unghi: "))

try:
    print(isTriangle(angle1, angle2, angle3))
except Exception as e:
    print(e)