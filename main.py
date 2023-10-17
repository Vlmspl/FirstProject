import math

def CheckIfNumberIsEven(n):
    if n/2 == math.floor(n/2):
        return True
    else:
        return False


a = int(input())

print("Число", a, "є парним:", CheckIfNumberIsEven(a))

